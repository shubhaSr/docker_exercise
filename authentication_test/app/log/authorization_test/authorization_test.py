import os
import requests

api_address = 'localhost'  # Replace with the actual API address
api_port = 8000

def perform_authorization_test(username, password, sentence, endpoint):
    url = f'http://{api_address}:{api_port}/{endpoint}'
    params = {'username': username, 'password': password, 'sentence': sentence}

    response = requests.get(url, params=params)
    status_code = response.status_code

    output = f'''
    ============================
        Authorization test
    ============================
    request done at "/{endpoint}"
    | username="{username}"
    | password="{password}"
    | sentence="{sentence}"
    expected result = 200
    actual result = {status_code}
    ==>  {"SUCCESS" if status_code == 200 else "FAILURE"}
    '''
    if status_code == 200:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    print(output.format(status_code=status_code, test_status=test_status))

    if os.environ.get('LOG') == '1':
        with open('api_test.log', 'a') as file:
            file.write(output)

# Perform authorization tests
perform_authorization_test('bob', 'builder', 'Some sentence', 'v1/sentiment')
perform_authorization_test('bob', 'builder', 'Another sentence', 'v2/sentiment')
perform_authorization_test('alice', 'wonderland', 'Some sentence', 'v1/sentiment')
perform_authorization_test('alice', 'wonderland', 'Another sentence', 'v2/sentiment')

