class Balloon:
    def __init__(self, defenseItem, color):
        self.__defenseItem = defenseItem
        self.__color = color
        self.__health = 100
        
    def GetDefenseItem(self):
        print(self.__defenseItem)
        return self.__defenseItem
    
    def ChangeHealth(self, health):
        self.__health = self.__health + health
        
    def CheckHealth(self):
        if self.__health <= 0:
            return True
        else:
            return False
    pass








defenseItem = input("Defensee Item: ")
color = input("Color: ")
Balloon1 = Balloon(defenseItem, color)
Balloon1.GetDefenseItem()


