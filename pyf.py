class StringTools:
    _string = ""

    def __init__(self, s):
        self.setString(s)

    def setString(self, s):
        self._string = s

    def get(self):
        return self._string

    def trim(self):
        self._string = self._string.strip()

    def stringRemoveLeft(self, n):
        self._string = self._string[n:]

    def countSting(self):
        return len(self._string)


