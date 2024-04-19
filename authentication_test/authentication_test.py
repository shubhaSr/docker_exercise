import os
import requests
import time

api_address = 'fast_api_container'  # Replace with the actual API address
api_port = 8000

def perform_authentication_test(username, password):
    url = f'http://{api_address}:{api_port}/permissions'
    params = {'username': username, 'password': password}
    print("url" +url)
    response = requests.get(url, params=params)
    status_code = response.status_code
    print(response)

    output = f'''
    ============================
        Authentication test
    ============================
    request done at "/permissions"
    | username="{username}"
    | password="{password}"
    expected result = 200
    actual result = {status_code}
    ==>  {"SUCCESS" if status_code == 200 else "FAILURE"}
    '''

    if status_code == 200:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    print(output.format(status_code=status_code, test_status=test_status))
    print(output)

    if os.environ.get('LOG') == '1':
        with open('./log/api_test.log', 'a') as file:
            file.write(output)

# Perform authentication tests
perform_authentication_test('alice', 'wonderland')
perform_authentication_test('bob', 'builder')
perform_authentication_test('clementine', 'mandarine')

