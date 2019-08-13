# 問題のあるコード
def index_words(text):
    """indexの位置を返すメソッド

    Arguments:
        text 文字列
    
    Returns:
        
    """
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result

address = 'Four score and sevean years ago...'
# address = 'Four score and seven years ago our fathers brought forth on this continent a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal.'
result = index_words(address)
print(result[:3])