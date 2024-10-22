#todo:
# 1. Создайте виртуальное окружение через терминал в текущей папки нового проекта.
# Название окружению дайте по названию проекта. Переключитесь на созданное новое окружение.

# 2. Установите пакет pandas.
# Убедитесь что он установился и добавился в папку виртуального окружения.


# 3. Создайте файл test_package.py в него добавьте строки

# import pandas as pd
# pd.test()

# Убедитесь что пакет подкючен.

# 4. Создайте свой пакет helpers со структурой

# helpers
#     __init__.py
#     io.py
#     crypt.py

# В модуль io.py разместите ранее написаный logger
# В модуль crypt.py добавьте функцию шифра цезаря.

# 5. Создайте новый файл test.py  Подключите в него функцию логера и шифрования.
# Проверьте их работу.

import pandas as pd
from helpers import caesar_cipher, logger

print(pd.test())
print(caesar_cipher('TEST'))
logger(error_type='WARNING',
           code=777,
           line=12,
           message_="File is locking",
           file='loger.txt')