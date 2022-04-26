# inputin = int(input('number of lines'))
# for i in range (inputin // 2):
    # print('*' * (i+1) )
# for i in range (inputin // 2, -1, -1):
#     print('*' * (i+1) )
# for c in range(10 - 1,-1,-1):
#     print (c)
n, m = map(int,input().split())
pattern = [('*'*(2*i + 1)).center(m, ' ') for i in range(n//2)]
print('\n'.join(pattern +  [( '' if n %2 == 0 else ('*' * n).center(m, ' '))] + pattern[::-1])) 