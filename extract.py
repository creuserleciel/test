import json

with open("raw.json") as f:
    data = json.load(f)

noms = [
    r["fields"].get("nom", "")
    for r in data.get("records", [])
    if r["fields"].get("nom")
]
noms.sort()

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(noms, f, ensure_ascii=False)

print(f"{len(noms)} élus exportés dans data.json")
