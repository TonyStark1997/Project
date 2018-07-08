#第八章函数练习

def greet_user():
	"""显示简单问候语"""
	print("Hello!")
greet_user()

def cube(x):
	x=x*x*x
	return x
print(cube(5))

def make_pizza(*toppings):
	print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')