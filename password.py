password = 'a123456'
x = 3
while True:
	pwd = input ('請輸入您的密碼:')
	if pwd == password :
		print ('登入成功')
		break
	else :
		x = x-1
		print ('還剩下',x,'次機會')
		if x == 0 :
			print ('登入失敗!')
			break
