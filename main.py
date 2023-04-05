import requests

URL = 'https://jsonplaceholder.typicode.com/comments'

response = requests.get(URL)

if response.status_code == 200:
    response_body = response.json()
    
    response_text = ''.join(str(element) for element in response_body)
    
    num_chars = len(response_text)
    
    
    print(num_chars)
else:
   
    print(f"Error: {response.status_code} - {response.reason}") 
