class Car:
    def __init__(self, speed, maker, model, color, price):
        self.speed = speed
        self.maker = maker
        self.model = model
        self.color = color
        self.price = price
    def setSpeed(self, speed):
        self.speed = speed
    def setMaker(self, maker):
        self.maker = maker
    def getMaker(self):
        return self.maker
    def getDesc(self):
        return "\n속도 =" + str(self.speed) + \
               "\n메이커 =" + self.maker + \
               "\n모델 =" + self.model + \
               "\n색 =" + self.color + \
               "\n가격 =" + str(self.price)

class SportsCar(Car):
    def __init__(self, speed, maker, model, color, price, turbo):
        super().__init__(speed, maker, model, color, price)
        self.turbo = turbo
    def setTurbo(self, turbo):
        self.turbo = turbo

class Truck(Car):
    def __init__(self, speed, maker, model, color, price, payload):
        super().__init__(speed, maker, model, color, price)
        self.payload = payload
    def setPayload(self, payload):
        self.payload = payload
    def getPayload(self):
        return "탑재량 =" + str(self.payload)

class Bus(Car):
    def __init__(self, speed, maker, model, color, price, num_of_seats):
        super().__init__(speed, maker, model, color, price)
        self.num_of_seats = num_of_seats
    def set_num_of_seats(self, num_of_seats):
        self.num_of_seats = num_of_seats
    def get_num_of_seats(self):
        return "탑승객수 =" + str(self.num_of_seats)

truck = Truck(100, "kia", "봉고3", "하얀색", 20000000, 10)
bus = Bus(150, "hyundai", "슈퍼에어로시티", "파란색", 15000000, 24)
print(truck.getDesc())
print(truck.getPayload())
print(bus.getDesc())
print(bus.get_num_of_seats())

