try:
    import tkinter
    import pySmartDL
    import psutil
except ImportError as e:
    print("Can't import library " + str(e.name) + ", try \"pip install -r ../gui-requirements.txt\" and retry")
    exit(1)

from windows.download import DownloadWindow
from utils.logger import Logger

if __name__ == "__main__":
    logger = Logger()
    
    window = tkinter.Tk()
    DownloadWindow(window, logger)
    window.mainloop()