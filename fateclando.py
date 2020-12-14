import rsa
import socket
from threading import Thread

with open('private.pem', 'rb') as f:
    privateFile = f.read()
pri = rsa.PrivateKey.load_pkcs1(privateFile, format='PEM')

with open('public.pem', 'rb') as f:
  publicKey = f.read()
pub = rsa.PublicKey.load_pkcs1(publicKey, format='PEM')
PORT = 20000

def conexao():
    tcpServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    orig = ('', PORT)
    tcpServidor.bind(orig)
    tcpServidor.listen(1)
    con, ip = tcpServidor.accept()
    print('####### Servidor rodando #######')

    while True:
        msg = con.recv(4096)
        if not msg: break
        print('\n', ip, rsa.decrypt(msg, pri))
    print('Finalizando conexao do cliente', ip)
    con.close()

def cliente():
    SERVER = input('Digite o IP do destinatario:')

    dest = (SERVER, PORT)
    tcpCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpCliente.connect(dest)

    msg = input('Enviar mensagem: ').encode('utf-8')
    while msg != '\x18':
        tcpCliente.send(rsa.encrypt(msg, pub))
        msg = input('Enviar mensagem: ').encode('utf-8')
    tcpCliente.close()


Thread(target=conexao).start()
Thread(target=cliente).start()
