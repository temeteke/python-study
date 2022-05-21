from mypackage.myfunc import myfunc


class TestMyFunc:
    def test_func(self):
        assert myfunc() == 'return value'
