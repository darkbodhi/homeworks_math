class Btree:

    def __init__(self):
        self._data = None
        self._ls = None
        self._rs = None

    def isempty(self):
        return self._data == None and self._ls == None and self._rs == None

    def maketree(self, data, t1, t2):
        self._data = data
        self._ls = t1
        self._rs = t2

    def root(self):
        if self.isempty():
            print('root: Дерево порожнє')
        exit(1)
        return self._data

    def leftson(self):

        if self.isempty():
            t = self._data
        else:
            t = self._ls
        return t

    def rightson(self):

        if self.isempty():
            t = self._data
        else:
            t = self._rs
        return t

    def updateroot(self, data):

        if self.isempty():
            self._ls = Btree()
            self._rs = Btree()

    def updateleft(self, t):
        self._ls = t

    def updateright(self, t):
        self._rs = t

    def search_data(self):
        search_for = input("Insert the data you want to search for: ")
        if search_for in self._data:
            print(search_for, "Інформація знаходиться в корені дерева.")
        elif search_for in self._ls:
            print(search_for, "Інформація знаходиться в лівому сині.")
        elif search_for in self._rs:
            print(search_for, "Інформація знаходиться в правому сині.")
        else:
            print("Помилка. Інформація не знайдена.")