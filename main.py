from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'AllanGregoryPrimaryKey'


@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", start_menu="-25%")
    else:
        if list(request.form.keys())[0] == "SignUp":
            return redirect("/reg")
        elif list(request.form.keys())[0] == "SignIn":
            return redirect("/signin")
        elif list(request.form.keys())[0] == "Sett":
            return render_template("index.html", start_menu="0%")


@app.route('/reg', methods=["GET", "POST"])
def reg():
    if request.method == "GET":
        return render_template("registration.html")


@app.route('/signin', methods=["GET", "POST"])
def signin():
    if request.method == "GET":
        return render_template("signin.html")


@app.route("/<Username>/profile")
def profile(Username):
    return render_template("profile.html")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
