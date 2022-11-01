from flask import Flask, render_template
app = Flask(__name__)
#flask = module and Flask = class
#route = part of url after the domain name
@app.route("/")
def hello_himanshu():
   return render_template('home.html')

if __name__== '__main__':
 app.run(host='0.0.0.0', debug=True) 
