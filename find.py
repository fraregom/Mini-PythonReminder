# coding=utf-8
import os
import re
import auxiliar


def op_find(order):
    anything_find = False
    if re.search("some", order):
        text_temp = ""
        ready = False
        re_result = auxiliar.styles
        for word in re.findall(r'"(\w+)"', order):
            re_result[word] = '\033[42m' + word + '\033[49m'
        for name_file in os.listdir(os.getcwd()):
            if name_file.endswith(".lpy"):
                tmp = open(name_file)
                for line in tmp:
                    if auxiliar.multiple_replace(re_result, line, "find"):
                        text_temp += auxiliar.multiple_replace(re_result, line, "find")
                        ready = True
                    else:
                        text_temp += line
                if ready:
                    anything_find = True
                    print "Found in " + name_file + ":\n"
                    print text_temp
                    text_temp = ""
                    ready = False
                    print "------------------------------"
                else:
                    text_temp = ""
                tmp.close()

    elif re.search("exact", order):
        text_temp = ""
        ready = False
        for name_file in os.listdir(os.getcwd()):
            if name_file.endswith(".lpy"):
                tmp = open(name_file)
                for line in tmp:
                    find = re.search(r'"(.*?)"', order).group(1)
                    if re.search(find, line):
                        text_temp += re.sub(find, '\033[42m' + find + '\033[0m', line)
                        ready = True
                    else:
                        text_temp += line
                if ready:
                    anything_find = True
                    print "Found in " + name_file + ":\n"
                    print auxiliar.multiple_replace(auxiliar.styles, text_temp, "find")
                    text_temp = ""
                    ready = False
                    print "------------------------------"
                else:
                    text_temp = ""
                tmp.close()
    else:
        anything_find = True
        print "Error: Incorrect Command"

    if not anything_find:
        print "Nothing was found.."

    return
