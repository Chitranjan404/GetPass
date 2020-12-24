import os
import getpass

a2=getpass.getuser()
a1='c:\\Users\\'
a3='\\Desktop\\'
a=a1+a2+a3
os.chdir('/tmp')
for i in range(1,21):
	f=str(i)
	os.mkdir(f)
	

