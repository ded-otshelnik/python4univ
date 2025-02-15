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

3. 

## Документация кода

## Задание
