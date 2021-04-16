class Editor:
    scheme = []
    size = 80

    def add_figure(self, figure):
        self.scheme.append(figure)

    def get_code(self):
        code = ""
        for i in self.scheme:
            code += i.code
        return code


class Start:
    def __init__(self, point, radius, text=""):
        self.size = ()
        self.code = "Img.onload = function() {\nctx.drawImage(Img," + str(point[0]) + ", " + str(point[1]) + ");\n}"
