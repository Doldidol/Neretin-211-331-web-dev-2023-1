# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
output = "Prefix {}\nAD/Metric {}\nNext-Hop {}\nLast update {}\nOutbound Interface {}\n"

with open("C:\Users\neret\OneDrive\Рабочий стол\РВП\DZ\07_files\ospf.txt") as file:
    for line in file:
        fields = line.split()
        prefix = fields[1]
        ad_metric = fields[2].strip("[]")
        next_hop = fields[4].rstrip(",")
        last_update = fields[5].rstrip(",")
        outbound_interface = fields[6]
        

        print(output.format(prefix, ad_metric, next_hop, last_update, outbound_interface))