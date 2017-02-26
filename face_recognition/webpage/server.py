import SimpleHTTPServer
import SocketServer
import BaseHTTPServer

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_OPTIONS(self):           
        self.send_response(200, "ok")       
        self.send_header('Access-Control-Allow-Origin', '*')                
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")        

    def do_GET(self):
        
        print(self.path)   
        if self.path=="/":
            self.path="page.html"

        try:
            #Check the file extension required and
            #set the right mime type

            sendReply = False
            if self.path.endswith(".php"):
                selft.path = 'camsave2.php'
                mimetype='application/x-php'
                sendReply = True
            if self.path.endswith(".html"):
                mimetype='text/html'
                sendReply = True
            if self.path.endswith(".jpg"):
                mimetype='image/jpg'
                sendReply = True
            if self.path.endswith(".gif"):
                mimetype='image/gif'
                sendReply = True
            if self.path.endswith(".js"):
                self.path = "script.js"
                mimetype='application/javascript'
                sendReply = True
            if self.path.endswith(".css"):
                mimetype='text/css'
                sendReply = True

            if sendReply == True:
                #Open the static file requested and send it
                f = open(self.path) 
                self.send_response(200)
                self.send_header('Content-type',mimetype)
                self.send_header('Access-Control-Allow-Origin', '*')
                # self.send_header('Content-type',    'text/html') 
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                self.connection.shutdown(1) 
                return

        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)


        # self.send_response(200)
                                        
        # self.end_headers()              
        # self.wfile.write(f.read())
        # f.close()
        # self.connection.shutdown(1) 

    def do_POST(self):
        print(self.path)   
        if self.path=="/":
            self.path="page.html"

        try:
            #Check the file extension required and
            #set the right mime type

            sendReply = False
            if self.path.endswith(".php"):
                self.path = 'camsave2.php'
                mimetype='application/x-php'
                sendReply = True
            if self.path.endswith(".html"):
                mimetype='text/html'
                sendReply = True
            if self.path.endswith(".jpg"):
                mimetype='image/jpg'
                sendReply = True
            if self.path.endswith(".gif"):
                mimetype='image/gif'
                sendReply = True
            if self.path.endswith(".js"):
                self.path = "script.js"
                mimetype='application/javascript'
                sendReply = True
            if self.path.endswith(".css"):
                mimetype='text/css'
                sendReply = True

            if sendReply == True:
                #Open the static file requested and send it
                f = open(self.path) 
                self.send_response(200)
                self.send_header('Content-type',mimetype)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
                self.send_header("Access-Control-Allow-Headers", "X-Requested-With") 
                # self.send_header('Content-type',    'text/html') 
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                self.connection.shutdown(1) 
                return

        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)



                        
        



PORT = 8005

Handler = MyHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()