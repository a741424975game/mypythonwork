import sys,time,os


import test1



print('back run')

try:
	if os.path.exists('lock.txt'):
		os.remove('lock.txt')
	global x
	x = open('lock.txt', 'w')
	print(x)
	x.write('test')
	
	output = sys.stdout = open('log.txt', 'a')
	
except:
	print ('dup run ,  exit')
	g = open('dup.txt', 'a')
	g.write('dup run ,  exit \n')
	sys.exit()
try:
	if __name__ == "__main__":
		while True:
			time.sleep(10)
			output.flush()
except Exception as e:
	x.close()
	os.remove('lock.txt')