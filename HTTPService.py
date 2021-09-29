from http.server import HTTPServer, BaseHTTPRequestHandler

# Class to define the HTTP endpoints
class helloworld(BaseHTTPRequestHandler):
    # HTTP endpoint /helloworld
    def do_GET(self):
        if self.path.endswith('helloworld'):
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            self.wfile.write('"Hello Stranger"\n'.encode())

def main():
    PORT = 8080
    server = HTTPServer(('', PORT), helloworld)
    print('Server running on port %s' % PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()