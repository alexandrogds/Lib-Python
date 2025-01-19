
"""
"""

import requests

def f(word):
    url = f"https://dicio-api-ten.vercel.app/v2/sinonimos/livro/{word}"

    response = requests.get(url)

    if response.status_code == 200:
        synonyms = response.json()
        return synonyms
    else:
        print(f"Failed to fetch synonyms for '{word}'. Status code: {response.status_code}")
        return []
