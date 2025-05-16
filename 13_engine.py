class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine started with {self.horsepower} horsepower.")

    def stop(self):
        print("Engine has stopped.")

class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine

    def start_car(self):
        print(f"starting {self.make} {self.model}")
        self.engine.start()

    def stop(self):
        print(f"stopping {self.make} {self.model}")
        self.engine.stop()

engine = Engine(660)
car = Car("Suzuki", "Alto", engine)

car.start_car()
car.stop()