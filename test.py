import requests

API_URL = "https://api-inference.huggingface.co/models/michellejieli/NSFW_text_classifier"
headers = {"Authorization": "Bearer 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"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


output = query({
    "inputs": "big tits woman suck dick",
})
print(output[0][0]["label"])