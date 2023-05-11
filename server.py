import os
import socket
import logging

HOST = ''  # Принимаем соединения с любых IP-адресов
PORT = 8080  # Используем порт 8080

# Конфигурация заголовков по умолчанию
DEFAULT_HEADERS = {
    'Access-Control-Allow-Origin': 'https://my-cool-site.com',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS'
}

# Сообщения статусов HTTP-ответов
HTTP_RESPONSE_MESSAGES = {
    200: 'OK',
    400: 'Bad Request',
    403: 'Forbidden',
    404: 'Not Found',
    500: 'Internal Server Error'
}

def create_logger(logfile_path):
    """
    Создает журнальный файл и настраивает логгер
    """
    # Создаем объект логгера
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)

    # Создаем объект обработчика для записи в файл
    file_handler = logging.FileHandler(logfile_path)

    # Настраиваем формат записей в журнале
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Добавляем обработчик в логгер
    logger.addHandler(file_handler)

    return logger



def handle_request(client_socket):
    loger = create_logger("logfile.log")
    # Получаем данные от клиента
    data = client_socket.recv(1024)
    # print(data)
    response = ''
    if not data:
        # Если данные не получены, закрываем соединение
        client_socket.close()
        return

    # Преобразуем данные в строку
    request = data.decode('utf-8')

    # Разбиваем строку запроса на части
    # print("tut",request.split('\r\n\r\n'))
    headers, body = request.split('\r\n\r\n')
    # print(headers,"\n body", body)
    headers = headers.split('\r\n')
    # print(headers)
    method, path, _ = headers[0].split(' ')
    # print(method,path,_)
    if path =="/favicon.ico":
        client_socket.close()
        return
    # Проверяем метод запроса
    if method == 'GET':
        # Обработка корневого пути
        if path == '/':
            path = 'C:/Users/100NOUT/PycharmProjects/Network_5/myfiles'
        # Формируем полный путь к файлу на сервере
        file_path = '.' + path
        # Инициализируем переменную response_headers
        response_headers = {}

        # Проверяем, существует ли файл
        if not os.path.exists(file_path):
            # Если файл не существует, отправляем клиенту статус 404 Not Found
            response_status = '404 Not Found'
            response_body = b'<h1>404 Not Found</h1>'
            loger.error("404 Not Found" + "path:"+file_path)
        else:
            # Если файл существует, читаем его содержимое
            with open(file_path, 'rb') as file:
                response_body = file.read()

        # Определяем тип содержимого
        content_type = 'text/html'
        if file_path.endswith('.txt'):
            content_type = 'text/txt'
        elif file_path.endswith('.js'):
            content_type = 'application/javascript'
        elif file_path.endswith('.svg'):
            content_type = 'image/svg+xml'
        elif file_path.endswith('.png'):
            content_type = 'image/png'

        # Формируем заголовки ответа
        response_headers = {
            'Content-Type': content_type,
            'Content-Length': str(len(response_body)),
            **DEFAULT_HEADERS
        }

        # Формируем успешный ответ с заголовками и телом
        response_status = '200 OK'
        response_headers = {}
        if 'response_headers' in locals():
            response_headers = {
                'Content-Type': content_type,
                'Content-Length': str(len(response_body)),
                **DEFAULT_HEADERS
            }
        response = f'HTTP/1.1 {response_status}\r\n'
        for header_name, header_value in response_headers.items():
            response += f'{header_name}: {header_value}\r\n'
        response += '\r\n'
        response = response.encode('utf-8') + response_body

        loger.info(f"Method:{headers[0]}, {response_status}, path:{file_path}")

    elif method == 'POST':
        file = '.' + path
        for header in range(len(headers)):
            if 'filename1:' in headers[header]:
                file = headers[header].split(" ")[1]
                break
        # print(file)
        if path == '/':
            path = 'C:/Users/100NOUT/PycharmProjects/Network_5/myfiles'
        # Формируем полный путь к файлу на сервере
        file_path = path +'/' + file
        # print(request_parts)
        # print(file_path)
        # Инициализируем переменную response_headers
        response_headers = {}
        # print("Туть ->", os.path.exists(file_path))
        # Проверяем, существует ли файл
        if os.path.exists(file_path):
            # Если файл уже существует, отправляем клиенту статус 403 Forbidden
            response_status = '403 Forbidden'
            response_body = b'<h1>403 Forbidden</h1>'
            loger.info(f"Method:{method}, status: {response_status}")
            # print("im here")
            # Формируем полный HTTP-ответ
            response = f'HTTP/1.1 {response_status}\r\n'
            for header_name, header_value in response_headers.items():
                response += f'{header_name}: {header_value}\r\n'
            response += '\r\n'
            response = response.encode('utf-8') + response_body
        else:
            # Если файл не существует, получ
            content_length = 0
            # print(request_parts)
            for header in headers:
                if 'Content-Length:' in header:
                    content_length = int(header.split(" ")[1])
                    break
            # print(content_length)
            request_body = body
            # print(type(request_body))
            # Записываем содержимое в новый файл
            # print(file_path, file)
            with open(os.path.join(path, file), 'w') as file:
                file.write(str(request_body))
            # print("here2")
            # Формируем заголовки ответа
            response_headers = {
                'Content-Type': 'text/txt',
                'Content-Length': f'{content_length}',
                **DEFAULT_HEADERS
            }

            # Формируем успешный ответ с заголовками и пустым телом
            response_status = '200 OK'
            response_body = b''
            # loger.info(f"Method:{request_parts[0]}, status: {response_status}")
            # Формируем полный HTTP-ответ
            # print("here3")
            response = f'HTTP/1.1 {response_status}\r\n'
            for header_name, header_value in response_headers.items():
                response += f'{header_name}: {header_value}\r\n'
            response += '\r\n'
            response = response.encode('utf-8') + response_body

    elif method == "OPTIONS":
        response_status = '200 OK'
        response_body = b''
        # Формируем полный HTTP-ответ
        response_headers = {}
        if 'response_headers' in locals():
            response_headers = {
                'Access-Control-Allow-Origin': 'https://my-cool-site.com',
                'Access-Control-Allow-Headers': 'Content-type',
                'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
                **DEFAULT_HEADERS
            }
        response = f'HTTP/1.1 {response_status}\r\n'
        for header_name, header_value in response_headers.items():
            response += f'{header_name}: {header_value}\r\n'
        response += '\r\n'
        response = response.encode('utf-8') + response_body

        loger.info(f"Method:{method}, status: {response_status}")

    else:
        #Метод не поддерживается
        response_status = '405 Method Not Allowed'
        response_body = b''
        # Формируем полный HTTP-ответ
        response_headers = {}
        if 'response_headers' in locals():
            response_headers = {
                'Content-Type': 'text/html',
                'Content-Length': '0',
                'Allow': 'GET, POST, OPTIONS',
                **DEFAULT_HEADERS
            }
        response = f'HTTP/1.1 {response_status}\r\n'
        for header_name, header_value in response_headers.items():
            response += f'{header_name}: {header_value}\r\n'
        response += '\r\n'
        response = response.encode('utf-8') + response_body

        loger.info(f"Method:{method}, status: {response_status}")

    # Отправляем HTTP-ответ клиенту
    print(response)
    client_socket.sendall(response)

    # Закрываем соединение
    client_socket.close()


def start_server():
    # Создаем сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Привязываем сокет к указанному хосту и порту
    server_socket.bind((HOST, PORT))

    # Начинаем слушать порт
    server_socket.listen()
    print(f'Server listening on port localhost:{PORT}')

    # В бесконечном цикле принимаем соединения
    while True:
        # Принимаем входящее соединение
        client_socket, address = server_socket.accept()
        # print(address)
        # Обрабатываем запрос в отдельном потоке
        handle_request(client_socket)

start_server()