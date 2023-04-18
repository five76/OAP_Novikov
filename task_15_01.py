import re
from pprint import pprint
def get_ip_from_cfg(s):
    regex = re.compile(r' ip address ((?:\d+\.){3}\d+) ((?:\d+\.){3}\d+)')
    return(regex.findall(s))
with open('config_R1.txt') as f:
    s = f.read()
pprint(get_ip_from_cfg(s))



