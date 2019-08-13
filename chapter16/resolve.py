def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset

address_lines = """Four score and seven years
ago our fathers brought forth on this
continent a new nation, conceived in liberty,
and dedicated to the proposition that all men
are created equal."""

# address_lines = """Four score and seven years ago our fathers brought forth on this"""
# with open('address.txt', 'w') as f:
#     f.write(address_lines)

from itertools import islice
with open('address.txt', 'r') as f:
    # generatorを返す
    it = index_file(f)
    results = islice(it, 0, 10)
    print(list(results))
