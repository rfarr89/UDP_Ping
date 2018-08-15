# UDPPingerClient.py
# Client program for UDP socket lab, COSC 4377 spring 2018, University of Houston
# Student: Ryan Farrell (1488274)

# import socket python module
import socket
# import datetime module
from datetime import datetime

# create the socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# set default timeout to 1.0 seconds
client.settimeout(1)
# send message to server 10 times
for i in range(1, 11):
    try:
        # try sending a ping
        # get current time
        SENT_TIME = datetime.now()
        # set message based on ping # and time
        MSG_SENT = 'ping {} {}'.format(i, str(SENT_TIME))
        # send message to the server
        client.sendto(MSG_SENT, ("127.0.0.1", 12000))
        # listen for a response
        MSG_REC, ADDRESS = client.recvfrom(1024)
        # calculate round trip time
        TRIP_TIME = datetime.now() - SENT_TIME
        # print response and reound trip time (assuming success)
        print('Message received: {}'.format(MSG_REC))
        print('PING {} RTT: {} seconds'.format(i, str(TRIP_TIME.total_seconds())))
    except socket.timeout:
        # if a timeout exception is encountered
        # print timeout message
        print("Request timed out.")
        # continue to next ping
        continue

# close socket
print("Closing socket.")
client.close()
