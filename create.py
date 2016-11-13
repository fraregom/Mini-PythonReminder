# coding=utf-8
import re,os,time,subprocess

#<create> ::= "create" (<name> ["edit"] | <name> {<name>}) [<tags>] ["in" <route>]
#<edit> ::= "edit" <name> ["in" <route>]
#<tags> ::= "with tags" (<tag-name> {<tag-name>})

#

# create "name1" "name2" "name3" with tags "tag10" "tag20" "tag30"
# create "hola mundo" "cosa" "uno" "dos" with tags "10" "20" "30" in /home/usr/doc
# create "hola mundo" edit with tags "10" "20" "30" in /home/usr/doc

#  create +(?:(?P<files>(?:".+?" *)+)|(?:(?P<edit>".+?") +edit +))(?:with +tags +(?P<tags>".*" *))?(?:in +(?P<path>(?:/.+)+))?
def create(input,PATH):
    patternCreate = ' *create +(?:(?P<files>(?:".+?" *)+)|(?:(?P<edit>".+?") +edit +))'
    patternOptional = '(?:with +tags +(?P<tags>".*" *))?(?:in +(?P<path>(?:/.+)+))?$'
    pattern = re.compile(patternCreate+patternOptional)
    match = pattern.match(input)
    #print 'grupo 0 '+match.group(0)

    if match:
        files = 'files'
        edit = 0
        if match.group('edit'):
            print 'grupo edit: '+match.group('edit')
            files = 'edit'
            edit = 1
        ls = match.group(files)
        metadata = open("metadata","a")
        for i in range(1,len(ls.split('"')),2):
            archivo = open(ls.split('"')[i]+".txt","w")
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
        #if edit:




        print '\n-----------\n'
    else:
        print "Comando invalido\n"

