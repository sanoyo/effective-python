def normalize(numbers):
    """全体の割合を出力する関数
    
    Arguments:
        numbers 数値
    
    Returns:
        100の内、どのくらいの割合かを返す
    """
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


visits = [15, 35, 80]
percentages = normalize(visits)
print(percentages)