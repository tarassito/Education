# Байт - мінімальна одиниця зберігання і обробки цифрової інформації.

# b'bytes'
# b'bytes'

# 'Байты'.encode('utf-8')
# b'\xd0\x91\xd0\xb0\xd0\xb9\xd1\x82\xd1\x8b'

# bytes('bytes', encoding = 'utf-8') Приймає агрументами строку
# та формат кодування. За замовченням utf-8
# b'bytes'

# bytes([50, 100, 76, 72, 41]) Якщо передати агрументом список чисел від 0 до 255, то до кожного елементу
# застосуєтсья функція chr().
# b'2dLH)'

# chr() - Приймає агрументом int, повертає , байти
# chr(77)
# 'M'
# chr(5466)
# 'ᕚ'
# chr(54611)
# '핓'

# ord() Зворотня функція до chr()
# ord('a')
# 97

# Bytearray - масив байт. Різниця з bytes в тому, що цей тип даних є змінним
# a = bytearray([97, 55])
# a
# bytearray(b'a7')
# a[0]
# 97
# a[0] = 12
# a
# bytearray(b'\x0c7')




# Python 3 stores str type in Unicode
# 'my_text', "my_text", '''my_text'''

# -*- coding: <encoding name> -*-
# Використовуючи це рядок можна визначити формат кодування

# "\N{GREEK CAPITAL LETTER DELTA}"  # Using the character name
# 'Δ'
# "\u0390"                          # Using a 16-bit hex value
# ΐ'
# "\U00000394"                      # Using a 32-bit hex value
# 'Δ'

# b'\x80abc'.decode("utf-8", "strict")
# Traceback (most recent call last):
#     ...
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0x80 in position 0:
#   invalid start byte

# b'\x80abc'.decode("utf-8", "replace")
# '?abc'
# b'\x80abc'.decode("utf-8", "backslashreplace")
# '\\x80abc'
# b'\x80abc'.decode("utf-8", "ignore")
# 'abc'

# u = chr(40960) + 'abcd' + chr(1972)
# u.encode('utf-8')

# Головне про Юнікод
# ASCII - система кодів, у якій числа від 0 до 127 включно поставлені у відповідність літерам, цифрам і символам пунктуації
# Unicode - стандарт, розроблений, щоб забезпечити цифрове представлення символів усіх писемностей світу та спеціальних символів
# Utf-8 - кодування, що реалізовує представлення Юнікоду, сумісне з 8-бітовим кодуванням тексту. Від 1 до 4 байт на символ
