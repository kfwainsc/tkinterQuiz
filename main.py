#  main.py     
#  Kendra Wainscott    TFD Quiz Project          2022
#############################################################
#  This file contains the driver code for TFD quiz program 
#############################################################
from tkinter import *
from tkinter import messagebox as mb
from questions_protocol import inQuestions, quizTitle
#from PIL import Image, ImageTk

from quizBody import Quiz

class QuizGui(Quiz):

    def __init__(self, title, questList):
        self.root = Tk()
        self.root.geometry("1200x700")
        self.root.title(quizTitle)

        super().__init__(questList)
        self._choiceBtns = [] 
        self._questLabel = None
        self._resourceLabel = None
        self._message = None
        self._selected = StringVar() # selected option

        self.makeChoiceBtns()
        self.showTitle(title)
        self.showQuestion()
        self.showChoices()
        self.next_check_quit_btns()

        self.root.mainloop()

    # Job: create list of radio btns for answer choices from current question
    def makeChoiceBtns(self, ):
        self._choiceBtns = self._qList[self._cur].choiceBtns(self.root, self._selected)
        #starting pos
        y_pos = 300 
        for choice in self._choiceBtns:
            choice.place(x = 100, y = y_pos)
            y_pos += 50  # move y-axis pos

    # Job: display quiz title @ top of window 
    # Arg: title of current question
    # Ret: title
    def showTitle(self, inTitle):
        title = Label(self.root, text=inTitle, wraplength=1000, justify=CENTER, anchor='w', height=3, width=100,
                bg="black", fg="red", font=("stencil",28))
        title.place(x=0, y=2)

    # Job: shows the current Question on the screen
    # Arg: 
    # Ret: 
    def showQuestion(self):
        if self._questLabel != None:
            self._questLabel.destroy()
        self._questLabel = Label(self.root, text=self._qList[self._cur].get('Q'),
                           pady=20, justify=LEFT, anchor='w', width=600, font=('ariel',14,'bold'))
        self._questLabel.place(x=70, y=150)

    # Job: clears last choice, display current question
    # Arg: list of options for current question
    # Ret: 
    def showChoices(self):
        self._selected.set(0) # deselecting the options
        self.clearChoices()
        self.makeChoiceBtns()

    # Job: clears all choices from window 
    # Arg: list of options for current question
    # Ret: 
    def clearChoices(self):
        for choice in self._choiceBtns:
            choice.destroy()

    # Job:
    # Arg:
    # Ret:
    def next_check_quit_btns(self):
        # CHECK BUTTON
        checkBtn = Button(self.root, text="Check", command=self.check,
                   width=10,bg="black",fg="white",font=("ariel",16,"bold"))
        checkBtn.place(x=250,y=610)
        # NEXT BUTTON
        nextBtn = Button(self.root, text="Next", command=self.next,
                  width=10,bg="black",fg="white",font=("ariel",16,"bold"))
        nextBtn.place(x=100,y=610)
        # QUIT BUTTON 
        quitBtn = Button(self.root, text="Quit", command=self.root.destroy,
                      width=5, bg="black", fg="white",font=("ariel",16," bold"))
        quitBtn.place(x=1100,y=20)

    # Job:
    # Arg:
    # Ret:
    def check(self):
        if self.checkAnswer(self._selected.get()):
            self._message = Label(self.root, text="Good Work!", anchor='w', 
                            width=55, fg="green", font=("ariel",14,"bold"))
        else:
            self._message = Label(self.root, text="Correct Answer:", width=55,
                            anchor='w', fg="red", font=("ariel",14,"bold"))
        self._message.place(x=700, y=300)       
        self._resourceLabel = self._qList[self._cur].resourceLabel(self.root)
        self._resourceLabel.place(x=700, y=350)

    # Job: checks user Answer after NEXT is clicked
    # Arg: 
    # Ret: True/False
    def next(self):
        self._cur += 1
        if self.endQuiz():
            self.showStats()
            self.root.destroy()
            quit()
        else:
            if self._message != None:
                self._message.destroy()
            if self._resourceLabel != None:
                self._resourceLabel.destroy()
            self.showQuestion()
            self.showChoices()

    # displays at end as a message Box
    def showStats(self):
        numCorrect =  0
        for q in self._qList:
            correct = q.getStats()
            if correct[0]:
                numCorrect += 1
        numWrong = self._numQs - numCorrect 
        correct = f"Correct: {numCorrect}"
        wrong = f"Wrong: {numWrong}"
        score = int(numCorrect / self._numQs * 100)
        result = f"Score: {score}%"
        # message box to show stats
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")


def main():

    quiz = QuizGui(quizTitle, inQuestions)


if __name__ == "__main__":
    main()
