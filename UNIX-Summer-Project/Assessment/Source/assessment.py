#!/usr/bin/python2

from mailsend import sendinfo
from questions import *

string_to_be_sent = raw_input("Your name? ")+"\n"
redoloop = True
while(redoloop):
    temp = ""
    for i in range(number_of_questions):
        temp +=  questions[i]+":"
        print questions[i]
        answers[i] = raw_input("Your Answer: ")
        temp += answers[i] +"\n"
    print "Your answers"
    print temp
    print "Are you sure you wish to proceed?"
    proceed = raw_input("Y - Confirm\nN - Retry questions\n")
    if proceed == "Y":
        redoloop = False
        string_to_be_sent += temp

try:
    print "Sending your answers. Please wait."
    sendinfo(string_to_be_sent)
    print "Your answers have been sent successfully."
except Exception as e:
    print "Unable to send your answers."
    print "Please check your Internet Connection."
