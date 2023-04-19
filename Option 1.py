import requests

API_ENDPOINT = "https://api.openai.com/v1/engines/text-davinci-003/completions"
API_KEY = input("ENTER YOUR API KEY: ")
prompt = input("Hello I am GPT-Z, How May I Help You? ")
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + API_KEY
}
data = {
    "prompt": prompt,
    "max_tokens": 100,
    "temperature": 0.5,
}
response = requests.post(API_ENDPOINT, headers=headers, json=data)
if response.status_code != 200:
    raise ValueError("Failed to generate text, status code: " + str(response.status_code))
print(response.json()["choices"][0]["text"])
