from flask import Flask

app = Flask(__name__)

IMG = 'https://media0.giphy.com/media/SIuI7syOPvm1HAd5GF/giphy.gif?cid' \
      '=ecf05e47cb9li5xlftjs2ttylits0dlvv4eh7ck72es1q1ei&ep=v1_gifs_search&rid=giphy.gif&ct=g'


def make_align_center(func):
    def align_center():
        return f"""<h1 style='text-align:center'>{func()}</h1>"""

    return align_center


def set_font(func):
    def font_style():
        return f"""<h1 style="font-family: Arial, sans-serif;background-color: #f2f2f2;color: #333;">{func()}</h1>"""

    return font_style


@app.route("/sample")
@set_font
@make_align_center
def sample():
    return 'Sample'


@app.route("/")
def home():
    return "<html style='background-color:black'>" \
           "<h1 style='text-align:Center;color:red'>GOKU</h1>" \
           "<p style='text-align:center;color: brown;'></p>" \
           f"<img style='margin-left:33%; height:600px;width:600px'  src='{IMG}'/></html>"


@app.route('/<name>')
def hello(name):
    return f'Hello {name}'


@app.route('/<name>/<int:age>')
def age_name(age, name):
    return f'My name is {name}, age is {age}'


# @app.route('/username/<path:name>')
# def bye(name):
#     return f'Bye {name}'


if __name__ == '__main__':
    app.run(debug=True)

# -------------------------PYTHON DECORATORS-------------------------------------------------
# import time
#
# current_time = time.time()
# print(current_time)
#
#
# def speed_calc_decorator(func):
#     def wrapper():
#         start_time = time.time()
#         func()
#         end_time = time.time()
#         print(f"{func.__name__} run speed : {end_time - start_time}")
#
#     return wrapper()
#
#
# @speed_calc_decorator
# def fast_function():
#     for i in range(1000000):
#         i * i
#
#
# @speed_calc_decorator
# def slow_function():
#     for i in range(10000000):
#         i * i
#
#
# if __name__ == "__main__":
#     fast_function()
#     slow_function()
# -----------------------------------------------------------------------------
