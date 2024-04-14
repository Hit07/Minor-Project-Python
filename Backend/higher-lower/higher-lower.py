import random

from flask import Flask, render_template

server = Flask(__name__)

IMG = 'https://media0.giphy.com/media/dH4eBrNQXB8S4/giphy.gif?cid=ecf05e47q83pw6kxvwfgr3xr2l49li8ascnckawv470bjrnh&ep' \
      '=v1_gifs_related&rid=giphy.gif&ct=g'
IMG_LOW = 'https://media0.giphy.com/media/8d081XOy4ZDSU/giphy.gif?cid' \
          '=ecf05e47lfetw6x9uob5cqdy2htzrb3nwdgaeu72bl6bscuh&ep=v1_gifs_search&rid=giphy.gif&ct=g'
IMG_HIGH = 'https://media0.giphy.com/media/z7Rtz6bPxpQ2c/giphy.gif?cid' \
           '=ecf05e47kyri9eeyi69zz0mdxfbp4qjv88ohs819qqweu1ib&ep=v1_gifs_search&rid=giphy.gif&ct=g'
IMG_MATCH = 'https://media0.giphy.com/media/pBIcFbc7Ru2go/giphy.gif?cid' \
            '=ecf05e47lfetw6x9uob5cqdy2htzrb3nwdgaeu72bl6bscuh&ep=v1_gifs_search&rid=giphy.gif&ct=g'


def text_style(fn):
    def align_center():
        return f"""<h1 style='text-align: center;font-family: 'Roboto', sans-serif; color: black'>{fn()}</h1>"""

    return align_center


@text_style
@server.route("/")
def home():
    return render_template('home.html',result='Guess the number between 0 and 9',image=IMG)


@server.route("/<int:input_num>")
def compare(input_num):
    num_choice = random.randint(0, 9)
    # print(num_choice)

    if num_choice > input_num:
        return render_template('result.html', result='Too Low, Try again!', image=IMG_LOW)
    elif input_num > num_choice:
        return render_template('result.html', result='Too high, Try again!', image=IMG_HIGH)
    else:
        return render_template('result.html', result='You found me!', image=IMG_MATCH)


if __name__ == '__main__':
    server.run(debug=True)

