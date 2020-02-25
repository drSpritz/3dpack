import SimpleHTTPServer
import SocketServer

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("192.168.0.102", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()