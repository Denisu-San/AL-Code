class Vehicle:
    def __init__(self, ID, XCoord, YCoord):
        self.__ID = ID
        self.__XCoord = XCoord
        self.__YCoord = YCoord
        

    def GetXCoord(self):
        return self.__XCoord
    def GetYCoord(self):
        return self.__YCoord
    
    def UpdateXCoord(self, x):
        if (x + self.__XCoord) <= 10000:
            self.__XCoord += x
        elif (x + self.__XCoord) < 0:
            self.__XCoord = 0
        elif (x + self.__XCoord) > 10000:
            self.__XCoord = 10000
        # print(self.__XCoord)
        return self.__XCoord
    
    def UpdateYCoord(self, y):
        if 0 < (y + self.__YCoord) <= 10000:
            self.__YCoord += y
        elif (y + self.__YCoord) < 0:
            self.__YCoord = 0
        else:
            self.__YCoord = 10000
        # print(self.__YCoord)
        return self.__YCoord

    # switch case for when direction is north etc.
    def Navigate(self, dir):
        match dir:
            case "north":
                self.UpdateYCoord(10)
            case "south":
                self.UpdateYCoord(-10)
            case "east":
                self.UpdateXCoord(10)
            case "west":
                self.UpdateXCoord(-10)

Rover = Vehicle("Rover", 50, 50)
# dragoncar = Vehicle("Dragon", 23, 22320)
# dragoncar.UpdateXCoord(122)



class SportsVehicle(Vehicle):
    def __init__(self, ID, XCoord, YCoord):
        super().__init__(ID, XCoord, YCoord)
        
    def Navigate(self, dir):
        match dir:
            case "north":
                self.UpdateYCoord(20)
            case "south":
                self.UpdateYCoord(-20)
            case "east":
                self.UpdateXCoord(20)
            case "west":
                self.UpdateXCoord(-20)
    
Viper = SportsVehicle("Viper", 100, 50)






Choice = input("Rover or Viper: ").lower()
Direction = input("Direction to move: ").lower()
if Choice == ("rover"):
    Rover.Navigate(Direction)
    print(f"Vehicle's new position is X = {Rover.GetXCoord()} & Y = {Rover.GetYCoord()}")
elif Choice == ("viper"):
    Viper.Navigate(Direction)
    print(f"Vehicle's new position is X = {Viper.GetXCoord()} & Y = {Viper.GetYCoord()}")
else:
    print("You need to select a vehicle")


