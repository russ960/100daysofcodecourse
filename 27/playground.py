def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(1,3,2,4,7,2))