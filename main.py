from flask import Flask, render_template, request


app = Flask(__name__)
app.config['SECRET_KEY'] = 'AllanGregoryPrimaryKey'


@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        print(1)
        print(request.form)
        return render_template("index.html")
    else:
        if list(request.form.keys())[0] == "SignUp":
            return render_template("registration.html")
        elif list(request.form.keys())[0] == "SignIn":
            return render_template("signin.html")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')