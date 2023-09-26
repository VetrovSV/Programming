# Установка и подготовка
`pip3 install selenium`

Для работы нужен:
1. драйвер браузера — отдельная библиотека, содержащая программный интерфейс (API) для работы с браузером [ [SO:more](https://stackoverflow.com/questions/54459701/what-is-selenium-and-what-is-webdriver) ]
Скачать драйвера можно здесь:
https://selenium-python.readthedocs.io/installation.html#drivers
Драйвер браузера поставляется одним файлом. Его нужно сохранить в папку, перечисленную в PATH, или явно указать имя при создании объекта, через который можно будет взаимодействовать с браузером.
2. Браузер, соответствующий драйверу.
В Linux, рекомендуется использовать браузер, который выполняется не в песочнице (например snap-пакет Firefox) и каталог профиля которого не находится в домашней папке пользователя [ [doc](https://github.com/mozilla/geckodriver/releases/tag/v0.31.0) ]. Microsoft Edge не обладает этими ограничениями. 

Во время разработки и отладки программы рекомендуется использовать среду похожую на Jupyter Notebook, где можно запускать отдельные части кода, без необходимости перезапуска всей программы при изменении или дополнении алгоритма. 


### Примеры использования
```python
from selenium import webdriver

# driver = webdriver.Chrome('./chromedriver')   # файл драйвера chromedriver находится в текущей папке
driver = webdriver.Edge()                       # файл драйвера находится в текущей папке

# переход на страницу
driver.get('http://md.zabgu.ru/login/index.php')

driver.close()
```

**Поиск и обращение к элементам интерфейса**
```python
from selenium.webdriver.common.by import By     # класс, описывающий критерии поиска элементов

# поиск элементов по XPATH, 
elements = driver.find_elements(By.XPATH, "//a[contains(text(),'какой-то текст')]")   # поиск ссылки (a), с текстом включающим ...

# поиск по тегу
fields = driver.find_elements(By.TAG_NAME, 'textarea')

# обращение к родителю родителя элемента
ext_search_btn.find_element(By.XPATH, '../..').click()

# обращекние к аттрибуту элемента
a.get_attribute('href')   # ссылка из тега a
```



#### Взаимодействие с элементами
```python
# клик
elements.click()

# очистка поля ввода
some_input.clear()

from selenium.webdriver.common.keys import Keys   # переменные, обозначающие клавиши
# заполнение поля ввода
some_input.send_keys('my login')

# скриншот элемента
element.screenshot('element.png')
```

#### Переключение на вкладку (переключение контекста)
```python
driver.switch_to.window( driver.window_handles[1] )
```
Фактически открытая вкладка не является активной, если не задана как контекст.


# Ссылки
https://selenium-python.readthedocs.io/
