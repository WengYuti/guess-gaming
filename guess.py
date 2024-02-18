import random
start = input('請決定隨機數字開始值:')
end = input('請決定隨機數字結束值:')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
	count += 1
	user = input('請猜數字:')
	user = int(user)
	if user == r:
		print('You got it')
		print('這是你猜的第', count, '次')
		break
	elif user > r:
		print('比答案大')
	elif user < r:
		print('比答案小') 
	print('這是你猜的第', count, '次')