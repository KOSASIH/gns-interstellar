import struct

def encode_message(message):
    """
    Encodes a message into a byte string.

    Parameters:
    message (str): The message to be encoded.

    Returns:
    bytes: The encoded message as a byte string.
    """
    message_bytes = message.encode()
    encoded_message = struct.pack('>I', len(message_bytes)) + message_bytes
    return encoded_message

def decode_message(encoded_message):
    """
    Decodes a byte string into a message.

    Parameters:
    encoded_message (bytes): The encoded message as a byte string.

    Returns:
    str: The decoded message.
    """
    message_length = struct.unpack('>I', encoded_message[:4])[0]
    message_bytes = encoded_message[4:4+message_length]
    message = message_bytes.decode()
    return message

def transmit_message(message, connection):
    """
    Transmits a message over a connection.

    Parameters:
    message (str): The message to be transmitted.
    connection: The connection over which the message will be transmitted.

    Returns:
    None
    """
    encoded_message = encode_message(message)
    connection.sendall(encoded_message)

def receive_message(connection):
    """
    Receives a message over a connection.

    Parameters:
    connection: The connection over which the message will be received.

    Returns:
    str: The received message.
    """
    encoded_message = connection.recv(4096)
    message = decode_message(encoded_message)
    return message
