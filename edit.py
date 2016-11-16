# coding=utf-8
import subprocess
import re
import auxiliar

def op_edit(order, main_path):
    regex = re.compile(r' *edit +"(?P<name>(?:.+))" *(?:in /(?P<in>(?:.+))/?)?')

    if regex.match(order).group('name'):
        #print regex.match(order).group('name')
        path = regex.match(order).group('name')
        if regex.match(order).group('in'):
            path = regex.match(order).group('in') + '/' + path
            if re.match(r'home/.+', path):
                path = '/' + path
        auxiliar.bd_edit([path],main_path,"edit")
        subprocess.call(['nano', path + '.lpy'])
        print "Successfully Edit"
    return

#faltaria analizar si el archivo que se va a editar existe o no para 
#arrogar el mensaje de error

#editar el re, para que no acepte .txt