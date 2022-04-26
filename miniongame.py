# def minion_game(string):
#     vowels = ['A', 'E', 'I', 'O', 'U']
#     kcounter = 0
#     scounter = 0
#     for i in range (len(string)):
#         if string[i] in vowels:
#             kcounter += len(string) - i
#         else:
#             scounter += len(string) - i
    
#     if kcounter > scounter:
#         print('Kevin '+ str(kcounter))
#     elif scounter > kcounter:
#         print('Stuart '+ str(scounter))
#     else:
#         print('Draw')

# if __name__ == '__main__':
#     s = input()
#     minion_game(s)

# def merge_the_tools(string, k):
#     index = len(string) // k
#     length = len(string)  
#     n = index  
#     chars = int(length/n)  
#     liist = []
#     liist.append([string[i: i+chars] for i in range (0, length, chars)])
#     for i in liist[0]:
#         print(''.join(sorted(set(i), key = i.index)))

    # print(index)
    # foo.append([string[i:i+index] for i in range (0, len(string), index)])
    # for i in foo[0]:
    #     print(''.join(sorted(set(i), key = i.index)))
# def merge_the_tools(string, k):
#     for i in range(0,len(string),k):
#         y=string[i:i+k]
#         print("".join(dict.fromkeys(y)))
# if __name__ == '__main__':
#     string, k = input(), int(input())
#     merge_the_tools(string, k)
# import re


# phone = 9587456281
# re.match(r"^(\([0-9]{3}\) ?|[0-9]{3}-)[0-9]{3}-[0-9]{4}$", phone)

n = int(input())
sizes = list(map(int, input().split()))
for _ in range(int(input())):
    size, price = list(map(int, input()))

print(n)
print(sizes)
print(size)
print(price)
