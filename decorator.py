# def decor(fun):
# 	def inner():
# 		a = fun()
# 		add = a + 5
# 		return add
# 	return inner

# def num():
# 	return 10

# result_fun = decor(num)
# print(result_fun())



#  OR

# def decor(num):
# 	def inner():
# 		a = num()
# 		add = a + 5
# 		return add
# 	return inner

# def num():
# 	return 10

# num = decor(num)
# print(num())


# OR

# def decor(num):
# 	def inner():
# 		a = num()
# 		add = a + 5
# 		return add
# 	return inner

# @decor
# def num():
# 	return 10

# print(num())



# Example:- 2
def decor1(num):
	def inner():
		b = num()
		multi = b * 5
		return multi
	return inner

def decor2(num):
	def inner():
		a = num()
		add = a + 5
		return add
	return inner


def num():
	return 10

num = decor2(decor1(num))
print(num())