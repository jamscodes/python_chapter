#1
# def a():
#     return 5
# print(a()) # should output 5

# #2
# def a():
#     return 5
# print(a()+a()) # should output 10

#3
# def a():
#     return 5
#     return 10
# print(a()) # should output 5

# #4
# def a():
#     return 5
#     print(10)
# print(a()) # should output 5

#5
# def a():
#     print(5) # will output 5 to the console
# x = a()
# print(x) # should output a written form of a() (I was wrong. It outputs "none" since there is no actual value associated with the variable.)

#6
# def a(b,c):
#     print(b+c)
# print(a(1,2) + a(2,3)) # should output 3 5 None error

#7
# def a(b,c):
#     return str(b)+str(c)
# print(a(2,5)) # should output 25

#8
# def a():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(a()) # should output 100 10

#9
# def a(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(a(2,3))
# print(a(5,3))
# print(a(2,3) + a(5,3)) # should output 7 14 21

#10
# def a(b,c):
#     return b+c
#     return 10
# print(a(3,5)) # should output 8

#11
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
# print(b)
# a()
# print(b)
# # should output 500 500 300 500

#12
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# a()
# printcopy(b)
# # should output 500 500 300 undefined error

#13
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=a()
# print(b)
# # should output 500 500 300 300

#14
# def a():
#     print(1)
#     b()
#     print(2)
# def b():
#     print(3)
# a()
# # should output 1 3 2

#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
# should output 1 3 5 10