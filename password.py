password = ('a123456')
times = int(3)
while times > 0:
	pwd = input('Please enter your password: ')
	if pwd == password:
		print('You are log in!')
		break # escape the loop
	else:
		print('Password is incorrect! You can try' , times, 'times.')
		times = times - 1