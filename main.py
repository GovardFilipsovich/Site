from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'AllanGregoryPrimaryKey'

count_menu = 0

@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def index():
    global count_menu
    if request.method == "GET":
        count_menu = 0
        return render_template("index.html", hidden="hidden")
    else:
        if list(request.form.keys())[0] == "SignUp":
            return redirect("/reg")
        elif list(request.form.keys())[0] == "SignIn":
            return redirect("/signin")
        elif list(request.form.keys())[0] == "Sett":
            print(count_menu)
            if count_menu % 2 == 0:
                count_menu += 1
                return render_template("index.html", hidden="")
            else:
                count_menu += 1
                return render_template("index.html", hidden="hidden")


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
