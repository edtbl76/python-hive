# Object Oriented Programming

A popular `programming paradigm` (a way to classify different programming languages and the unique features they offer) characterized by classes and objects. 

OOP has 4 Pillars
- Inheritance
- Polymorphism
- Abstraction
- Encapsulation


#### Example 1
```python
class Dog:
  sound = "Woof"
 
  def __init__(self, name, age):
    self.name = name
    self.age = age
 
  def bark(self):
    print(Dog.sound)
```

#### Example 2
```python
# Write your code below
class Employee:
  new_id = 1

  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is ", self.id)


e1 = Employee()
e2 = Employee()

e1.say_id() # 1
e2.say_id() # 2
```

----

## Inheritance

#### Two Distinct Classes
Here we have 2 classes w/ different attributes and capabilities. 
```python
class Dog:
 
  def bark(self):
    print('Woof!')
 
class Cat:
 
  def meow(self):
    print('Meow!')
```

#### Parent Classes
However, if we wanted to create a capability that was shared between the two (say, something that all animals do.. like eat)
```python
class Animal: 
  def eat(self): 
    print("Nom Nom Nom...eating food!")
```

#### Child Classes.
In order to "pass" this functionality down to its children, we have to create a hierarchical model to allow the children to inherit functionality provided by the parent. 

Example
```python
class ParentClass:
  #class methods/properties...
 
class ChildClass(ParentClass):
  #class methods/properties...
```

In Practice
```python
class Dog(Animal):
  def bark(self):
    print('Bark!')
 
class Cat(Animal):
  def meow(self):
    print('Meow!')

fluffy = Dog()
zoomie = Cat()

fluffy.eat() # Nom Nom Nom...eating food!
zoomie.eat() # Nom Nom Nom...eating food!
```

#### Building on Previous Example:
```python
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

# Write your code below
class Admin(Employee):
  pass

e1 = Employee()         
e2 = Employee()
e3 = Admin()
e3.say_id()             # My id is 3
```

### Overriding (Inheritance - Continued)
Method overriding is a way to change the behavior of an inherited method in a derived class. 
- The method in the child class OVERRIDES the inherited behavior in order to do something different.

#### Parent
```python
class Animal:
  def __init__(self, name):
    self.name = name
 
  def make_noise(self):
    print("{} says, Grrrr".format(self.name))
 
pet1 = Animal("Rex")
pet1.make_noise() # Rex says, Grrrr
```

#### Child, w/ Method Override
```python
class Cat(Animal):
 
  def make_noise(self):
    print("{} says, Meow!".format(self.name))
 
pet2 = Cat("Maisy")
pet2.make_noise() # Maisy says, Meow!
```

#### Continued Example (Employee)
```python
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class Admin(Employee):
  # Write your code below
  def say_id(self):
    print("I am an Admin")

e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_id()     # I am an Admin
```

### super()
`super()` provides a way to access an overridden method and its behavior by creating a `proxy object` which allows the invocation of the same method on the Parent (or `superclass`)

#### Example - Changing Child behavior by accessing parent's __init__()
```python
class Animal:
  def __init__(self, name, sound="Grrrr"):
    self.name = name
    self.sound = sound
 
  def make_noise(self):
    print("{} says, {}".format(self.name, self.sound))
 
class Cat(Animal):
  def __init__(self, name):
    super().__init__(name, "Meow!") 
 
pet_cat = Cat("Rachel")
pet_cat.make_noise() # Rachel says, Meow!
```

#### Continued Example (Employee)
```python
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class Admin(Employee):
  def say_id(self):
    # Write your code below:
    super().say_id()
    print("I am an admin.")

e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_id()

# OUTPUT:
#
# My id is 3.
# I am an admin.
#
```

### Multiple Inheritance
This is when a subclass inherits from more than one superclass
- hierarchical multiple inheritance is when a subclass inherits members from both its superclass and its super-superclass
  - (Grandparents!)
  
#### Basic Example
```python
class Animal:
  def __init__(self, name):
    self.name = name
 
  def say_hi(self):
    print("{} says, Hi!".format(self.name))
 
class Cat(Animal):
  pass
 
class Angry_Cat(Cat):
  pass
 
my_pet = Angry_Cat("Mr. Cranky")
my_pet.say_hi() # Mr. Cranky says, Hi!
```

#### Continued Example (Employee)
```python
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class Admin(Employee):
  def say_id(self):
    super().say_id()
    print("I am an admin.")

# Write your code below
class Manager(Admin):
  def say_id(self):
    super().say_id()
    print("I'm in charge!")

e1 = Employee()
e2 = Employee()
e3 = Admin()
e4 = Manager()
e4.say_id()

# OUTPUT
#
#   My id is 4.
#   I am an admin.
#   I'm in charge!  
#

```


- parallel multiple inheritance is when one class inherits directly from two parent classes, and can use the attributes and methods of both

#### Basic Example
```
class Animal:
  def __init__(self, name):
    self.name = name
 
class Dog(Animal):
  def action(self):
    print("{} wags tail. Awwww".format(self.name))
 
class Wolf(Animal):
  def action(self):
    print("{} bites. OUCH!".format(self.name))
 
class Hybrid(Dog, Wolf):
  def action(self):
    super().action()
    Wolf.action(self)
 
my_pet = Hybrid("Fluffy")
my_pet.action() # Fluffy wags tail. Awwww
                # Fluffy bites. OUCH!
```


#### Continued Example (Employee)

```
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class User:
  def __init__(self, username, role="Customer"):
    self.username = username
    self.role = role

  def say_user_info(self):
    print("My username is {}".format(self.username))
    print("My role is {}".format(self.role))

# Write your code below
class Admin(Employee, User):
  def __init__(self):
    super().__init__()
    User.__init__(self, self.id, "Admin")

  def say_id(self):
    super().say_id()
    print("I am an admin.")

e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_user_info()

# OUTPUT
#
#   My username is 3
#   My role is Admin
#
```

---

## Polymorphism
The ability to apply an identical operation onto different types of objects. 
- This is especially useful when an object type may not be known at the program runtime. 

#### Basic Example

```python
class Animal:
  def __init__(self, name):
    self.name = name
 
  def make_noise(self):
    print("{} says, Grrrr".format(self.name))
 
class Cat(Animal):
 
  def make_noise(self):
    print("{} says, Meow!".format(self.name))
 
class Robot:
 
  def make_noise(self):
    print("beep.boop...BEEEEP!!!")

an_animal = Animal("Bear")
my_pet = Cat("Maisy")
my_vacuum = Robot()
objects = [an_animal, my_pet, my_vacuum]

#
#   We have added objects of different types to a collection
#   we iterate through that collection and call make_noise()
#   Against that collection, w/o having to know the type
#
for o in objects:
    o.make_noise()

# OUTPUT
# "Bear says, Grrrr"
# "Maisy says, Meow!"
# "beep.boop...BEEEEP!!!"
```
#### Continued Example (Employee)

```python
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class Admin(Employee):
  def say_id(self):
    super().say_id()
    print("I am an admin.")

class Manager(Admin):
  def say_id(self):
    super().say_id()
    print("I am in charge!")

# Write your code below
meeting = [Employee(), Admin(), Manager()]
for object in meeting:
  object.say_id()

#
# OUTPUT
# My id is 1.
# My id is 2.
# I am an admin.
# My id is 3.
# I am an admin.
# I am in charge!
#
```
### Method Overloading (Dunder Methods) - More Polymorphism
In Python, the name "Dunder" is derived from `D`ouble `under`scores. 
- `__init__()`
- `__repr__()`
  - (a method that only takes `self` as a parameter and returns the `string representation` of the class)
  - This is intended to provide a human-readable means for displaying a class. 

#### Defining a class's dunder methods is a way to perform operator overloading
```python
class Animal:
  def __init__(self, name):
    self.name = name
 
  def __repr__(self):
    return self.name
 
  def __add__(self, another_animal):
    return Animal(self.name + another_animal.name)
 
a1 = Animal("Horse")
a2 = Animal("Penguin")
a3 = a1 + a2
print(a1) # Prints "Horse"
print(a2) # Prints "Penguin"
print(a3) # Prints "HorsePenguin"
```

#### Continued Example (Employee)
```python
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

class Meeting:
  def __init__(self):
    self.attendees = []
  
  def __add__(self, employee):
    print("ID {} added.".format(employee.id))
    self.attendees.append(employee)

  # Write your code
  def __len__(self):
    return len(self.attendees)

e1 = Employee()
e2 = Employee()
e3 = Employee()
m1 = Meeting()
m1.__add__(e1)
m1.__add__(e2)
m1.__add__(e3)
print(len(m1))

# OUTPUT
# 
# ID 1 added.
# ID 2 added.
# ID 3 added.
# 3
#
```

---

## Abstraction
helps code design by defining necessary behaviors to be implemented in a class structure. 
- prevents leaving out or overlapping class functionality as the hierarchies grow and become more complex and intricate. 

`ABC` = Abstract Base Class.
- often used w/ decorator `abstractmethod`, which defines a method contract that must be inherited by classes that impl the ABC

#### Basic Example
```python
from abc import ABC, abstractmethod

class Animal(ABC):
  def __init__(self, name):
    self.name = name
 
  @abstractmethod
  def make_noise(self):
    pass
 
class Cat(Animal):
  def make_noise(self):
    print("{} says, Meow!".format(self.name))
 
class Dog(Animal):
  def make_noise(self):
    print("{} says, Woof!".format(self.name))
 
kitty = Cat("Maisy")
doggy = Dog("Amber")
kitty.make_noise() # "Maisy says, Meow!"
doggy.make_noise() # "Amber says, Woof!"
```

#### ABC can't be instantiated...
Like other languages, the interface/ABC class can't be instantiated, because it is abstract. It serves to act as a blueprint for concrete implementations that will inherit (or implement) the structure it defines. 
```python
an_animal = Animal("Scruffy")
 
# TypeError: Can't instantiate abstract class Animal with abstract method make_noise
```

#### Continuing Example (Employee)
```python
from abc import ABC, abstractmethod

class AbstractEmployee(ABC):
  new_id = 1
  def __init__(self):
    self.id = AbstractEmployee.new_id
    AbstractEmployee.new_id += 1

  @abstractmethod
  def say_id(self):
    pass

class Employee(AbstractEmployee):
    def say_id(self):
      print("My id is", self.id)

e1 = Employee()
e1.say_id()         # My id is 1
```

## Encapsulation
The process of making methods and data hidden inside the object that they relate to. 

### Access Modifiers
Many programming languages accomplish encapsulation through the use of access modifiers such as
- `public`
  - accessed from anywhere
- `protected`
  - accessed from the code within the same module
  - (Intended to allow inherited objects to access the members of their ancestors w/o exposing them publicly)
- `private`
- only accessible from code within the class in which these members are defined. 

#### Python is iffy.
- Python has no built in mechanism to prevent access. 
  - ALL MEMBERS ARE PUBLIC
  - There are common recommended conventions to communicate implied access modification.
```python
# Protected uses a single underscore.
self._x

# Private uses a double underscore
self.__x
```

- `name mangling` occurs on class members preceded w/ a double underscore.
  - The names are internally modified to `obj._Classname__x`

#### Continued Example (Employee)
```python
class Employee():
    def __init__(self):
        self.id = None
        self._id = "protected"
        self.__id = "private"
        

e = Employee()
print(dir(e))

# OUTPUT
# - Notice the name mangling in the first example
# ['_Employee__id', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
#  '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', 
#  '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', 
#  '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
#  '__weakref__', '_id', 'id']
```

### Getter, Setter, Deleters

#### Basic Example
```python
class Animal:
    
    # NOTE: Single Underscore implies protected usage. 
    def __init__(self, name):
        self._name = name
        self._age = None

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if isinstance(new_age, int):
            self._age = new_age
        else:
            raise TypeError

    def delete_age(self):
        print("_age Deleted")
        del self._age



a = Animal("Rufus")
print(a.get_age()) # None

a.set_age(10)
print(a.get_age()) # 10

a.set_age("Ten") # Raises a TypeError

a.delete_age() # "_age Deleted"
print(a.get_age()) # Raises a AttributeError
```
#### Continued Example (Employee)
```python
class Employee():
  new_id = 1
  def __init__(self, name=None):
    self.id = Employee.new_id
    Employee.new_id += 1
    self._name = name

  # Write your code below
  def get_name(self):
    return self._name

  def set_name(self, name):
    self._name = name

  def del_name(self):
    del self._name
  

e1 = Employee("Maisy")
e2 = Employee()



e1 = Employee("Maisy")
e2 = Employee()
print(e1.get_name())

e2.set_name("Fluffy")
print(e2.get_name())

e2.del_name()
print(e2.get_name())
```

### @property Decorator
A more pythonic way to implement getters and setters into OOP programs. 
