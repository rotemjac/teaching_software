
1. Please see this reference for understaning of the process of client-server sockets
https://realpython.com/python-sockets/

2. You can see that we uses encode() and decode() methods. This is because
   if you don't do it - you'll get: TypeError: a bytes-like object is required, not 'str'


with lsof -i:8080 you will see the socket connection:

COMMAND   PID  USER   FD   TYPE  DEVICE SIZE/OFF NODE NAME
python3 14773 rotem    3u  IPv4 5775803      0t0  TCP *:http-alt (LISTEN)
python3 14773 rotem    4u  IPv4 5775804      0t0  TCP localhost:53946->localhost:http-alt (ESTABLISHED)
python3 14773 rotem    5u  IPv4 5776520      0t0  TCP localhost:http-alt->localhost:53946 (ESTABLISHED)