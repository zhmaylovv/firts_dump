class Test:

    def __init__(self):
        pass

    @staticmethod
    def assert_equals(function, result):
        if function == result:
            print("\tTest Passed!")
        else:
            print("\tTest Failed:", f"\t'{function}' should equal '{result}'")
