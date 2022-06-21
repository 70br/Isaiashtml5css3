
import http.server
import socketserver
import os


PORT = 33333
os.chdir('isaiashtml5css3')
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("servido iniciado", PORT)
    httpd.serve_forever()
