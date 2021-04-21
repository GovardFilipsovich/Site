from flask import Flask, render_template, request, redirect, url_for, flash
from loginform import LoginForm
from regform import RegForm
from Editor import Editor, Start, End, Condition, Cycle, Input, Declar, Func
from data import db_session
from data.users import User
from hashlib import sha256

app = Flask(__name__)
app.config['SECRET_KEY'] = 'AllanGregoryPrimaryKey'
port = 8080
host = '127.0.0.1'
with open("static/resourses/version_num", "r") as file:
    v_num_canvas = int(file.read())

with open("static/js/editor-script.js", "w") as file:
    pass

count_menu = 0


@app.route("/")
@app.route("/index")
def index():
    return redirect("/guest/profile")


@app.route("/guest/profile", methods=["GET", "POST"])
def guest():
    global count_menu
    if request.method == "GET":
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
def page_editor(Username):
    global count_menu, v_num_canvas
    editor = Editor()
    with open("static/resourses/version_num", "w") as file:
        file.write(str(v_num_canvas))
    if request.method == "GET":
        print("Hello")
        v_num_canvas += 1
        return render_template("editor.html", name=Username, hidden="hidden", v_num_canvas=v_num_canvas)
    else:
        if list(request.form.keys())[0] == "Sett":
            if count_menu % 2 == 0:
                count_menu += 1
                return render_template("editor.html", hidden="", name=Username, v_num_canvas=v_num_canvas)
            else:
                count_menu += 1
                return render_template("editor.html", hidden="hidden", name=Username, v_num_canvas=v_num_canvas)
        elif list(request.form.keys())[0] == "Name":
            return redirect(f"/{Username}/")
        elif list(request.form.keys())[-1] == "but5":
            if request.form.get("List") == "Начало":
                with open("static/js/editor-script.js", "w") as file:
                    start = Start((275, 50))
                    editor.add_figure(start)
                    file.write(editor.get_code())
            elif request.form.get("List") == "Конец":
                with open("static/js/editor-script.js", "w") as file:
                    end = End((275, 50))
                    editor.add_figure(end)
                    file.write(editor.get_code())
            elif request.form.get("List") == "Условие":
                with open("static/js/editor-script.js", "w") as file:
                    cond = Condition((275, 50))
                    editor.add_figure(cond)
                    file.write(editor.get_code())
            elif request.form.get("List") == "Цикл":
                with open("static/js/editor-script.js", "w") as file:
                    cycle = Cycle((275, 50))
                    editor.add_figure(cycle)
                    file.write(editor.get_code())
            elif request.form.get("List") == "Ввод/вывод":
                with open("static/js/editor-script.js", "w") as file:
                    inp = Input((275, 50))
                    editor.add_figure(inp)
                    file.write(editor.get_code())
            elif request.form.get("List") == "Объявление":
                with open("static/js/editor-script.js", "w") as file:
                    decl = Declar((275, 50))
                    editor.add_figure(decl)
                    file.write(editor.get_code())
            elif request.form.get("List") == "Функция":
                with open("static/js/editor-script.js", "w") as file:
                    func = Func((275, 50))
                    editor.add_figure(func)
                    file.write(editor.get_code())
            return redirect(f"/{Username}/profile/Editor")
        elif list(request.form.keys())[-1] == "but4":
            editor.scheme[-1].move_right()
            with open("static/js/editor-script.js", "w") as file:
                file.write(editor.get_code())
            return redirect(f"/{Username}/profile/Editor")
        elif list(request.form.keys())[-1] == "but3":
            editor.scheme[-1].move_left()
            with open("static/js/editor-script.js", "w") as file:
                file.write(editor.get_code())
            return redirect(f"/{Username}/profile/Editor")
        elif list(request.form.keys())[-1] == "but1":
            editor.scheme[-1].move_up()
            with open("static/js/editor-script.js", "w") as file:
                file.write(editor.get_code())
            return redirect(f"/{Username}/profile/Editor")
        elif list(request.form.keys())[-1] == "but2":
            editor.scheme[-1].move_down()
            with open("static/js/editor-script.js", "w") as file:
                file.write(editor.get_code())
            return redirect(f"/{Username}/profile/Editor")


@app.route('/reg', methods=["GET", "POST"])
def reg():
    form = RegForm()
    if form.validate_on_submit() and form.check_password() and form.check_user() == None:
        user = User()
        user.name = form.username.data
        user.password = sha256(form.password.data.encode('utf-8')).hexdigest()
        db_sess = db_session.create_session()
        db_sess.add(user)
        db_sess.commit()
        return redirect(f'/{form.username.data}/')
    elif form.check_user() != None:
        flash(u"Такой пользователь уже есть", "error")
    elif form.check_password() is False:
        flash(u"Не совпадают пароли", "error")
    return render_template('registration.html', title='Авторизация', form=form)


@app.route('/signin', methods=["GET", "POST"])
def signin():
    form = LoginForm()
    if form.validate_on_submit() and form.is_in_db():
        return redirect(f'/{form.get_user()}/')
    return render_template('signin.html', title='Авторизация', form=form)


if __name__ == '__main__':
    db_session.global_init("db/blogs.db")
    app.run(port=port, host=host)
