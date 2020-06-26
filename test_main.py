from main import *

def test_soma():
    assert soma(3,3) == 6, "Should be 6"
    assert type(soma(3,3)) == int, 'Should be int type'

if __name__ == "__main__":
    test_soma()
    print("Everything passed")