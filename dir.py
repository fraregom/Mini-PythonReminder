# coding=utf-8
import os
import re


def op_dir(order, path):
    regex = re.compile(r' *dir +(?:here|/(?P<route>.+)/?) *')
    if regex.match(order):
        try:
            if regex.match(order).group('route'):
                route = regex.match(order).group('route')
                if re.match(r'home/.*', route):
                    path = '/' + route
                else:
                    path = os.getcwd() + '/' + route
                os.chdir(path)
                print "New PATH: " + os.getcwd()
            else:
                os.chdir(path)
                print "Original PATH: " + path
        except OSError:
            print "Error: PATH does not exist"
    else:
        print "Error: Incorrect Command"
    return
