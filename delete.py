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
    default_route = os.getcwd() + '/'
    if regex.match(order):  # Se verifica si se produjo un match, de lo contrario retorna comando incorrecto.
        route = regex.match(order).group('route')
        name = regex.match(order).group('name_file')
        is_active = regex.match(order).group('is_file')
        contains_active = regex.match(order).group('contains_file')
        tag_active = regex.match(order).group('tag_name')
        if route:
            if not os.path.exists(path):
                print "Error: This PATH does not exists"
                return
            if re.match(r'home/.+', route):
                default_route = '/' + route + '/'
            else:
                default_route = default_route + route + '/'

        if regex.match(order).group('all_activo'):
            if is_active:  # Trabaja unicamente cuando es invocado "is"
                filelist = [f for f in os.listdir(default_route) if f == is_active + ".lpy"]
                for f in filelist:
                    os.remove(default_route + f)
                    trash.append(default_route + f)

            elif contains_active:  # Trabaja unicamente cuando es invocado "contains_file"
                filelist = [f for f in os.listdir(default_route)
                            if contains_active in f.strip('.lpy').split() and f.endswith('.lpy')]
                for f in filelist:
                    os.remove(default_route + f)
                    trash.append(default_route + f)

            elif tag_active:  # Eliminara todos los archivos que contengan un tag en especial del directorio actual
                metadata = open(path + '/.metadata')
                for line in metadata:
                    aux = line.strip().split("|")
                    if tag_active in re.findall(r'"(\w+)"', aux[4]):
                        if default_route == aux[1] + '/':
                            os.remove(default_route + aux[0] + '.lpy')
                            trash.append(default_route + aux[0])
                metadata.close()
            else:  # esto borra todos los archivos que terminan con .lpy
                filelist = [f for f in os.listdir(default_route) if f.endswith(".lpy")]
                for f in filelist:
                    os.remove(default_route + f)
                    trash.append(default_route + f)

        elif name:  # Es el encargado de borrar unicamente un archivo
            try:
                os.remove(default_route + name + '.lpy')
                trash.append(default_route + name)
            except OSError:
                pass

        auxiliar.bd_edit(trash, path, "clear")
    else:
        print "Error: Incorrect command"
    return
