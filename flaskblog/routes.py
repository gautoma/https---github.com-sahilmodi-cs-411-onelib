from flask import render_template, url_for, flash, redirect
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User

posts = [
    {
        'author': 'Subhadip Das',
        'title': 'Post 1',
        'content': 'First post content',
        'date_posted': 'April 24, 2024'
    },
    {
        'author': 'Jane Doe',
        'title': 'Post 2',
        'content': 'Second post content',
        'date_posted': 'May 21, 2021'
    }
]



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(firstname=form.firstname.data, lastname=form.lastname.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your Account has been created','success')
        flash(f'Account created for {form.firstname.data} !', 'Success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Create Account', form=form)


@app.route("/login")
def login():
    form = RegistrationForm()
    return render_template('login.html', title='Login', form=form)