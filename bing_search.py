import requests

subscription_key = "02283410-2548-4d41-948a-c19c40667368"
search_url = "https://api.bing.microsoft.com/"
search_term = "hadsiha"

headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
params  = {"q": search_term}

response = requests.get(search_url, headers=headers, params=params)
response.raise_for_status()
search_results = response.json()

for result in search_results["webPages"]["value"]:
    print(result["name"])
    print(result["url"])
