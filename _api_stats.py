import sys, json
d = json.load(sys.stdin)
print(f"Total: {d['total']} species")
cats = {}
for r in d['results']:
    c = r.get('conservation', '?')
    cats[c] = cats.get(c, 0) + 1
print(f"By conservation: {dict(sorted(cats.items()))}")
# Show some samples
print(f"\nFirst 5: {[r['chinese'] for r in d['results'][:5]]}")
print(f"Last 5: {[r['chinese'] for r in d['results'][-5:]]}")
