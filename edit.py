# coding=utf-8
import subprocess
import re


def op_edit(order):
    regex = re.compile(r' *edit +"(?P<name>(?:.+))" *(?:in /(?P<in>(?:.+))/?)?')

    if regex.match(order).group('name'):
        print regex.match(order).group('name')
        path = regex.match(order).group('name')
        if regex.match(order).group('in'):
            path = regex.match(order).group('in') + '/' + path
            if re.match(r'home/.+', path):
                path = '/' + path
        subprocess.call(['nano', path + '.lpy'])
        print "Successfully Edit"
    return

#faltaria analizar si el archivo que se va a editar existe o no para 
#arrogar el mensaje de error

#editar el re, para que no acepte .txt