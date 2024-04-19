
import os
import requests

api_address = 'localhost'  # Replace with the actual API address
api_port = 8000

def perform_content_test(username, sentence, endpoint):
    url = f'http://{api_address}:{api_port}/{endpoint}'
    payload = {'username': username, 'sentence': sentence}

    response = requests.post(url, json=payload)
    sentiment_score = response.json().get('score', None)

    sentiment = "positive" if sentiment_score == 1 else "negative"

    output = f'''
    ============================
        Content test
    ============================
    request done at "/{endpoint}"
    | username="{username}"
    | sentence="{sentence}"
    sentiment result = {sentiment}
    '''

    print(output)

    if os.environ.get('LOG') == '1':
        with open('api_test.log', 'a') as file:
            file.write(output)

# Perform content tests for v1 and v2 endpoints
perform_content_test('alice', 'life is beautiful', 'v1/sentiment')
perform_content_test('alice', 'life is beautiful', 'v2/sentiment')
perform_content_test('alice', 'that sucks', 'v1/sentiment')
perform_content_test('alice', 'that sucks', 'v2/sentiment')

