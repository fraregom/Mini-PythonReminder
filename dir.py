# coding=utf-8
import os
import re

def op_dir(orden):
    if re.search("here",orden):
        print "Se señalo que el directorio de trabajo es: " + os.getcwd()
        print '\033[35m' + 'esto es magenta' + '\033[39m'
    else:
        os.chdir(re.search('(/\w+)+',orden).group())
        print '\033[31m' + 'esto es rojo' + '\033[39m'
        print '\033[33m' + 'esto es amarillo' + '\033[39m'
        print '\033[34m' + 'esto es azul' + '\033[39m'
        print '\033[32m' + 'esto es verde' + '\033[39m'
        print '\033[35m' + 'esto es magenta' + '\033[39m'
        print '\033[4m' + 'esto es un subrayado' + '\033[24m'
        print '\033[1;30m' + 'esto es una negrita' + '\033[0m'
        print '\033[3m' + 'user' + '\033[0m'
        print "Se cambio el directorio de trabajo, ahora es: " + os.getcwd()
    return

