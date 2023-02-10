#!/usr/bin/python3
class Base:
    pass
print(Base().__class__)
print(Base.__class__)
print(Base().__dict__)
print(Base.__dict__)
print(Base().__str__)
print(Base().__str__())

print(Base().__repr__())
print(Base.__name__)