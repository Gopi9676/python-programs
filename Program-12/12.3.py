class Myclass:
    def __init__(self):
        self.public_attribute="I'm a public attribute"
        self._protected_attribute="I'm a protected attribute"
        self._private_attribute="I'm a private attribute"
    def public_method(self):
        print("I'm a public method")
    def _protected_method(self):
        print("I'm a protected method")
    def _private_method(self):
        print("I'm a private method")
obj=Myclass()
print(obj.public_attribute)
obj.public_method()
print(obj._protected_attribute)
obj._protected_method()
print(obj._private_attribute)
obj._private_method()
