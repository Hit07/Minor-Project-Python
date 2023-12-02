# ------------Advance Python decorators using positional args and keyword args--------------------------
# from flask import Flask
#
# mod = Flask(__name__)
#

# class User:
#
#     def __init__(self, name_of_user):
#         self.name = name_of_user
#         self.signed_up = False
#
#
# def authenticate_user(function):
#     def wrapper(*args, **kwargs):
#         if args[0].signed_up:
#             function(args[0])
#
#     return wrapper
#
#
# @authenticate_user
# def created_post(new_user):
#     print(f"{new_user.name} has new update!!")
#
#
# obj = User("hitesh")
# obj.signed_up = True
# created_post(new_user=obj)
#
# if __name__ == "__main__":
#     mod.run()
# ----------------------------------------------------------------------------------------------

# inputs = eval(input())
# def logging_decorator(function):
#     def wrapper(*args, **kwargs):
#         print(f'You called {function.__name__}({args[0]}, {args[1]}, {args[2]})')
#         result = function(*args, **kwargs)
#         print(f'It returned:{result}')
#     return wrapper
#
#
# @logging_decorator
# def a_function(a, b, c):
#     return a * b * c
#
#
# a_function(inputs[0], inputs[1], inputs[2])
