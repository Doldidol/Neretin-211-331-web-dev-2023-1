# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_address = input("Введите IP-адрес в формате 10.0.1.1: ")

while True:
    octets = ip_address.split(".")
    if len(octets) != 4:
        print("Неправильный IP-адрес")
        ip_address = input("Введите IP-адрес в формате 10.0.1.1: ")
        continue

    invalid_ip = False
    for octet in octets:
        if not octet.isdigit() or int(octet) < 0 or int(octet) > 255:
            print("Неправильный IP-адрес")
            invalid_ip = True
            break

    if invalid_ip:
        ip_address = input("Введите IP-адрес в формате 10.0.1.1: ")
        continue

    break

first_octet = int(octets[0])

if first_octet >= 1 and first_octet <= 223:
    print("unicast")
elif first_octet >= 224 and first_octet <= 239:
    print("multicast")
elif ip_address == "255.255.255.255":
    print("local broadcast")
elif ip_address == "0.0.0.0":
    print("unassigned")
else:
    print("unused")