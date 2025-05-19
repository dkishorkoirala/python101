class Car:
    def __init__(self, speed):
        self.__speed = speed
    
    def get_speed(self):
        return self.__speed
    
    def set_speed(self, set_speed):
        if set_speed > 0 :
            self.__speed = set_speed
        else:
            print("Speed must be greater than 0")
    
    def show_speed(self):
        print("The car speed is: ", self.__speed)

s1 = Car(40)
s1.show_speed()

print(s1.get_speed())
s1.set_speed(60)
print(s1.get_speed())

s1.set_speed(-5)

