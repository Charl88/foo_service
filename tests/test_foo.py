from services.foo import FooService


def test_square_odd():
    foo = FooService()
    # given a list of odd and even numbers
    assert foo.square_odd([1, 2, 3, 4, 5, 6, 7]) == [1, 2, 9, 4, 25, 6, 49]
    # given a list of only odd numbers
    assert foo.square_odd([3, 5, 7]) == [9, 25, 49]
    # given a list of only even numbers
    assert foo.square_odd([2, 4, 6]) == [2, 4, 6]
    # given a list of numbers including floats
    assert foo.square_odd([1, 2.4, 3.4]) == [1, 2, 9]

def test_encoding_decoding():
    foo = FooService()
    strings = ['this is a test string', 'this is another test string']
    code = foo.encode(strings)
    # test that the encoded string successfully decodes to the same string
    assert strings[0] == foo.decode(code[strings[0]])
    assert strings[1] == foo.decode(code[strings[1]])