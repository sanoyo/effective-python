class ReadVisits(object):
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        """
        イテレータオブジェクト作成
        """
        with open(self.data_path) as f:
            for line in f:
                yield int(line)

def normalize_defensive(numbers):
    print(iter(numbers))
    if iter(numbers) is iter(numbers):
        print(iter(numbers))
        raise TypeError('Must supply a container')
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

visits = [15, 35, 80]
# print(normalize_defensive(visits))

# visits = ReadVisits('my_numbers.txt')
# print(normalize_defensive(visits))

it = iter(visits)
normalize_defensive(it)