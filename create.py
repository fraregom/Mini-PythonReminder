# coding=utf-8
import re,os,time,subprocess

def create(input,PATH):
    patternCreate = '^ *create +(?:(?:(?P<edit>".+?") *edit *)|(?P<files>(?:".+?" *)+))'
    patternOptional = '(?:with +tags +(?P<tags>".*" *))?(?:in +/(?P<path>(?:.+)+))?$'
    pattern = re.compile(patternCreate+patternOptional)
    match = pattern.match(input)
    if match:
        files = 'files'
        path = os.getcwd()
        if match.group('edit'):
            files = 'edit'
        if match.group('path'):
            if re.match(r"/home/.+", match.group('path')):
                path = match.group('path')
            else:
                path = os.getcwd()+'/'+match.group('path')
            if not os.path.exists(path):
                print "Error: Incorrect Path"
                return
        ls = match.group(files)

        metadata = open(PATH+"/metadata","a")
        for i in range(1,len(ls.split('"')),2):
            archivo = open(path+"/"+ls.split('"')[i]+".txt","w")
            archivo.close()
            date = time.strftime("%d/%m/%Y-%H:%M:%S")
            tags = ""
            path = os.getcwd()
            if match.group('tags'):
                tags = match.group('tags')
            if match.group('path'):
                path = match.group('path')
            meta = ls.split('"')[i]+'|'+path+'|'+date+'|'+date+'|'+tags+'\n'
            metadata.write(meta)
        metadata.close()
        if files == "edit": #comando EDIT
            subprocess.call(['nano', path+"/"+ match.group(files).strip('"') + '.txt'])
    else:
        print "Error: Incorrect Command\n"

