from flask import Flask,render_template, request

valid_users = {
    "prasxor": "123",
    "rahul": "456",
    "swetha": "789"
}

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/sumbit", methods=["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")
    # return render_template("login.html")
    # if username == "prasxor" and password == "123":
    #     return render_template("demo.html", name = username)
    # else:
    #     return "invalid credentials"
    
    if username in valid_users and password == valid_users[username]:
        return render_template("demo.html", name = username)
    else:
        return "invalid credentials"