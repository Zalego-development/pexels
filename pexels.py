import requests
import json
from requests.structures import CaseInsensitiveDict

def pexels():
    key_words = [
        'man', 'woman','old man','old woman','baby girl','baby boy','teenage girl','teenage boy'
        ]
    #i is the number of the keyword you want to run eg 0 = man
    i = 0
    page = 1
    while True:
        url = f"https://api.pexels.com/v1/search?query={key_words[i]}&per_page=80&page={page}"
        headers = CaseInsensitiveDict()
        #Replace [YOUR_API_KEY] with the key that pexels generates for you.
        headers["Authorization"] = "Bearer [YOUR_API_KEY]"
        resp = requests.get(url, headers=headers)
        our_json = json.loads(resp.text)
        with open(f'{key_words[i]}.txt', 'a') as pt:
            pt.write("%s\n" % our_json)
        page+=1
    print(page)
pexels()