# coding=utf-8
import re
import os


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

def multiple_replace(dictionary, text):
    regex = re.compile("(%s)" % "|".join(map(re.escape, dictionary.keys())))
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
        print "name in trash: "+ name
        if name.endswith('.lpy'):
            trash_new.append(name.split('.lpy')[0])
        else:
            trash_new.append(name)

    if type == "clear":
        clear(metadata_old, metadata_new, trash_new)
    metadata_new.close()
    metadata_old.close()
    os.remove(path + '/.metadata')
    os.renames(path + '/.metadata_tmp', path + '/.metadata')
    return


def clear(metadata_old, metadata_new, trash_new):
    for line in metadata_old:
        print "line in metadataOld: " +line
        if not line.strip().split('|')[0] in trash_new:
            metadata_new.write(line)
        else:
            print "Successfully deleted: " + line.strip().split('|')[0] + '.lpy'

