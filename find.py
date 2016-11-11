# coding=utf-8
import os
import re

def multiple_replace(dict, text):
  regex = re.compile("(%s)" % "|".join(map(re.escape, dict.keys())))
  return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text)


def op_find(orden):
    if None != re.search("some", orden):
        re_result = dict()
        for word in re.findall('"(\w+)"', orden, re.IGNORECASE):
            re_result[word] = '\033[42m' + word + '\033[0m'

        for file in os.listdir(os.getcwd()):
            if file.endswith(".txt"):
                tmp = open(file)
                print "------------------------------"
                for line in tmp:
                    print multiple_replace(re_result,line)
                tmp.close()

    elif None != re.search("exact", orden):
        #text_temp = ""
        #ready = False
        for file in os.listdir(os.getcwd()):
            if file.endswith(".txt"):
                tmp = open(file)
                for line in tmp:
                    find = re.search('"(.+)"',orden).group(0)
                    if None != re.search(find,line):
                        print "entro"
                        word = re.search('"(.+)"', orden).group(0)
                        print re.sub(word, '\033[42m' + word + '\033[0m', line)
                        #ready = True
                tmp.close()
                #if ready == True:
                    #print text_temp
    else:
        print "Error: Comando desconocido."
    return

    # word_tmp += re.sub(word,'\033[42m' + word + '\033[0m',line)

#    try:
#       fh = open("testfile", "w")
#       fh.write("This is my test file for exception handling!!")
#    except IOError:
#       print "Error: can\'t find file or read data"
#    else:
#       print "Written content in the file successfully"
#       fh.close()
#