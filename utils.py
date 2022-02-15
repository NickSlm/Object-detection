from matplotlib.font_manager import json_dump, json_load
import win32gui
import json

# List all running windows application titles
def winEnumHandler( hwnd, ctx ):
    if win32gui.IsWindowVisible( hwnd ):
        print(hex(hwnd), win32gui.GetWindowText( hwnd ))
        
# win32gui.EnumWindows( winEnumHandler, None )

def get_recipes():
    with open(r'D:\Find image on screen\data\recipes.json') as f:
        data = json.load(f)
    return data
