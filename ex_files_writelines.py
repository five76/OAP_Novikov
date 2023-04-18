
cfg_lines = ['!',
             'service timestamps debug datetime msec localtime show-timezone year',
             'service timestamps log datetime msec localtime show-timezone year',
             'service password-encryption',
             'service sequence-numbers',
             '!',
             'no ip domain lookup',
             '!',
             'ip ssh version 2',
             '!'
             ]
f = open('f2.txt', 'w')

f.writelines(cfg_lines)
f.close()