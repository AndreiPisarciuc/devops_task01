import requests

URL = 'https://jsonplaceholder.typicode.com/comments'

# Making the request
response = requests.get(URL)

responseBody = response.json()

if responseBody:
    for element in responseBody:
        print('%s: %s' % ('postId', element['postId']))
        #print('%s: %s' % ('id', element['id']))
        #print('%s: %s' % ('name', element['name']))
        #print('%s: %s' % ('email', element['email']))
        
else:
    print('Error: empty response!')