# if __name__ == '__main__':
#     x, y, z, n = (int(input()) for _ in range(4))

    # nestlest = []
    # mylist = []
    # """ 2 2 2 """
    # print([
    # [i,j,k]
    # for i in range(x + 1)
    #     for j in range(y +1 )
    #         for k in range(z+1) if i + j + k != n
    #         ])

    # listijk = [] #an empty list to be filled as following
    # for i in range(x + 1): #it will output 0, and will only output 1 after the next conditions ('for j' and 'for k') are met.
    #     for j in range (y + 1): #it will output 0, and will only output 1 after the next condition ('for k') is met.
    #         for k in range (z + 1): #it will output 0 and then 1.
    #             listijk.append([i,j,k]) #it will add i, j and k values to the list
    # print(listijk) #print the list properly filled

# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())

#     print(sorted(list(set(arr)))[-2])

    # max = arr[0]
    # less_max = 0
    # print('-' * 50)
    # for num in arr:
    #     if num > max:
    #         less_max = max
    #         max = num



    # print(max)
    # print(less_max)


# if __name__ == '__main__':
#     nameandgrade = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         nameandgrade.append([name,score])
#     min = nameandgrade[0][1]
#     for clock in range(len(nameandgrade)):
#         if min < nameandgrade[clock][1]:
#             min = min
#     for list in sorted(nameandgrade):
#         if list[1] == min:
#             print (list[0])
# marksheet = []
# for _ in range(0,int(input())):
#     marksheet.append([input(), float(input())])

# second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
# print(second_highest)
# print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))

# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#     for key in student_marks.keys():
#         if key == query_name:
#             print('{0:.2f}'.format(sum(student_marks[key])/ len(student_marks[key])))

# friends = ['Mohammed', 'Ahmed', 'ebrahim', 'Morsy', 'elsisy hwa r2ysy']
# for name in friends:
#     if name.strip()[0].isupper():
#         print(name)
#     else: continue
# if __name__ == '__main__':
#     n = int(input())
#     opdict = {}
#     insertlist = []
#     for _ in range(n):
#              name, *line = input().split()
#              scores = list(map(int, line))
#              opdict[name] = scores
#     print (opdict)
#     # {'insert': [0, 6], 'print': [], 'remove': [6], 'append': [1], 'sort': [], 'pop': [], 'reverse': []}
#     for key in opdict.keys():
#         if key == 'insert':
#             # print (opdict[key][0], opdict[key][1])
#             insertlist.insert(opdict[key][0], opdict[key][1])
#         elif key == 'print':
#             print(insertlist)
#         elif key == 'remove':
#             insertlist.remove(opdict[key][0])
#         elif key == 'apppend':
#             insertlist.append(opdict[key][0])
#         elif key == 'sort':
#             insertlist = insertlist.sort()
#         elif key == 'reverse':
#             insertlist.reverse()
#         else:
#             break

    # print(opdict.values())
    # print(opdict.keys())
    # opdict.fromkeys()
    # print(opdict.items())
    # for key in opdict.keys():
    #     insertlist.key(int(opdict[key]))
    #     print(insertlist)
    # print(insertlist)
    # print('\n'.join([a for a,b in opdict ]))
        
    # for items in opdict.values()
    


# n = int(input())
# l = []
# for _ in range(n):
#     s = input().split()
#     print(s, 's value')
#     cmd = s[0]
#     print(cmd, 'cmd value')
#     args = s[1:]
#     print(args, ' args values')
#     if cmd !="print":
#         cmd += "("+ ",".join(args) +")"
#         eval("l."+cmd)
#     else:
#         print (l)
# print (' hat ever we have here '.center(50, '-'))
# friends = ['Mohammed', 'Ahmed', 'ebrahim', 'Morsy', 'elsisy hwa r2ysy']
# for name in friends:
#     if name.strip()[0].isupper():
#         print(name)
#     else: continue
# if __name__ == '__main__':
#     n = int(input())
#     integer_list = tuple(map(int, input().strip().split(' ')))
#     print(hash(integer_list))
    
# def swap_case(s):
#     s2 = ''
#     for letter in s:
        
#         if letter.islower():
#             s2 += ''.join(letter.upper())
#         elif letter.isupper():
            
#             s2 +=''.join(letter.lower())
#         else:
#             s2 +=''.join(letter)
#     return s2
    
    
# s = 'HackerRank.com presents "Pythonist 2".'
# print(swap_case(s))

# print (''.join([i.lower() if i.isupper() else i.upper() for i in input()]))
# def split_and_join(line):
#     # write your code here
#     s = line.split(" ")
#     print(s)
#     s = '-'.join(s)
#     print(s)

#     return  s
            
# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)

# s = input()
# print (any((a.isalnum() for a in s)))
# print (any((a.isalpha() for a in s)))
# print (any((a.isdigit() for a in s)))
# print (any((a.islower() for a in s)))
# print (any((a.isupper() for a in s)))

#Replace all ______ with rjust, ljust or center. 

# #Replace all ______ with rjust, ljust or center. 

# thickness = int(input()) #This must be an odd number
# c = 'H'

# #Top Cone
# for i in range(thickness):
#     print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

# #Top Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# #Middle Belt
# for i in range((thickness+1)//2):
#     print((c*thickness*5).center(thickness*6))    

# #Bottom Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

# #Bottom Cone
# for i in range(thickness):
#     print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# import math

# c='♥'
# width = 40

# print ((c*2).center(width//2)*2)

# for i in range(1,width//10+1):
#     print (((c*int(math.sin(math.radians(i*width//2))*width//4)).rjust(width//4)+
#            (c*int(math.sin(math.radians(i*width//2))*width//4)).ljust(width//4))*2)

# for i in range(width//4,0,-1):
#     print ((c*i*4).center(width))
# print ((c*2).center(width))

# import textwrap

# def wrap(string, max_width):
    
#     # for fourletter in range(0,len(string), max_width):
#     return '\n'.join([string[fourletter:fourletter+max_width] for fourletter in range(0, len(string), max_width)])
    

# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)

# n, m = map(int,input().split())
# pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
# print (pattern)
# print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))

# n, m = map(int, input().split())
# pattern = [('.|.'*(2*i+1)).center(m, '-') for i in range (n//2)]
# print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))