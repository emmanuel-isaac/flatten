def flatten(array):
    result = []
    for i in array:
        if isinstance(i, int):
            result.append(i)
        elif isinstance(i, list):
            result.extend(flatten(i))
    return result
