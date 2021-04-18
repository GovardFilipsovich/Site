from flask import url_for


class Editor:
    scheme = []
    size = 80

    def add_figure(self, figure):
        self.scheme.append(figure)

    def get_code(self):
        code = "var example = document.getElementById(\"Canvas\"),\nctx = example.getContext(" \
               "'2d');\nexample.height = 750;\nexample.width  = 650;\n"
        for i in self.scheme:
            code += i.get_code()
        return code


class Scheme_Object:
    def __init__(self, point):
        self.size = ()
        self.point = point
        self.code = ""


class Start(Scheme_Object):
    def get_code(self):
        self.code = "Img = new Image();"
        self.code += f"Img.src = '{url_for('static', filename='img/start.png')}';\n"
        self.code += "Img.onload = function() {\nctx.drawImage(Img," + str(self.point[0]) + ", " + str(
            self.point[1]) + ");\n}\n"
        return self.code


class End(Scheme_Object):
    def get_code(self):
        self.code = "Img = new Image();"
        self.code += f"Img.src = '{url_for('static', filename='img/end.png')}';\n"
        self.code += "Img.onload = function() {\nctx.drawImage(Img," + str(self.point[0]) + ", " + str(
            self.point[1]) + ");\n}\n"
        return self.code


class Condition(Scheme_Object):
    def get_code(self):
        self.code = "Img = new Image();"
        self.code += f"Img.src = '{url_for('static', filename='img/condition.png')}';\n"
        self.code += "Img.onload = function() {\nctx.drawImage(Img," + str(self.point[0]) + ", " + str(
            self.point[1]) + ");\n}\n"
        return self.code


class Cycle(Scheme_Object):
    def get_code(self):
        self.code = "Img = new Image();"
        self.code += f"Img.src = '{url_for('static', filename='img/cycle.png')}';\n"
        self.code += "Img.onload = function() {\nctx.drawImage(Img," + str(self.point[0]) + ", " + str(
            self.point[1]) + ");\n}\n"
        return self.code

class Input(Scheme_Object):
    def get_code(self):
        self.code = "Img = new Image();"
        self.code += f"Img.src = '{url_for('static', filename='img/input.png')}';\n"
        self.code += "Img.onload = function() {\nctx.drawImage(Img," + str(self.point[0]) + ", " + str(
            self.point[1]) + ");\n}\n"
        return self.code


class Declar(Scheme_Object):
    def get_code(self):
        self.code = "Img = new Image();"
        self.code += f"Img.src = '{url_for('static', filename='img/declar.png')}';\n"
        self.code += "Img.onload = function() {\nctx.drawImage(Img," + str(self.point[0]) + ", " + str(
            self.point[1]) + ");\n}\n"
        return self.code


class Func(Scheme_Object):
    def get_code(self):
        self.code = "Img = new Image();"
        self.code += f"Img.src = '{url_for('static', filename='img/function.png')}';\n"
        self.code += "Img.onload = function() {\nctx.drawImage(Img," + str(self.point[0]) + ", " + str(
            self.point[1]) + ");\n}\n"
        return self.code
