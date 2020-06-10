class Car():
    def __init__(self,name, model, make):
        self.name=name
        self.model=model
        self.make=make
    def Start(self):
        print("Car",self.name,self.model,self.make, "Start")
    def Stop(self):
        print("Car",self.name,self.model,self.make, "Stop")

T = Car("Tesla","Model3","Germany")
T.Start()
T.Stop()
