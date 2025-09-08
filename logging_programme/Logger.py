from datetime import datetime, timedelta
import json

class Log():
    def __init__(self, Name, TimeIn, TimeOut, DateIn, DateOut):
        self.__Name = str(Name)
        self.__TimeIn = TimeIn
        self.__TimeOut = TimeOut
        self.__DateIn = DateIn
        self.__DateOut = DateOut
        
    def __str__(self):
        return f"{self.__Name} | {self.__DateIn} | {self.__DateOut} | {self.__TimeOut} - {self.__TimeIn}"
    
    def GetName(self):
        return self.__Name
    
    def GetTimeServed(self):
        fmt = '%d/%m/%Y %H:%M'
        tdelta = datetime.strptime(self.__DateOut +' '+ self.__TimeOut, fmt) - datetime.strptime(self.__DateIn +' '+ self.__TimeIn, fmt)
        return tdelta
    
    def to_dict(self):
        return {
            "Name": str(self.__Name),
            "DateIn": self.__DateIn,
            "DateOut": self.__DateOut,
            "TimeIn": self.__TimeIn,
            "TimeOut": self.__TimeOut,
            "Duration": str(self.GetTimeServed())
        }



#----MAIN PROGRAM----
def run_logger():
    print("-----LOGGER PROGRAM-----")
    print("Enter the following details:")
    
    log = Log(
        input("Enter Name: "),
        input("Enter Time In (HH:MM): "),
        input("Enter Time Out (HH:MM): "),
        input("Enter DateIn (dd/mm/yyyy): "),
        input("Enter DateOut (dd/mm/yyyy): ")
    )
    print("----------------------------------------")
    
    
#--------OUTPUT--------

    print(f"Hours served by {log.GetName()}: {log.GetTimeServed()}")
    log_data = log.to_dict()
    
    
#---------CHECKER/OVERWRITE--------
    try:
        with open("logs.txt", "r") as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                existing_log = json.loads(line)
                if existing_log["Name"] == log_data["Name"] and existing_log["DateIn"] == log_data["DateIn"]:
                    print(f"Log entry for {log_data['Name']} on {log_data['DateIn']} already exists. Overwriting...")
                    lines[i] = json.dumps(log_data) + "\n"
                    with open("logs.txt", "w") as fw:
                        fw.writelines(lines)
                    break
            else:
                raise FileNotFoundError  # Trigger append if no match found
    except (FileNotFoundError, json.JSONDecodeError):
        pass
#--------WRITE TO FILE--------
    
    try:
        with open("logs.txt", "a") as f:
            f.write(json.dumps(log_data) + "\n")
    
    except FileNotFoundError:
        print("File logs.txt not found.")
    except PermissionError:
        print("Cannot read logs.txt: permission denied.")
    except IOError:
        print("Error reading logs.txt.")

run_logger()
