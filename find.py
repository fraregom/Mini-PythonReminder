# coding=utf-8
import os
import re

def multiple_replace(dict, text):
  regex = re.compile("(%s)" % "|".join(map(re.escape, dict.keys())))
  if regex.search(text):
    return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text)
  return

def op_find(orden):
    text_temp = ""
    ready = False
    nothing = True
    if re.search("some", orden):
        re_result = dict()
        for word in re.findall(r'"(\w+)"', orden):
            re_result[word] = '\033[42m' + word + '\033[0m'
        for file in os.listdir(os.getcwd()):
            if file.endswith(".txt"):
                tmp = open(file)
                for line in tmp:
                    if None != multiple_replace(re_result,line):
                        text_temp += multiple_replace(re_result,line)
                        ready = True
                    else:
                        text_temp += line
                tmp.close()
                if ready == True:
                    print text_temp
                    text_temp = ""
                    ready = False
                    print "------------------------------"
                else:
                    text_temp = ""

    elif re.search("exact", orden):
        text_temp = ""
        ready = False
        for file in os.listdir(os.getcwd()):
            if file.endswith(".txt"):
                tmp = open(file)
                for line in tmp:
                    find = re.search(r'"(.*?)"',orden).group(1)
                    if re.search(find,line):
                        text_temp += re.sub(find, '\033[42m' +find+ '\033[0m', line)
                        ready = True
                    else:
                        text_temp += line
                tmp.close()
                if ready == True:
                    print text_temp
                    text_temp = ""
                    ready = False
                    print "------------------------------"
                else:
                    text_temp = ""
    else:
        print "Error: Comando desconocido."
    return