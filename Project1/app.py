from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def student_profile():
    return render_template(
        "index.html",
        name="Arun",
        is_topper = True,
        subjects = ["Maths", "science", "History"]
    )