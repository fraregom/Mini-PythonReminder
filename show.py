# coding=utf-8
import os
import re
import auxiliar


def show(order,path_origin):
    regex = re.compile(r'^ *show +(?:"(?P<name_file>.*)"|'
                       r'(?P<all>all(?: +where(?:(?: +name(?: +is +"(?P<is>.*?)"|'
                       r' +contains +"(?P<contains>.*?)"))|(?: +tag +is +"(?P<tag>.+?)")))?)'
                       r'(?: +sorted +by +(?P<sort>(?:names|tags|modified|creation)))?)'
                       r'(:? +in +/(?P<route>(.*))/?)? *$')
    match = regex.match(order)
    if match:
        metadata_path = path_origin + '/.metadata'
        name = match.group("name_file")
        all = match.group("all")
        iss = match.group("is")
        contains = match.group("contains")
        tag = match.group("tag")
        sort = match.group("sort")
        route = match.group("route")
        if route:
            route = str(route)
            if re.match(r'home/.+', route):
                route = "/"+route
            else:
                route = os.getcwd()+"/"+route
        else:
            route = os.getcwd()
        if name:
            auxiliar.print_info(metadata_path,name,route)
        elif all:
            for_order = []
            if not sort:
                sort = None
            if iss:
                filelist = [f for f in os.listdir(route) if f.endswith(".lpy")]
                for f in filelist:
                    if iss+".lpy" == f:
                        for_order.append((iss,route))
                        #auxiliar.print_info(metadata_path,iss,route)
                auxiliar.sorted_by(for_order,metadata_path,sort)
            elif contains:
                filelist = [f for f in os.listdir(route) if contains in f.strip(".lpy").split() and f.endswith('.lpy')]
                for f in filelist:
                    #auxiliar.print_info(metadata_path,f.split(".lpy")[0],route)
                    for_order.append((f.split(".lpy")[0], route))
                auxiliar.sorted_by(for_order, metadata_path, sort)
            elif tag:
                metadata = open(metadata_path)
                for line in metadata:
                    aux = line.strip().split("|")
                    if tag in re.findall(r'"(\w+)"',aux[4]) and route == aux[1]:#agregamos a for_show la ruta+nombre que tienen match
                        #auxiliar.print_info(metadata_path, aux[0],route)
                        for_order.append((aux[0], route))
                auxiliar.sorted_by(for_order, metadata_path, sort)
                metadata.close()
            else:# all
                filelist = [f for f in os.listdir(route) if f.endswith(".lpy")]
                for f in filelist:
                    for_order.append((f.split(".lpy")[0], route))
                    #auxiliar.print_info(metadata_path,f.split(".lpy")[0],route)
                auxiliar.sorted_by(for_order, metadata_path, sort)
    else:
        print "Error: Incorrect Command"

