# from http.server import *
from http.server import HTTPServer, ThreadingHTTPServer, BaseHTTPRequestHandler

host = 'localhost'
port = 5555
class TestServer(BaseHTTPRequestHandler): 
    def do_GET(self): 
        self.send_response(200) 
        self.send_header('content-type', 'text/html') 
        self.end_headers() 
        self.wfile.write('<h1>Hello, world!</h1>'.encode())

    def do_POST(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write('<h1>POST request received!</h1>'.encode()) 

    def do_PUT(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write('<h1>PUT request received!</h1>'.encode())

if __name__ == '__main__': 
    server = ThreadingHTTPServer((host, port), TestServer) 
    print(f'Server running on port {port}')

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    server.server_close()
    print('Server stopped')