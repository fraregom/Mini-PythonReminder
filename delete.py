# coding=utf-8
import os
import re


def bd_cleaner(trash, path):
    metadata_old = open(path + '/metadata')
    metadata_new = open(path + '/metadata_tmp', 'w')
    trash_new = []
    if not trash:
        print "No file was deleted"
        return

    for name in trash:
        if name.endswith('.txt'):
            trash_new.append(name.split('.txt')[0])
        else:
            trash_new.append(name)

    for line in metadata_old:
        if not line.strip().split('|')[0] in trash_new:
            metadata_new.write(line)
        else:
            print "Successfully deleted: " + line.strip().split('|')[0] + '.txt'

    metadata_new.close()
    metadata_old.close()
    os.remove(path + '/metadata')
    os.renames(path + '/metadata_tmp', path + '/metadata')
    return


def op_delete(order, path):
    regex = re.compile(r'^ *delete +(:?"(?P<name_file>.*)"|'
                       r'(?P<all_activo>all+(:? +where +(:?(:?name +is +"(?P<is_file>.+)"|'
                       r'name +contains +"(?P<contains_file>.+)")|'
                       r'tag +is +"(?P<tag_name>.+)"))?))(:? +in +/(?P<route>(.*))/*)?$')

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
                if in_route:
                    filelist = [f for f in os.listdir(new_route) if f.startswith(name) and f.endswith('.txt')]
                else:
                    filelist = [f for f in os.listdir(".") if f.startswith(name) and f.endswith('.txt')]
                for f in filelist:
                    if in_route:
                        os.remove(new_route + f)
                    else:
                        os.remove(f)
                    trash.append(f)

            elif regex.match(order).group('contains_file'):
                name = regex.match(order).group('contains_file')
                route_exists = False
                for_delete = []
                if in_route:
                    filelist = [f for f in os.listdir(new_route) if f.endswith('.txt')]
                    route_exists = True
                else:
                    filelist = [f for f in os.listdir(".") if f.endswith('.txt')]
                for f in filelist:
                    if route_exists:
                        file_open = open(new_route + f)
                    else:
                        file_open = open(f)
                    if re.search(name, file_open.read(), re.MULTILINE):
                        for_delete.append(f)
                    file_open.close()

                if for_delete:
                    for f in for_delete:
                        if route_exists:
                            os.remove(new_route + f)
                        else:
                            os.remove(f)
                        trash.append(f)

            elif regex.match(order).group('tag_name'):
                route_exists = False
                for_delete = []
                metadata = open(path + '/metadata')
                tag = regex.match(order).group('tag_name')

                if new_route:
                    route_exists = True

                for line in metadata:
                    if tag in re.findall(r'"(.+?)"', line):
                        for_delete.append(line.strip().split('|')[0])

                if for_delete:
                    for f in for_delete:
                        if route_exists:
                            os.remove(new_route + f + '.txt')
                            trash.append(f)
                        else:
                            os.remove(f + '.txt')
                            trash.append(f)
            else:
                if in_route:
                    filelist = [f for f in os.listdir(new_route) if f.endswith(".txt")]
                else:
                    filelist = [f for f in os.listdir(".") if f.endswith(".txt")]
                for f in filelist:
                    if in_route:
                        os.remove(new_route + f)
                    else:
                        os.remove(f)
                    trash.append(f)

        elif regex.match(order).group('name_file'):
            if in_route:
                os.remove(new_route + regex.match(order).group('name_file') + '.txt')
                trash.append(regex.match(order).group('name_file'))
            else:
                os.remove(regex.match(order).group('name_file') + '.txt')
                trash.append(regex.match(order).group('name_file'))
    else:
        print "Error: Incorrect command"

    bd_cleaner(trash, path)

    return
