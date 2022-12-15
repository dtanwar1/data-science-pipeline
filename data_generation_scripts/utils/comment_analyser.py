import requests
import json

# key new_d AIzaSyCaMtCrjMgdytO0ShcIyu-z-Tgsf6iH0_c
#key old AIzaSyBEcF8TGrTX7VagfgF0TFc_ord6y8EYE1c
#key temp AIzaSyDHfMQmGuadUpIU-SHp_91aM6r1pnhftBw
#key temp1 AIzaSyA-5FZ9evYw49HwLWJ5tVdp7GfGipbbKig
def analyseComment(text) :
    url = "https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze?key=AIzaSyA-5FZ9evYw49HwLWJ5tVdp7GfGipbbKig"

    payload = json.dumps({
    "comment": {
        "text": text
    },
    "languages": [
        "en"
    ],
    "requestedAttributes": {
        "TOXICITY": {}
    }
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    try :
        resp = response.json()
        return resp["attributeScores"]["TOXICITY"]["summaryScore"]["value"]  
    except:
        return 0
