from flask import Flask ,request

app  =Flask(__name__)
@app.route("/")
def home():
    return 'Hello user! this is my first flask app'


@app.route("/about")
def about():
    return 'This is all about '



@app.route("/contact")
def contact():
    return 'contact Us '


@app.route("/submit",methods=["GET","POST"])
def submit():
    if request.method=="POST":
        return "You send data!"
    else:
        return "You are only viewing the form"