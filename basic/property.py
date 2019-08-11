class SampleProperty(object):
    def __init__(self, value):
        self._x = value
    
    # 読み込み
    # propertyの時は、getterと同じキョドになる
    @property
    def sample(self):
        return self._x

    # 書き込み
    @sample.setter
    def sample(self, v):
        self._x = abs(v) # 更新前に何らかの処理をはさめる

    # 削除
    @sample.deleter
    def sample(self):
        self._x = None

mypro = SampleProperty(100)
print(mypro.sample) # 100

mypro.sample = -200
print(mypro.sample) # 200

del mypro.sample
print(mypro.sample) # None