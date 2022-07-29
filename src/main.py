import tkinter
from windows.download import DownloadWindow
from utils.logger import Logger

logger = Logger()

window = tkinter.Tk()
DownloadWindow(window, logger)
window.mainloop()