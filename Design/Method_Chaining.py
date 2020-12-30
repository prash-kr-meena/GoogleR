""" https://www.tutorialspoint.com/Explain-Python-class-method-chaining"""


class Foo(object):
    def bar(self):
        print("Foo.bar called")
        return self

    def baz(self):
        print("Foo.baz called")
        return self


if __name__ == '__main__':
    foo1 = Foo()
    foo2 = foo1.bar().baz()
    print("id(foo1):", id(foo1))
    print("id(foo2):", id(foo2))
