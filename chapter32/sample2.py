class ValidationDB(object):
    def __init__(self):
        self.exists = 5
        
    def __getattribute__(self, name):
        print('Called __getattribute__(%s)' % name)
        try:
            return super(type(name)).__getattribute__(name)
        except AttributeError:
            value = 'Value for %s' % name
            setattr(self, name, value)
            return value

data = ValidationDB()
print('exists:', data.exists)
print('foo:   ', data.foo)
print('foo:   ', data.foo)