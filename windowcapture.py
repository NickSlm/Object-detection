import numpy
import win32gui
import win32ui
import win32con


class WindowCapture:
    def __init__(self, window_name) -> None:

        self.HEIGHT = 1024
        self.WIDTH = 1920
        self.hwnd = win32gui.FindWindow(None, window_name)

    def capture_screen(self):

        # bmpfilenamename = "out.bmp"

        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj=win32ui.CreateDCFromHandle(wDC)
        cDC=dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.WIDTH, self.HEIGHT)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0,0),(self.WIDTH, self.HEIGHT) , dcObj, (0,0), win32con.SRCCOPY)

        # save screenshot
        # dataBitMap.SaveBitmapFile(cDC, bmpfilenamename)

        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = numpy.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (1024,1920,4)

        # Free Resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        return img

