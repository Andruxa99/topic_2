byte_size: int = 1234567890

kilo_size: float = 123456789 / 1024
mega_size: float = kilo_size / 1024
giga_size: float = mega_size / 1024

# print('Размер в байтах:', byte_size)
# print('Размер в килобайтах:', kilo_size)
# print('Размер в мегабайтах:', mega_size)
# print('Размер в гигабайтах:', giga_size)

print('Размер в байтах: ' + str(byte_size),
      'Размер в килобайтах: ' + str(kilo_size),
      'Размер в мегабайтах: ' + str(mega_size),
      'Размер в гигабайтах: ' + str(giga_size), sep='\n')
