import re
#import funciones
import delete, edit, show, dir, create, funciones


print "Welcome to py-note\n"
while 1 :
    input = raw_input()
    if None !=re.match("create",input) :
        print "creaaate"
    elif None != re.match("dir", input):
        print "diiiiiir"
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
