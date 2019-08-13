def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)

def normalize_func(get_iter):
    total = sum(get_iter())   # New iterator
    result = []
    for value in get_iter():  # New iterator
        percent = 100 * value / total
        result.append(percent)
    return result

percentages = normalize_func(lambda: read_visits('my_numbers.txt'))
print(percentages)