import http.client
import base64

class WebClient:
	def get(self, host, port, path):
		conn = http.client.HTTPConnection(host, port)
		#conn = http.client.HTTPSConnection("localhost", 8080)
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
	def decode(s):
		bRes = base64.b64decode(s.encode('utf-8'))
		sRes = bRes.decode('utf-8')
		return sRes

if __name__ == "__main__":
	print("Test our web client...")
	wc = WebClient()
	#wc.get('localhost', 12345, 'oauth.vk.com')
	inp = input()
	print(wc.get('localhost',12345, inp))
