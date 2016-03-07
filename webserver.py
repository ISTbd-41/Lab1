import http.server
import urllib

class WebServer:
        def __init__(self, port):
                self.port = port;
        
        def listen(self):
                server_address = ("localhost", self.port)
                httpd = http.server.HTTPServer(server_address, WebServerRequestHandler)
                print("Web server started on port %s" % self.port)
                httpd.serve_forever()

class WebServerRequestHandler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
                if self.path == '/1':
                        self.send_response(302)
                        self.send_header("Location", "https://oauth.vk.com/access_token?"+\
                                         "client_id=5318198&client_secret=dAkdhabnGH6eUD3XEapS&"+\
                                         "redirect_uri=http://localhost&code=1f0e801d12c3aeb3e3")
                        self.end_headers()
                        return
                if self.path == '/':
                        self.send_response(200)
                        url = 'https://oauth.vk.com/authorize?client_id=5318198&display=mobile&redirect_uri=http://localhost:12345&scope=friends&response_type=code&v=5.45'
                        s = 'Browser URL: '
                        self.send_header("Content-type", "text/html")
                        self.end_headers()
                        self.wfile.write(("%s %s" % (s, url)).encode('utf-8'))
                        return
                if self.path == '/code.php':
                        url = 'http://localhost:12345/code.php?code=abc123&test=123'
                        s = urllib.parse.urlparse(url)
                        par = urllib.parse.parse_qs(s.query)
                        self.send_response(200)
                        self.send_header("Content-type", "text/html")
                        self.end_headers()
                        self.wfile.write(("<h1> %s %s %s %s!</h1>" % (s, par['code'], par['test'], self.client_address[0])).encode('utf-8'))
                        return
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(("<h1>hello, %s %s!</h1>" % (self.path, self.client_address[0])).encode('utf-8'))

if __name__ == "__main__":
        print("Start our web server...")
        ws = WebServer(12345)
        ws.listen()
