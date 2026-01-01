# 🐍 Python Complete Mastery Guide

## Table of Contents
1. [Zen of Python & Core Concepts](#zen-of-python--core-concepts)
2. [Functional Programming](#functional-programming)
3. [Object-Oriented Programming](#object-oriented-programming)
4. [Advanced Concepts](#advanced-concepts)
5. [Data Validation](#data-validation)
6. [Writing Robust Code](#writing-robust-code)
7. [Type Checking and Linting](#type-checking-and-linting)
8. [Comprehensions and Generators](#comprehensions-and-generators)
9. [Concurrency and Parallelism](#concurrency-and-parallelism)
10. [Testing and Debugging](#testing-and-debugging)
11. [Development Environment](#development-environment)
12. [Project Organization](#project-organization)
13. [IDE Setup](#ide-setup)

---

## Zen of Python & Core Concepts

### The Zen of Python
```python
import this
```

**Key Principles:**
- Beautiful is better than ugly
- Explicit is better than implicit
- Simple is better than complex
- Readability counts
- There should be one obvious way to do it

### Python Syntax Fundamentals

#### Snake Case Convention
```python
# Variables and functions
user_name = "john_doe"
def calculate_total_price():
    pass

# Constants (ALL_CAPS)
MAX_CONNECTIONS = 100
API_BASE_URL = "https://api.example.com"

# Classes (PascalCase)
class UserManager:
    pass
```

#### PEP Guidelines
- **PEP 8**: Style Guide for Python Code
- **PEP 20**: The Zen of Python
- **PEP 257**: Docstring Conventions

```python
def calculate_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle.
    
    Args:
        length: The length of the rectangle
        width: The width of the rectangle
    
    Returns:
        The area of the rectangle
    """
    return length * width
```

### Duck Typing & Dynamic Typing

#### Duck Typing
```python
class Duck:
    def quack(self):
        return "Quack!"
    
    def fly(self):
        return "Flying like a duck"

class Airplane:
    def quack(self):
        return "Airplane can't quack"
    
    def fly(self):
        return "Flying like an airplane"

def make_it_fly(thing):
    # If it walks like a duck and quacks like a duck, it's a duck
    return thing.fly()

duck = Duck()
plane = Airplane()
print(make_it_fly(duck))    # Works
print(make_it_fly(plane))   # Also works
```

#### Dynamic Typing
```python
# Variable can hold different types
x = 42          # int
x = "hello"     # str
x = [1, 2, 3]   # list
x = {"key": "value"}  # dict
```

### Modules vs Packages vs Libraries

#### Module
```python
# math_utils.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# Using the module
import math_utils
result = math_utils.add(5, 3)
```

#### Package
```
my_package/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        submodule.py
```

```python
# __init__.py
from .module1 import function1
from .module2 import function2

# Usage
from my_package import function1
```

#### Library
A collection of packages and modules (e.g., NumPy, Pandas, Requests)

---

## Functional Programming

### Args and Kwargs

#### *args (Variable Positional Arguments)
```python
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))  # 15
```

#### **kwargs (Variable Keyword Arguments)
```python
def create_profile(**kwargs):
    profile = {}
    for key, value in kwargs.items():
        profile[key] = value
    return profile

user = create_profile(name="John", age=30, city="New York")
print(user)  # {'name': 'John', 'age': 30, 'city': 'New York'}
```

#### Combined Usage
```python
def flexible_function(required_arg, *args, **kwargs):
    print(f"Required: {required_arg}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

flexible_function("hello", 1, 2, 3, name="John", age=25)
```

### Decorators

#### Basic Decorator
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@my_decorator
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
```

#### Decorator with Parameters
```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()  # Prints "Hello!" three times
```

#### Built-in Decorators
```python
class MyClass:
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, val):
        self._value = val
    
    @staticmethod
    def static_method():
        return "Static method called"
    
    @classmethod
    def class_method(cls):
        return f"Class method called on {cls.__name__}"
```

### Lambda Expressions

#### Basic Lambda
```python
# Regular function
def square(x):
    return x ** 2

# Lambda equivalent
square_lambda = lambda x: x ** 2

print(square_lambda(5))  # 25
```

#### Lambda with Built-in Functions
```python
numbers = [1, 2, 3, 4, 5]

# Map
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# Filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# Sorted
students = [('Alice', 85), ('Bob', 90), ('Charlie', 78)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)  # [('Charlie', 78), ('Alice', 85), ('Bob', 90)]
```

### Higher-Order Functions

#### Functions as First-Class Objects
```python
def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def apply_operation(func, x, y):
    return func(x, y)

result1 = apply_operation(add, 5, 3)      # 8
result2 = apply_operation(multiply, 5, 3)  # 15
```

#### Closures
```python
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

add_10 = outer_function(10)
print(add_10(5))  # 15
```

---

## Object-Oriented Programming

### Classes and Inheritance

#### Basic Class
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old"
    
    def __str__(self):
        return f"Person(name='{self.name}', age={self.age})"

person = Person("Alice", 30)
print(person.introduce())
print(person)
```

#### Inheritance
```python
class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary
    
    def introduce(self):
        return f"{super().introduce()}. I work here as employee #{self.employee_id}"
    
    def get_annual_salary(self):
        return self.salary * 12

employee = Employee("Bob", 25, "E001", 5000)
print(employee.introduce())
```

#### Multiple Inheritance
```python
class Flyable:
    def fly(self):
        return "Flying high!"

class Swimmable:
    def swim(self):
        return "Swimming fast!"

class Duck(Flyable, Swimmable):
    def quack(self):
        return "Quack!"

duck = Duck()
print(duck.fly())
print(duck.swim())
print(duck.quack())
```

### Properties and Data Hiding

#### Properties
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
    
    @property
    def area(self):
        return 3.14159 * self._radius ** 2
    
    @property
    def diameter(self):
        return 2 * self._radius

circle = Circle(5)
print(circle.area)      # 78.53975
print(circle.diameter)  # 10
circle.radius = 3
print(circle.area)      # 28.27431
```

#### Data Hiding (Encapsulation)
```python
class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance  # Private attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False
    
    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # 1500
# print(account.__balance)    # AttributeError
```

### Class and Static Methods

#### Class Methods
```python
class Person:
    species = "Homo sapiens"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def get_species(cls):
        return cls.species
    
    @classmethod
    def from_string(cls, person_str):
        name, age = person_str.split('-')
        return cls(name, int(age))

# Usage
person1 = Person.from_string("Alice-30")
print(Person.get_species())  # Homo sapiens
```

#### Static Methods
```python
class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

# Usage (no instance needed)
print(MathUtils.add(5, 3))      # 8
print(MathUtils.is_prime(17))   # True
```

---

## Advanced Concepts

### Metaclasses

#### Basic Metaclass
```python
class MyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        # Modify class creation
        attrs['class_id'] = f"{name.lower()}_class"
        return super().__new__(cls, name, bases, attrs)
    
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        print(f"Created class: {name}")

class MyClass(metaclass=MyMetaclass):
    def __init__(self, value):
        self.value = value

obj = MyClass(42)
print(obj.class_id)  # myclass_class
```

#### Singleton Metaclass
```python
class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self):
        self.connection = "Connected to database"

db1 = Database()
db2 = Database()
print(db1 is db2)  # True
```

### Mixin Classes

#### Basic Mixin
```python
class JSONMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)
    
    def from_json(self, json_str):
        import json
        data = json.loads(json_str)
        for key, value in data.items():
            setattr(self, key, value)

class TimestampMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from datetime import datetime
        self.created_at = datetime.now()

class User(JSONMixin, TimestampMixin):
    def __init__(self, name, email):
        super().__init__()
        self.name = name
        self.email = email

user = User("Alice", "alice@example.com")
print(user.to_json())
print(user.created_at)
```

---

## Data Validation

### Dataclasses

#### Basic Dataclass
```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class Person:
    name: str
    age: int
    email: str = ""
    hobbies: List[str] = field(default_factory=list)
    
    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")

person = Person("Alice", 30, "alice@example.com", ["reading", "coding"])
print(person)
```

#### Advanced Dataclass Features
```python
from dataclasses import dataclass, field, asdict, astuple

@dataclass(frozen=True, order=True)
class Product:
    name: str
    price: float
    category: str = "general"
    tags: List[str] = field(default_factory=list, compare=False)
    
    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative")

products = [
    Product("Laptop", 999.99, "electronics"),
    Product("Book", 19.99, "education"),
    Product("Phone", 699.99, "electronics")
]

sorted_products = sorted(products)
print(asdict(products[0]))
print(astuple(products[0]))
```

### Pydantic

#### Basic Pydantic Model
```python
from pydantic import BaseModel, validator, Field
from typing import Optional
from datetime import datetime

class User(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    age: int = Field(..., ge=0, le=150)
    email: str
    created_at: datetime = Field(default_factory=datetime.now)
    is_active: bool = True
    
    @validator('email')
    def validate_email(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email format')
        return v
    
    @validator('name')
    def validate_name(cls, v):
        return v.strip().title()

# Usage
user_data = {
    "name": "  alice  ",
    "age": 30,
    "email": "alice@example.com"
}

user = User(**user_data)
print(user.json())
print(user.dict())
```

### Attrs

#### Basic Attrs Usage
```python
import attr
from attr import validators

@attr.s
class Person:
    name = attr.ib(validator=validators.instance_of(str))
    age = attr.ib(validator=validators.instance_of(int))
    email = attr.ib(validator=validators.instance_of(str))
    
    @age.validator
    def check_age(self, attribute, value):
        if value < 0:
            raise ValueError("Age must be positive")

person = Person("Alice", 30, "alice@example.com")
print(person)
```

---

## Writing Robust Code

### Design Patterns

#### Singleton Pattern
```python
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Usage
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True
```

#### Factory Pattern
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type.lower() == "dog":
            return Dog()
        elif animal_type.lower() == "cat":
            return Cat()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

# Usage
dog = AnimalFactory.create_animal("dog")
print(dog.make_sound())  # Woof!
```

#### Observer Pattern
```python
class Subject:
    def __init__(self):
        self._observers = []
        self._state = None
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)
    
    def notify(self):
        for observer in self._observers:
            observer.update(self._state)
    
    def set_state(self, state):
        self._state = state
        self.notify()

class Observer:
    def __init__(self, name):
        self.name = name
    
    def update(self, state):
        print(f"{self.name} received update: {state}")

# Usage
subject = Subject()
observer1 = Observer("Observer 1")
observer2 = Observer("Observer 2")

subject.attach(observer1)
subject.attach(observer2)
subject.set_state("New State")
```

### Error Handling

#### Exception Handling
```python
def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    except TypeError:
        print("Error: Invalid input types")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
    finally:
        print("Division operation completed")

# Custom Exceptions
class CustomError(Exception):
    def __init__(self, message, error_code=None):
        super().__init__(message)
        self.error_code = error_code

def validate_age(age):
    if not isinstance(age, int):
        raise CustomError("Age must be an integer", "TYPE_ERROR")
    if age < 0:
        raise CustomError("Age cannot be negative", "VALUE_ERROR")
    if age > 150:
        raise CustomError("Age seems unrealistic", "RANGE_ERROR")
    return True
```

### Logging

#### Basic Logging
```python
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def process_data(data):
    logger.info("Starting data processing")
    try:
        # Process data
        result = len(data)
        logger.info(f"Processed {result} items")
        return result
    except Exception as e:
        logger.error(f"Error processing data: {e}")
        raise

# Usage
process_data([1, 2, 3, 4, 5])
```

#### Advanced Logging
```python
import logging
from logging.handlers import RotatingFileHandler

class CustomFormatter(logging.Formatter):
    def format(self, record):
        if record.levelno >= logging.ERROR:
            record.msg = f"🚨 {record.msg}"
        elif record.levelno >= logging.WARNING:
            record.msg = f"⚠️ {record.msg}"
        return super().format(record)

# Setup logger with custom formatter
logger = logging.getLogger('my_app')
logger.setLevel(logging.DEBUG)

handler = RotatingFileHandler('app.log', maxBytes=1024*1024, backupCount=5)
handler.setFormatter(CustomFormatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)
```

---

## Type Checking and Linting

### Type Hints

#### Basic Type Hints
```python
from typing import List, Dict, Optional, Union, Tuple, Callable

def greet(name: str) -> str:
    return f"Hello, {name}!"

def process_numbers(numbers: List[int]) -> Dict[str, int]:
    return {
        "sum": sum(numbers),
        "count": len(numbers),
        "max": max(numbers) if numbers else 0
    }

def find_user(user_id: int) -> Optional[Dict[str, str]]:
    # Might return None if user not found
    users = {1: {"name": "Alice", "email": "alice@example.com"}}
    return users.get(user_id)

def process_data(data: Union[str, List[str]]) -> List[str]:
    if isinstance(data, str):
        return [data]
    return data
```

#### Advanced Type Hints
```python
from typing import TypeVar, Generic, Protocol, Literal
from abc import abstractmethod

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []
    
    def push(self, item: T) -> None:
        self._items.append(item)
    
    def pop(self) -> T:
        return self._items.pop()

# Protocol for duck typing
class Drawable(Protocol):
    @abstractmethod
    def draw(self) -> str:
        ...

def render(obj: Drawable) -> str:
    return obj.draw()

# Literal types
def set_mode(mode: Literal["read", "write", "append"]) -> None:
    print(f"Mode set to: {mode}")
```

### MyPy Configuration

#### mypy.ini
```ini
[mypy]
python_version = 3.9
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = True
disallow_incomplete_defs = True
check_untyped_defs = True
disallow_untyped_decorators = True
no_implicit_optional = True
warn_redundant_casts = True
warn_unused_ignores = True
warn_no_return = True
warn_unreachable = True
strict_equality = True
```

### Linting with Flake8 and Black

#### .flake8
```ini
[flake8]
max-line-length = 88
extend-ignore = E203, W503
exclude = .git,__pycache__,docs/source/conf.py,old,build,dist
```

#### pyproject.toml (Black configuration)
```toml
[tool.black]
line-length = 88
target-version = ['py39']
include = '\.pyi?$'
extend-exclude = '''
/(
  # directories
  \.eggs
  | \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | build
  | dist
)/
'''
```

---

## Comprehensions and Generators

### List Comprehensions

#### Basic List Comprehensions
```python
# Traditional approach
squares = []
for x in range(10):
    squares.append(x**2)

# List comprehension
squares = [x**2 for x in range(10)]

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]

# Nested comprehensions
matrix = [[i*j for j in range(3)] for i in range(3)]
print(matrix)  # [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
```

#### Advanced List Comprehensions
```python
# Multiple conditions
numbers = [x for x in range(100) if x % 2 == 0 if x % 3 == 0]

# Multiple iterables
pairs = [(x, y) for x in range(3) for y in range(3) if x != y]

# String processing
words = ["hello", "world", "python"]
capitalized = [word.upper() for word in words if len(word) > 4]
```

### Dictionary and Set Comprehensions

#### Dictionary Comprehensions
```python
# Basic dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# From two lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = {k: v for k, v in zip(keys, values)}

# Conditional dictionary comprehension
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
```

#### Set Comprehensions
```python
# Basic set comprehension
unique_lengths = {len(word) for word in ["hello", "world", "hi", "python"]}
print(unique_lengths)  # {2, 5, 6}

# Conditional set comprehension
vowels_in_words = {char for word in ["hello", "world"] for char in word if char in "aeiou"}
```

### Generators

#### Generator Functions
```python
def fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Usage
fib_gen = fibonacci_generator(10)
for num in fib_gen:
    print(num, end=" ")  # 0 1 1 2 3 5 8 13 21 34
```

#### Generator Expressions
```python
# Generator expression
squares_gen = (x**2 for x in range(10))
print(type(squares_gen))  # <class 'generator'>

# Memory efficient processing
def process_large_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip().upper()

# Usage
# for processed_line in process_large_file('large_file.txt'):
#     print(processed_line)
```

#### Advanced Generator Patterns
```python
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

def take(n, iterable):
    """Take first n items from iterable"""
    for i, item in enumerate(iterable):
        if i >= n:
            break
        yield item

# Usage
first_10 = list(take(10, infinite_sequence()))
print(first_10)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## Concurrency and Parallelism

### Threading

#### Basic Threading
```python
import threading
import time

def worker(name, delay):
    for i in range(5):
        print(f"Worker {name}: {i}")
        time.sleep(delay)

# Create threads
thread1 = threading.Thread(target=worker, args=("A", 1))
thread2 = threading.Thread(target=worker, args=("B", 1.5))

# Start threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()
```

#### Thread Synchronization
```python
import threading
import time

class Counter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()
    
    def increment(self):
        with self.lock:
            current = self.value
            time.sleep(0.001)  # Simulate some work
            self.value = current + 1

counter = Counter()

def worker():
    for _ in range(100):
        counter.increment()

threads = []
for i in range(10):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Final counter value: {counter.value}")  # Should be 1000
```

### Multiprocessing

#### Basic Multiprocessing
```python
import multiprocessing
import time

def cpu_intensive_task(n):
    """Simulate CPU-intensive work"""
    result = 0
    for i in range(n):
        result += i ** 2
    return result

if __name__ == "__main__":
    # Sequential execution
    start_time = time.time()
    results = [cpu_intensive_task(1000000) for _ in range(4)]
    sequential_time = time.time() - start_time
    
    # Parallel execution
    start_time = time.time()
    with multiprocessing.Pool() as pool:
        results = pool.map(cpu_intensive_task, [1000000] * 4)
    parallel_time = time.time() - start_time
    
    print(f"Sequential time: {sequential_time:.2f}s")
    print(f"Parallel time: {parallel_time:.2f}s")
    print(f"Speedup: {sequential_time/parallel_time:.2f}x")
```

### Asyncio

#### Basic Async/Await
```python
import asyncio
import aiohttp
import time

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def fetch_multiple_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

# Usage
async def main():
    urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/1"
    ]
    
    start_time = time.time()
    results = await fetch_multiple_urls(urls)
    end_time = time.time()
    
    print(f"Fetched {len(results)} URLs in {end_time - start_time:.2f} seconds")

# asyncio.run(main())
```

#### Async Context Managers and Iterators
```python
import asyncio

class AsyncContextManager:
    async def __aenter__(self):
        print("Entering async context")
        await asyncio.sleep(1)
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Exiting async context")
        await asyncio.sleep(1)

class AsyncIterator:
    def __init__(self, max_count):
        self.max_count = max_count
        self.count = 0
    
    def __aiter__(self):
        return self
    
    async def __anext__(self):
        if self.count >= self.max_count:
            raise StopAsyncIteration
        await asyncio.sleep(0.1)
        self.count += 1
        return self.count

async def demo():
    async with AsyncContextManager():
        async for item in AsyncIterator(5):
            print(f"Item: {item}")

# asyncio.run(demo())
```

---

## Testing and Debugging

### Unit Testing with unittest

#### Basic Unit Tests
```python
import unittest

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class TestMathFunctions(unittest.TestCase):
    
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)
    
    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)
    
    def test_divide_normal(self):
        self.assertEqual(divide(10, 2), 5)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)
    
    def setUp(self):
        """Called before each test method"""
        self.test_data = [1, 2, 3, 4, 5]
    
    def tearDown(self):
        """Called after each test method"""
        pass

if __name__ == "__main__":
    unittest.main()
```

### Testing with pytest

#### Basic pytest Tests
```python
# test_math_functions.py
import pytest

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (10, -5, 5)
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected
```

#### Fixtures and Mocking
```python
import pytest
from unittest.mock import Mock, patch

@pytest.fixture
def sample_data():
    return {"users": [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]}

@pytest.fixture(scope="module")
def database_connection():
    # Setup
    connection = Mock()
    connection.connect.return_value = True
    yield connection
    # Teardown
    connection.close()

def test_with_fixture(sample_data):
    assert len(sample_data["users"]) == 2
    assert sample_data["users"][0]["name"] == "Alice"

@patch('requests.get')
def test_api_call(mock_get):
    mock_get.return_value.json.return_value = {"status": "success"}
    mock_get.return_value.status_code = 200
    
    # Your function that makes API call
    # result = make_api_call()
    # assert result["status"] == "success"
```

### Debugging

#### Using pdb
```python
import pdb

def complex_function(data):
    result = []
    for item in data:
        pdb.set_trace()  # Debugger will stop here
        processed = item * 2
        if processed > 10:
            result.append(processed)
    return result

# Usage
# complex_function([1, 2, 3, 4, 5, 6])
```

#### Logging for Debugging
```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def debug_function(x, y):
    logger.debug(f"Input parameters: x={x}, y={y}")
    
    result = x + y
    logger.debug(f"Addition result: {result}")
    
    if result > 10:
        logger.warning(f"Result {result} is greater than 10")
    
    return result
```

---

## Development Environment

### Virtual Environments

#### venv (Built-in)
```bash
# Create virtual environment
python -m venv myenv

# Activate (Windows)
myenv\Scripts\activate

# Activate (Unix/MacOS)
source myenv/bin/activate

# Deactivate
deactivate

# Install packages
pip install requests pandas

# Save requirements
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt
```

#### conda
```bash
# Create environment
conda create -n myenv python=3.9

# Activate environment
conda activate myenv

# Install packages
conda install numpy pandas matplotlib

# Install from pip
pip install requests

# Export environment
conda env export > environment.yml

# Create from environment file
conda env create -f environment.yml

# List environments
conda env list
```

### Interactive Environments

#### IPython
```python
# Enhanced interactive shell
# %magic commands
%timeit sum(range(100))
%who  # List variables
%whos  # Detailed variable info
%history  # Command history

# System commands
!ls  # Run shell command
files = !ls  # Capture output

# Debugging
%debug  # Enter debugger after exception
%pdb on  # Auto-enter debugger on exception
```

#### Jupyter Lab/Notebook
```python
# Cell magic commands
%%time
# Code to time

%%writefile myfile.py
# Write cell content to file

%%bash
# Run bash commands

# Display magic
from IPython.display import HTML, Image, Markdown
display(HTML("<h1>Hello World</h1>"))
```

---

## Project Organization

### Project Structure

#### Basic Project Structure
```
my_project/
├── pyproject.toml
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── src/
│   └── my_project/
│       ├── __init__.py
│       ├── main.py
│       ├── models/
│       │   ├── __init__.py
│       │   └── user.py
│       └── utils/
│           ├── __init__.py
│           └── helpers.py
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   └── test_models/
│       └── test_user.py
├── docs/
│   └── README.md
└── scripts/
    └── setup.py
```

#### pyproject.toml
```toml
[build-system]
requires = ["setuptools>=45", "wheel", "setuptools_scm[toml]>=6.2"]
build-backend = "setuptools.build_meta"

[project]
name = "my-project"
version = "0.1.0"
description = "A sample Python project"
readme = "README.md"
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
license = {text = "MIT"}
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
]
keywords = ["sample", "project"]
dependencies = [
    "requests>=2.25.0",
    "click>=8.0.0",
]
requires-python = ">=3.9"

[project.optional-dependencies]
dev = [
    "pytest>=6.0",
    "black>=22.0",
    "flake8>=4.0",
    "mypy>=0.950",
]
docs = [
    "sphinx>=4.0",
    "sphinx-rtd-theme>=1.0",
]

[project.urls]
Homepage = "https://github.com/username/my-project"
Repository = "https://github.com/username/my-project"
Documentation = "https://my-project.readthedocs.io"
"Bug Tracker" = "https://github.com/username/my-project/issues"

[project.scripts]
my-cli = "my_project.main:cli"

[tool.setuptools.packages.find]
where = ["src"]

[tool.black]
line-length = 88
target-version = ['py39']

[tool.mypy]
python_version = "3.9"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
```

### Package Management

#### setup.py (Legacy)
```python
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="my-project",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A sample Python project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/username/my-project",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
    extras_require={
        "dev": ["pytest>=6.0", "black>=22.0", "flake8>=4.0"],
        "docs": ["sphinx>=4.0", "sphinx-rtd-theme>=1.0"],
    },
    entry_points={
        "console_scripts": [
            "my-cli=my_project.main:cli",
        ],
    },
)
```

### Version Control Integration

#### .gitignore for Python
```gitignore
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# celery beat schedule file
celerybeat-schedule

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/
```

---

## IDE Setup

### VS Code Configuration

#### settings.json
```json
{
    "python.defaultInterpreterPath": "./venv/bin/python",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": false,
    "python.linting.flake8Enabled": true,
    "python.linting.mypyEnabled": true,
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": ["--line-length=88"],
    "python.sortImports.args": ["--profile", "black"],
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.organizeImports": true
    },
    "python.testing.pytestEnabled": true,
    "python.testing.unittestEnabled": false,
    "python.testing.pytestArgs": [
        "tests"
    ],
    "files.exclude": {
        "**/__pycache__": true,
        "**/*.pyc": true
    }
}
```

#### Recommended Extensions
```json
{
    "recommendations": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-python.black-formatter",
        "ms-python.isort",
        "ms-python.flake8",
        "ms-python.mypy-type-checker",
        "ms-toolsai.jupyter",
        "ms-vscode.test-adapter-converter",
        "littlefoxteam.vscode-python-test-adapter"
    ]
}
```

### PyCharm Configuration

#### Key Features to Configure
- **Interpreter**: Set up virtual environment interpreter
- **Code Style**: Configure Black formatter
- **Inspections**: Enable type checking, PEP 8 compliance
- **Testing**: Configure pytest as default test runner
- **Version Control**: Git integration
- **Plugins**: Install useful plugins like .ignore, Requirements

#### Useful PyCharm Shortcuts
```
Ctrl+Shift+F10  - Run current file
Ctrl+Shift+F9   - Debug current file
Ctrl+Alt+L      - Reformat code
Ctrl+Alt+O      - Optimize imports
Ctrl+Shift+T    - Create/Go to test
Ctrl+B          - Go to declaration
Ctrl+Shift+F    - Find in files
Alt+Enter       - Show intention actions
```

---

## Best Practices Summary

### Code Quality
- Follow PEP 8 style guidelines
- Use type hints for better code documentation
- Write comprehensive docstrings
- Keep functions small and focused
- Use meaningful variable and function names

### Testing
- Write tests for all public functions
- Aim for high test coverage (>80%)
- Use fixtures for test data setup
- Mock external dependencies
- Test edge cases and error conditions

### Project Organization
- Use virtual environments for dependency isolation
- Structure projects with clear separation of concerns
- Use pyproject.toml for modern Python packaging
- Include comprehensive documentation
- Set up CI/CD pipelines for automated testing

### Performance
- Use generators for memory-efficient iteration
- Profile code to identify bottlenecks
- Choose appropriate data structures
- Consider async programming for I/O-bound tasks
- Use multiprocessing for CPU-bound tasks

### Security
- Validate all input data
- Use environment variables for sensitive configuration
- Keep dependencies updated
- Follow secure coding practices
- Use tools like bandit for security analysis

---

This comprehensive guide covers all the essential Python concepts and practices needed for professional development. Each section includes practical examples and best practices to help you write clean, efficient, and maintainable Python code.