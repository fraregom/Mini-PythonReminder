# coding=utf-8
import re
import delete
import edit
#import show
import dir
#import create
import find

print "Welcome to py-note!\n"
while True:
    input = raw_input("Command: ")
    if re.match("create",input) :
        print "creaaate"
    elif re.match("dir", input):
        dir.op_dir(input)
    elif re.match("show", input):
        print "shoooooow"
    elif re.match("edit", input):
        edit.op_edit(input)
    elif re.match("delete", input):
        delete.op_delete(input)
    elif re.match("find", input):
        find.op_find(input)
    elif input == "exit":
        break
    else:
        print "Comando invalido\n"
