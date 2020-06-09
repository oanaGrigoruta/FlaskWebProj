from flask import Flask, redirect, url_for,render_template,request,session

from datetime import timedelta
from flask.helpers import flash



app=Flask(__name__)
app.secret_key= "hello"
app.permanent_session_lifetime= timedelta(minutes=5)


@app.route("/")
def home():
    # return "Hello! Test <h1>Hello</h1 >"
    return render_template("index.html")

@app.route("/testing")
def test():
    # return "Hello! Test <h1>Hello</h1 >"
    return render_template("new.html")

@app.route("/login",methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent=True
        user=request.form["nm"]
        session['user']=user
        flash(f"Logged in succesful!", "info")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already logged In!", "info")
            return redirect(url_for("user"))

        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user=session["user"]
        return render_template("user.html",user=user)
    else:
        flash("You are now logged in", "info")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    flash("You have been logged out", "info")
    session.pop("user",None)
    return redirect(url_for("login"))


# @app.route("/<name>")
# def user(name):
#     return f"Hello {name}!"

# @app.route("/admin/")
# def admin():
#     return redirect(url_for("home",name="Admin!"))

# ChECK Oana repo

if __name__=='__main__':
    app.run(debug=True)
