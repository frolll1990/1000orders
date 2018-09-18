import socket
HOST = str(input('Enter wik5 IP or for default press ENTER\nDefault 127.0.0.1  \n->'))
if HOST == '' :
    HOST = '127.0.0.1'

PORT = str(input('Enter wik5 port or for default press ENTER\nDefault = 12345 \n->'))
if PORT == '':
    PORT = int(12345)

login = str(input('enter login: \n->'))
symbol = str(input('enter SYMBOL: \n->'))
cmd = str(input('enter cmd: \n 0 = buy \n 1 = sell \n->'))
vol = int(float(input('enter NORMAL volume \n 10.1 losts = 10.1 : \n->'))* 10000)
query = "action=openorder&login="+ login +"&symbol=" + symbol + "&cmd=" + cmd + "&volume=" + str(vol)
print("\n", query, "\n")
start = str(input("Start spaming with query? Y/N \n"))
if start == "Y" or start == "y" or start == "":
    for a in range(1,1000):#если нужно другое кол-во ордеров, то измени второе число на нужное кол-во ордеров
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        print("sending: ", query, "\n")
        s.send(query.encode())
        while s.recv(1024) == True:
            print(s.recv(1024))

    s.close()

else:
    print("==O==K==A==Y==")

#while start == "Y" or start == "y" or start == "":
#    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#    s.connect((HOST, PORT))
#    print("sending: ", query, "\n")
#    s.send(query.encode())
#    while s.recv(1024) == True:
#        print(s.recv(1024))
#
#s.close()