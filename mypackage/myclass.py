class MyClass:
    def __init__(self, value):
        self._value = value

    def get_value(self):
        return self._value

    @property
    def value(self):
        return self._value
