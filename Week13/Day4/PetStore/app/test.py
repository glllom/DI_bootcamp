import requests
print((requests.get("https://dog.ceo/api/breed/doberman/images/random")).json()['message'])
