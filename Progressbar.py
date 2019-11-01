import sys

class Progressbar:
    minimum = 0
    maximum = 100

    def __init__(self, minimum=0, maximum=100):
        self.minimum = minimum
        self.maximum = maximum

    def print(self, value, length=50):
        bar = "|"
        percent = value / (self.maximum - self.minimum)
        numberOfFullChars = int(length * percent)
        for i in range(0, numberOfFullChars + 1, 1):
            bar += '\u2588'

        for i in range(0, length - numberOfFullChars, 1):
            bar += '-'

        bar += '|'
        sys.stdout.write('\r' + bar)
        sys.stdout.flush()
