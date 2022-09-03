from datetime import datetime
import os

class Logger:

    def __init__(self):
        self.start_date = datetime.now()
        # Check if log folder exists
        if not os.path.exists("../logs"):
            os.makedirs("../logs")
            print("Created 'log' folder because it didn't exist")
        self.log_file = "../logs/MSD_" + str(self.start_date.year) + "-" + str(self.start_date.day) + "-" + str(self.start_date.month) + "_" + str(self.start_date.hour) + "h" + str(self.start_date.minute) + "m" + str(self.start_date.second) + "s.log"
        with open(self.log_file, "w+") as log_file: log_file.close()


    def log(self, window_name:str, msg:str):
        current_date = datetime.now()
        msg = "[" + str(current_date.month) + "/" + str(current_date.day) + "/"  + str(current_date.year) + "-" + str(current_date.hour) + ":" + str(current_date.minute) + ":" + str(current_date.second) + "." + str(current_date.microsecond) + "]" + "[" + window_name + "] " + str(msg)
        
        with open(self.log_file, "a") as file:
            file.write(msg + "\n")
            file.close()
        
        print(msg)
