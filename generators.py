#1

# def numOfSquare(num):
#     for i in num:
#         yield (i * i)
#
# numbers = numOfSquare([1, 2, 3, 4, 5])
#
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))

#2

# def evenNum(num):
#     for i in range(0, num + 1):
#         if i % 2 == 0:
#             yield i
#
# num = int(input("text a num: "))
# values = []
#
# for i in evenNum(num):
#     values.append(str(i))
#
# print(','.join(values))

#3

# def numDivFor(num):
#     for i in range(1, num + 1):
#         if i % 3 == 0 and i % 4 == 0:
#             yield i
#
# numbers = int(input("text a num: "))
#
# total = []
# for i in numDivFor(numbers):
#     total.append(str(i))
#
#
# print(','.join(total))

#4

# def squares(a, b):
#     while a <= b:
#         yield a * a
#         a += 1
#
# for i in squares(1, 5):
#     print(i)

#5

def numToReturn(num):
    while num >= 0:
        yield num
        num -= 1

for i in numToReturn(10):
    print(i)
