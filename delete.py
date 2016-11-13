import re
import os


def op_delete(orden,PATH):
    regex = re.compile(r'^ *delete +(:?"(?P<name_file>.*)"|'
                       r'(?P<all_activo>all+(:? +where +(:?(:?name +is +"(?P<is_file>.+)"|'
                       r'name +contains +"(?P<contains_file>.+)")|'
                       r'tag +is +"(?P<tag_name>.+)"))?))(:? +in +/(?P<route>(.*))/*)?$')

    in_route = False
    new_route = ''
    if regex.match(orden):
        if regex.match(orden).group('route'):
            in_route = True
            if re.match(r'home/.+', new_route):
                new_route = '/' + new_route + '/'
            else:
                new_route = regex.match(orden).group('route') + '/'

        if regex.match(orden).group('all_activo'):
            if regex.match(orden).group('is_file'):
                name = regex.match(orden).group('is_file')
                if in_route:
                    filelist = [f for f in os.listdir(new_route) if f.startswith(name) and f.endswith('.txt')]
                    for f in filelist:
                        print "Successfully deleted: " + f
                        os.remove(new_route + f)
                else:
                    filelist = [f for f in os.listdir(".") if f.startswith(name) and f.endswith('.txt')]
                    for f in filelist:
                        print "Successfully deleted: " + f
                        os.remove(f)

            elif regex.match(orden).group('contains_file'):
                name = regex.match(orden).group('contains_file')
                route_exists = False
                for_delete = []
                if in_route:
                    filelist = [f for f in os.listdir(new_route) if f.endswith('.txt')]
                    route_exists = True
                else:
                    filelist = [f for f in os.listdir(".") if f.endswith('.txt')]
                for f in filelist:
                    if route_exists:
                        file = open(new_route + f)
                    else:
                        file = open(f)
                    if re.search(name, file.read(), re.MULTILINE):
                        for_delete.append(f)
                    file.close()

                if for_delete != []:
                    for f in for_delete:
                        if route_exists:
                            os.remove(new_route + f)
                        else:
                            os.remove(f)
                        print "Successfully deleted: " + f
                else:
                    print "No file was deleted"

            elif regex.match(orden).group('tag_name'):
                route_exists = False
                for_delete = []
                metadata = open(PATH+'/metadata')
                tag = regex.match(orden).group('tag_name')

                if new_route:
                    route_exists = True

                for line in metadata:
                    if tag in re.findall(r'"(.+?)"',line):
                        for_delete.append(line.strip().split('|')[0])

                if for_delete != []:
                    for f in for_delete:
                        if route_exists:
                            os.remove(new_route + f)
                        else:
                            os.remove(f)
                        print "Successfully deleted: " + f
                else:
                    print "No file was deleted"

            else:
                if in_route:
                    filelist = [f for f in os.listdir(new_route) if f.endswith(".txt")]
                    for f in filelist:
                        print "Successfully deleted: " + f
                        os.remove(new_route + f)
                else:
                    filelist = [f for f in os.listdir(".") if f.endswith(".txt")]
                    for f in filelist:
                        print "Successfully deleted: " + f
                        os.remove(f)

        elif regex.match(orden).group('name_file'):
            print "Successfully deleted: " + regex.match(orden).group('name_file') + '.txt'
            if in_route:
                os.remove(new_route + regex.match(orden).group('name_file') + '.txt')
            else:
                os.remove(regex.match(orden).group('name_file') + '.txt')

    else:
        print "Error: Incorrect command"

    return