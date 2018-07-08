#第五章练习

apples=['iphone_x','ipad_pro','macbook_pro','imac_pro','apple_watch']
#条件测试
phone='apple'
print(phone.title()=='Apple')
#数值比较
age_0=18
age_2=20
print(age_0 > 15 and age_2 < 22)
print(age_0 > 120 or age_2 < 22)
#检查特定值是否包含在列表中
print('macbook_pro' in apples)
print('apple_pencil' not in apples)
#if 语句的多个条件测试
macbook_pro=18000
if macbook_pro <= 15000:
	print('buy it!')
elif 15000 < macbook_pro <= 20000:
	print('ask to my parents')
elif 20000 < macbook_pro <= 25000:
	print("you can't buy it")
else:
	print('fuck the Apple')

if 'macbook_pro' in apples:
	print('you have it')
else:
	print('buy one')