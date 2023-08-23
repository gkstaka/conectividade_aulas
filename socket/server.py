import socket as socket
import sys
HOST = '127.0.0.1'
PORT = 9999

# PORT = int(input('Porta do servidor: '))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((HOST,PORT))

except:
    print('erro de bind')
    sys.exit()

s.listen(5) # backlog numero de conexoes pendentes



while True:
    print(f'aguardando conexoes em: {PORT}')
    conn, addr = s.accept()
    print(f'recebi uma conexao de {addr}')  

    while True:
        try:
            data = conn.recv(1024)
            print(f'recebi {len(data)} bytes')

            if not data:
                print('o cliente encerrou a conexao')
                break
        
            print(data)

        except Exception as e:
            print('o cliente encerrou: ', e)
            break
    print('a conexao foi encerrada')
    conn.close()