import requests

# Exempel-URL och headers (justera efter behov)
url = "https://fakestoreapi.com/products"
headers = {"Authorization": "Bearer YOUR_API_KEY"}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Kastar ett fel vid problem
    data = response.json()  # Om svaret är JSON
    print(data)
except requests.exceptions.RequestException as e:
    print(f"Fel vid API-anrop: {e}")
