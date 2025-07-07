"""
cve_parser.py
Author: Carlos Joseph Guagnelli Villagrán

Description:
Connects to NIST's NVD public API to fetch CVE data for a given year.
Filters relevant vulnerabilities by keyword and outputs a structured CSV
with severity, attack vector, and summaries for risk analysis.

Use:
python3 cve_parser.py

Dependencies:
- requests
- csv
"""


import requests
import json
import csv
from datetime import datetime

# Año que queremos consultar 
YEAR = "2023"
NVD_FEED_URL = f"https://services.nvd.nist.gov/rest/json/cves/2.0?pubStartDate={YEAR}-01-01T00:00:00.000&pubEndDate={YEAR}-12-31T23:59:59.999"

# Filtrar CVEs que contengan estas palabras clave
KEYWORDS = ["network", "authentication", "encryption", "input validation", "buffer overflow"]

# Archivo de salida
OUTPUT_CSV = f"cves_filtered_{YEAR}.csv"

print(f"[+] Downloading CVE data from NVD for {YEAR}...")
response = requests.get(NVD_FEED_URL)
if response.status_code != 200:
    print("[-] Error fetching data from NVD")
    exit()

data = response.json()

print(f"[+] Processing {len(data.get('vulnerabilities', []))} vulnerabilities...")
filtered = []

for item in data.get("vulnerabilities", []):
    cve_id = item["cve"]["id"]
    description = item["cve"]["descriptions"][0]["value"].lower()
    published = item["cve"]["published"]

    # Extraer CVSS si existe
    metrics = item["cve"].get("metrics", {})
    if "cvssMetricV31" in metrics:
        score_info = metrics["cvssMetricV31"][0]["cvssData"]
    elif "cvssMetricV30" in metrics:
        score_info = metrics["cvssMetricV30"][0]["cvssData"]
    elif "cvssMetricV2" in metrics:
        score_info = metrics["cvssMetricV2"][0]["cvssData"]
    else:
        score_info = {}

    severity = score_info.get("baseSeverity", "N/A")
    attack_vector = score_info.get("attackVector", "N/A")

    if any(keyword in description for keyword in KEYWORDS):
        filtered.append({
            "CVE ID": cve_id,
            "Published": published,
            "Severity": severity,
            "Attack Vector": attack_vector,
            "Description": description[:100] + "..."  # Shorten for preview
        })

print(f"[+] Found {len(filtered)} matching vulnerabilities. Saving to {OUTPUT_CSV}...")

# Guardar como CSV
with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=filtered[0].keys())
    writer.writeheader()
    writer.writerows(filtered)

print("[✓] Done!")
