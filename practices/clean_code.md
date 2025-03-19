# Лабораторная работа 4. Чистый код: написание кода, понятного всем

## Содержание

+ [Что такое "Чистый код"?]()
+ [Принципы написания кода]()
+ [Чистый код на Python: руководство по написанию]()
+ [Запахи и антипаттерны]()
+ [Критика методологии]()
+ [Задание]()

## Что такое "Чистый код"?

**"Чистый код"** - набор правил и принципов, помогающих сделать код читаемым, обслуживаемым и масштабируемым. Одноименная книга была опубликована в 2008 году **[Робертом Мартином](https://ru.wikipedia.org/wiki/%D0%9C%D0%B0%D1%80%D1%82%D0%B8%D0%BD,_%D0%A0%D0%BE%D0%B1%D0%B5%D1%80%D1%82_(%D0%B8%D0%BD%D0%B6%D0%B5%D0%BD%D0%B5%D1%80))**, более известный как **Дядюшка Боб (Uncle Bob)**, и с тех пор является бестселлером, а принципы чистого кода прочно вошли в практику IT-сообщества при разработке различного рода ПО.

Мартин описывает методологию "Чистого кода" как **школу мыслей**, для последователей которого описанные далее концепции, принципы и т.п. **являются беспрекословноей истиной, но не абсолютной**. У чистого кода как методологии есть множество недостатков, что делает ее не везде применимой, однако многие идеи можно принять как **вечные и прописные истины, которые программист обязан соблюдать**.

## Принципы написания кода

В рамках книги Мартин рассматривает множество тем, связанных с различными аспектами написания кода (именование, написание функций и комментариев, и т.п.), а также описывает многие принципы, которые в некоторой степени стали уже мемом в IT-коммьюнити: DRY, KISS, SOLID, YAGNI, SINE, и т.п.

<img src="images/clean_code_meme.png" alt="Clean code meme" width="500"/>

### DRY (Don't Repeat Yourself) - Не повторяйся

Данная концепция была впервые сформулирована в книге Энди Ханта и Дэйва Томаса «Программист-прагматик: путь от подмастерья к мастеру», и звучит она следующим образом: **дублирование кода – пустая трата времени и ресурсов**, если есть код, который дублируется в нескольких местах, то следует выделить общую логику и обернуть в функцию. Повторное использование кода - всегда разумное решение.

### KISS (Keep It Simple, Stupid) - Будь проще

Данный принцип постулирует, что **простые системы будут работать лучше и надежнее**, не придумывайте более сложного решения, чем требуется. Написание производительного, эффективного и простого кода - наиболее разумное решение.

### SOLID

**SOLID** - это аббревиатура из первых букв названий пяти принципов:

+ **Single Responsibility** - принцип единственной ответственности;
+ **Open/Closed** - принцип открытости/закрытости;
+ **Liskov Substitution** - принцип подстановки Барбары Лисков;
+ **Interface Segregation** - принцип разделения интерфейсов;
+ **Dependency Injection** - принцип инверсии зависимостей;

Эти пять принципа являются базовыми при написании кода, улучшая гибкость, масштабируемость и поддерживаемость ООП-кода.

**Принцип единственной ответственности** постулирует, что **каждый объект, класс или метод должен иметь одну и только одну причину для изменений**. Это означает, что объект/класс/метод должен отвечать за свою функциональность, не должны существовать "функций/классов/методов бога", которые делают очень много действий, влияющих на всю систему.

Пусть есть класс для файлового менеджера, который умеет читать, записывать и работать с архивами.

```python
from pathlib import Path
from zipfile import ZipFile

class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, data, encoding="utf-8"):
        self.path.write_text(data, encoding)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()
```

Класс нарушает принцип единой ответственности, так как обрабатывает больше одного типа файла. Отрефакторив этот класс согласно принципу, получатся следующие два класса:

```python
from pathlib import Path
from zipfile import ZipFile

class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, data, encoding="utf-8"):
        self.path.write_text(data, encoding)

class ZipFileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()
```

Теперь код становится более поддерживаемым, а также более контролируемым тестами.

**Принцип открытости/закрытости** постулирует, что **класс должен быть открыт для расширения, но закрыт для изменений.**, т.е. добавление новой функциональности не должно происходить через изменение существующего кода.

Пусть есть класс Shape

```python
import math

class Shape:
    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type
        if self.shape_type == "rectangle":
            self.width = kwargs["width"]
            self.height = kwargs["height"]
        elif self.shape_type == "circle":
            self.radius = kwargs["radius"]

    def calculate_area(self):
        if self.shape_type == "rectangle":
            return self.width * self.height
        elif self.shape_type == "circle":
            return math.pi * self.radius**2
```

Данный класс очень плохо масштабируется, так как добавление новой фугуры потребует изменение существующих методов, что непрактично. Если выделить общую логику в отдельный класс, то добавление новой фигуры становится достаточно простым:

```python
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self, shape_type):
        self.shape_type = shape_type

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius**2

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        super().__init__("square")
        self.side = side

    def calculate_area(self):
        return self.side**2
```

Здесь абстрактный класс фигуры определяет группу схожих объектов (поэтому и абстрактный класс, а не интерфейс), от которого наследуются все конкретные реализации.

**Принцип подстановки Барбары Лисков** говорит, что **код, использующий базовый тип, должен иметь возможность использовать подклассы, не зная об этом**.

Пусть есть класс Rectangle и класс-наследник Square (квадрат - прямоугольник с равными сторонами):

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in ("width", "height"):
            self.__dict__["width"] = value
            self.__dict__["height"] = value

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in ("width", "height"):
            self.__dict__["width"] = value
            self.__dict__["height"] = value
```

Когда используется класс Square, то написанный код гарантирует, что квадрат будет одинаковой стороны. Но такая реализация нарушает принцип подстановки Лисков, так как класс Square нельзя использовать как Rectangle. Более того, реализация ломает интерфейс базового класса, меняя его поведение и потенциально приводя к нежелательным последствиям, например, при дебаггинге.

Чтобы исправить ситуацию, можно определить базовый класс, который может использоваться обоими классами:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2
```

При такой иерархии следующий код будет работать корректно:

```python
def get_total_area(shapes):
    return sum(shape.calculate_area() for shape in shapes)

print(get_total_area([Rectangle(10, 5), Square(5)]))
# output: 75
```

Из-за того, что функция учитывает только метод calculate_area базового класса, применение любого класса-наследника не убивает программу. В этом и состоит принцип подстановки Барбары Лисков.

**Принцип разделения интерфейсов** говорит, что **не нужно заставлять клиента (класс) реализовывать интерфейс, который не имеет к нему отношения**. Это означает, что интерфейсы должны быть максимально маленькими таким образом, чтобы классы, их имплементирующие, не были вынуждены реализовывать ненужные методы.

Пусть есть абстрактный класс Printer и два класса-наследника:

```python
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")

    def fax(self, document):
        raise NotImplementedError("Fax functionality not supported")

    def scan(self, document):
        raise NotImplementedError("Scan functionality not supported")

class ModernPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")
```

В данном примере Printer выступает как интерфейс для OldPrinter и ModernPrinter. Однако, OldPrinter **вынужден** имплементировать (фактически, делать заглушку) методы, которые ему не нужны.

Решением данной проблемы является декомпозиция базового класса на более мелкие интерфейсы таким образом, чтобы наследовались только нужные фичи:

```python
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass

class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")

class NewPrinter(Printer, Fax, Scanner):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")
```

Теперь для OldPrinter не требуется имплементация ненужных методов, позволяя создавать различные классы под конкретные задачи без ненужного кода.

**Принцип **