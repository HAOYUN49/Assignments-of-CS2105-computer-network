from socket import *
import sys
import pickle
import base64
from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto import Random
from AESCipher import AESCipher

recvName = 'localhost'
recvPort = int(sys.argv[1])

with open("bob-python.pub", "r") as f:
  public_key = RSA.importKey(f.read())

sendSocket = socket(AF_INET, SOCK_STREAM)
sendSocket.connect((recvName, recvPort))

rsa = PKCS1_OAEP.new(public_key)
key = Random.get_random_bytes(32)
cipherKey = rsa.encrypt(key)
sendSocket.send(pickle.dumps(cipherKey))

cipher = AESCipher(key)

with open("msgs.txt", "w+") as new_f:
  recvtext = sendSocket.recv(2048)
  while len(recvtext):
    ciphertext = pickle.loads(recvtext)
    text = cipher.decrypt(ciphertext)
    new_f.write(text.decode())
    recvtext = sendSocket.recv(2048)


sendSocket.close()
