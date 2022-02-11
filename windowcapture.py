import numpy
import win32gui
import win32ui
import win32con


class WindowCapture:
    def __init__(self) -> None:
        self.HEIGHT = 1024
        self.WIDTH = 1920
        self.hwnd = win32gui.FindWindow(None, "Path of Exile")    #TODO: CONFIRM THE WINDOW TITLE 
    def capture_screen(self):
        bmpfilenamename = "out.bmp"

        
        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj=win32ui.CreateDCFromHandle(wDC)
        cDC=dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.WIDTH, self.HEIGHT)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0,0),(self.WIDTH, self.HEIGHT) , dcObj, (0,0), win32con.SRCCOPY)
        dataBitMap.SaveBitmapFile(cDC, bmpfilenamename)

        singed_ints_array = dataBitMap.GetBitMapBits(True)
        img = numpy.fromstring(singed_ints_array, dtype='uint8')

        # Free Resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())
