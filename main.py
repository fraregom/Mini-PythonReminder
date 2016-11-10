# coding=utf-8
import re
#import delete
#import edit
#import show
import dir
#import create
#import funciones


print "Welcome to py-note!\n"
while 1 :
    input = raw_input("Comando: ")
    if None !=re.match("create",input) :
        print "creaaate"
    elif None != re.match("dir", input):
        dir.op_dir(input)
    elif None != re.match("show", input):
        print "shoooooow"
    elif None != re.match("edit", input):
        print "ediiiiiit"
    elif None != re.match("delete", input):
        print "deleeeeeet"
    elif None != re.match("find", input):
        print "fiiiiiind"
    elif input == "exit":
        break
    else:
        print "Comando invalido\n"
