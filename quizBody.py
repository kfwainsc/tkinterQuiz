#  quizBody.py     
#  Kendra Wainscott    TFD Quiz Project          2022
################################################################
#  File contains implementation of the Quiz & Question classes 
################################################################
import random
from tkinter import *
#from tkinter import Radiobutton, Label


# QUESTION #####################################################
#            'attempts' number of times question attempted
#            'correct'  right answer has been given 
#            'resources' additional info to explain answer
class Question:
    def __init__(self, question):
        self._attempts = 0
        self._correct = False
        self._question = question[0]
        self._choices = question[1]
        self._answer = question[1][0]
        self._resources = question[2] 

    def isCorrect(self, answer):
        if self._answer == answer:
            self._attempts += 1
            self._correct = True
        return self._correct

    def get(self, field):
        if field == 'Q': return self._question
        if field == 'C': return self._choices
        if field == 'A': return self._answer
        if field == 'R': return self._resources
        else: raise Exception("Invalid Question Field")

    def getStats(self):
        return (self._correct, self._attempts)

    # Job: make buttons for answer choices
    # Arg: root window, select variable for buttons in gui
    # Ret: list of answer choices as radio buttons 
    def choiceBtns(self, root, var):
        cBtnList = []
        for choice in self._choices:
            cBtn = Radiobutton(root, text=choice, wraplength=550, justify=LEFT, anchor='w', variable=var, 
                                value=choice, font=("ariel",12))
            cBtnList.append(cBtn)
        # mix up order of answer choices 
        random.shuffle(cBtnList)
        return cBtnList

    # Job: make resources lable
    # Arg: root window
    # Ret: resources for the correct answer 
    def resourceLabel(self, root):
        resource = Label(root, text=self._resources, wraplength=900, justify=LEFT, anchor='w',width=50, 
                bg="light gray", fg="black", font=("ariel",12))
        return resource

class Quiz:

    def __init__(self, inputQs):
        self._numQs = len(inputQs)
        self._cur = 0             
        self._qList= []
        for x in range(len(inputQs)):
           self._qList.append(Question(inputQs[x]))

    def checkAnswer(self, answer):
        return self._qList[self._cur].isCorrect(answer)

    def endQuiz(self):
        return self._cur >= self._numQs

