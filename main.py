# coding=utf-8
import os
import re
import create
import delete
import dir
import edit
import find

print "Welcome to py-note!\n"
PATH = os.getcwd()
if not os.path.isfile("metadata"):
    arc = open("metadata", "w")
    arc.close()
while True:
    command = raw_input("Command: ")
    if re.match("create", command):
        create.create(command, PATH)
    elif re.match("dir", command):
        dir.op_dir(command)
    elif re.match("show", command):
        print "shoooooow"
    elif re.match("edit", command):
        edit.op_edit(command)
    elif re.match("delete", command):
        delete.op_delete(command, PATH)
    elif re.match("find", command):
        find.op_find(command)
    elif command == "exit":
        break
    else:
        print "Comando invalido\n"
