# ООП

## 1. Введение в объектно-ориентированную модель Python

**Класс** — пользовательский тип данныхю Определяется через ключевое слово `class`. Класс обычно содержит поля (атрибуты) и методы.

**Поля** — переменные объявленные внутри класса. Поля 
Атрибуты экземпляра обычно определяются в методе инициализации.

Модификаторов public, private, protcted в чистом виде нет. Для *обозначения* таких модификаторов используется знаки подчеркивания в начале имени поля.
- `self.public_field`
- `self._protected_field`
- `self.__private_name`


Пример класса

```python
class SensorData:
    # аналог статического поля, принадлежит классу, а не объекту
    temp_units = "Celsius"

    # конструктор
    def __init__(self, temperature, humidity, pressure):
        # поля принято объявлять именно в конструкторе
        # self = this
        self.name = "sensor_1234"                 # название датчика
        self._location = "ванная"                 # расположение датчика;
        self.__notes = "мне нечего скрывать"
        self.__temp = temperature
        self.__humidity = humidity
        self.__pressure = pressure

    def surprise_field(self, value):
        # в других методах тоже можно объявлять поля, но это не принято
        self.description = value

# s1 - объект (на самом деле ссылка на объект, т.к. класс - ссылочный тип)
# объект = экземпляр класса
s1 = SensorData(26.3, 42.1, 91.534)     # вызов конструктора
s2 = SensorData(22, 22, 92)             # вызов конструктора

# примеры обращения к полям объекта
print(s1.name)              # Ok
print(s1._location)         # сомнительно, но можно
# print(s1.__temp)            # Нет!
print(s1._SensorData__temp)   # Секретное имя закрытого поля! (так можно, но зачем?)

# print(s1.description)         # Ошибка AttributeError! поле ещё не создано
s1.surprise_field('датчик возле вентиляции')
print(s1.description)         # Ok

s1.description_surprise = "Внезапно добавленное в ОБЪЕКТ поле"
print(s1.description_surprise)      # Ок
# print(s2.description_surprise)      # Ошибка AttributeError!


print(s1.temp_units)                # обращение к полю класса
print(SensorData.temp_units)        # обращение к полю класса
s1.temp_units = "Fahrenheit"        # Создание поля ЭКЗЕМПЛЯРА!
print(s1.temp_units)                # обращение к полю ЭКЗЕМПЛЯРА!
print(s2.temp_units)                # обращение к полю класса
```


## 2. Метод **init** и атрибуты экземпляра

Метод `__init__` вызывается сразу после создания объекта. Он выполняет начальную настройку состояния объекта. `self` указывает на сам экземпляр. Атрибуты, присвоенные через `self.имя`, будут хранить данные.

Пример:

```python
class SensorReading:
    def __init__(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
```

## 3. Методы класса

Метод — это функция, определённая внутри класса. Первый параметр метода — это ссылка на экземпляр класса.

Пример метода для вычисления средней величины:

```python
class SensorReading:
    def __init__(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

    def average(self):
        return (self.temperature + self.humidity + self.pressure) / 3
```

Метод вызывается через экземпляр:

```python
reading.average()
```


## 4. Специальные методы

Python поддерживает механизм специальных методов. Они позволяют интегрировать объекты в синтаксис языка. Класс может определять строки представления, правила сравнения и многое другое.

Пример переопределения представления объекта:

```python
class SensorReading:
    def __init__(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

    def __repr__(self):
        return f"SensorReading(temp={self.temperature}, hum={self.humidity}, pres={self.pressure})"
```

Теперь объект печатается в удобном виде:

```python
print(reading)  # SensorReading(temp=23.5, hum=40.2, pres=1012.3)
```

## @staticmethod, @classmethod



## 5. Инкапсуляция и свойство property

Инкапсуляция ограничивает доступ к данным. В Python нет строгого механизма сокрытия данных. Однако принято использовать имя, начинающееся с подчёркивания, чтобы указать на внутренний атрибут.

Свойства (`property`) позволяют управлять доступом к атрибуту. Можно определять логику чтения, обновления и удаления. Это обеспечивает защиту данных.

Пример:

```python
class SensorReading:
    def __init__(self, temperature):
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -100 or value > 100:
            raise ValueError("Недопустимая температура")
        self._temperature = value
```



## 6. Атрибуты класса

Существуют атрибуты, значения которых общие для всех экземпляров. Они определяются в теле класса, но вне методов.

Пример:

```python
class SensorReading:
    unit = "SI"

    def __init__(self, temperature):
        self.temperature = temperature
```

Обращение:

```python
SensorReading.unit
reading.unit
```



## 7. Наследование

Класс может расширять другой класс и наследовать его свойства. Это позволяет переиспользовать код и создавать иерархии.

Пример:

```python
class ExtendedReading(SensorReading):
    def __init__(self, temperature, humidity, pressure, co2):
        super().__init__(temperature, humidity, pressure)
        self.co2 = co2
```

Использование `super()` обеспечивает вызов методов, например конструктора, родительского (базового) класса.



## 8. Проблема шаблонного кода и решение через датаклассы

При создании классов, содержащих только данные, приходится писать шаблонный код: `__init__`, `__repr__`, методы сравнения. Датаклассы позволяют автоматически генерировать такие методы.

Датакласс создаётся с помощью декоратора `@dataclass` из модуля `dataclasses`.

Пример:

```python
from dataclasses import dataclass

@dataclass
class SensorReading:
    temperature: float
    humidity: float
    pressure: float
```

Датакласс автоматически создаёт методы `__init__`, `__repr__` и `__eq__`.

Экземпляр создаётся привычным способом:

```python
reading = SensorReading(23.5, 40.2, 1012.3)
```


## 9. Параметры датаклассов

Датаклассы поддерживают параметры для настройки поведения.

Пример создания неизменяемого класса:

```python
@dataclass(frozen=True)
class SensorData:
    temperature: float
    humidity: float
    pressure: float


s1 = SensorData(25, 65, 90)
print(s1)                       # SensorData(temperature=25, humidity=65, pressure=90) 

s1.temperature = 33     # Ошибка dataclasses.FrozenInstanceError

s2 = SensorData()
s2.temperature = 33     # Ошибка dataclasses.FrozenInstanceError
```

При попытке изменить значение атрибута будет выброшено исключение.

Можно определять значения по умолчанию.

```python
from dataclasses import dataclass, field

@dataclass
class SensorReading:
    temperature: float
    humidity: float = 50.0
    pressure: float = field(default=1013.0)
```



## 10. Методы в датаклассах

Датаклассы могут содержать методы так же, как обычные классы.

```python
@dataclass
class SensorReading:
    temperature: float
    humidity: float
    pressure: float

    def strange_average(self):
        return (self.temperature + self.humidity + self.pressure) / 3
```

При необходимости можно переопределить методы. Например, определить собственное строковое представление.

```python
@dataclass
class SensorReading:
    temperature: float
    humidity: float
    pressure: float

    def __str__(self):
        return f"T={self.temperature} H={self.humidity} P={self.pressure}"
```


## Инициализация после создания объекта

Иногда требуется выполнить дополнительную логику сразу после автоматической инициализации. Для этого используется метод `__post_init__`.

Пример:

```python
@dataclass
class SensorReading:
    temperature: float
    humidity: float
    pressure: float

    def __post_init__(self):
        if self.temperature < -100 or self.temperature > 100:
            raise ValueError("Недопустимая температура")
```

Метод вызывается сразу после автоматически сгенерированного `__init__`.

#### Сравнение датаклассов и обычных классов

Датаклассы уменьшают количество шаблонного кода. Они подходят для объектов, представляющих данные. Обычные классы подходят для объектов со сложным поведением. Датакласс остаётся полноценным классом. Его можно расширять или включать в иерархию.
