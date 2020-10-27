from http.server import BaseHTTPRequestHandler, HTTPServer


class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        print('In GET request')

        self.send_response(200)
        self.send_header('Content-Type', 'text-http')
        self.end_headers()

        self.wfile.write('<h1>Hello World!</h1>'.encode())


httpd = HTTPServer(('localhost', 8080), MyHandler)
print('Starting...')
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print('Bye!')
