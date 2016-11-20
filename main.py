# coding=utf-8
import os
import re
import create
import delete
import dir
import edit
import find
import show

print """\
 _      __    __                     __         ___           _  __     __      __
| | /| / /__ / /______  __ _  ___   / /____    / _ \__ ______/ |/ /__  / /____ / /
| |/ |/ / -_) / __/ _ \/  ' \/ -_) / __/ _ \  / ___/ // /___/    / _ \/ __/ -_)_/
|__/|__/\__/_/\__/\___/_/_/_/\__/  \__/\___/ /_/   \_, /   /_/|_/\___/\__/\__(_)
                                                  /___/
"""
PATH = os.getcwd()
if not os.path.isfile(".metadata"):
    arc = open(".metadata", "w")
    arc.close()
while True:
    command = raw_input("Command: ")
    if re.match(" *create", command):
        create.create(command, PATH)
    elif re.match(" *dir", command):
        dir.op_dir(command,PATH)
    elif re.match(" *show", command):
        show.show(command,PATH)
    elif re.match(" *edit", command):
        edit.op_edit(command,PATH)
    elif re.match(" *delete", command):
        delete.op_delete(command, PATH)
    elif re.match(" *find", command):
        find.op_find(command)
    elif command == "exit":
        break
    else:
        print "Error: Incorrect Command\n"
