class Test:
    def __init__(self):
        self.public = 'public'
        self._protected = 'protected'
        self.__private = 'private'


test = Test()
# print(test.public)
# print(test._protected)
# print(test.__private)
print()
print(test.__dict__)
print(dir(test))
print()
# print(test.__private)
