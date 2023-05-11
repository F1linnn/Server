import requests

def POST_request():
    url = 'http://localhost:8000'
    filename = 'my.txt'
    with open(filename, 'rb') as f:
        response = requests.post(url, headers={'filename': filename}, data=f)
        print(response.status_code)

def OPTIONS_request():
    url = 'http://localhost:8000'
    headers = {
        'Access-Control-Request-Method': 'POST',
        'Origin': 'https://my-cool-site.com'
    }
    response = requests.options(url, headers=headers)
    print(response.headers)
    print(response.status_code)


while True:
    print("POST запрос - 1\n"
          "OPTIONS запрос - 2\n"
          "EXIT - exit")
    choose = input("Ваш выбор: ")
    if choose == '1':
        POST_request()
    elif choose == '2':
        OPTIONS_request()
    elif choose == 'exit': exit()
    else: print("\nInvalid input."
                "Try again:\n")