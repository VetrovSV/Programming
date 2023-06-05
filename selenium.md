# Установка и подготовка
`pip3 install selenium`

Для работы нужен:
1. драйвер браузера — отдельная библиотека, содержащая програмный интерфейс (API) для работы с браузером
Скачать драйвера можно здесь:
https://selenium-python.readthedocs.io/installation.html#drivers
Драйвер браузера поставляется одним файлом. Его нужно сохранить в папку, перечисленную в PATH, или явно указать имя при создании объекта, через который можно будет взаимодействовать с браузером.
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
В Linux, рекомендуется использовать браузер, дистрибутив которого не распространяется через snap пакет и каталог профиля браузера не находится в домашней папке пользователя [ [doc](https://github.com/mozilla/geckodriver/releases/tag/v0.31.0) ]. Один из таких браузеров - Microsoft Edge.

