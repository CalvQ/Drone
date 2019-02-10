import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
# substitute the TCP port you want to listen on for 10000 below
server_address = ('192.168.137.1', 2399)

print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)
print("o1")
# Listen for incoming connections
sock.listen(1)
print("oi")
while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()

    try:
        print >>sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print >>sys.stderr, 'received "%s"' % data
            if data:
                print >>sys.stderr, 'Data received - starting other Python script'
                #<insert Python code to start other Python script>
            else:
                print >>sys.stderr, 'no more data from', client_address
                break

    finally:
        # Clean up the connection
        connection.close()
