from flask import Flask, render_template, redirect, request, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key="oiwajefoaiwnegwboughuao"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def results():
    error = False
    if len(request.form['fname']) < 1:
        flash("First Name cannot be empty!", "error") # just pass a string to the flash function
        error = True
    elif not request.form['fname'].isalpha():
        flash("First Name cannot contain numbers!", "error")
        error = True
    if len(request.form['lname']) < 1:
        flash("Last Name cannot be empty!", "error")
        error = True
    elif not request.form['lname'].isalpha():
        flash("Last Name cannot contain numbers!", "error")
        error = True
    if len(request.form['email']) < 1:
        flash("Email cannot be empty!", "error")
        error = True
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", "error")
        error = True
    if len(request.form['password']) < 1:
        flash("Password cannot be empty!", "error")
        error = True
    elif len(request.form['password']) < 8:
        flash("Password must be longer than 8 characters", "error")
        error = True
    if request.form['password'] != request.form['confirmPassword']:
        flash("Passwords don't match!", "error")
        error = True
    if not error:
        session.clear()
        flash("success", "success")
        return redirect('/')

    flash(request.form, "data")

    return redirect('/') # either way the application should return to the index and display the message

@app.route("/display_results")
def display():
    return render_template("results.html")

app.run(debug=True)