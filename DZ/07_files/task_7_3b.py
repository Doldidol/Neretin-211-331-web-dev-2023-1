# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

vlan_number = input("Введите номер VLAN: ")

with open("CAM_table.txt") as file:
    cam_table = []
    for line in file:
        words = line.split()
        if words and words[0].isdigit() and words[0] == vlan_number:
            vlan, mac_address, _, interface = line.split()
            cam_table.append([int(vlan), mac_address, interface])

    sorted_cam_table = sorted(cam_table, key=lambda x: (x[0], x[1]))

    for entry in sorted_cam_table:
        vlan, mac_address, interface = entry
        print("{:<9} {:<17} {:<10}".format(vlan, mac_address, interface))
