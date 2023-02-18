class Foo (object):
    def __init__(self, *dt, **p):
        self.a = dt
        self.p = p
        print('init', end='')
o = Foo(123,456,456)

print(o.a)