from encodings import utf_8
import socket
import sys

HOST = '127.0.0.1'
PORT = 9999     

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#o cliente nao chama bind, por isso nao escolhe a porta
try:
    s.connect((HOST, PORT))
except Exception as e:
    print('erro de conexao ', e)
    sys.exit()

while True:
    try:
        line = input('digite o texto a ser transmitido: ')
        if not line:
            print('linha vazia encerra o programa')
            break
    except:
        print('programa abortado com ctrl + c')
        break

    # data = bytes(line, 'utf-8')
    data = line.encode() # coloca automaticamente em utf8 pelo editor de texto
    try:
        tam = s.send(data)
        print(f'enviei {tam} bytes')
        print(data)
    except Exception as e:
        print('erro de conexao com o servidor: ', e)
        break