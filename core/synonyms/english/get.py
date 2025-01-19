
"""
"""

import requests

def f(word, api_key='17f3b2acffmshd9e2a5a0b1d3ea2p1a0a59jsnac4d09338abf'):
    url = f"https://wordsapiv1.p.rapidapi.com/words/{word}/synonyms"

    headers = {
        "X-RapidAPI-Key": api_key
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        synonyms = data.get("synonyms", [])
        return synonyms
    else:
        print(f"Failed to fetch synonyms for '{word}'. Status code: {response.status_code}")
        return []
