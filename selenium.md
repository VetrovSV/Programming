# Установка и подготовка
`pip3 install selenium`

Для работы нужен:
1. драйвер браузера -- отдельная библиотека, содержащая реализацию браузера и програмный интерфейс (API) для работы с браузером.
Скачать драйвера можно здесь:
https://selenium-python.readthedocs.io/installation.html#drivers

Драйвер браузера -- поставляется одним файлом. Его нужно положить в папку, перечисленную в PATH, или явно указать имя при создании объекта, через который можно будет взаимодействовать с браузером.
2. Браузер, соответствующий драйверу.

```python
from selenium import webdriver
import os

driver = webdriver.Chrome('./chromedriver')   # файл chromedriver лежит в текущей папке
driver.get('http://md.zabgu.ru/login/index.php')

login = driver.find_element_by_id('username')
login.send_keys('qwerty')

driver.close()


# Ссылки
https://selenium-python.readthedocs.io/
```
