from flask import Flask,render_template,request,url_for,flash,redirect
from forms import RegistrationForm

app = Flask(__name__)
app.secret_key = "my-secret-key"

# @app.route("/", methods=["GET", "POST"])
# def form():
#     if request.method == 'POST':
#         name = request.form.get("username")
#         if not name:
#             flash("Name cannot be empty")
#             return redirect(url_for("form"))
#         flash(f"Thanks {name}, your feedback was save")
#         return redirect(url_for("thankyou"))
#     return render_template("form.html")

# @app.route("/thankyou")
# def thankyou():
#     return render_template("thankyou.html")

@app.route("/", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        flash(f"welcome, {name}! you Registered Successfully", "success")
        return redirect(url_for("success"))
    return render_template("register.html", form=form)

@app.route("/success")
def success():
    return render_template("success.html")

# redirect is used for redirecting the page without reload
# good and bad syntax for it 
# redirect(url_for("file_name")) - its good
# redirect("/file_name") - its breaks when file not found