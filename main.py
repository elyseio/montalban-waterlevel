from curl_cffi import requests

# XHR
url = 'https://pasig-marikina-tullahanffws.pagasa.dost.gov.ph/water/table_list.do'

try:
    resp = requests.post(url, impersonate='chrome', timeout=10)
    resp.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"[ERROR] Failed to fetch data: {e}")
    exit()

try:
    data = resp.json()
except ValueError:
    print("[ERROR] Response is not valid JSON.")
    exit()

# Filter for Montalban
montalban_data = data[4]
water_level = montalban_data.get('wl').replace('(*)', '')

if montalban_data:
    print(f"Montalban Water Level : {water_level}")
else:
    print("[INFO] Montalban station not found in the response.")

