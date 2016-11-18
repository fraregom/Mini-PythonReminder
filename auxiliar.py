# coding=utf-8
import re
import os
import time


styles = {"<rojo>":"\033[31m",
          "<amarillo>":"\033[33m",
          "<azul>":"\033[34m",
          "<verde>":"\033[32m",
          "<margenta>":"\033[35m",
          "<subrayado>":"\033[4m",
          "<negrita>":"\033[1m",
          "<cursiva>":"\033[3m",
          "</subrayado>":"\033[24m",
          "</negrita>":"\033[21m",
          "</cursiva>":"\033[23m",
          "</color>":"\033[39m"
        }

def multiple_replace(dictionary, text,flag):
    regex = re.compile("(%s)" % "|".join(map(re.escape, dictionary.keys())))
    if flag == "show":
        return regex.sub(lambda mo: dictionary[mo.string[mo.start():mo.end()]], text)
    if flag == "find":
        if regex.search(text):
            return regex.sub(lambda mo: dictionary[mo.string[mo.start():mo.end()]], text)
        return

def bd_edit(trash, path,type):
    metadata_old = open(path + '/.metadata')
    metadata_new = open(path + '/.metadata_tmp', 'w')
    trash_new = []
    if not trash:
        print "No file was found"
        return

    for name in trash:
        if name.endswith('.lpy'):
            trash_new.append(name.split('.lpy')[0])
        else:
            trash_new.append(name)

    for line in metadata_old:
        info = line.strip().split('|')
        if not info[0] in trash_new:
            metadata_new.write(line)
        elif type == "clear":
            print "Successfully deleted: " + info[0] + '.lpy'
        elif type == "edit":
            date = time.strftime("%d/%m/%Y-%H:%M:%S")
            metadata_new.write("|".join([info[0], info[1], info[2], date, info[4]])+"\n")

    metadata_new.close()
    metadata_old.close()
    os.remove(path + '/.metadata')
    os.renames(path + '/.metadata_tmp', path + '/.metadata')
    return

#def print_machine(name,route,in_route)
