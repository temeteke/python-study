from mypackage.myclass import MyClass, MyClassManager
from unittest.mock import patch


class TestMyClass:
    def test_get_value(self):
        assert MyClass('test_value').get_value() == 'test_value'

    def test_value(self):
        assert MyClass('test_value').value == 'test_value'


class TestMyClassManager:
    @patch('mypackage.myclass.MyClass')
    def test_get_values(self, MockMyClass):
        values = MyClassManager(n=5).get_values()
        assert values
        for value in values:
            assert value == MockMyClass()

    @patch('mypackage.myclass.MyClass')
    def test_values(self, MockMyClass):
        values = MyClassManager(n=5).values
        assert values
        for value in values:
            assert value == MockMyClass()
