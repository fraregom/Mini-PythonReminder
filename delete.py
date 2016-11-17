# coding=utf-8
import os
import re
import auxiliar


def op_delete(order, path):
    regex = re.compile(r'^ *delete +(:?"(?P<name_file>.*)"|'
                       r'(?P<all_activo>all+(:? +where +(:?(:?name +is +"(?P<is_file>.+)"|'
                       r'name +contains +"(?P<contains_file>.+)")|'
                       r'tag +is +"(?P<tag_name>.+)"))?))(:? +in +/(?P<route>(.*))/*)? *$')

    trash = []
    in_route = False
    new_route = ''
    if regex.match(order):
        if regex.match(order).group('route'):
            new_route = regex.match(order).group('route')
            in_route = True
            if re.match(r'home/.+', new_route):
                new_route = '/' + new_route + '/'
            else:
                new_route = regex.match(order).group('route') + '/'

        if regex.match(order).group('all_activo'):
            if regex.match(order).group('is_file'):
                name = regex.match(order).group('is_file')
                print name
                if in_route:
                    filelist = [f for f in os.listdir(new_route) if os.path.isfile(name+".lpy")]
                else:
                    filelist = [f for f in os.listdir(".") if os.path.isfile(name+".lpy")]
                for f in filelist:
                    if in_route:
                        os.remove(new_route + f)
                    else:
                        os.remove(f)
                    trash.append(f)

            elif regex.match(order).group('contains_file'):
                name = regex.match(order).group('contains_file')
                if in_route:
                    filelist = [f for f in os.listdir(new_route) if name in f and f.endswith('.lpy')]
                else:
                    filelist = [f for f in os.listdir(".") if name in f and f.endswith('.lpy')]
                for f in filelist:
                    if in_route:
                        os.remove(new_route + f)
                    else:
                        os.remove(f)
                    trash.append(f)

            elif regex.match(order).group('tag_name'):
                route_exists = False
                for_delete = []
                metadata = open(path + '/.metadata')
                tag = regex.match(order).group('tag_name')

                if new_route:
                    route_exists = True

                for line in metadata:
                    if tag in re.findall(r'"(.+?)"', line):
                        for_delete.append(line.strip().split('|')[0])

                if for_delete:
                    for f in for_delete:
                        if route_exists:
                            if os.path.isfile(new_route + f + '.lpy'):
                                os.remove(new_route + f + '.lpy')
                                trash.append(f)
                        else:
                            if os.path.isfile(f + '.lpy'):
                                print "enterrrr"
                                os.remove(f+ '.lpy')
                                trash.append(f)
            else:
                if in_route:
                    filelist = [f for f in os.listdir(new_route) if f.endswith(".lpy")]
                else:
                    filelist = [f for f in os.listdir(".") if f.endswith(".lpy")]
                for f in filelist:
                    if in_route:
                        os.remove(new_route + f)
                    else:
                        os.remove(f)
                    trash.append(f)

        elif regex.match(order).group('name_file'):
            if in_route:
                os.remove(new_route + regex.match(order).group('name_file') + '.lpy')
                trash.append(regex.match(order).group('name_file'))
            else:
                os.remove(regex.match(order).group('name_file') + '.lpy')
                trash.append(regex.match(order).group('name_file'))
    else:
        print "Error: Incorrect command"

    auxiliar.bd_edit(trash, path,"clear")

    return

#falta verificar si existe el archivo, cuando se desea borrar uno y
#arrogar el mensaje de error en caso que no exista