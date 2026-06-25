"""Final FishBase scrape for remaining species."""
import sqlite3, ssl, re, time
from urllib.request import urlopen, Request

DB = 'D:/Reasonix/fish-ecology-assistant/data/species.db'
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def fetch(sn):
    try:
        url = f"https://fishbase.se/summary/{sn.replace(' ','-')}"
        req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(req, timeout=8, context=ctx) as resp:
            return resp.read().decode('utf-8', errors='replace')
    except Exception:
        return None

def extract(html):
    t = {}
    m = re.search(r'Max length\s*:\s*([\d.]+)\s*cm', html)
    if m: t['max_len'] = float(m.group(1))
    m = re.search(r'Body shape.*?:\s*(\w+)', html)
    if m: t['shape'] = m.group(1).lower()
    m = re.search(r'Trophic level.*?:\s*([\d.]+)', html)
    if m: t['troph'] = float(m.group(1))
    m = re.search(r'Resilience.*?:\s*(\w+)', html)
    if m: t['resilience'] = m.group(1)
    m = re.search(r'Vulnerability.*?(\d+)\s*of\s*100', html)
    if m: t['vuln'] = float(m.group(1))
    return t

db = sqlite3.connect(DB, timeout=5)

# Focus on species missing BOTH morphology AND feeding
species = db.execute("""
    SELECT id, scientific FROM species WHERE lower_yangtze=1
    AND id NOT IN (SELECT DISTINCT species_id FROM traits_feeding WHERE trophic_level IS NOT NULL)
    LIMIT 60
""").fetchall()

print(f"Target: {len(species)} (feeding + lifestyle)")
ok = 0
for sid, sn in species:
    html = fetch(sn)
    if not html: time.sleep(0.2); continue
    t = extract(html)
    if not t or (not t.get('max_len') and not t.get('troph') and not t.get('resilience')): 
        time.sleep(0.2); continue
    
    try:
        if t.get('max_len') or t.get('shape'):
            db.execute("INSERT INTO traits_morphology(species_id,max_length_cm,body_shape,source,source_url,confidence,notes) VALUES(?,?,?,?,?,?,?)",
                (sid, t.get('max_len'), t.get('shape'), 'FishBase', 'https://fishbase.se/summary/', 3, ''))
        if t.get('troph'):
            db.execute("INSERT OR REPLACE INTO traits_feeding(species_id,trophic_level,source,confidence) VALUES(?,?,?,?)",
                (sid, t['troph'], 'FishBase', 3))
        if t.get('resilience') or t.get('vuln'):
            db.execute("INSERT OR REPLACE INTO traits_life_history(species_id,resilience,vulnerability,source,confidence) VALUES(?,?,?,?,?)",
                (sid, t.get('resilience'), t.get('vuln'), 'FishBase', 3))
        ok += 1
    except Exception:
        pass  # skip malformed entries, continue with next
    db.commit()
    time.sleep(0.5)

db.close()
print(f"\nDone: {ok} species")
