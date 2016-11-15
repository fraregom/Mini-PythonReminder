# coding=utf-8
import os
import re


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
    regex = re.compile(r' *show +(?:"(?P<name_file>.*)"|'
                       r'(?P<all>all(?: +where(?:(?: +name(?: +is +"(?P<is>.*?)"|'
                       r' +contains +"(?P<contains>.*?)"))|(?: +tag +is +"(?P<tag>.+?)")))?)'
                       r'(?: +sorted +by +(?P<sort>(?:names|tags|modified|creation)))?)'
                       r'(:? +in +/(?P<route>(.*))/*)?')
    