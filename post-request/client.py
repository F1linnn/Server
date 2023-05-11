import requests
import argparse

# создаем парсер аргументов командной строки
parser = argparse.ArgumentParser(description='Отправка HTTP-запросов')
parser.add_argument('--url', required=True, help='URL-адрес сервера')
parser.add_argument('--method', default='GET', help='HTTP-метод запроса (по умолчанию GET)')
parser.add_argument('--headers', nargs='*', help='Заголовки запроса')
parser.add_argument('--data', help='Тело запроса в виде строки')
parser.add_argument('--file', help='Путь к файлу с телом запроса')

# парсим аргументы командной строки
args = parser.parse_args()

# формируем словарь заголовков
headers = {}
if args.headers:
    for header in args.headers:
        key, value = header.split(':')
        headers[key.strip()] = value.strip()

# отправляем запрос на сервер
if args.method == 'GET':
    response = requests.get(args.url, headers=headers)
elif args.method == 'POST':
    with open(args.file, 'rb') as f:
        print(args.file)
        files = {'filename1': args.file}
        response = requests.post(args.url, headers=files, data=f)
else:
    if args.file:
        with open(args.file, 'rb') as f:
            data = f.read()
    elif args.data:
        data = args.data.encode()
    else:
        data = None
    response = requests.request(args.method, args.url, headers=headers, data=data)

# выводим результат
print(response.status_code)
print(response.headers)
print(response.text)

#client.py --url http://localhost:8080 --method POST --file my.txt