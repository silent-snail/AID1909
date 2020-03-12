class Person:
    def __init__(self):
        self.__a = 2

    def __add(self):
        self.__a += 2

    def run(self):
        self.__add()
        return self.__a * 2


class Student(Person):
    def __init__(self):
        super().__init__()

    def __add(self):
        pass

    def run(self):
        return super().run()


if __name__ == '__main__':
    s = Student()
    print(s.run())