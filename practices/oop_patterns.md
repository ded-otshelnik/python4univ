# Лабораторная работа 3. Паттерны объектно-ориентированного проектирования

## Содержание

+ [Концепции ООП: класс, объект, и т.д.](oop_patterns.md#концепции-ооп-класс-объект-и-тд)
+ [Классификация паттернов объектно-ориентированного проектирования](oop_patterns.md#классификация-паттернов-объектно-ориентированного-проектирования)
+ [Порождающие паттерны](oop_patterns.md#порождающие-паттерны)
+ [Структурные паттерны](oop_patterns.md#структурные-паттерны)
+ [Паттерны поведения](oop_patterns.md#паттерны-поведения)
+ [Задания](oop_patterns.md#задания)

Доминирующей парадигмой программирования на протяжении уже 30 лет является **объектно-ориентированное программирование (ООП)**. Большинство языков программирования так или иначе поддерживает хотя бы некоторые концепты ООП.

С повсеместным внедрением ООП в код многие программисты, которые практикуют данный подход, пришли к выводу, что необходимо систематизировать **шаблоны проектирования (design patterns)**. Исходя из этого, группа из 4-х программистов, прозванных позднее **Бандой четырех (Gang of Four)**, Эрих Гамма, Ричард Хелм, Ральф Джонсон и Джон Влиссидесс, написала в 1994 году книгу **"Design Patterns: Elements of Reusable Object-Oriented Software"**, или **Паттерны объектно-ориентированного проектирования**, которая рассматривает преимущества и недостатки ООП, а также содержит описание 23 классических паттернов, которые продемонстрированы на примерах (хотя примеры эти написаны на языках С++ и Smalltalk). Книга уже является классической для разработчиков, так как паттерны, описанные в ней, применяются повсеместно.

## Концепции ООП: класс, объект, и т.д

Прежде, чем рассматривать паттерны ООП подробно, определим некоторые важные термины:

+ **Класс** - модель, по которой строятся объекты, описывающая их структуру (набор полей и начальное состояние) и связанные с классом алгоритмы (методы).

    ```python
    class MyClass:
        ...
    ```

+ **Объект** - экземпляр класса с собственным состоянием. Взаимодействовать с объектом можно через методы класса, к которому объект принадлежит.
  
    ```python
    my_object = MyClass()
    ```

+ **Состояние объекта** - данные (в том числе и ссылки на другие данные), которые храняться в объекте. Представляется в виде полей.
+ **Поведение объекта** - методы объекта, ассоциированного с конкретным классом.
+ **Инкапсуляция** - свойство системы, позволяющее объединить данные и методы, которые с ними работают, в классе, а также скрывать детали имплементации.

    ```python
    class MyClass:
        def __init__(self) -> None:
            self._private = 1
        
        def get_private(self) -> int:
            return self._private
    ```

+ **Абстракция** - набор общих характеристик объекта без описания их конкретных/детальных реализаций. Такой подход позволяет изменять реаизацию, не меняя способ взаимодействия с объектом.
+ **Наследование** - механизм, который позволяет новому классу (дочернему классу, классу-наследнику) *унаследовать* поведение уже существующего класса. В рамках отношений между классами описывается как "является" ("is")

    ```python
    class MySubClass(MyClass):
        ...
    ```

+ **Ассоциация** - ситуация, когда класс включает в себя как поле другой класс. В рамках отношений между классами описывается как "имеет/содержит" ("contains").
+ **Композиция** - частный случай ассоциации, когда класс, вложенный в другой класс, **полностью** управляется классом-"контейнером", т.е. объект вложенного класса не существует отдельно от внешнего класса.
+ **Агрегация** - частный случай ассоциации, когда класс, вложенные в другой класс, создается **вне основного класса** и передается в конструктор как параметр.
+ **Интерфейс** - класс-контракт, определяющий методы, которые **должны** быть определены в классах-наследниках.

    ```python
    class MyInterface(Protocol):
        def needed_method(self) -> str:
            ...
    ```

+ **Полиморфизм** - свойство системы использовать объекты с одинаковым интерфейсом без информации о типе и внутренней структуре объекта.

    ```python
    class ConcreteImplementationA:
        def needed_method(self) -> str:
            return "concrete_a"

    class ConcreteImplementationB:
        def needed_method(self) -> str:
            return "concrete_b"

    def polymorphic_function(obj: MyInterface) -> None:
        print(obj.needed_method())
    ```

## Классификация паттернов объектно-ориентированного проектирования

**Паттерн проектирования** - высокоуровневое решение часто встречающейся проблемы при разработке программного обеспечения.

Согласно Банде четырех, паттерны проектирования делятся на 3 группы:

+ Порождающие паттерны:
  1. Одиночка (Singleton);
  2. Прототип (Prototype);
  3. Строитель (Builder);
  4. Абстрактная фабрика (Abstract Factory);
  5. Фабричный метод (Factory Method).
+ Структурные паттерны:
  1. Адаптер (Adapter);
  2. Декоратор (Decorator);
  3. Заместитель (Proxy);
  4. Компоновщик (Composite);
  5. Мост (Bridge);
  6. Приспособленец (Flyweight);
  7. Фасад (Facade).
+ Паттерны поведения:
  1. Интерпретатор (Interpreter);
  2. Шаблонный метод (Template method);
  3. Итератор (Iterator);
  4. Команда (Command);
  5. Наблюдатель (Observer);
  6. Посетитель (Visitor);
  7. Посредник (Mediator);
  8. Состояние (State);
  9. Стратегия (Strategy);
  10. Хранитель (Memento);
  11. Цепочка обязанностей (Chain of responsibilities).

Далее будут рассмотрены наиболее важные и популярные паттерны, которые могут встретиться при разработке программного обеспечения.

## Порождающие паттерны

**Порождающие паттерны** - паттерны, абстрагирующие процесс создания объектов. Они позволяют сделать систему независимой от способа создания, композиции и представления объектов.

Для порождающих паттернов важны два аспекта: во-первых, паттерны инкапсулируют знания о конкретных классах, которые применяются в системе, во-вторых, они скрывают подробности создания и компоновки объектов классов. Единственная информация, которая известна - это интерфейсы, поэтому порождающие паттерны обеспечивают большую гибкость в отношении того, **что** создается, **кто** это создает, **как** и **когда**.

### Одиночка (Singleton)

**Одиночка** - порождающий паттерн, целью которого является гарантия существования только одного экземпляра класса, предоставляя к нему глобальную точку доступа.

Реализуется обычно паттерн следующим образом:

```python
class Singleton:
    _instance: Optional[Singleton] = None

    def __new__(cls) -> Singleton:
        instance: Singleton
        if cls._instance is None:
            instance = object.__new__(cls)
            cls._instance = instance
        else:
            instance = cls._instance
        return instance
```

Благодаря паттерну класс будет работать следующим образом

```python
>>> singleton1 = Singleton()
>>> singleton2 = Singleton()
>>> singleton1 is singleton2
True
```

Преимущества паттерна:

+ Контролируемый доступ к единственному экземпляру;
+ Сокращение пространства имен;
+ Возможность уточнения операций и представления (через наследование);
+ Возможность использования переменного числа экземпляров (легко изменить класс, чтобы было более одного экзепляра);

### Прототип (Prototype)

**Прототип** - порождающий паттерн, который позволяет системе создавать объекты через клонирования некоторого объекта-прототипа с возможностью модификации клона.

Пусть есть интерфейс и две имплементации вида:

```python
class Prototype(Protocol):
    def clone(self) -> Prototype:
        ...

    def change(self, x: int) -> int:
        ...

    def get_result(self) -> int:
        ...

class ConcretePrototype1(Prototype):
    def __init__(self, x: int) -> None:
        self._x = x

    def clone(self) -> ConcretePrototype1:
        return self.__class__(x=self._x)

    def change(self, x: int) -> int:
        self._x = x

    def get_result(self) -> int:
        return self._x + 1

class ConcretePrototype2(Prototype):
    def __init__(self, x: int, y: int) -> None:
        self._x = x
        self._y = y

    def clone(self) -> ConcretePrototype2:
        return self.__class__(x=self._x, y=self._y)

    def change(self, x: int) -> int:
        self._x = x

    def get_result(self) -> int:
        return self._x + self._y
```

И есть клиент, работающий с прототипом:

```python
class Client:
    def __init__(self, prototype: Prototype) -> None:
        self._prototype = prototype

    def create(self, x: int) -> Prototype:
        new_obj = self._prototype.clone()
        new_obj.change(x=x)
        return new_obj
```

Тогда можно использовать классы-прототипы следующим образом:

```python
>>> client1 = Client(ConcretePrototype1(x=1))
>>> new_1 = client1.create(7)
>>> new_2 = client1.create(9)
>>> new_1.get_result()
7
>>> new_2.get_result()
9
>>> client2 = Client(ConcretePrototype2(x=1, y=2))
>>> new_3 = client2.create(3)
>>> new_3.get_result()
5
>>> new_3 = client2.create(4)
>>> new_4.get_result()
6
```

Преимущества паттерна:

+ Добавление и удаление продуктов во время выполнения через регистрацию на стороне клиента;
+ Определение новых объектов путем изменения значений (де-факто, убирая необходимость в создании дополнительных классов);
+ Динамическая настройка конфигурации приложения классами.

Единственная проблема - необходимость реализации функции клонирования, что не всегда легко, особенно если во внутреннем представлении объекта присутствуют другие некопируемые объекты или циклические ссылки, но в большинстве случаев вопросы являются решаемыми.

### Строитель (Builder)

Строитель - порождающий паттерн, который отделяет логику создания сложного объекта от самого объекта таким образом, чтобы эта же логика могла быть использована для построения абсолютно разных объектов.

Пусть есть некоторый класс, который необходимо сконструировать, и класс, который создает необходимый объект:

```python
class Product:
   def __init__(self) -> None:
       self._parts: List[str] = []

   def add_part(self, part: str) -> None:
       self._parts.append(part)

   def get_parts(self) -> List[str]:
       return self._parts

class ConcreteBuilder:
    def __init__(self) -> None:
        self.product = Product()

    def build_part_a(self) -> None:
        self.product.add_part("part A")

    def build_part_b(self) -> None:
        self.product.add_part("part B")

    def get_result(self) -> Product:
        return self.product
```

Логикой конструирования объекта пользуется класс **Director**, обладая интерфейсом **Builder**:

```python
class Builder(Protocol):
    def build_part_a(self) -> None:
        ...

    def build_part_b(self) -> None:
        ...

    def get_result(self) -> Product:
        ...


class Director:
    def __init__(self, builder: Builder) -> None:
        self._builder = builder

    def construct() -> None:
        self._builder.build_part_a()
        self._builder.build_part_b()
```

При такой конфигурации следующий код работает нормально:

```python
>>> builder = ConcreteBuilder()
>>> director = Director(builder)
>>> director.construct(builder)
>>> product = builder.get_result()
>>> product.get_parts()
["part A", "part B"]
```

Преимущества паттерна:

+ Паттерн позволяет легко изменять внутреннее представление продукта благодаря разбиению процесса создания объекта на несколько шагов.
+ Разделение создания продукта и самого продукта делает имплементацию целевого класса проще.

Единственный недостаток - излишняя сложность и дополнительные классы.

### Фабричный метод (Factory Method)

**Фабричный метод** - порождающий паттерн, целью которого является делегирование создания различных объектов, которые обладают одним интерфейсом. При этом классу, использующему данный паттерн, заранее не известно, объекты каких классов ему нужно создавать.

Имплементация выглядит следующим образом: определяется интерфейс **Creator**, который описывает создание объектов по интерфейсу **Product**:

```python
class Creator(Protocol):
    def factory_method(self) -> Product:
        ...

class Product(Protocol):
    def product_method(self):
        ...
```

В данном контексте, классы, которые удовлетворяют интерфейсу *Creator*, должны имплементировать метод `factory_method()`, который возвращает объект класса, подходящего под *Product*. Тогда функция-клиент, которая использует фабричный метод "создателя", может выглядеть следующим образом:

```python
def client_function(creator: Creator) -> int:
    product = creator.factory_method()
    return product.product_method()
```

Клиентская функция **заранее не знает** о типе продукта, который будет создан и впоследствии использован, тем самым освобождаясь от необходимости знать детали реализации.

Таким же способом можно создать семейство классов-создателей и классов-продуктов:

```python
class ConcreteCreatorA:
    def factory_method(self) -> ConcreteProductA:
        return ConcreteProductA()

class ConcreteProductA:
    def product_method(self) -> int:
        return 0

class ConcreteCreatorB:
    def factory_method(self) -> ConcreteProductB:
        return ConcreteProductB()

class ConcreteProductB:
    def product_method(self) -> int:
        return 1
```

И все вышеописанные классы могут использоваться клиентской функцией, к примеру:

```python
>>> creator_a = ConcreteCreatorA()
>>> creator_b = ConcreteCreatorB()
>>> client_function(creator_a)
0
>>> client_function(creator_b)
1
```

Преимущества паттерна:

+ Подклассам предоставляются **операции-зацепки (hooks)**, которые позволяют подклассам предоставлять расширенной версии объекта.
+ Паттерн позволяет соединять параллельные иерархии в единое и взаимосвязанное целое.

Потенциальный недостаток - необъодимость создания нового класса-создателя для каждого нового класса-продукта.

### Абстрактная фабрика (Abstract Factory)

**Абстрактная фабрика** - порождающий паттерн, который используется для создания семейств взаимосвязанных или взаимозависимых объектов, не специфицируя их конкретных классов. По сути, это дополнительный уровень абстракции или обобщение паттерна "фабричный метод".

Реализуется паттерн следующим образом: сначала определяются интерфейсы для фабрик и всех ассоциированных типов продуктов.

```python
class AbstractFactory(Protocol):
    def create_product_a(self) -> AbstractProductA:
        ...

    def create_product_b(self) -> AbstractProductB:
        ...

class AbstractProductA(Protocol):
    def get_int(self) -> int:
        ...

class AbstractProductB(Protocol):
    def get_str(self) -> str:
        ...

```

Клиентский код при использовании паттерна может выглядеть так:

```python
def client_function(factory: AbstractFactory) -> None:
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    print(product_b.get_str() * product_a.get_int())
```

При такой конфигурации можно реализовать различные классы-фабрики и классы-продукты,, например:

```python
class ConcreteFactory1:
    def create_product_a(self) -> ConcreteProductA1:
        return ConcreteProductA1()

    def create_product_b(self) -> ConcreteProductB1:
        return ConcreteProductB1()

class ConcreteProductA1:
    def get_int(self) -> int:
        return 1

class ConcreteProductB1:
    def get_str(self) -> str:
        return "b1"


class ConcreteFactory2:
    def create_product_a(self) -> ConcreteProductA2:
        return ConcreteProductA2()

    def create_product_b(self) -> ConcreteProductB2:
        return ConcreteProductB2()

class ConcreteProductA2:
    def get_int(self) -> int:
        return 2

class ConcreteProductB1:
    def get_str(self) -> str:
        return "b2"
```

Вышеописанная структура позволяет следующему коду работать корректно:

```python
>>> factory_1 = ConcreteFactory1()
>>> factory_2 = ConcreteFactory2()
>>> client_function(factory_1)
b1
>>> client_function(factory_2)
b2b2
```

Преимущества паттерна:

+ Все преимущества паттерна "фабричный метод" применимы и к абстрактной фабрике;
+ Абстрактная фабрика изолирует конкретные классы и делает их контролируемыми;
+ Гарантирует сочетаемость продуктов и упрощает замену семейств продуктов.

Недостатки паттерна проявляются в ситуации, когда требуется выполнить операцию, зависящую от подкласса: через абстрактный интерфейс это сделать проблематично и порой невозможно из-за часто встречающихся проблем с безопасностью.

## Структурные паттерны

Структурные паттерны - паттерны, которые определяют **каким образом** из классов и объектов образуются более крупные структуры.

Структурные паттерны *уровня класса* используют наследование для составления композиций из интерфейсов и реализаций. Паттерны *уровня объекта* компонуют объекты для получения новой функциональности таким образом, что достигается дополнительная гибкость паттерна: композиция объектов **может быть изменена во время выполнения программы**.

### Адаптер (Adapter)

**Адаптер** - структурный паттерн, который обеспечивает совместную работу классов с несовместимыми интерфейсами, преобразуя интерфейс одного класса в другой интерфейс, на который рассчитаны клиенты. Другое название паттерна - **Wrapper (Обертка)**.

Пусть есть функция-клиент, который ожидает объект, который удовлетворяет целевому интерфейсу:

```python
class Target(Protocol):
    def expected_function(self) -> int:
        ...


def client_function(obj: Target) -> str:
    integer = obj.expected_function()
    return f"The number was {integer + 1}"
```

И есть класс, который должен быть адаптирован:

```python
class Adaptee:
    def unexpected_function(self) -> float:
        return 3.1415
```

Мы хотим, чтобы этот класс мог использоваться в контексте интерфейса Target **без модификации самого класса**. Тогда требуется создать **класс-адаптер**:

```python
class Adapter:
    def __init__(self, incompatible: Adaptee) -> None:
        self._incompatible = incompatible

    def expected_function(self) -> int:
        return int(self._incompatible.unexpected_function())
```

Теперь класс может использоваться клиентом, а следующий код будет работать как ожидается:

```python
>>> incompatible = Adaptee()
>>> adapted = Adapter(incompatible)
>>> client_function(adapted)
The number was 4
```

Преимущества паттерна:

+ Подстраивание кастомных классов под существующий код (но не подклассы);
+ Возможность замещения некоторых операций адаптируемого класса;
+ Возможность создания сменных (адаптация интерфейсов) и двусторонних адаптеров (прозрачность и предоставление разных представлений одного объекта).

Трудность применения паттерна возникает тогда, когда требуется замещение операций класса Adaptee. В этом случае требуется породить подкласс класса-адаптера, заставив подкласс ссылаться на новый адаптируемый подкласс.

### Декоратор (Decorator)

**Декоратор** - структурный паттерн, который динамически добавляет объекту новые обязанности без изменения самого объекта или класса, к которому принадлежит объект. Паттерн схож с адаптером (иногда даже паттерн называется оберткой, как и предыдущий паттерн), но в отличие от него **не должен изменять интерфейс объекта**, паттерн должен только расширять уже существующую функциональность.

Пусть есть клиент, который ожидает объект с конкретным интерфейсом, и некоторая имплементация этого интерфейса:

```python
class Component(Protocol):
    def operation(self) -> int:
        ...

class ConcreteComponent:
    def operation(self) -> int:
        return 5

def client_function(obj: Component) -> str:
    integer = obj.operation()
    return f"The number was {integer + 1}"
```

Декоратор должен имплементировать тот же интерфейс, но при этом декоратор может ссылаться на некоторый объект с этим интерфейсом:

```python
class Decorator:
    def __init__(self, component: Component) -> None:
        self._component = component

    def operation(self) -> int:
        print("Do some additional work")
        return self._component.operation()
```

Декоратор сам по себе не перекрывает декорируемый объект, поэтому результат работы с таким объектом не будет меняться, но при этом декоратор будет выполнять некоторую дополнительную работу:

```python
>>> component = ConcreteComponent()
>>> decorated = Decorator(component)
>>> print(client_function(component))
The number was 6
>>> print(client_function(decorated))
Do some additional work
The number was 6
```

Преимущества паттерна:

+ Динамическое и прозрачное для клиентов добавления обязанностей объектам;
+ Реализация обязанностей, которые могут быть сняты;
+ Декоратор меняет *оболочку* (или *view - представление*) объекта, а не сам объект.

В Python присутствует встроенный синтаксис применения декораторов для функций, классов и методов:

```python
@decorator
class ConcreteComponent:
    ...
```

В общем случае, синтаксис декораторов выглядит следующим образом:

```python
def decorator_name(func):
    def wrapper(*args, **kwargs):
        # Add functionality before the original function call
        result = func(*args, **kwargs)
        # Add functionality after the original function call
        return result
    return wrapper

@decorator_name
def function_to_decorate():
    # Original function code
    pass
```

Примеры использования:

+ Если вы хотите, чтобы декоратор превращал некоторый класс в класс-одиночку, то можно поступить следующим образом:

```python
def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

@singleton
class MyClass:
    ...
```

+ Если вы хотите реализовать некоторую функцию, которая **должна выполняться на выходе из программы**, то можно поступить следующим образом:

```python
def onexit(f):
    import atexit
    atexit.register(f)
    return f

@onexit
def func():
    ...
```

Подробнее о декораторах расписано в [PEP 318](https://peps.python.org/pep-0318/)

### Фасад (Facade)

**Фасад** - структурный паттерн, который предоставляет унифицированный высокоуровневый интерфейс вместо набора интерфейсов некоторой подсистемы таким образом, чтобы доступ к элементам подсистемы мог быть осуществлен **только** через фасад. Это позволяет упростить взаимодействия между частями кода, скрывая полную функциональность классов и модулей и оставляя в публичном доступе только необходимое.

Допустим, что у нас есть несколько классов, которые вместе формируют подсистему:

```python
class ClassA:
    def method1(self):
        ...

    def method2(self):
        ...


class ClassB:
    def method3(self):
        ...

    def method4(self):
        ...
```

Фасад может использовать комбинацию скрытой функциональности, клиенту не требуется взаимодействовать непосредственно с классами, поскольку взаимодействие возможно только через фасад:

```python
class Facade:
    def __init__(self):
        self._subsystemA = ClassA()
        self._subsystemB = ClassB()

    def operation(self):
        self._subsystemA.method1()
        self._subsystemA.method2()
        self._subsystemB.method3()
        self._subsystemB.method4()
```

Преимущества паттерна:

+ Изоляция клиента от классов подсистемы;
+ Ослабление связанности между подсистемой и ее клиентами;
+ Фасад не препятствует приложениям использовать классы подсистемы отдельно от фасада.

Однако, если подсистема не продумана заранее должным образом, клиентам может потребоваться разные фасады, что приводит к повышенной сложности в реализации паттерна.

### Заместитель/прокси (Proxy)

**Прокси** - структурный паттерн, который выступает в виде посредника между клиентом и реальным объектом, *"притворяясь"* этим самым объектом, имплементируя один и тот же интерфейс.

Суть прокси - **откладывание** операций инициализации или доступа к какому-либо ресурсу (память, процессоры, данные, и т.п.) до момента фактической необходимости ресурса или объекта.

Например, пусть есть объект, который считывает данные с файла (предположим, что достаточно большого):

```python
class RealSubject:
    def __init__(self, data: str) -> None:
        self._data = data

    def operate_on_data(self) -> None:
        print(self._data)

    @classmethod
    def from_file(cls, filename: str) -> RealSubject:
        with open(filename, "r") as f:
            data = f.read()
        return cls(data)
```

Данные из файла нужны только при вызове метода `operate_on_data()`. Чтобы не создавать каждый раз объект и не считывать файлы, можно создать прокси-объект, откладывающий момент создания до момента, когда данные фактически нужны:

```python
class ProxyObject:
    def __init__(self, filename: str) -> None:
        self._filename = filename
        self._real_obj: Optional[RealSubject] = None

    def operate_on_data(self) -> None:
        real_obj = self._real_obj
        if real_obj is None:
            real_obj = RealSubject.from_file(self._filename)
            self._real_obj = real_obj  
        real_obj.operate_on_data()
```

Прокси может быть использован как и замещенный объект клиентами, так как прокси **обязан** имплементировать тот же интерфейс:

```python
from typing import Protocol

class ExpectedObject(Protocol):
    def operate_on_data() -> None:
        ...

def client_function(obj: ExpectedObject) -> None:
    obj.operate_on_data()
```

Тогда следующий код будет работать корректно:

```python
>>> proxy = ProxyObject("big_file.txt")
>>> client_function(proxy)
... # file contents printed
```

## Паттерны поведения

**Паттерны поведения** связаны с алгоритмами и распределением обязанностей между объектами, причем речь идет не только о самих объектах и классах, но и о типичных схемах взаимодействия между ними.

### Стратегия (Strategy)

**Стратегия** - паттерн поведения, который определяет семейство алгоритмов, инкапсулирует каждый из их и делает их взаимозаменяемыми. Паттерн позволяет изменять алгоритмы независимо от клиентов, которые ими пользуются.

Для работы паттерна требуется следующая структура классов: есть класс, который должен менять поведение, исходя из выбранной стратегии, и есть интерфейс стратегий:

```python
class Strategy(Protocol):
    def run(self) -> None:
        ...

class Context:
    def __init__(self, strategy: Strategy) -> None:
        self.strategy = strategy

    def run(self) -> None:
        self.strategy.run()
```

Пусть есть два класса под стратегии:

```python
class StrategyA:
    def run(self) -> None:
        print("Context is using strategy A")

class StrategyB:
    def run(self) -> None:
        print("Context is using strategy B")
```

Тогда контекст можно использовать следующим образом:

```python
>>> context_1 = Context(StrategyA())
>>> context_2 = Context(StrategyB())
>>> context_1.run()
Context is using strategy A
>>> context_2.run()
Context is using strategy B
```

Преимущества паттерна:

+ Стратегии позволяют порождать семейства родственных алгоритмов, реиспользуемых в разных контекстах;
+ Паттерн позволяет избавиться от условных конструкций;
+ Стратегии могут предоставлять различные реализации одного и того же поведения.

Недостатки паттерна:

+ Клиенты должны знать о различных стратегиях;
+ При общем интерфейсе контекст может генерировать избыточную информацию;
+ Увеличение числа объектов в приложении (стратегии - тоже объекты).

### Цепочка обязанностей (Chain of responsibilities)

**Цепочка обязанностей** - паттерн поведения, который отвязывает отправителя запроса к его получателю, предоставляя возможность обработать запрос нескольким объектам.

Пусть есть некоторая функция-клиент и интерфейс **обработчика**:

```python
class Handler(Protocol):
    def handle_request(self, request: str) -> Optional[str]:
        ...


def client_function(
    request: str, 
    handler: Handler,
) -> None:
    print(handler.handle_request(request))
```

Мы можем реализовать конкретного обработчика, который показывает как цепочка обязанностей работает:

```python
class ConcreteHandler:
    def __init__(
        self, 
        request_strategy: Strategy,
        successor: Optional[Handler] = None,
    ) -> None:
        self._strategy = request_strategy
        self._successor = successor

    def handle_request(self, request: str) -> Optional[str]:
        if self._strategy.matches(request):
            return self._strategy.operation()
        elif self._successor is not None:
            return self._successor.handle_request(request)
        else:
            return None


class Strategy:
    def __init__(
        matching_request: str,
        to_return: str,
    ) -> None:
        self._matching_request = matching_request
        self._to_return = to_return

    def matches(self, request: str) -> bool:
        return request == self._matching_request

    def operation(self) -> str:
        return self._to_return
```

Ключевая особенность здесь в том, что обработчик может хранить ссылку на другого обработчика, тем самым они могут вызывать друг друга по цепочке. Объект Strategy (паттерн Стратегия) определяет как обработчик ведет себя с запросом.

Приведенный выше пример можно использовать следующим образом:

```python
>>> chainlink_1 = ConcreteHandler(Strategy("request_a", "foo"))
>>> chainlink_2 = ConcreteHandler(Strategy("request_b", "bar"), chainlink_1)
>>> chainlink_3 = ConcreteHandler(Strategy("request_c", "baz"), chainlink_2)
>>> client_function("request_a", chainlink_3)
foo
>>> client_function("request_d", chainlink_3)
```

Преимущества паттерна:

+ Ослабление связанности между обработчиками и вызывающим объектом;
+ Гибкость при распределении обязанностей;

Потенциальные проблемы:

+ Получение не гарантированно, если запрос не может быть обработан ни одним элементом цепочки или цепочка не сконфигурирована корректно;
+ Производительность обработки через цепочку может проседать (цепочка обязанностей имеет схожую структуру со односвязным списком);
+ Если один из элементов цепочки обработал запрос некорректно, то остальная часть цепочки, скорее всего, тоже отработает неверно.

### Шаблонный метод (Template Method)

**Шаблонный метод** - паттерн поведения, который определяет основу алгоритма и позволяет подклассам переопределить некоторые шаги алгоритма, не изменяя его структуру в целом.

Обычно алгоритм (шаблонный метод) в данном паттерне представляется в виде абстрактного класса:

```python
class Abstract(ABC):
    def template_method(self, x: int) -> int:
        x = x**2 + x + 1
        y = self.operation_1(x)
        z = self.operation_2(y)
        return z
    
    @abstractmethod
    def operation_1(self, value: int) -> int:
        raise NotImplementedError

    @abstractmethod
    def operation_2(self, value: int) -> int:
        raise NotImplementedError
```

Здесь шаблонный метод зависит от двух абстрактных операций, которые должны имплементироваться классами-наследниками, например:

```python
class Concrete(Abstract):
    def operation_1(self, value: int) -> int:
        return 5 * value

    def operation_2(self, value: int) -> int:
        return value + 2
```

При такой организации "алгоритм" можно использовать следующим образом:

```python
>>> concrete = Concrete()
>>> concrete.template_method(2)
37
```

Шаблонный метод - один из фундаментальных приемов повторного использования кода, предоставляя возможность вынести общее поведение в библиотечные классы. При этом шаблонный метод приводит к инвертированнной структуре кода, которую иногда называют принципом Голливуда и описывают фразой: "Не звоните нам, мы сами вами позвоним", т.е. родительский класс вызывает операции подкласса, а не наоборот.

### Итератор (Iterator)

**Итератор** - паттерн поведения объектов, который предоставляет способ последовательного обращения ко всем элементам составного объекта без раскрытия его внутреннего представления.

Данный паттерн лежит в основе доступа к элементам коллекций без необходимости знать как конкретная коллекция устроена. Благодаря итераторам можно проходить по коллекциям, причем элементы могут не всегда существовать в памяти (тогда итератор становится **генератором**), а могут вычисляться в процессе итерирования.

Python уже имеет встроенные имплементации этого паттерна. К примеру, если для списка требуется реализовать итератор, который может итерировать в обратном направлении (предположим, что мы не знаем про срезы и магию наподобие ```list[::-1]```), то это можно сделать следующим образом:

```python
from typing import Iterator

class BackwardIterator(Iterator[T]):
    def __init__(self, lst: List[T]) -> None:
        self._lst = lst
        self._index = len(lst) - 1

    def __iter__(self) -> BackwardIterator:
        return self

    def __next__(self) -> T:
        if self._index == -1:
            raise StopIteration
        item = self._lst[self._index]
        self._index -= 1
        return item
```

Такой итератор можно использовать в цикле `for`:

```python
>>> lst = [1, 2, 3, 4]
>>> iterator = BackwardIterator(lst)
>>> for i in iterator:
...     print(i)
...
4
3
2
1
```

Методы `__iter__()`, `__next__()` являются встроенными в Python, язык умеет вызывать эти методы в циклах. Итерации будут проходить до тех пор, пока не будет выброшено исключение `StopIteration`.

### Наблюдатель (Observer)

**Наблюдатель** - паттерн поведения, который определяет зависимость типа "один ко многим" между объектами таким образом, что при изменении состояния одного объекта все зависящие от него оповещаются об этом и автоматически обновляются. Иногда еще паттерн называют **Dependents (Подчиненные)** или **Publish-Subscribe (Издатель - Подписчик)**.

В данной системе есть два элемента: наблюдатели и субъекты. Наблюдатели "подписываются на уведомления" субъектов, когда состояние субъектов изменяется, все наблюдатели уведомляются об этом.

Реализуется это следующим образом:

```python
class Subject:
    def __init__(self) -> None:
        self._counter = 0
        self._observers: set[Observer] = set()

    def increment(self) -> None:
        self._counter += 1
        self.notify()

    def get_counter(self) -> int:
        return self._counter

    def subscribe(observer: Observer) -> None:
        self._observers.add(observer)

    def unsubscribe(observer: Observer) -> None:
        self._observers.remove(observer)

    def notify() -> None:
        for observer in self._observers:
            observer.update()


class Observer(Protocol)
    def update(self) -> None:
        ...
```

Можно имплементировать классы по интерфейсу наблюдателя:

```python
class ConcreteObserver:
    possible_states = ("happy", "sad", "angry")

    def __init__(self, subject: Subject) -> None:
        self._subject = subject
        self._state = self.possible_states[0]

    def update(self) -> None:
        new_index = self._subject.get_counter() % 3
        self._state = self.possible_states[new_index]
        print(f"The observer's state changes to: {self._state}")
```

Теперь, наблюдателей можно настроить для отслеживания состояния:

```python
>>> subject = Subject()
>>> observer = ConcreteObserver(subject)
>>> subject.subscribe(object)
>>> subject.increment()
The observer's state changes to: sad
>>> subject.increment()
The observer's state changes to: angry
```

Преимущества паттерна:

+ Абстрактая связность субъекта и наблюдателя;
+ Поддержка широковещательных коммуникаций;
+ Легко расширяемые системы.

Недостаток паттерна - неожиданные обновления могут привести к непредвиденным последствиям, поскольку наблюдатели не обладают информацией друг об друге и о том, во что обходится изменение субъекта.

## Посетитель (Visitor)

**Посетитель** - паттерн поведения, который описывает операцию, выполняемую с каждым объектом из некоторой структуры, не изменяя классы этих объектов. Де-факто, посетитель - это обобщение паттерна Итератор.

Пусть есть следующие элементы структуры классов:

```python
class Element(Protocol):
    def accept(self, visitor: Visitor) -> None:
        ...


class ConcreteElementA:
    def accept(self, visitor: Visitor) -> None:
        visitor.visit_concrete_element_a(self)

    def operation_a(self) -> int:
        return 1


class ConcreteElementB:
    def accept(self, visitor: Visitor) -> None:
        visitor.visit_concrete_element_b(self)

    def operation_b(self) -> int:
        return 5
```

Определим интерфейс посетителя и его имплементацию:

```python
class Visitor(Protocol):
    def visit_concrete_element_a(self, element: ConcreteElementA) -> None:
        ...

    def visit_concrete_element_b(self, element: ConcreteElementB) -> None:
        ...

class ConcreteVisitor:
    def __init__(self) -> None:
        self._counter = 0

    def get_counter(self) -> int:
        return self._counter

    def visit_concrete_element_a(self, element: ConcreteElementA) -> None:
        self._counter += element.operation_a()

    def visit_concrete_element_b(self, element: ConcreteElementB) -> None:
        self._counter += element.operation_b()
```

Теперь посетитель может выполнять определенные действия над коллекцией элементов:

```python
>>> collection = [ConcreteElementA(), ConcreteElementA(), ConcreteElementB()]
>>> visitor = ConcreteVisitor()
>>> for element in collection:
...     element.accept(visitor)

>>> visitor.get_counter()
7
```

Преимущества паттерна:

+ Упрощение добавления новых операций;
+ Объединение родственных операций;
+ Посещение различных иерархий классов.

Недостаток паттерна заключается в том, что добавление новых типов элементов требует изменения классов-посетителей.

## Задания

### Паттерн Одиночка (Singleton)

Задача:
Реализуйте класс логгера (например, Logger), который гарантирует создание только одного экземпляра во всём приложении.

Требования:

+ При попытке создать новый объект класс должен возвращать уже существующий экземпляр.
+ Реализуйте запись сообщений в файл или консоль, демонстрируя, что изменения в одном экземпляре отражаются во всех ссылках.

### Паттерн Прототип (Prototype)

Задача:
Предложите класс и реализуйте для него возможность копирования объектов посредством паттерна Prototype.

Требования:

+ Создайте класс, который поддерживает метод clone(), возвращающий копию объекта.
+ Учтите, какие атрибуты нужно копировать глубоко, а какие – поверхностно.

### Паттерн Декоратор (Decorator)

Задача:
Создайте систему, позволяющую динамически добавлять объектам новое поведение без изменения их кода. Пример – добавление логирования или проверки прав доступа при вызове методов.

Требования:

+ Реализуйте базовый класс, который будет декорироваться.
+ Создайте декораторы, оборачивающие объекты базового класса и расширяющие их функциональность.

### Паттерн Наблюдатель (Observer)

Задача:
Реализуйте систему оповещений, где объект (Subject) уведомляет множество подписчиков (Observers) об изменении своего состояния.

Требования:

+ Создайте класс Subject, который поддерживает список наблюдателей и предоставляет методы для добавления/удаления наблюдателей.
+ Каждый наблюдатель должен реализовывать метод обновления (например, update()).
+ Смоделируйте изменение состояния и уведомление всех наблюдателей (например, изменение температуры, цены и т.д.)

### Паттерн Заместитель (Proxy)

Задача:
Напишите функцию для вычисления чисел Фибоначчи, которая работает рекурсивно. Прокси должен кэшировать уже вычисленные значения, чтобы избежать повторных вычислений для одних и тех же аргументов.

Требования:

+ Определите интерфейс с методом, например, fib(n).
+ Реализуйте класс RealFibonacci, который рекурсивно вычисляет n-е число Фибоначчи.
+ Создайте класс FibonacciCacheProxy, который хранит результаты вычислений и при повторном вызове с одинаковым значением n возвращает закэшированный результат.
