# import numpy as np


# array1 = []
# try:    
#     arrayavf = int(input('How many day\'s temperature: '))
# except ValueError: 
#     raise ValueError('error not int')
# for clock in range(0,arrayavf):
#     array1.append(int(input('Day {}\'s high remp: '.format(clock+1))))
#     # array2 = np.insert(array1, clock, input('Day {}\'s high remp: '.format(clock)))
# averaging = sum(array1) / len(array1)
# print(averaging)
# above = 0
# for number in array1:
#     if number > averaging:
#         above += 1

# print('{} day\'s above average'.format(above))
allno = input('')
f_no = int(allno.split(' ')[0])
s_no = int(allno.split(' ')[1])
print('{0} + {1} = {2} \n{0} * {1} = {3}\n{0} - {1} = {4}\n'.format(f_no, s_no, f_no + s_no, f_no*s_no, f_no-s_no))
# allno = input('')
# f_no = int(allno.split(' ')[0])
# s_no = int(allno.split(' ')[1])
# thrd_no = int(allno.split(' ')[2])
# fourth_no = int(allno.split(' ')[3])
# print('Difference = {}'.format((f_no*s_no)-(thrd_no*fourth_no)))