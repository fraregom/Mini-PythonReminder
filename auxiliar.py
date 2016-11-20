# coding=utf-8
import re
import os
import time
import collections


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


def print_info(path,name,route):
    metadata = open(path)
    print ">>Title:        " + name
    for line in metadata:
        aux = line.strip().split("|")
        if name + "|" + route in line:
            print ">>Creation:     " + aux[2] + "\n>>Modification: " + aux[3]
    archivo = open(route + "/" + name + ".lpy")
    print multiple_replace(styles, archivo.read(), "show")
    print "\033[0;39m"
    archivo.close()

def sorted_by(ls,metadata_path,sort):
    if sort:
        metadata = open(metadata_path)
        dic = {}
        for linea in metadata:
            ls_split= linea.strip().split("|")
            for i in ls:
                if i[0]+"|"+i[1] in linea:
                    if sort == "names":
                        order = ls_split[0]
                    elif sort == "tags":
                        order = ls_split[4]
                        print order
                    elif sort == "modified":
                        order = ls_split[3]
                    elif sort == "creation":
                        order = ls_split[2]
                    dic[order] = i

        temp = collections.OrderedDict(sorted(dic.items()))
        ls=[]
        for _,value in temp.iteritems():
            ls.append(value)
    for element in ls:
        print_info(metadata_path,element[0],element[1])

