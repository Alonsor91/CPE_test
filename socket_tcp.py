import socket

s_tcp = int(input("Start UDP port:")) #Start TCP dst port
e_tcp = int(input("End UDP port:")) #End TCP dst port
d_ip = input("Destenation IP:") #Destination IP address

for tcp in range(s_tcp,e_tcp):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect_ex((d_ip, tcp))
    print ("TCP, Dst Port: {} IPv4, Dst: {}".format(tcp,d_ip))

#Hello world!