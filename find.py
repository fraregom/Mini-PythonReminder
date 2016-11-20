# coding=utf-8
import os
import re
import auxiliar


# permite el mostrar por pantalla un elemento encontrado
def aux_print(name_file, text_temp):
    print ">>Found in " + name_file + ":\n"
    if auxiliar.multiple_replace(auxiliar.styles, text_temp, "find"):
        print auxiliar.multiple_replace(auxiliar.styles, text_temp, "find")
    else:
        print text_temp

# la funcion se encarga de buscar segun lo espeficado
def op_find(order):
    anything_find = False
    text_temp = ""
    ready = False

    #
    if re.search("some", order):
        exclude = re.compile(r'\W+')
        wanted = re.findall(r'"([A-Za-z]+)"', order)
        filelist = [f for f in os.listdir(os.getcwd()) if f.endswith('.lpy')]
        for name_file in filelist:
            tmp = open(name_file)
            for line in tmp:
                line = line.split()
                for word in line:
                    if '\n' in word:
                        filtred_word = exclude.sub('', word)
                        if filtred_word in wanted:
                            text_temp += '\033[46m' + word + '\033[49m' + '\n'
                            ready = True
                        else:
                            text_temp += word + " "
                    else:
                        filtred_word = exclude.sub('', word)
                        if filtred_word in wanted:
                            text_temp += '\033[46m' + word + '\033[49m' + " "
                            ready = True
                        else:
                            text_temp += word + " "
            if ready:
                anything_find = True
                aux_print(name_file, text_temp)
                text_temp = ""
                ready = False
                print "\033[0;39m"

            else:
                text_temp = ""
            tmp.close()

    elif re.search("exact", order):
        filelist = [f for f in os.listdir(os.getcwd()) if f.endswith('.lpy')]
        for name_file in filelist:
            tmp = open(name_file)
            for line in tmp:
                find = re.search(r'"(.+)"', order).group(1)
                find = " " + find + " "
                line = " " + line
                if re.search(find, line):
                    text_temp += re.sub(find, '\033[46m' + find + '\033[49m', line)
                    ready = True
                else:
                    text_temp += line
            if ready:
                anything_find = True
                aux_print(name_file, text_temp)
                text_temp = ""
                ready = False
                print "\033[0;39m"
            else:
                text_temp = ""
            tmp.close()

    else:
        anything_find = True
        print "Error: Incorrect Command"

    if not anything_find:
        print "Nothing was found.."

    return
