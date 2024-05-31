import socketserver
import http.server

PORT = 8000


class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            # Handle the root endpoint
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Hello, World!')
        else:
            # Handle undefined endpoints
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Endpoint not found')


with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
