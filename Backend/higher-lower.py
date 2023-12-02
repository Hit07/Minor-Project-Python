from flask import Flask

server = Flask(__name__)

IMG = 'https://media0.giphy.com/media/dH4eBrNQXB8S4/giphy.gif?cid=ecf05e47q83pw6kxvwfgr3xr2l49li8ascnckawv470bjrnh&ep=v1_gifs_related&rid=giphy.gif&ct=g'

inputs = eval(input(''))
def text_style(fn):
    def align_center():
        return f"""<h1 style='text-align: center;font-family: 'Roboto', sans-serif; color: black'>{fn()}</h1>"""

    return align_center


@text_style
@server.route("/")
def home():
    return f"<h1>Guess a number between 0 and 9 </h1>" \
           f"<img src='{IMG}'/>"


if __name__ == '__main__':
    server.run(debug=True)
