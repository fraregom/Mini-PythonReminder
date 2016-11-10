# coding=utf-8
import os
import re

def op_find(orden):
    if None != re.search("some", orden):
        for file in os.listdir(os.getcwd()):
            if file.endswith(".txt"):
                tmp = open(file)
                for line in tmp:
                    for word in re.findall('"(\w+)"',orden,re.IGNORECASE):
                        #print repr('\b+str(word)+\b')
                        #if None != re.search("\b"+str(word)+"\b",line):
                        if None != re.search(word, line):
                            print re.sub(word,'\033[42m' + word + '\033[0m',line)
                tmp.close()


    elif None != re.search("exact", orden):
        print "Se selecciono exact"

    else:
        print "Error: Comando desconocido."
    return

#    try:
#       fh = open("testfile", "w")
#       fh.write("This is my test file for exception handling!!")
#    except IOError:
#       print "Error: can\'t find file or read data"
#    else:
#       print "Written content in the file successfully"
#       fh.close()
#