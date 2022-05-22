class MyClass:
    def __init__(self, value):
        self._value = value

    def get_value(self):
        return self._value

    @property
    def value(self):
        return self._value


class MyClassManager:
    def __init__(self, n=5):
        self._values = [MyClass(x) for x in range(n)]

    def get_values(self):
        return self._values

    @property
    def values(self):
        return self._values
