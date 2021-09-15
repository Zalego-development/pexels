import requests
import json
from requests.structures import CaseInsensitiveDict

def pexels():
    key_words = [
        'man', 'woman','old man','old woman','baby girl','baby boy','teenage girl','teenage boy'
        ]
    i = 6
    page = 1
    while True:
        count = 1
        for reqs in range(200):
            url = f"https://api.pexels.com/v1/search?query={key_words[i]}&per_page=80&page={page}"
            headers = CaseInsensitiveDict()
            headers["Authorization"] = "Bearer 563492ad6f9170000100000152b68c48108449c694c5e2b5571ce90a"
            resp = requests.get(url, headers=headers)
            our_json = json.loads(resp.text)
            with open(f'{key_words[i]}.txt', 'a') as pt:
                pt.write("%s\n" % our_json)
            page+=1
            count += 1
            if count == 101:
                page = 1
                i +=1
pexels()