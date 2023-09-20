import hello;

class TestHello:
    def test_one(self):
        assert hello.hello_world() == "Hello!"

    def test_two(self):
        assert hello.plus_one(5) == 6
 
    def test_three(self):
        assert hello.plus_two(2) == 4
