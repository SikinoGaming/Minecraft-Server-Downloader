from datetime import datetime

class Logger:

    def __init__(self):
        self.start_date = datetime.now()
        self.log_file = "MSD_" + str(self.start_date.year) + "-" + str(self.start_date.day) + "-" + str(self.start_date.month) + "_" + str(self.start_date.hour) + ":" + str(self.start_date.minute) + ":" + str(self.start_date.second) + ".log"
        with open(self.log_file, "w+") as log_file: log_file.close()


    def log(self, window_name, msg):
        current_date = datetime.now()
        msg = "[" + str(current_date.month) + "/" + str(current_date.day) + "/"  + str(current_date.year) + "-" + str(current_date.hour) + ":" + str(current_date.minute) + ":" + str(current_date.second) + "." + str(current_date.microsecond) + "]" + "[" + window_name + "] " + str(msg)
        
        with open(self.log_file, "w+") as log_file:
            log_file.write(msg + "\n")
            log_file.close()
        
        print(msg)
