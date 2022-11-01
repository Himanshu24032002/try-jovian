from flask import Flask
app = Flask(__name__)
#flask = module and Flask = class
#route = part of url after the domain name
@app.route("/")
def hello_himanshu():
 return "Hello, Himanshu"

if __name__== "__main__":
 app.run(host='0.0.0.0', debug=True) 
