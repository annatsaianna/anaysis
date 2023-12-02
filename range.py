range(5)#[0, 1, 2, 3, 4]清單產生器
import random

for i in range(5):#重覆產生次數
	r = random.randint(1,1000)
	print('這是第', i+1, '次產生隨機數:', r)