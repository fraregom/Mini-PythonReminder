# coding=utf-8
import os
import re
import auxiliar

# show "hola mundo"
# show "hola mundo" in /home/cosa
# show all
# show all in /home/cosa
# show all where name is "hola mundo"
# show all where name contains "hola mundo"
# show all where name contains "hola mundo" in /home/cosa
# show all where tag is "taaaags"
# show all where tag is "taaaags" sorted by modified
# show all where name is "hola mundo" sorted by tags  in /home/cosa

# *show +(?:"(?P<name_file>.*)"|(?P<all>all(?: +where(?:(?: +name(?: +is +"(?P<is>.*?)"| +contains +"(?P<contains>.*?)"))|(?: +tag +is +"(?P<tag>.+?)")))?)(?: +sorted +by +(?P<sort>(?:names|tags|modified|creation)))?)(:? +in +/(?P<route>(.*))/*)?

def show(order,path_origin):
    regex = re.compile(r'^ *show +(?:"(?P<name_file>.*)"|'
                       r'(?P<all>all(?: +where(?:(?: +name(?: +is +"(?P<is>.*?)"|'
                       r' +contains +"(?P<contains>.*?)"))|(?: +tag +is +"(?P<tag>.+?)")))?)'
                       r'(?: +sorted +by +(?P<sort>(?:names|tags|modified|creation)))?)'
                       r'(:? +in +/(?P<route>(.*))/?)? *$')
    match = regex.match(order)
    if match:
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
        #print "la ruta es :"+ route
        metadata = open(path_origin + '/.metadata')
        if name:
            #print "el nombre es: "+name
            print "-----Title:" + name + "-----"
            for line in metadata:
                aux = line.strip().split("|")
                if name+"|"+route in line:
                    print "Creation: "+aux[2]+" --- Modification: "+aux[3]
            archivo = open(route +"/"+ name + ".lpy")
            print auxiliar.multiple_replace(auxiliar.styles,archivo.read(),"show")
            archivo.close()
        elif all:
            if iss:
                filelist = [f for f in os.listdir(route) if f.endswith(".lpy")]
                for f in filelist:
                    if iss+".lpy" == f:
                        print "-----Title:" + f +"-----"
                        archivo = open(route +"/"+ iss + ".lpy")
                        print auxiliar.multiple_replace(auxiliar.styles, archivo.read(),"show")
                        archivo.close()

            elif contains:
                filelist = [f for f in os.listdir(route) if contains in f.strip(".lpy").split() and f.endswith('.lpy')]
                for f in filelist:
                    print "-----Title:" + f + "-----"
                    archivo = open(route +"/"+ f )
                    print auxiliar.multiple_replace(auxiliar.styles, archivo.read(),"show")
                    archivo.close()
            elif tag:
                # if new_route:
                for line in metadata:
                    aux = line.strip().split("|")
                    if tag in aux[4]:#agregamos a for_show la ruta+nombre que tienen match
                        #route+"/"+aux[0]
                        if route == aux[1]:
                            print "-----Title:" + aux[0] + ".lpy-----"
                            archivo = open(route + "/" + aux[0]+ ".lpy")
                            print auxiliar.multiple_replace(auxiliar.styles, archivo.read(), "show")
                            archivo.close()

            else:# all
                filelist = [f for f in os.listdir(route) if f.endswith(".lpy")]
                for f in filelist:
                    print "-----Title:" + f + "-----"
                    archivo = open(route + "/" + f )
                    print auxiliar.multiple_replace(auxiliar.styles, archivo.read(), "show")
                    archivo.close()

    else:
        print "Error: Incorrect Command"

