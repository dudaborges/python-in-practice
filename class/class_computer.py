class Computer():
    #construtor
    def __init__(self, name):
        self.name = name
        self.sales = 0

    def sold(self, sales):
        self.sales = sales

    def goal(self, goal):
        if self.sales > goal:
            print(self.name, 'bateu a meta')
        else:
            print(self.name, 'não bateu a meta')