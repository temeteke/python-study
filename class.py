class Parent:
    def foo(self):
        print("parent foo")
        self.bar()
    
    def bar(self):
        print("parent bar")


class Child(Parent):
    def foo(self):
        print("child foo")
        super().foo()

    def bar(self):
        print("child bar")
        super().bar()


if __name__ == '__main__':
    Child().foo()