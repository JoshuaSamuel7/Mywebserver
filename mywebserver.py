from http.server import HTTPServer,BaseHTTPRequestHandler

content='''
<!doctype html>
<html>
<head>
<title> My Web Server</title>
</head>
<body>
<h1> Top five Web Application Development Frameworks </h1>
<h2> 1.Django </h2>
</body>
</html>



'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request recieved...")
        self.send_response(200)
        self.end()
        self.wfile.write(content.encode())

print("This is my Webserver")
server_address=('',80)
https=HTTPSever(server_address,Myserver)
http.serve_forever()