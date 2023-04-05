import requests

URL = 'https://jsonplaceholder.typicode.com/comments'

# Making the request
response = requests.get(URL)

responseBody = response.json()

longestEmail = ""

if responseBody:
    for element in responseBody:
        email = element['email']
        if len(email) > len(longestEmail):
            longestEmail = email

    print(longestEmail)
else:
    print('Error: empty response!')
