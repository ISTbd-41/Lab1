import http.server
import http.client
import urllib
a = ''
flag = True
def keep_running():
        return flag

class WebClient:
        def get(self, host, path):
                conn = http.client.HTTPSConnection(host)
                conn.request('GET', path)
                resp = conn.getresponse()
                data = resp.read()
                conn.close()
                return data

class Base64Code:
        def encoder(s):
                bRes = base64.b64encode(s.encode('utf-8'))
                sRes = bRes.decode('utf-8')
                return sRes
        def decoder(s):
                bRes = base64.b64decode(s.encode('utf-8'))
                sRes = bRes.decode('utf-8')
                return sRes

class WebServer:
        def __init__(self, port):
                self.port = port;
        
        def listen(self):
                server_address = ("", self.port)
                httpd = http.server.HTTPServer(server_address, WebServerRequestHandler)
                print("Web server started on port %s" % self.port)
                #httpd.serve_forever()
                while keep_running():
                        httpd.handle_request() 

class WebServerRequestHandler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
                if self.path == '/':
                        self.send_response(302)
                        self.send_header("Location", "https://oauth.vk.com/authorize?client_id=5347056&display=mobile&redirect_uri=http://localhost:12344/verify&scope=friends&response_type=code&v=5.45")
                        self.end_headers()
                        return
                if self.path == '/1':
                        self.send_response(200)
                        url = 'https://oauth.vk.com/authorize?client_id=5347056&display=mobile&redirect_uri=http://localhost:12344/verify&scope=friends&response_type=code&v=5.45'
                        s = 'Browser URL: '
                        self.send_header("Content-type", "text/html")
                        self.end_headers()
                        self.wfile.write(("%s %s" % (s, url)).encode('utf-8'))
                        return
                if self.path.startswith("/1verify"):
                        url = self.path
                        self.send_response(200)
                        self.senf_header("Content-type","text/html")
                        self.end_headers()
                        self.wfile.write(("%s" % url).encode('utf-8'))
                        return
                if self.path.startswith("/verify"):
                        url = self.path.split('?code=')[-1]
                        #s = urllib.parse.urlparse(url)
                        #par = urllib.parse.parse_qs(s.query)
                        self.send_response(200)
                        self.send_header("Content-type", "text/html")
                        self.end_headers()
                        self.wfile.write(("%s" % (url)).encode('utf-8'))
                        global a
                        a = url
                        
                        global flag
                        flag = False
        
if __name__ == "__main__":
        flag = True
        print("Start web server...")
        ws = WebServer(12344)
        print('Please type in the browser: \nhttps://oauth.vk.com/authorize?client_id=5347056&display=mobile&redirect_uri=http://localhost:12344/verify&scope=friends&response_type=code&v=5.45')
        ws.listen()
        wc = WebClient()
        
        print("\n\n")
        print("Web client...")
        print(a)
        pathurl= (("/access_token?client_id=5347056&client_secret=jeUsnlyxhvDNSnA5hp4I&redirect_uri=http://localhost:12344/verify&code=%s" % a))
        t = (wc.get("oauth.vk.com", pathurl)).decode('utf-8')
        print(pathurl)
        print(t)
        t = t.replace('{','')
        t = t.replace('}','')
        s = t.replace('"','')
        s = s.replace(',',':')
        slist = list(s.split(':'))
        token = slist[1]
        user = slist[-1]
        print("___________________________________________")
        print("Token: %s , User: %s" % (token, user))
        print("___________________________________________")
        method = ("/method/friends.getOnline?user_id=%s&v=5.45&access_token=%s" % (user,token))
        print(wc.get("api.vk.com",method))
        
