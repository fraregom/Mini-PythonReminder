import re
import os

def op_delete(orden):
    regex = re.compile(r' *delete +(:?"(?P<name_file>.*)"|'
                       r'(?P<all_activo>all+(:? +where +(:?(:?name +is +"(?P<is_file>.+)"|'
                       r'name +contains +"(?P<contains_file>.+)")|'
                       r'tag +is +"(?P<tag_name>.+)"))?))(:? +in +/(?P<route>(.*))/*)?')

    print "contains_file: " + regex.match(orden).group('contains_file')
    print "route: " + regex.match(orden).group('route')
    return