import http.server
import socketserver
import os

PORT = 8000
DIRECTORY = 'C:/Users/100NOUT/PycharmProjects/Network_5/myfiles' # указываете путь к вашей директории
LOG_FILE = "logfile.log"

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        filename = self.headers['filename']
        with open(os.path.join(DIRECTORY, filename), 'wb') as f:
            f.write(self.rfile.read(content_length))
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', 'https://my-cool-site.com')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', 'https://my-cool-site.com')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Allow', 'GET, POST, OPTIONS')
        self.end_headers()

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', 'https://my-cool-site.com')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        super().end_headers()

    def log_request(self, code='-', size='-'):
        with open(LOG_FILE, 'a') as f:
            f.write('%s - - [%s] "%s" %s %s\n' % (
            self.client_address[0], self.log_date_time_string(), self.requestline, str(code), str(size)))

os.chdir(DIRECTORY)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()



