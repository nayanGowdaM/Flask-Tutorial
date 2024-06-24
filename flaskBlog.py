from flask import Flask, render_template , flash,redirect, url_for
from forms import RegistrationForm, LoginForm

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


app = Flask(__name__)
app.config['SECRET_KEY'] = '23a230f1e6975df4fd7e0b23135ce83b'

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html" ,posts=posts ,title="Home")

@app.route("/about")
def about():
    return render_template("about.html",title="About")

@app.route("/register", methods=['GET','POST'])
def register(): 
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template( "register.html", title='Register', form=form)

@app.route("/login",  methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template( "login.html", title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)