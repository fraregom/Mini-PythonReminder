# coding=utf-8
import re

#<create> ::= "create" (<name> ["edit"] | <name> {<name>}) [<tags>] ["in" <route>]
#<edit> ::= "edit" <name> ["in" <route>]
#<tags> ::= "with tags" (<tag-name> {<tag-name>})

#

# create "hola mundo" "cosa" "uno" "dos" with tags "10" "20" "30"
# create "hola mundo" "cosa" "uno" "dos" with tags "10" "20" "30" in /home/usr/doc
# create "hola mundo" edit with tags "10" "20" "30" in /home/usr/doc

#  create +(?:(?P<files>(?:".+?" *)+)|(?:(?P<edit>".+?") +edit +))(?:with +tags +(?P<tags>".*" *))?(?:in +(?P<path>(?:/.+)+))?
def create(input):
    patternCreate = ' *create +(?:(?P<files>(?:".+?" *)+)|(?:(?P<edit>".+?") +edit +))'
    patternOptional = '(?:with +tags +(?P<tags>".*" *))?(?:in +(?P<path>(?:/.+)+))?$'
    pattern = re.compile(patternCreate+patternOptional)
    match = pattern.match(input)
    #print 'grupo 0 '+match.group(0)
    edit = 0
    files = 'files'
    if match:
        if match.group('edit'):
            print 'grupo edit: '+match.group('edit')
            edit = 1
            files = 'edit'
        #else:
            #print 'grupo files ' + match.group('files')

        ls = match.group(files)
        for i in range(1,len(ls),2):
            archivo = open(ls[i]+".txt","w")
            archivo.close()

            archivo.write("")




        if match.group('tags'):
            print 'grupo tags ' + match.group('tags')
        if match.group('path'):
            print 'grupo path ' + match.group('path')
        print '\n-----------\n'
    else:
        print "Comando invalido\n"

