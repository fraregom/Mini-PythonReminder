# coding=utf-8
import os
import re
import subprocess
import time


def create(order, path_origin):
    pattern = re.compile(r'^ *create *(?:(?:"(?P<edit>[^/"]+?)" *edit *)|'
                         r'(?P<files>(?:".+?" *)+))'
                         r'(?:with +tags +(?P<tags>".*" *))?'
                         r'(?:in +/(?P<path>(?:.+)+)/?)?$')
    match = pattern.match(order)
    if match: # Entra si la expresion regular coincide
        files = 'files'
        path = os.getcwd()
        if match.group('edit'):
            files = 'edit'
        if match.group('path'): # Se define la ruta absoluta
            if re.match(r'home/.+', match.group('path')):
                path = '/' + match.group('path')
            else:
                path = os.getcwd()+'/'+match.group('path')
            if not os.path.exists(path):
                print "Error: Incorrect PATH"
                return
        ls = match.group(files)
        metadata = open(path_origin+"/.metadata", "a")
        for i in range(1, len(match.group(files).split('"')), 2):
            archivo = open(path+"/"+ls.split('"')[i]+".lpy", "w")
            archivo.close()
            date = time.strftime("%d/%m/%Y-%H:%M:%S")
            tags = ""
            if match.group('tags'):
                tags = match.group('tags')
            if match.group('path'):
                new_path = match.group('path')
                if re.match(r'home/.+', new_path):
                    path = '/' + new_path
                else:
                    path = os.getcwd() + '/' + match.group('path')
            meta = ls.split('"')[i]+'|'+path+'|'+date+'|'+date+'|'+tags+'\n'
            metadata.write(meta)
        metadata.close()
        print "Successfully create: " + ls
        if files == "edit": #Para editar llamamos abrimos el archivo con NANO
            subprocess.call(['nano', path + "/" + match.group(files).strip('"') + '.lpy'])
    else:
        print "Error: Incorrect Command"
