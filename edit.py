# coding=utf-8
import subprocess
import auxiliar
import re
import os

def op_edit(order, main_path):
    regex = re.compile(r' *edit +"(?P<name>(?:[^/]+))" *(?:in /(?P<in>(?:.+))/?)?')
    if regex.match(order):
        name = regex.match(order).group('name')
        route = regex.match(order).group('in')
        path = os.getcwd() + '/' + name + '.lpy'
        if route:
            if re.match(r'home/.+', route):
                path = '/' + route + '/' + name + '.lpy'
            else:
                path = os.getcwd() + '/' + route + '/' + name + '.lpy'
        if not os.path.isfile(path) and not os.path.exists(path):
            print "Error: This file or PATH does not exists"
        else:
            auxiliar.bd_edit([path],main_path,"edit")
            subprocess.call(['nano', path])
            print "Successfully Edit"
            return
    else:
        print "Error: Incorrect Command"
