class Car:
    def __init__(self):
        self.acc = False
        self.clutch = False
        self.brk = False

    def start(self):
       self.clutch = True
       self.acc = True
    print("car started...")


    def stop(self):
       self.clutch = False
       self.acc = False
    print("car stopped...")

car1 =Car()
car1.start()
car1.stop()
