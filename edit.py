import os
import subprocess
import re

def op_edit(orden):
    regex = re.compile(r'edit +"(?P<name>(?:.+))" *(?:in /(?P<in>(?:.+))/?)?')
    if regex.match(orden).group('name'):
        path = regex.match(orden).group('name')
        if regex.match(orden).group('in'):
            path = regex.match(orden).group('in')+ '/' + path
            if re.match(r'home/.+',path):
                path = '/'+path
        subprocess.call(['nano',path+'.txt'])
    return