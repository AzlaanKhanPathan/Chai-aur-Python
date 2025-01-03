def sum_of_all(*args):
    print(args)
    for i in args:
        print(i * 2)
    return sum(args)

print(sum_of_all(1,2,3))
# print(sum_of_all(1,2,3,4))
# print(sum_of_all(1,2,3,4,5,6))



