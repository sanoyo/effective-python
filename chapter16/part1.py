def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1

address = 'Four score and seven years ago...'
result = list(index_words_iter(address))
result = result
print(result[:3])


## 問題点

### 入力が大量の際は、メモリがた食いつぶされてしまう

### 