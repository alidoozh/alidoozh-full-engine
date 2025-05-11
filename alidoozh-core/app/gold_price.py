
import requests

def get_gold_price():
    try:
        response = requests.get("https://www.gold-api.com/api/XAU/USD")
        if response.status_code == 200:
            data = response.json()
            return data.get("price")
    except Exception as e:
        print(f"Gold API error: {e}")
    return None
