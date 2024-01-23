from flask import render_template,url_for,flash,redirect
from flaskblog.form import signup,login
from flaskblog.models import User,Posts
from flaskblog import app
posts=[
{
    'author':"Melona Pandey",
    'title':"1st blog",
    "content": "temp1",
    "date":"21-01-2024"
},
{
    'author':"Rajesh Mukhwas",
    'title':"2nd blog",
    "content": "temp2",
    "date":"13-04-2024"
},
{
    'author':"Aditya Roy Kapoor",
    'title':"3rd blog",
    "content": "temp3",
    "date":"21-06-2023"
}

]


@app.route("/")
def home():
    return render_template('home.html',posts=posts)


@app.route("/aboutus")
def about():
    return render_template('aboutus.html')

@app.route("/register", methods=['GET','POST'])
def register():
    form=signup()
    if form.validate_on_submit():
        flash(f'Account creation for {form.username.data}','success')
        return redirect(url_for('home'))
    return render_template('register.html',form=form,title='register')

@app.route("/login")
def login_route():
    form=login()
    return render_template('login.html',form=form,title='login')
