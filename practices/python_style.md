# Лабораторная работа 1. Оформление Python-кода. Стиль кода, комментарии, документация

В любом языке программирования рано или поздно сообщество приходит к выводу, что необходимо **стандартизировать** правила написания и оформления кода, использования или добавления/удаления инструментов языка, и т.д. Python не является исключением: с 2000 года публикуются специальные документы - **Python Enhancement Proposals (PEPs)**, которые предоставляют информацию сообществу Python, а также описывает изменения в языке (добавление/удаление функций, описания проблем и изменений в связи с ними сделанными).

В 2001 году вышли наиболее важные PEP под авторством BDFL ("Benevolent Dictator for Life" - доброжелательный пожизненный диктатор) и одновременно создателя языка Python, Гвидо ван Россума, а именно - **[PEP 8](https://peps.python.org/pep-0008/)** и **[PEP 257](https://peps.python.org/pep-0257/)**. Документы описывают принятые в Python-коммьюнити договоренности и соглашения о том как правильно писать и оформлять код, как называть переменные/функции/классы и т.п., а также как документировать и описывать код, написанный разработчиком. Правила, представленные в этих документах являются **официальным стандартом** оформления кода на Python.

## Zen of Python, питонический код, PEP 8 и PEP 257

Гвидо ван Россум создавал Python как легко расширяемый, легко читабельный и понятный для тех, кто не имеет сильного бэкграунда в программировании на таких достаточно громозких и порой сложных языках как C/C++, Java, FORTRAN. Благодаря модульности, гиганской расширяемости и минимализму языка разработчик может концентрироваться не на синтаксисе и грамматике, а на методологии программирования, решении конкретных задач.

Идея сформулировать фундаментальные принципы Python была реализована в 1999 году одним из разработчиков языка и его "золотого стандарта" CPython, придумавшем также алгоритм сортировки [Timsort](https://ru.wikipedia.org/wiki/Timsort) - Тимом Питерсом. Набор 20 принципов (хотя в реальности их 19), который он написал , стал называться **Zen of Python (Дзен Пайтона)**, и он сейчас доступен в интерпретаторе через вызов ```import this```:

```txt
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

Эти принципы, оформленные в виде афоризмов, описывают основные рекомендации, которых должны придерживаться программисты. Данные идеи нашли отражения в тех конвенциях, соглашениях, которые приняты в PEP 8 и PEP 257. Код, который придерживается вышеописанным принципам (по большей части) и соответствует PEP 8 и PEP 257, называется **Питоническим (Pythonic)**.

## Оформление кода

### Отступы

Для отступа должны использоваться 4 пробела (именно пробелы, не tab).

```python
# Correct:

# Aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Hanging indents should add a level.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)

# Wrong:

# Arguments on first line forbidden when not using vertical alignment.
foo = long_function_name(var_one, var_two,
    var_three, var_four)

# Further indentation required as indentation is not distinguishable.
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)
```

Для продолжения строк правило 4-х пробелов может не выполняться:

```python
# Hanging indents *may* be indented to other than 4 spaces.
foo = long_function_name(
  var_one, var_two,
  var_three, var_four)
```

Несколько операторов ``if`` должны разделяться следующим образом:

```python
# No extra indentation.
if (this_is_one_thing and
    that_is_another_thing):
    do_something()

# Add a comment, which will provide some distinction in editors
# supporting syntax highlighting.
if (this_is_one_thing and
    that_is_another_thing):
    # Since both conditions are true, we can frobnicate.
    do_something()

# Add some extra indentation on the conditional continuation line.
if (this_is_one_thing
        and that_is_another_thing):
    do_something()
```

```python
# Correct:

my_list = [
    1, 2, 3,
    4, 5, 6,
    ]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
    )

# Also works: 

my_list = [
    1, 2, 3,
    4, 5, 6,
]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)
```

### Длина строки

Максимальная длина строки кода - 79 символов, для текста (docstrings, комментарии) - 72 символа. Если требуется больше, то лучше воспользоваться скобками, чтобы обернуть строки кода, хотя при этом язык позволяет использовать обратный слэш ```\```:

```python
with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())
```

### Бинарные операторы

Для бинарных операторов, по традиции математиков и рекомендации Дональда Кнута, должен использоваться следующий формат:

```python
# Correct:
# easy to match operators with operands
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```

Для отделения основной функции и определений классов должны использоваться две пустые строки, методов внутри классов или логических секций внутри кода - одна, для отделение групп похожих функций может использоваться больше одной пустой строки.

### Кодировка файлов с исходным кодом

Код на языке Python должен **всегда** использоваться UTF-8 и не должен иметь в начале файла определения кодировки. Использование символов не из кодировки UTF-8 допускается только в тестах.

Все идентификаторы в библиотеках Python (как std, так и open-source проекты) **обязаны** содержать только слова на английском, где это возможно (во многих случаях используются технические термины и\или аббревиатуры, которые не являются английскими, поэтому такое допускается).

### Импорты

Импорты библиотек должны находиться в начале файла и должны быть раздельными:

```python
# Correct:
import os
import sys

# Wrong:
import sys, os

# Correct:
from subprocess import Popen, PIPE
```

Импорты должны быть отсортированы в следующем порядке, все группы должны разделяться пустой строкой:

1. Импорты модулей стандартной библиотеки;
2. Импорты сторонних модулей;
3. Импорты локальных модулей.

Рекомендованы абсолютные импорты как более читабельные и лучше работающие (по крайней мере, ошибки более понятные). Несмотря на это, позволяется использовать относительные импорты:

```python
import mypkg.sibling
from mypkg import sibling
from mypkg.sibling import example

from . import sibling
from .sibling import example
```

Когда импортируется класс из модуля, обычно это записывается следующим образом:

```python
from myclass import MyClass
from foo.bar.yourclass import YourClass
```

Если модули содержат одинаковые имена, то рекомендуется использовать обращение через модуль:

```python
import myclass
import foo.bar.yourclass

obj1 = myclass.MyClass()
obj2 = foo.bar.yourclass.YourClass()
```

Объявления вида ```from module import *``` должны избегаться максимально по причине возможных конфликтов пространств имен.

### Специальные имена уровня модуля

Специальные имена уровня модуля такие, как ```__all__, __author__, __version__``` и т.п., должны быть размещены после docstring модуля, но перед любым импортом, кроме ```from __future__``` импортов:

```python
"""This is the example module.

This module does stuff.
"""

from __future__ import barry_as_FLUFL

__all__ = ['a', 'b', 'c']
__version__ = '0.1'
__author__ = 'Cardinal Biggles'

import os
import sys
```

### Кавычки для строк

Общей рекомендации как определять строки (через ```"``` или ```'```) не существует. Единственное, что использование одновременно одинарных кавычек и двойных решает проблему экранирования кавычек.

### Пробелы в выражениях и операторах

Избегайте переиспользования пробела в следующих ситуациях:

1. Внутри скобок:

    ```python
    # Correct:
    spam(ham[1], {eggs: 2})
    # Wrong:
    spam( ham[ 1 ], { eggs: 2 } )
    ```

2. Между последней запятой и закрывающей скобкой:

    ```python
    # Correct:
    foo = (0,)
    # Wrong:
    bar = (0, )
    ```

3. В срезах (поскольку : ведет себя как бинарный оператор):

    ```python
    # Correct:
    ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
    ham[lower:upper], ham[lower:upper:], ham[lower::step]
    ham[lower+offset : upper+offset]
    ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
    ham[lower + offset : upper + offset]
    # Wrong:
    ham[lower + offset:upper + offset]
    ham[1: 9], ham[1 :9], ham[1:9 :3]
    ham[lower : : step]
    ham[ : upper]
    ```

4. При вызове функции:

    ```python
    # Correct:
    spam(1)

    # Wrong:
    spam (1)
    ```

5. При индексации и срезе перед открывающей скобкой:

    ```python
    # Correct:
    dct['key'] = lst[index]

    # Wrong:
    dct ['key'] = lst [index]
    ```

6. При операции присваивания:

    ```python
    # Correct:
    x = 1
    y = 2
    long_variable = 3

    # Wrong:
    x             = 1
    y             = 2
    long_variable = 3
    ```

Также рекомендуется окамлять пробелами составные операторы (```+=, -=```, и т.д.), булевы операторы (```and, not, or, not``` и их комбинации), сравнения (```==, <>, !=``` и т.д.).

Пробелы также рекомендуется добавлять между операторами с разными приоритетами выполнения:

```python
# Correct:
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)

# Wrong:
i=i+1
submitted +=1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)
```

В аннотациях функции должны использоваться обычные правила для двоеточий и иметь пробелы следующим образом:

```python
# Correct:
def munge(input: AnyStr): ...
def munge() -> PosInt: ...

# Wrong:
def munge(input:AnyStr): ...
def munge()->PosInt: ...
```

При использовании = для указания аргумента ключевого слова в вызове функции не используйте пробелы:

```python
# Correct:
def complex(real, imag=0.0):
    return magic(r=real, i=imag)

# Wrong:
def complex(real, imag = 0.0):
    return magic(r = real, i = imag)
```

### Соглашение по именованиям

Имена, которые следует избегать:

1. Односимвольные имена (кроме счетчиков или итераторов). **Никогда** не используйте строчную `l`, заглавную `O` и `I` как имена переменных, так как в некоторых шрифтах они практически неотличимы от нуля или единицы.
2. Дефисы в именах модулей и пакетов.
3. Двойные подчеркивания (в начале и конце имен, например, `__all__`) не для специальных переменных и\или функций.

Правила именования:

+ Для функций и переменных - **snake_case** (слова из маленьких букв с разделяющими подчеркиваниями, например, `my_variable`)
+ Для констант - имена только из заглавных букв с разделителем в виде нижнего подчеркивания (например, `MAX_OVERFLOW`)
+ Имена классов - **CamelCase** с заглавным символом в начале.

### Общие рекомендации

+ Для конкатенации строк рекомендуется использовать `''.join(...)` из-за особенностей реализации строк и их конкатенации.
+ Сравнение объектов-синглтонов (присутствующих в глобальном пространстве имен только один раз), например, `None`, должно всегда выполняться через `is` или `is not` и никогда через `==`.
+ Используйте в булевых выражениях следующий формат (пока позволяет логика и смысл булевого выражения):
  
  ```python
  # Correct:
    if foo is not None:
        
    # Wrong:
    if not foo is None:
  ```

+ При реализации упорядочивания и сравнения рекомендуется имплементировать все 6 операций сравнения: `__eq__, __ne__, __lt__, __le__, __gt__, __ge__`, которые являются методами, перегружающие операторы `==, !=, <, <=, >, >=` соответственно. При реализации важно учитывать **рефлексивность операций** (например, если x > y истинно, то y < x тоже должно быть истинно).
+ Всегда используйте вместо `lambda` оператор `def` для функций, которые определяются для использования дальше по коду, так как при отладке в таком случае предоставляется более понятная и читабельная информация.
+ При отлавливании исключений указывайте в блоке `except` имена всех возможных исключений вместо "голого" `except` для более понятной отладки. Единственные два исключения: логгирование (например, для HTTP запросов иногда такое может иметь место) и выполнение некоторой работе по закрытию/очистке ресурсов (вместе с конструкцией try...finally) с передачей исключения вверх по стеку вызовов.
+ Ограничивайте максимальным образом блоки `try/except`, например:

    ```python
    # Correct:
    try:
        value = collection[key]
    except KeyError:
        return key_not_found(key)
    else:
        return handle_value(value)

    # Wrong:
    try:
        # Too broad!
        return handle_value(collection[key])
    except KeyError:
        # Will also catch KeyError raised by handle_value()
        return key_not_found(key)
    ```

+ Когда требуется подключение какого-либо ресурса локально, используйте менеджер контекста `with` или, если первое невозможно, блок `try...finally`.
+ Внутри блока `with` менеджеры контекста должны вызываться через раздельные функции или методы всегда, когда они что-то делают, кроме ситуаций захвата и высвобождения ресурса:

    ```python
    # Correct:
    with conn.begin_transaction():
        do_stuff_in_transaction(conn)

    # Wrong:
    with conn:
        do_stuff_in_transaction(conn)
    ```

+ Прописывайте все конструкции ``return``, где по логике кода функция должна **явно** возвращать значение:

    ```python
    # Correct:

    def foo(x):
        if x >= 0:
            return math.sqrt(x)
        else:
            return None

    def bar(x):
        if x < 0:
            return None
        return math.sqrt(x)

    # Wrong:

    def foo(x):
        if x >= 0:
            return math.sqrt(x)

    def bar(x):
        if x < 0:
            return
        return math.sqrt(x)
    ```

+ Не сравнивайте булевские значения с True|False используя `==` или `is`:

    ```python
    # Correct:
    if greeting:

    # Wrong:
    if greeting == True:

    # Wrong:
    if greeting is True:
    ```

## Документация кода

### Комментарии

Комментарии должны быть законченными предложениями и начинаться с заглавной буквы. Также они должны находиться на том же отступе, что и код, к которому комментарий написан, и **перед** самим кодом, а не на той же строке.

Комментарии, которые противоречат коду, хуже, чем их полное отсутствие. Старайтесь держать комментарии актуальными при изменении кода. Помимо этого, комментарии должны не быть тривиальными, а должны пояснять суть работы кода или задумки программиста.

### Docstrings

**Docstring** - строка, возникающая как первое выражение в модуле, функции, классе или методе и являющаяся (чаще всего) документацией для описываемого кода. Такие строки доступны через атрибут `__doc__` объекта.

Все модули должны иметь docstrings, и все функции, классы и публичные методы, экспортируемые модулем также должны иметь строки документации. Пакеты могут быть задокументированными через docstring, лежащий в `__init__.py`.

Выглядят docstrings следующим образом:

```python
def kos_root():
    """Return the pathname of the KOS root directory."""
    global _kos_root
    if _kos_root: return _kos_root
    ...

def complex(real=0.0, imag=0.0):
    """Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)
    """
    if imag == 0.0 and real == 0.0:
        return complex_zero
    ...
```

Рекомендации по использованию docstring:

1. Для таких строк используются тройные двойные кавычки `"""`;
2. В docstrings нельзя указывать сигнатуру функции/метода. Вместо этого опишите что делает функция словами. Для описания сигнатуры есть аннотации, рассматриваемые далее.

### Аннотации

**Аннотации** в Python - метаданные, которые говорят о типах данных, принимаемых в качестве аргументов и возвращаемых как результат выполнения кода.

Синтаксис аннотаций выглядит следующим образом:

```python
def greeting(name: str) -> str:
    return 'Hello ' + name
```

Аннотации поддерживают объединение типов, псевдонимы через модуль `typing`, а с недавних пор еще и указание типа-дженерика, позволяя описывать функциональность для любого типа с сохранением логической связи в метаданных для большей удобочитаемости. Например:

```python
from typing import Generic, TypeVar
T = TypeVar('T')

class Box(Generic[T]):
    def __init__(self, content):
        self.content: T = content
```

После выхода Python 3.12 дженерики теперь не требуют модуль `typing` и выглядят следующим образом:

```python
from collections import deque

class Queue[T]:
    def __init__(self) -> None:
        self.elements: deque[T] = deque()

    def push(self, element: T) -> None:
        self.elements.append(element)

    def pop(self) -> T:
        return self.elements.popleft()
```

Важно: несмотря на то, что аннотации доступны в процессе выполнения через атрибут `__annotations__`, **никакой проверки типов в процессе выполнения не происходит**. Ключевая идея использования аннотаций - дать пользователю и/или программисту информацию о том, что разработчиком полагается как аргументы функции или метода, а также что должно вернуться в результате (или должно ли вернуться что-то вообще). Также этот инструмент позволяет использовать специальные утилиты - **линтеры** - для "проверки" типов **отдельно от выполнения программы**. Наиболее популярными линтерами для Python являются **Pylint**, **Flake8** и **mypy**.

Помимо того, в Python позволяется аннотировать переменные, к примеру:

```python
# Tuple packing with variable annotation syntax
t: Tuple[int, ...] = (1, 2, 3)
# or
t: Tuple[int, ...] = 1, 2, 3  # This only works in Python 3.8+

# Tuple unpacking with variable annotation syntax
header: str
kind: int
body: Optional[List[str]]
header, kind, body = message
```

Однако, при аннотации переменных они не инициализуруются, из-за чего следующий код не запустится и выдаст ошибку:

```python
a: int
print(a)  # raises NameError
```

Или:

```python
def f():
    a: int
    print(a)  # raises UnboundLocalError
    # Commenting out the a: int makes it a NameError.
```

## Задание

Представлены 5 кусков кода:

```python
# 1st: function
def outer(a,b):
 def inner(x):
  return x*x
 result = inner(a) + inner(b)
 return result

# 2nd: function
def processData(d1,d2,d3):
    """Функция обрабатывает три значения"""
    avg=(d1+d2+d3)/3
    return avg

# 3rd: class
class calculator:
 def __init__(self,a,b):
  self.a=a
  self.b=b
 def add(self):
  return self.a+self.b
 def subtract(self):
  return self.a-self.b

# 4th: function
def sumList(lst):
  """считает сумму списка"""
  s=0
  for i in lst: s+=i
  return s

# 5th: class
class bankaccount:
  def __init__(self,owner,balance=0):
    self.owner=owner
    self.balance=balance
  def deposit(self,amount):
    self.balance+=amount
  def withdraw(self,amount):
    if amount<=self.balance:
      self.balance-=amount
    else:
      print("Недостаточно средств")
```

Задание: исправить код, приведя и задокументируя его по правилам Python.
