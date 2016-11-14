# coding=utf-8
import os
import re
import subprocess
import time


def create(order, path_origin):
    pattern = re.compile(r'^ *create +(?:(?:(?P<edit>".+?") *edit *)|(?P<files>(?:".+?" *)+))'
                         r'(?:with +tags +(?P<tags>".*" *))?(?:in +/(?P<path>(?:.+)+)/?)?$')
    match = pattern.match(order)
    if match:
        files = 'files'
        path = os.getcwd()
        if match.group('edit'):
            files = 'edit'
        if match.group('path'):
            if re.match(r'home/.+', match.group('path')):
                path = '/' + match.group('path')
            else:
                path = os.getcwd()+'/'+match.group('path')
            if not os.path.exists(path):
                print "Error: Incorrect PATH"
                return
        ls = match.group(files)

        metadata = open(path_origin+"/metadata", "a")
        for i in range(1, len(match.group(files).split('"')), 2):
            archivo = open(path+"/"+ls.split('"')[i]+".txt", "w")
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
        if files == "edit":
            subprocess.call(['nano', path + "/" + match.group(files).strip('"') + '.txt'])
    else:
        print "Error: Incorrect Command"
