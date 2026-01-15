from flask import Flask, request

app = Flask(__name__) # create a website for me

@app.route("/")
def home():
    return "hello user!"

@app.route("/about")
def about():
    return "this is about section"

@app.route("/contact")
def contact():
    return "this is contant us page"

# handling http methods 
# GET : it is used to read the data
# POST : It is ask something to perform 

@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == 'POST':
        return "you sent the data"
    else:
        return "you are just viewing the form"