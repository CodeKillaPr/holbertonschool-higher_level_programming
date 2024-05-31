import json
import socketserver
from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8000


class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            response = json.dumps(data).encode('utf-8')
            print(f"Response to /data: {response}")
            self.wfile.write(response)
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            status = {
                "status": "OK"
            }
            response = json.dumps(status).encode('utf-8')
            print(f"Response to /status: {response}")
            self.wfile.write(response)
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_message = {
                "error": "Endpoint not found"
            }
            response = json.dumps(error_message).encode('utf-8')
            print(f"Response to undefined endpoint {self.path}: {response}")
            self.wfile.write(response)


with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
