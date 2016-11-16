# coding=utf-8
import re


def multiple_replace(dictionary, text):
    regex = re.compile("(%s)" % "|".join(map(re.escape, dictionary.keys())))
    if regex.search(text):
        return regex.sub(lambda mo: dictionary[mo.string[mo.start():mo.end()]], text)
    return

styles = {"<rojo>":"\033[31m",
          "<amarillo>":"\033[33m",
          "<azul>":"\033[34m",
          "<verde>":"\033[32m",
          "<margenta>":"\033[35m",
          "<subrayado>":"\033[4m",
          "<negrita>":"\033[1m",
          "<cursiva>":"\033[3m",
          "</subrayado>":"\033[24m",
          "</negrita>":"\033[21m",
          "</cursiva>":"\033[23m",
          "</color>":"\033[39m"
        }