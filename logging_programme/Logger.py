from datetime import datetime
import json

class Log():
    def __init__(self, Name, TimeIn, TimeOut, Date):
        self.__Name = Name
        self.__TimeIn = TimeIn
        self.__TimeOut = TimeOut
        self.__Date = Date
    def __str__(self):
        return f"{self.__Name} | {self.__Date} | {self.__TimeIn} - {self.__TimeOut} | {self.__Duration}"
    
    def GetName(self):
        return self.__Name
    
    def GetTimeServed(self):
        fmt = '%H:%M'
        tdelta = datetime.strptime(self.__TimeOut, fmt) - datetime.strptime(self.__Time, fmt)
        return tdelta
        
    def to_dict(self):
        return {
            "Name": self.__Name,
            "Date": self.__Date,
            "TimeIn": self.__TimeIn,
            "TimeOut": self.__TimeOut,
            "Duration": str(self.__Duration)
        }
    



#----MAIN PROGRAM----

log = input("Enter log details (Name, TimeIn, TimeOut, Date) separated by commas: ")
log_data = log.to_dict()
with open("logs.txt", "a") as f:
    f.write(json.dumps(log_data) + "\n")


