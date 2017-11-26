class MockObject(object):
    """
    Generic mock class allowing arbitrary access and invocation of any property without throwing.
    """

    def __getattr__(self, item):
        return MockObject()

    def __call__(self, *args, **kwargs):
        return MockObject()


class PiCamera(object):
    """
    Mock PiCamera class. Does not implement any logic, but rather places a stub in place of any and
    all operations a client might perform on an instance of the real class.
    """

    def __init__(self, *args, **kwargs):
        pass

    def __getattr__(self, item):
        return MockObject()
