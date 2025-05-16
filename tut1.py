from flask import Flask
app = Flask(__name__)



@app.route('/')
def home():
   return  "This is a home page"

@app.route('/<name>')
def hello_name(name):
   return  f'user name is {name}'

if __name__ == '__main__':
   app.run(debug = True)