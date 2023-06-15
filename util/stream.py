from abc import ABC, abstractmethod


class Stream(ABC):
    @abstractmethod
    def receive(self):
        raise NotImplementedError

    @abstractmethod
    def send(self, data):
        raise NotImplementedError

    @abstractmethod
    def close(self):
        raise NotImplementedError


class SocketStream(Stream):
    def __init__(self, sock):
        self.sock = sock

    def receive(self):
        return self.sock

    def send(self, data):
        print("Send socket stream")

    def close(self):
        print("Closing socket stream")


s = SocketStream(10)


def send_request(stream, request):
    if not isinstance(stream, Stream):
        raise TypeError('Expected Stream')
    stream.send(request)
    return stream.receive()


send_request(s, "T")
