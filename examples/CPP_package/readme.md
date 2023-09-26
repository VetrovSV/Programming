# Компиляция библиотеки для использования в Python
PyBing11 - один из подходов создания C++ библиотеки, пригодной для использования в Python.

Установка модуля для связывания библиотек
```bash
pip install pybind11
```


### Пример библиотеки
Для примера приведём содержимое файла-обёртки для C++ кода. Рекомендуется вместо непосредственного приведения кода в таких файлах использовать отдельные cpp и заголовочные файлы, а уже потом в дополнении к ним создавать этот файл-обёртку.
```cpp
// файл для взаимодействия с Python окружением

#include <pybind11/pybind11.h>
#include <vector>


// ==================================================== Код на С++:

/// return body mass index; m - mass, kg; р - tall, m;
float BMI(float m, float h){
	return m/h/h;
}



// ==================================================== Код, для настройки взаимодействия с Python:

namespace py = pybind11;
constexpr auto byref = py::return_value_policy::reference_internal;



// раздел описания модуля на С++ для Python
PYBIND11_MODULE(MyLib, m)		// этот макрос вызывается при подключение (import) модуля в Python
								// MyLib - название модуля; имя cpp файла такое же
{
	// документация модуля
	m.doc() = "module docstring";

	// описание всего, что модуль предоставляет(типы, функции):

	// описание функции
	m.def("BMI", &BMI, "return body mass index; m - mass, kg; р - tall, m;");

}
```


Компиляция C++ библиотеки:
```bash
g++ -O3 -Wall -shared -std=c++20 -fPIC $(python3 -m pybind11 --includes) pywrap.cpp -o MyLib$(python3-config --extension-suffix)
```
- `O3` - 3-й уровень оптимизации кода
- `Wall` - отключить все предупреждения  
- `shared` - создать разделяемую библиотеку
- `fPIC` - generate Position Independent Code
- `$(python3 -m pybind11 --includes)` выдаёт пути подключения (вместе с ключом I) заголовочных файлов, например:
	`-I/usr/include/python3.10 -I/home/username/.local/lib/python3.10/site-packages/pybind11/include`
g++ -shared -std=c++19 -fPIC $(python3 -m pybind11 --includes) pywrap.cpp -o MyLib$(python3-config --extension-suffix)
- `-o MyLib$(python3-config --extension-suffix)` - составление имени выходного файла из MyLib и вывода команды `python3-config --extension-suffix`, например `.cpython-310-x86_64-linux-gnu.so`

Появится .so файл - файл статической библиотеки, например с таким именем: example.cpython-310-x86_64-linux-gnu.so


### Подключение из Python
```python
# подключаемая библиотека должна находится в текущей папке
# или путь к папке с библиотекой нужно добавить:
#     import sys
#     sys.path.append('/.../application/app/folder')

import MyLib
```

# Ссылки
- https://www.matecdev.com/posts/cpp-call-from-python.html
- https://realpython.com/python-bindings-overview/#pybind11 - обзор способов связывания библиотек, преобразования и совместимости типов.

