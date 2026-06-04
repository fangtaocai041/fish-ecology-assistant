# ============================================================
#  Reasonix One-Click Migration Script
#  Run this on a new machine to replicate your full setup
#
#  Usage (from project root):
#    powershell -ExecutionPolicy Bypass -File .reasonix\setup-migrate.ps1
# ============================================================

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot\..    # Back to project root

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Reasonix Environment Migration / Init" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# ---- Step 1: Check base dependencies ----
Write-Host "[1/5] Checking base dependencies..." -ForegroundColor Yellow

$issues = @()

# Node.js
try {
    $nodeVer = node --version 2>$null
    Write-Host "  OK Node.js $nodeVer" -ForegroundColor Green
} catch {
    $issues += "Node.js not installed — https://nodejs.org/ (recommend LTS)"
    Write-Host "  MISSING Node.js" -ForegroundColor Red
}

# npm
try {
    $npmVer = npm --version 2>$null
    Write-Host "  OK npm $npmVer" -ForegroundColor Green
} catch {
    # npm comes with Node.js, don't report separately
}

# uvx (for rplay MCP)
try {
    $uvxVer = uvx --version 2>$null
    Write-Host "  OK uvx $uvxVer" -ForegroundColor Green
} catch {
    $issues += "uvx not installed — run: powershell -c `"irm https://astral.sh/uv/install.ps1 | iex`""
    Write-Host "  MISSING uvx" -ForegroundColor Red
}

# R (for rplay)
$rHome = $null
try {
    $rHome = "C:\Program Files\R\R-4.6.0"
    if (Test-Path "$rHome\bin\R.exe") {
        $rVer = & "$rHome\bin\R.exe" --version 2>$null | Select-Object -First 1
        Write-Host "  OK $rVer" -ForegroundColor Green
    } else {
        # Try to find other versions
        $rDirs = Get-ChildItem "C:\Program Files\R" -Directory -ErrorAction SilentlyContinue | Sort-Object Name -Descending
        if ($rDirs) {
            $rHome = $rDirs[0].FullName
            Write-Host "  OK Found R at $rHome" -ForegroundColor Green
        } else {
            $issues += "R not installed — https://cran.r-project.org/"
            Write-Host "  MISSING R" -ForegroundColor Red
        }
    }
} catch {
    $issues += "R not installed — https://cran.r-project.org/"
    Write-Host "  MISSING R" -ForegroundColor Red
}

if ($issues.Count -gt 0) {
    Write-Host ""
    Write-Host "WARNING: The following dependencies are missing:" -ForegroundColor Magenta
    $issues | ForEach-Object { Write-Host "  * $_" -ForegroundColor Magenta }
    Write-Host ""
    $proceed = Read-Host "Continue anyway? (Some MCP services will be unavailable) [y/N]"
    if ($proceed -ne 'y' -and $proceed -ne 'Y') {
        Write-Host "Cancelled." -ForegroundColor Red
        exit 1
    }
}

# ---- Step 2: Install ocr-fallback npm dependencies ----
Write-Host ""
Write-Host "[2/5] Installing ocr-fallback dependencies..." -ForegroundColor Yellow

$ocrDir = ".reasonix\mcp-servers\ocr-fallback"
if (Test-Path "$ocrDir\package.json") {
    Push-Location $ocrDir
    try {
        if (-not (Test-Path "node_modules")) {
            npm install --silent
            Write-Host "  OK ocr-fallback dependencies installed" -ForegroundColor Green
        } else {
            Write-Host "  OK ocr-fallback dependencies already present, skipping" -ForegroundColor Green
        }
    } catch {
        Write-Host "  WARN ocr-fallback install failed (offline OCR won't work, other services unaffected)" -ForegroundColor Yellow
    }
    Pop-Location
} else {
    Write-Host "  WARN ocr-fallback directory not found, skipping" -ForegroundColor Yellow
}

# ---- Step 3: Generate global config.json ----
Write-Host ""
Write-Host "[3/5] Generating global Reasonix config..." -ForegroundColor Yellow

$globalReasonix = "$env:USERPROFILE\.reasonix"
if (-not (Test-Path $globalReasonix)) {
    New-Item -ItemType Directory -Path $globalReasonix -Force | Out-Null
}

$configPath = "$globalReasonix\config.json"

# Check if already exists
if (Test-Path $configPath) {
    Write-Host "  WARN config.json already exists, backing up as config.json.bak" -ForegroundColor Yellow
    Copy-Item $configPath "$configPath.bak" -Force
}

$config = @{
    mcp = @(
        # ---- Pure npx services (no env vars needed, direct registration) ----
        @{ name = "scholar";    command = "npx"; args = @("-y", "scholar-mcp") },
        @{ name = "article";    command = "npx"; args = @("-y", "article-mcp") },
        @{ name = "scholarly";  command = "npx"; args = @("-y", "scholarly-research-mcp") },
        @{ name = "playwright"; command = "npx"; args = @("-y", "@playwright/mcp") },
        @{ name = "thinking";   command = "npx"; args = @("-y", "@modelcontextprotocol/server-sequential-thinking") },
        @{ name = "coderunner"; command = "npx"; args = @("-y", "mcp-server-code-runner@latest") },

        # ---- Wrapper scripts (contain env vars / API keys) ----
        @{ name = "tavily";   command = "cmd"; args = @("/c", ".reasonix\\mcp-servers\\tavily.bat") },
        @{ name = "exa";      command = "cmd"; args = @("/c", ".reasonix\\mcp-servers\\exa.bat") },
        @{ name = "github";   command = "cmd"; args = @("/c", ".reasonix\\mcp-servers\\github.bat") },
        @{ name = "rplay";    command = "cmd"; args = @("/c", ".reasonix\\mcp-servers\\rplay.bat") },
        @{ name = "paddleocr"; command = "cmd"; args = @("/c", ".reasonix\\mcp-servers\\paddleocr.bat") },
        @{ name = "ocr-fallback"; command = "cmd"; args = @("/c", ".reasonix\\mcp-servers\\ocr-fallback.bat") },
        @{ name = "zotero";   command = "cmd"; args = @("/c", ".reasonix\\mcp-servers\\zotero.bat") }
    )
}

$config | ConvertTo-Json -Depth 3 | Set-Content $configPath -Encoding UTF8
Write-Host "  OK config.json generated: $configPath" -ForegroundColor Green

# ---- Step 4: Check API Key files ----
Write-Host ""
Write-Host "[4/5] Checking API Key configuration..." -ForegroundColor Yellow

$keyFiles = @(
    @{ Name = "Tavily Search"; Path = ".reasonix\mcp-servers\tavily.bat";  Key = "TAVILY_API_KEY" },
    @{ Name = "Exa Semantic";  Path = ".reasonix\mcp-servers\exa.bat";     Key = "EXA_API_KEY" },
    @{ Name = "GitHub API";    Path = ".reasonix\mcp-servers\github.bat";   Key = "GITHUB_TOKEN" },
    @{ Name = "PaddleOCR";     Path = ".reasonix\mcp-servers\paddleocr-server.mjs"; Key = "AUTH_TOKEN" }
)

$missingKeys = @()
foreach ($kf in $keyFiles) {
    if (Test-Path $kf.Path) {
        Write-Host "  OK $($kf.Name) — file present" -ForegroundColor Green
    } else {
        $missingKeys += $kf
        Write-Host "  MISSING $($kf.Name) — $($kf.Path)" -ForegroundColor Red
    }
}

if ($missingKeys.Count -gt 0) {
    Write-Host ""
    Write-Host "WARNING: The following API Key files are missing — create them manually:" -ForegroundColor Magenta
    Write-Host ""
    foreach ($mk in $missingKeys) {
        Write-Host "  $($mk.Name) -> Create $($mk.Path), example content:"
        if ($mk.Path.EndsWith('.bat')) {
            Write-Host "    @echo off"
            Write-Host "    set $($mk.Key)=YOUR_KEY_HERE"
            Write-Host "    npx -y <package-name>" -ForegroundColor DarkGray
        } elseif ($mk.Path.EndsWith('.mjs')) {
            Write-Host "    Edit the AUTH_TOKEN constant in the file"
        }
        Write-Host ""
    }
    Write-Host "  Tip: Copy these files from your original machine (they are git-ignored)" -ForegroundColor DarkGray
}

# ---- Step 5: Check path-dependent configuration ----
Write-Host "[5/5] Checking path-dependent configuration..." -ForegroundColor Yellow

$pathIssues = @()

# rplay.bat: R_HOME
if (Test-Path ".reasonix\mcp-servers\rplay.bat") {
    $rplayContent = Get-Content ".reasonix\mcp-servers\rplay.bat" -Raw
    if ($rplayContent -match 'R_HOME=(.+)') {
        $configuredRHome = $Matches[1]
        if (-not (Test-Path $configuredRHome)) {
            $pathIssues += "rplay.bat R_HOME=$configuredRHome does not exist — update to actual R path"
        }
    }
    # uvx path
    if ($rplayContent -match 'uvx\.exe') {
        $uvxPath = "$env:USERPROFILE\.local\bin\uvx.exe"
        if (-not (Test-Path $uvxPath)) {
            $pathIssues += "uvx.exe not found at $uvxPath — update uvx path in rplay.bat"
        }
    }
}

# zotero.bat: database path
if (Test-Path ".reasonix\mcp-servers\zotero.bat") {
    Write-Host "  NOTE: zotero.bat uses a placeholder db-path. Update it to your Zotero SQLite location." -ForegroundColor Yellow
    Write-Host "    Edit .reasonix\mcp-servers\zotero.bat and set --db-path to your actual path" -ForegroundColor DarkGray
}

if ($pathIssues.Count -gt 0) {
    Write-Host ""
    Write-Host "WARNING: The following paths need manual adjustment:" -ForegroundColor Magenta
    $pathIssues | ForEach-Object { Write-Host "  * $_" -ForegroundColor Magenta }
}

# ---- Done ----
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Migration Complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor White
Write-Host "  1. Restart Reasonix (new config takes effect next session)"
Write-Host "  2. If API Key files are missing, copy the .bat / .mjs files from your original machine"
Write-Host "  3. Update zotero.bat with your Zotero database path"
Write-Host "  4. Project-level skills are already in the repo — no extra steps needed"
Write-Host ""
Write-Host "MCP Services (13 total):" -ForegroundColor DarkGray
Write-Host "  Search: tavily, exa, scholar, scholarly, article"
Write-Host "  Dev:    github, playwright, thinking, coderunner"
Write-Host "  Research: rplay, zotero, paddleocr, ocr-fallback"
Write-Host ""
