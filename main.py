from flask import Flask, render_template, request, redirect
from loginform import LoginForm
from regform import RegForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'AllanGregoryPrimaryKey'

count_menu = 0


@app.route("/")
@app.route("/index")
def index():
    return redirect("/guest/profile")


@app.route("/guest/profile", methods=["GET", "POST"])
def guest():
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
            if count_menu % 2 == 0:
                count_menu += 1
                return render_template("index.html", hidden="")
            else:
                count_menu += 1
                return render_template("index.html", hidden="hidden")

@app.route("/<Username>/", methods=["GET", "POST"])
def redir(Username):
    return redirect(f"/{Username}/profile")


@app.route("/<Username>/profile", methods=["GET", "POST"])
def profile(Username):
    global count_menu
    if request.method == "GET":
        count_menu = 0
        return render_template("profile.html", name=Username, hidden="hidden",
                               functional="Для вас доступен весь функционал сайта")
    else:
        if list(request.form.keys())[0] == "Sett":
            if count_menu % 2 == 0:
                count_menu += 1
                return render_template("profile.html", hidden="", name=Username)
            else:
                count_menu += 1
                return render_template("profile.html", hidden="hidden", name=Username)
        elif list(request.form.keys())[0] == "Name":
            return render_template("profile.html", name=Username, hidden="hidden",
                                   functional="Для вас доступен весь функционал сайта")


@app.route("/<Username>/profile/Editor", methods=["GET", "POST"])
def Editor(Username):
    global count_menu
    if request.method == "GET":
        count_menu = 0
        return render_template("editor.html", name=Username, hidden="hidden")
    else:
        if list(request.form.keys())[0] == "Sett":
            if count_menu % 2 == 0:
                count_menu += 1
                return render_template("editor.html", hidden="", name=Username)
            else:
                count_menu += 1
                return render_template("editor.html", hidden="hidden", name=Username)
        elif list(request.form.keys())[0] == "Name":
            return redirect(f"/{Username}/")


@app.route('/reg', methods=["GET", "POST"])
def reg():
    form = RegForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('registration.html', title='Авторизация', form=form)


@app.route('/signin', methods=["GET", "POST"])
def signin():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('signin.html', title='Авторизация', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
