#第四章练习

apples=['iphone_x','ipad_pro','macbook_pro','imac_pro','apple_watch']
#for循环
for apple in apples:
	print(apple.title())
#range（）函数的使用
for value in range(1,6):
	print(str(value) +". " + apple.title())
#list（）函数的使用
numbers=list(range(1,6))
print(numbers)
#平方数字
squares=[]
for value in range(1,11):
	squares.append(value**2)
print(squares)
#数字字符串的函数：最小值、最大值、求和
print(min(squares))
print(max(squares))
print(sum(squares))
#字符串的切片
print(apples[1:4])
#字符串的复制
Appples=apples
print(Appples)