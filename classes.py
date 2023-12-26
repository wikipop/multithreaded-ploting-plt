class Packet:
    def __init__(self, data, origin):
        self.data = data
        self.origin = origin
        self.end_signal = False

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)