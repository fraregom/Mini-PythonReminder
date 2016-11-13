# coding=utf-8
import re,os,time,subprocess

#<create> ::= "create" (<name> ["edit"] | <name> {<name>}) [<tags>] ["in" <route>]
#<tags> ::= "with tags" (<tag-name> {<tag-name>})

#

# create "name1" "name2" "name3" with tags "tag10" "tag20" "tag30"
# create "hola mundo" "uno" "dos" with tags "10" "20" "30" in /doc
# create "hola mundo" edit with tags "10" "20" "30" in /home/usr/doc

#  create +(?:(?P<files>(?:".+?" *)+)|(?:(?P<edit>".+?") +edit +))(?:with +tags +(?P<tags>".*" *))?(?:in +(?P<path>(?:/.+)+))?
def create(input,PATH):
    patternCreate = '^ *create +(?:(?P<files>(?:".+?" *)+)|(?:(?P<edit>".+?") +edit +))'
    patternOptional = '(?:with +tags +(?P<tags>".*" *))?(?:in +/(?P<path>(?:.+)+))?$'
    pattern = re.compile(patternCreate+patternOptional)
    match = pattern.match(input)
    if match:
        files = 'files'
        path = os.getcwd()
        if match.group('edit'):
            print "enterEdit"
            files = 'edit'
        if match.group('path'):
            print "enterPath"
            if re.match(r"/home/.+", match.group('path')):
                path = match.group('path')
                print "ruta absoluta"
            else:
                path = os.getcwd()+'/'+match.group('path')
                print "ruta relativa"
            print path
            if not os.path.exists(path):
                print "explocioon!!"
                return
        #print "si explota no deberia ver esto"
        ls = match.group(files)
        #print PATH+"/metadata"
        metadata = open(PATH+"/metadata","a")
        for i in range(1,len(ls.split('"')),2):
            #print path+"/"+ls.split('"')[i]+".txt"
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
            print "raw 1:"
            raw_input()
            subprocess.call(['nano', path + match.group(files) + '.txt'])
            print "raw 2:"
            raw_input()
        print '\n-----------\n'
    else:
        print "Comando invalido\n"

