# coding=utf-8
import re,os
#import delete
#import edit
#import show
import dir
import create
import find

PATH = os.getcwd()
archivo = open("metadata","w")
archivo.close()
print "Welcome to py-note!\n"
while True:
    input = raw_input("Command: ")
    if re.match("create",input) :
        create.create(input,PATH)
    elif re.match("dir", input):
        dir.op_dir(input)
    elif re.match("show", input):
        print "shoooooow"
    elif re.match("edit", input):
        print "ediiiiiit"
    elif re.match("delete", input):
        print "deleeeeeet"
    elif re.match("find", input):
        find.op_find(input)
    elif input == "exit":
        break
    else:
        print "Comando invalido\n"
