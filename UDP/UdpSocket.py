import socket

Target_host = "127.0.0.1"
target_port = 9997

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #udp

#kirinm data
client.sendto(b"Halloo brokuuu",(Target_host, target_port))

#menerima data
data, addr = client.recvfrom(4096)
print("Pesan dari server: \"{}\"".format(data.decode()))

client.close()