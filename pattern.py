n = int(input("Enter The Value : "))

# for i in range(n):
# 	print("*",end=' ')

# output
# * * * * *


# for i in range(n):
# 	print("* "*n)

# Output
# * * * * *
# * * * * *
# * * * * *



# for i in range(n):
# 	print((str(n)+" ")*n)

# Output
# 3 3 3
# 3 3 3
# 3 3 3


# for i in range(n):
# 	print((str(i+1)+' ')*n)

# Output
# 1 1 1
# 2 2 2
# 3 3 3


# for i in range(n):
# 	print('A '*n)

# Output
# A A A
# A A A
# A A A


# for i in range(n):
# 	print((chr(65+i)+' ')*(i+1))

# Output
# A 
# B B 
# C C C 
# D D D D 
# E E E E E 


# for i in range(n):
# 	print('* '*(n-i))

# Output
# * * * * *
# * * * * 
# * * * 
# * * 
# * 

# for i in range(n):
# 	print('* '*(i+1))

# Output
# * 
# * * 
# * * * 
# * * * * 
# * * * * *


# for i in range(n):
# 	for j in range(n-i):
# 		print(j+1,end=' ')
# 	print()

# Output
# 1 2 3 4
# 1 2 3 
# 1 2 
# 1 


# for i in range(n):
# 	print(' '*(n-i-1)+(str(i+1)+' ')*(i+1))

# Output
#     1 
#    2 2 
#   3 3 3 
#  4 4 4 4 
# 5 5 5 5 5


# for i in range(n):
# 	print(' '*(n-i-1),end='')
# 	for j in range(i+1):
# 		print(chr(64+n-j),end=' ')
# 	print()

# Output
#     E 
#    E D 
#   E D C 
#  E D C B 
# E D C B A



# for i in range(n):
# 	for j in range(i+1):
# 		print(chr(65+j),end=' ')
# 	print()
# for i in range(n-1):
# 	for j in range(n-i-1):
# 		print(chr(65+j),end=' ')
# 	print()


# Output
# A 
# A B 
# A B C 
# A B C D 
# A B C D E
# A B C D 
# A B C 
# A B 
# A 


# for i in range(n):
# 	print(' '*i,end='')
# 	for j in range(n-i):
# 		print(chr(65+j),end=' ')
# 	print()

# Output
# A B C D E
#  A B C D 
#   A B C 
#    A B 
#     A 



# for i in range(n):
# 	print(' '*(n-i-1)+'* '*(i+1))
# for i in range(n-1):
# 	print(' '*(i+1)+'* '*(n-i-1))


# Output
#    * 
#   * * 
#  * * * 
# * * * *
#  * * * 
#   * * 
#    * 



# for i in range(n):
# 	print('* '*(i+1))
# for i in range(n-1):
# 	print('* '*(n-i-1))


# Output
# * 
# * * 
# * * * 
# * * * * 
# * * * * *
# * * * * 
# * * * 
# * * 
# * 


# for i in range(n):
# 	print('  '*(n-i-1)+'* '*(i+1))
# for i in range(n-1):
# 	print('  '*(i+1)+'* '*(n-i-1))


# Output
#       *
#     * *
#   * * *
# * * * *
#   * * *
#     * *
#       *



# for i in range(n):
# 	print('  '*(n-i-1)+'* ',end='')
# 	if i>= 1:
# 		print('  '*(2*i-1)+'*',end='')
# 	print()

# Output
#       * 
#     *   *
#   *       *
# *           *


# for i in range(n):
# 	print('  '*i+'* ',end='')
# 	if i!=(n-1):
# 		print('  '*(2*n-2*i-3)+'*',end='')
# 	print()

# Output
# *           *
#   *       *
#     *   *
#       * 


# for i in range(n):
# 	print('  '*i+chr(65+i)+'  ',end='')
# 	if i != n-1 :
# 		print('  '*(2*n-2*i-3)+chr(65+i),end='')
# 	print()

# Output
# A            A
#   B        B
#     C    C
#       D  




# for i in range(n):
# 	print('  '*(n-i-1),end='')
# 	for j in range(i+1):
# 		print(j+1,end=' ')
# 	print()
# for i in range(n-1):
# 	print('  '*(i+1),end='')
# 	for j in range(n-i-1):
# 		print(j+1,end=' ')
# 	print()

# Output
#         1
#       1 2
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5
#   1 2 3 4
#     1 2 3
#       1 2
#         1
