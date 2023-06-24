# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

# network = input("Введите IP-сеть в формате xxx.xxx.xxx.xxx/yy: ")

# ip, mask = network.split('/')
# ip_octets = ip.split('.')
# mask_binary = '1' * int(mask) + '0' * (32 - int(mask))

# template = '''
# Network:
# {:<10}  {:<10}  {:<10}  {:<10}
# {:<10}  {:<10}  {:<10}  {:<10}

# Mask:
# /{}
# {:<10}  {:<10}  {:<10}  {:<10}
# {:<10}  {:<10}  {:<10}  {:<10}
# '''

# print(template.format(ip_octets[0], ip_octets[1], ip_octets[2], ip_octets[3],
#                       bin(int(ip_octets[0])), bin(int(ip_octets[1])), bin(int(ip_octets[2])), bin(int(ip_octets[3])),
#                       mask,
#                       mask_binary[:8], mask_binary[8:16], mask_binary[16:24], mask_binary[24:]))


# network = input("Введите IP-сеть в формате xxx.xxx.xxx.xxx/yy: ")

# ip, mask = network.split('/')
# ip_octets = ip.split('.')
# mask_binary = '1' * int(mask) + '0' * (32 - int(mask))

# template = '''
# Network:
# {:<10}  {:<10}  {:<10}  {:<10}
# {:<10s}  {:<10s}  {:<10s}  {:<10s}

# Mask:
# /{}
# {:<10}  {:<10}  {:<10}  {:<10}
# {:<10}  {:<10}  {:<10}  {:<10}
# '''

# print(template.format(ip_octets[0], ip_octets[1], ip_octets[2], ip_octets[3],
#                       bin(int(ip_octets[0]))[2:], bin(int(ip_octets[1]))[2:], bin(int(ip_octets[2]))[2:], bin(int(ip_octets[3]))[2:],
#                       mask,
#                       mask_binary[:8], mask_binary[8:16], mask_binary[16:24], mask_binary[24:]))


network = input("Введите адрес сети: ")

ip, mask = network.split("/")
ip_octets = ip.split(".")
mask = int(mask)

bin_mask = "1" * mask + "0" * (32 - mask)
mask_octets = [
    int(bin_mask[0:8], 2),
    int(bin_mask[8:16], 2),
    int(bin_mask[16:24], 2),
    int(bin_mask[24:32], 2),
]

ip_output = f"""
Network:
{ip_octets[0]:<8}  {ip_octets[1]:<8}  {ip_octets[2]:<8}  {ip_octets[3]:<8}
{int(ip_octets[0]):08b}  {int(ip_octets[1]):08b}  {int(ip_octets[2]):08b}  {int(ip_octets[3]):08b}"""

mask_output = f"""
Mask:
/{mask}
{mask_octets[0]:<8}  {mask_octets[1]:<8}  {mask_octets[2]:<8}  {mask_octets[3]:<8}
{mask_octets[0]:08b}  {mask_octets[1]:08b}  {mask_octets[2]:08b}  {mask_octets[3]:08b}"""

print(ip_output)
print(mask_output)
