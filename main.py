from curl_cffi import requests

# XHR
url = 'https://pasig-marikina-tullahanffws.pagasa.dost.gov.ph/water/table_list.do'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'X-Requested-With': 'XMLHttpRequest',
    'Accept': 'application/json',
}

try:
    resp = requests.post(url, headers=headers, impersonate='chrome', timeout=10)
    resp.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"[ERROR] Failed to fetch data: {e}")
    exit()

try:
    data = resp.json()
except ValueError:
    print("[ERROR] Response is not valid JSON.")
    exit()

# Filter for Montalban station by ID or name
montalban_data = data[4]

if montalban_data:
    print(f"Montalban Water Level : {montalban_data.get('wl')}m")
else:
    print("[INFO] Montalban station not found in the response.")

