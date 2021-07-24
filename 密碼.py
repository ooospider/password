password = 'a123456'
x = 3
while x > 0 :
	x = x-1
	pwd = input ('請輸入您的密碼:')
	if pwd == password :
		print ('登入成功')
		break
	else :
		print ('密碼錯誤')
		if x > 0 :
			print ('還剩下',x,'次機會')
			     





			     