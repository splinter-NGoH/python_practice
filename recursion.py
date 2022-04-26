

# def factorial (n):
#     assert n >= 0 and int(n) == n, 'the number must be postive'
#     if n in [1,0]:
#         return 1
#     else:
#         print(n)
#         return n * factorial(n-1)


# print (factorial(10))

# def febonacci (n):
#     assert n >= 0 and int(n) == n, 'number must be postive'
#     if n in [0,1]:
#         return n
#     else:    
#         print(n)
#         return febonacci(n-1) + febonacci(n-2)


# print(febonacci(-6))



# def likes(names):
#     if not names:
#         return 'no one likes this'
#     elif len(names) == 1:
#         return '{} likes this'.format(names[0])
#     elif len(names) == 2:
#         return '{0} and {1} like this'.format(names[0], names[1])
#     elif len(names) == 3:
#         return '{0}, {1} and {2} like this'.format(names[0], names[1], names[2])
#     else:
#         return '{0}, {1} and {2} others like this'.format(names[0], names[1], len(names) - 2 )

print ('5 + 10 = {}'.format(5+10))