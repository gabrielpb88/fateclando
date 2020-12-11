import rsa
import socket
from threading import Thread

with open('private.pem', 'rb') as f:
    privateFile = f.read()
privateKey = rsa.PrivateKey.load_pkcs1(privateFile, format='PEM')

with open('public.pem', 'rb') as f:
  publicKey = f.read()

# Endereco IP do Servidor
HOST = '127.0.0.1'
PORT = 5000
tcpServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcpServidor.bind(orig)
tcpServidor.listen(1)
print('####### Servidor rodando #######')

# TODO: Coloque abaixo o endereco IP do Amigo
SERVER = '192.168.100.75'
dest = (SERVER, PORT)
tcpCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpCliente.connect(dest)

def conexao(con, cli):
    while True:
        msg = con.recv(1024)
        if not msg: break
        print('\n', cli, rsa.decrypt(msg, privateKey))
    print('Finalizando conexao do cliente', cli)
    con.close()

def cliente():
    msg = input('Enviar mensagem: ').encode('utf-8')
    pub = rsa.PublicKey.load_pkcs1(publicKey, format='PEM')
    while msg != '\x18':
        tcpCliente.send(rsa.encrypt(msg, pub))
        msg = input('Enviar mensagem: ').encode('utf-8')
    tcpCliente.close()

while True:
    con, ip = tcpServidor.accept()
    print('Conectado por ', ip)
    Thread(target=conexao, args=(con, ip)).start()
    Thread(target=cliente).start()
