# RTOS-Assignment-1

Server side: Compile the myserver.c using the command 'gcc -o server myserver.c' and then while executing use the command :
'./server port no.'.

Client Side: Compile the client with a similar command as above but with the client file and then execute with './client <username> port no.'.

Usage: 
While sending a text to other client use 'send' command followed by the client id as specified at the server & then type your message
in the following line.

For creating group use 'creategroup' and then pass the group name, no. of clients and their ids as arguments. Then use 'sendgroup' command followed
by the group id and then the message to be sent.

