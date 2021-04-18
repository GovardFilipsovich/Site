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
            code += i.code
        return code


class Start:
    def __init__(self, point):
        self.size = ()
        self.code = "Img = new Image();"
        self.code += f"Img.src = '{url_for('static', filename='img/start.png')}';\n"
        self.code += "Img.onload = function() {\nctx.drawImage(Img," + str(point[0]) + ", " + str(point[1]) + ");\n}\n"
