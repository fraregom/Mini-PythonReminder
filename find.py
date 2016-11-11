# coding=utf-8
import os
import re

def multiple_replace(dict, text):
  regex = re.compile("(%s)" % "|".join(map(re.escape, dict.keys())))
  return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text)


def op_find(orden):
    if re.search("some", orden):
        text_temp = ""
        ready = False
        re_result = dict()
        for word in re.findall(r'"(\w+)"', orden, re.IGNORECASE):
            re_result[word] = '\033[42m' + word + '\033[0m'

        for file in os.listdir(os.getcwd()):
            if file.endswith(".txt"):
                tmp = open(file)
                print "------------------------------"
                for line in tmp:
                    print multiple_replace(re_result,line)
                tmp.close()

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