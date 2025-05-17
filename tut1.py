from flask import Flask , redirect, url_for , render_template


app = Flask(__name__)


@app.route("/admin")
def admin_():
   return "this is an admin page"


@app.route("/home<user_name>")
def index( user_name ):
    if user_name == "admin":
       return redirect(url_for("admin_"))
    else:
       return  f"hello handsome user {user_name}"
   

if __name__ == '__main__':
   app.run(debug=True , port=8000 ) # start the flask server 





