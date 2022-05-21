from myclass import MyClass


class TestMyClass:
    def test_get_value(self):
        assert MyClass('test_value').get_value() == 'test_value'

    def test_value(self):
        assert MyClass('test_value').value == 'test_value'
