import socket as s
from sys import argv

if len(argv) != 2:
    print "Usage: python bot.py LOGFILE"
    exit()
    
irc = s.socket(s.AF_INET,s.SOCK_STREAM)
irc.connect(("irc.freenode.org",6667))
irc.send("PASS password\r\n")
irc.send("NICK TheSilentSpectat\r\n")
irc.send("USER TheSilentSpectat 8 password : LoggingBot\r\n")
irc.send("JOIN #ieee-UNIX\r\n")
irc.setblocking(False)
log = open(argv[1],"a")
#print "Entering loop" Debugging
while True:
    try:
        text = irc.recv(1024)
        if text != "":
            #print text Debugging only
            log.write(text)
    
        if text.find('PING') != -1:
            irc.send('PONG '+ text.split()[1]+'\r\n')
            #print 'PONG '+ text.split()[1]+'\r\n' Debugging
    except Exception as e:
        continue
