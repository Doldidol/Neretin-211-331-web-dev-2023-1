# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def get_int_vlan_map(config_filename):
    result_access = dict()
    result_trunk = dict()
    mode = ''
    with open(config_filename, 'r') as file:
        temp = list()
        for line in file:
            if line.find('interface') != -1:
                temp.append(line[10:].rstrip())
            elif line.find("vlan") != -1:
                mode = 'access' if line.find('access') != -1 else 'trunk'
                temp.append(line[line.find('vlan')+5:].rstrip().split(','))
            if len(temp) == 2:
                if mode == 'access':
                    result_access.update({temp[0]: int(*temp[1])})
                elif mode == 'trunk' and type(temp[1]) is list:
                    temp_l = [int(item) for item in temp[1]]
                    result_trunk.update({temp[0]: temp_l})
                temp.clear()

    return result_access, result_trunk


print(get_int_vlan_map("config_sw1.txt"))