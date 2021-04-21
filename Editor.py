from flask import url_for


class Editor:
    scheme = []
    size = 80

    def add_figure(self, figure):
        figure.id = len(self.scheme)
        self.scheme.append(figure)

    def get_code(self):
        code = "var example = document.getElementById(\"Canvas\"),\nctx = example.getContext(" \
               "'2d');\nexample.height = 750;\nexample.width  = 650;\n"
        for i in self.scheme:
            code += i.get_code()
        return code


class Scheme_Object:
    def __init__(self, point):
        self.id = 0
        self.size = ()
        self.point = point
        self.code = ""

    def move_right(self):
        self.point = (self.point[0] + 30, self.point[1])

    def move_left(self):
        self.point = (self.point[0] - 30, self.point[1])

    def move_up(self):
        self.point = (self.point[0], self.point[1] - 30)

    def move_down(self):
        self.point = (self.point[0], self.point[1] + 30)


class Start(Scheme_Object):
    def get_code(self):
        self.code = f"Img{self.id} = new Image();"
        self.code += f"Img{self.id}.src = '{url_for('static', filename='img/start.png')}';\n"
        self.code += f"Img{self.id}.onload" + "= function()"
        self.code += "{\nctx.drawImage(" + "Img" + str(self.id) + ", " + str(self.point[0]) + ", " + str(
            self.point[1]) + ");\n}\n"
        return self.code


class End(Scheme_Object):
    def get_code(self):
        self.code = f"Img{self.id} = new Image();"
        self.code += f"Img{self.id}.src = '{url_for('static', filename='img/end.png')}';\n"
        self.code += f"Img{self.id}.onload" + "= function()"
        self.code += "{\nctx.drawImage(" + "Img" + str(self.id) + ", " + str(self.point[0]) + ", " + str(
            self.point[1]) + ");\n}\n"
        return self.code


class Condition(Scheme_Object):
    def get_code(self):
        self.code = f"Img{self.id} = new Image();"
        self.code += f"Img{self.id}.src = '{url_for('static', filename='img/condition.png')}';\n"
        self.code += f"Img{self.id}.onload" + "= function()"
        self.code += "{\nctx.drawImage(" + "Img" + str(self.id) + ", " + str(self.point[0]) + ", " + str(
            self.point[1]) + ");\n}\n"
        return self.code


class Cycle(Scheme_Object):
    def get_code(self):
        self.code = f"Img{self.id} = new Image();"
        self.code += f"Img{self.id}.src = '{url_for('static', filename='img/cycle.png')}';\n"
        self.code += f"Img{self.id}.onload" + "= function()"
        self.code += "{\nctx.drawImage(" + "Img" + str(self.id) + ", " + str(self.point[0]) + ", " + str(
            self.point[1]) + ");\n}\n"
        return self.code


class Input(Scheme_Object):
    def get_code(self):
        self.code = f"Img{self.id} = new Image();"
        self.code += f"Img{self.id}.src = '{url_for('static', filename='img/input.png')}';\n"
        self.code += f"Img{self.id}.onload" + "= function()"
        self.code += "{\nctx.drawImage(" + "Img" + str(self.id) + ", " + str(self.point[0]) + ", " + str(
            self.point[1]) + ");\n}\n"
        return self.code


class Declar(Scheme_Object):
    def get_code(self):
        self.code = f"Img{self.id} = new Image();"
        self.code += f"Img{self.id}.src = '{url_for('static', filename='img/declar.png')}';\n"
        self.code += f"Img{self.id}.onload" + "= function()"
        self.code += "{\nctx.drawImage(" + "Img" + str(self.id) + ", " + str(self.point[0]) + ", " + str(
            self.point[1]) + ");\n}\n"
        return self.code


class Func(Scheme_Object):
    def get_code(self):
        self.code = f"Img{self.id} = new Image();"
        self.code += f"Img{self.id}.src = '{url_for('static', filename='img/function.png')}';\n"
        self.code += f"Img{self.id}.onload" + "= function()"
        self.code += "{\nctx.drawImage(" + "Img" + str(self.id) + ", " + str(self.point[0]) + ", " + str(
            self.point[1]) + ");\n}\n"
        return self.code
