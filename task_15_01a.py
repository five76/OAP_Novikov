import re
from pprint import pprint


def get_dict_ip_from_cfg(s):

    """
    Функция для формирования словаря, ключами которого являются имена интерфейсов,
    а значениями - кортежи, состоящие из ip адреса и маски
    :param s: - вывод команды "show run", записанный одной строкой
    :return:
    """

    regex = r'interface (\S+)(?:(?!interface).)+ip address ((?:\d+\.){3}\d+) ((?:\d+\.){3}\d+)'
    match = re.finditer(regex, s, re.DOTALL)
    ip_dict = {}
    for m in match:
        a, b, c = m.groups()
        ip_dict[a] = (b, c)
    return ip_dict

with open('config_R1.txt') as f:
    s = f.read()
pprint(get_dict_ip_from_cfg(s))



