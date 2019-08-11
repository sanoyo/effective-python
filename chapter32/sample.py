class LazyDB(object):
    def __init__(self):
        self.exists = 5

    def __getattr__(self, name):
        value = 'Value for %s' % name
        setattr(self, name, value)
        return value


# 実行
data = LazyDB()
print('Before:', data.__dict__)
print('foo:   ', data.hogehoge)
print('After: ', data.__dict__)
