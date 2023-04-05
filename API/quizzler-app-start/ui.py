THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score:0", fg="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        # background_img = PhotoImage(file="background.png")
        # canvas.create_image(150, 207, image=background_img)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="",
                                                     width=250,
                                                     font=("Arial", 18),
                                                     fill="black")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image,
                                  bg=THEME_COLOR,
                                  highlightbackground=THEME_COLOR,
                                  highlightthickness=0,
                                  command=self.right_answer)

        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image,
                                   bg=THEME_COLOR,
                                   highlightbackground=THEME_COLOR,
                                   highlightthickness=0,
                                   command=self.wrong_answer)

        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        # self.window.geometry("500x500+50+50")  # Set window size and position
        # self.window.update()  # Update the window

        self.window.mainloop()
        # print("Hi")

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            self.score.configure(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            # print(q_text)
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.score.configure(fg=THEME_COLOR)
            self.canvas.itemconfig(self.question_text,
                                   text=f"🎊Done!!🎊\n"
                                        f"\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def right_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong_answer(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        self.window.after(1000, self.get_next_question)
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        # self.canvas.itemconfig(self.question_text,
        #                        text=f"🎊Done!!🎊\n"
        #                             f"\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")
        # self.quiz.score = 0
