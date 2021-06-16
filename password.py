password = ('a123456')
times = int(3)
while times > 0:
	pwd = input('Please enter your password: ')
	if pwd == password:
		print('You are log in!')
		break # escape the loop
	else if times > 0:
		print('Password is incorrect!')
		times = times - 1
		if times > 0:
			print('You can try' , times, 'times.')
