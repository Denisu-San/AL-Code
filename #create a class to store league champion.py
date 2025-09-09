#create a class to store league champion abilities, into a python dictionary and store it in a json file
import json

class Champion():
    def __init__(self, Champ_Name, Q, W, E, R):
        self.__Champ_Name = Champ_Name
        self.__Q = Q
        self.__W = W
        self.__E = E
        self.__R = R
    
    def __str__(self):
        pass
    
    def GetUlt(self):
        return self.__R
    
    def GetQ(self):
        return self.__Q
    
    def GetW(self):
        return self.__W
    
    def GetE(self):
        return self.__E
    
    def to_dict(self):
        return {
            "Champion" : str(self.__Champ_Name),
            "Q": str(self.__Q),
            "W": str(self.__W),
            "E": str(self.__E),
            "R": str(self.__R)
        }


def LogChamp():
    
    log = Champion(
        input("Champ Name: "),
        input("Champ Q: "),
        input("Champ W: "),
        input("Champ E: "),
        input("Champ R: ")
    )
    
    
    
    champ_log = log.to_dict()

    try:
        with open("champ.txt", 'a') as f:
            f.write(json.dumps(champ_log) + "\n")
            
    except FileNotFoundError:
        return "Unable to find json file"
    except EOFError:
        return "Can't Read Beyond End of File"
    
    
    
LogChamp()