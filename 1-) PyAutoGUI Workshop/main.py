import pyautogui as pg

def what_do_we_got_here():
    # 1-) What do we got here ?

    """
    The PyAtuGUI module has the following functions and attributes:

    Exceptions : FailSafeException, ImageNotFoundException, PyAutoGUIException, useImageNotFoundException
    Fields : DARWIN_CATCH_UP_TIME, FAILSAFE, FAILSAFE_POINTS

    Prims : LEFT, MIDDLE, RIGHT

    Snakes : KEYBOARD_KEYS, MINIMUM_DURATION, MINIMUM_SLEEP, PAUSE

    BithParams : logScreenshot=True, interval ....

    The Rest :
    'Size', 'Window', 'alert', 'center', 'click', 'collections', 'collectionsSequence', 'confirm', 'contextmanager', 
    'countdown', 'datetime', 'displayMousePosition', 'division', 'doubleClick', 'drag', 'dragRel', 'dragTo', 'easeInBack', 'easeInBounce', 
    'easeInCirc', 'easeInCubic', 'easeInElastic', 'easeInExpo', 'easeInOutBack', 'easeInOutBounce', 'easeInOutCirc', 'easeInOutCubic', 
    'easeInOutElastic', 'easeInOutExpo', 'easeInOutQuad', 'easeInOutQuart', 'easeInOutQuint', 'easeInOutSine', 'easeInQuad', 'easeInQuart', 
    'easeInQuint', 'easeInSine', 'easeOutBack', 'easeOutBounce', 'easeOutCirc', 'easeOutCubic', 'easeOutElastic', 'easeOutExpo', 'easeOutQuad', 
    'easeOutQuart', 'easeOutQuint', 'easeOutSine', 'failSafeCheck', 'functools', 'getActiveWindow', 'getActiveWindowTitle', 'getAllTitles', 
    'getAllWindows', 'getInfo', 'getPointOnLine', 'getWindowsAt', 'getWindowsWithTitle', 'grab', 'hold', 'hotkey', 'hscroll', 'isShiftCharacter', 
    'isValidKey', 'keyDown', 'keyUp', 'leftClick', 'linear', 'locate', 'locateAll', 'locateAllOnScreen', 'locateCenterOnScreen', 'locateOnScreen', 
    'locateOnWindow', 'middleClick', 'mouseDown', 'mouseInfo', 'mouseUp', 'mouseinfo', 'move', 'moveRel', 'moveTo', 'onScreen', 'os', 'password', 
    'pixel', 'pixelMatchesColor', 'platform', 'platformModule', 'position', 'press', 'printInfo', 'print_function', 'prompt', 'pyscreeze',
    'rightClick', 'run', 'screenshot', 'scroll', 'size', 'sleep', 'sys', 'time', 'tripleClick', 'typewrite',, 'vscroll', 'write'
    """

    print(dir(pg))

def lets_roll_into_screen():
    # 2-) Let's roll into screen !

    """
    Some of the most used "screen" tools of the PyAutoGUI module:

    size() # returns the screen size
    position() # returns the mouse position
    onScreen(x, y) # returns True if the coordinates are within the !primary! screen
    
    
    """

    width, height = pg.size() # tuple conversion

    print(width, height)
    print(pg.size())
    print(*pg.size())
    print(pg.position())
    print(*pg.position())
    print(pg.onScreen(0, 92))

def lets_roll_into_mouse():
    # 3-) Let's roll into mouse !

    def example():
        import time
        # show, FAILSAFE here !
        #pg.FAILSAFE = False
        distance = 200
        t = 0.5
        time.sleep(5)
        while distance > 0:
            pg.drag(distance, 0, duration=t)   # move right
            distance -= 5
            pg.drag(0, distance, duration=t)   # move down
            pg.drag(-distance, 0, duration=t)  # move left
            distance -= 5
            pg.drag(0, -distance, duration=t)  # move up

    """
    Some of the most used "mouse" tools of the PyAutoGUI module:

    moveTo(x, y, duration) # moves the mouse to the given coordinates
    moveRel(x, y, duration) # moves the mouse to the given coordinates relative to the current position
    
    click(x, y, clicks, interval, button) # clicks the mouse at the given coordinates
    
    dragTo(x, y, duration, button) # drags the mouse to the given coordinates
    dragRel(x, y, duration, button) # drags the mouse to the given coordinates relative to the current position
    
    scroll(amount) # scrolls the mouse wheel
    """

    pg.moveTo(100, 100, duration=1)
    pg.moveRel(100, 100, duration=1)
    
    pg.click(500, 100, clicks=2, interval=1, button='left')

    pg.dragTo(100, 100, duration=1, button='left')
    pg.dragRel(100, 100, duration=1, button='left')
    
    pg.scroll(100)

    #example()

def lets_roll_into_keyboard():
    # 4-) Let's roll into keyboard !

    import pyperclip as pc # will use this module to copy and paste, sometimes pyautogui doesn't work properly with special characters, ie: ç,ğ,ü,ö,ş,ı

    """
    Some of the most used "keyboard" tools of the PyAutoGUI module:

    press(key, presses, interval, pause, _pause) # presses the given key
    keyDown(key, pause, _pause) # presses the given key
    keyUp(key, pause, _pause) # releases the given key
    
    hotkey(key1, key2, key3, ...) # presses and releases the given keys

    with hold(key1): # holding

    typeWrite(message, interval, pause, _pause) # types the given message

    """

    #pg.press('a', presses=20, interval=0)
    
    #pg.keyDown('a')
    #pg.keyUp('a')

    #pg.press(["ctrl", "v"]) # ["ctrl", "v"] == "ctrl" + "v" not "ctrlv"
    
    #pg.hotkey('ctrl', 'v')

    #pg.hotkey('ctrl', 'shift', 'esc')
    #pg.keyDown('ctrl')
    #pg.keyDown('shift')
    #pg.keyDown('esc')
    #pg.keyUp('esc')
    #pg.keyUp('shift')
    #pg.keyUp('ctrl')

    """with pg.hold("ctrl"):
        with pg.hold("shift"):
            pg.press("p")

    pg.typewrite("Reload Window", interval=0)

    pg.press("enter")"""

    pc.copy("iŞçÇüĞÜöÖşŞıİ")
    pg.typewrite(pc.paste(), interval=0) # not working properly
    pg.hotkey("ctrl", "v") # working properly
             
def lets_roll_into_messages():
    # 5-) Let's roll into messages !

    """
    Some of the most used "messages" tools of the PyAutoGUI module:

    alert(text, title, button) # displays an alert message
    confirm(text, title, buttons) # displays a confirmation message
    prompt(text, title, default) # displays a prompt message
    password(text, title, default, mask) # displays a password message
    """

    outputs = [
        pg.alert("Hello World !", "Alert", "OK"),
        pg.confirm("Hello World !", "Confirm", ["OK", "Cancel"]),
        pg.prompt("Hello World !", "Prompt", "Default"),
        pg.password("Hello World !", "Password", "Default", "*")
    ]
    print(outputs)

def lets_roll_into_images():
    # 6-) Let's roll into images !

    """
    Some of the most used "images" tools of the PyAutoGUI module:

    locateOnScreen(image, region, grayscale, confidence) # returns the coordinates of the given image on the screen
    locateCenterOnScreen(image, region, grayscale, confidence) # returns the coordinates of the center of the given image on the screen
    locateAllOnScreen(image, region, grayscale, confidence) # returns the coordinates of all the given image on the screen
    locateOnWindow(image, window, region, grayscale, confidence) # returns the coordinates of the given image on the given window
    """

    # we only care locateCenterOnScreen() for now !, first method gives upper corner, third one gives all occurences and the last one is built in.

    img_path = "test.png"

    location = None
    while location == None:
        location = pg.locateCenterOnScreen(img_path, grayscale=False, confidence=0.6)
    
    pg.click(location)

if __name__ == "__main__":
    
    what_do_we_got_here()
    #lets_roll_into_screen()
    #lets_roll_into_mouse()
    #lets_roll_into_keyboard()
    #lets_roll_into_messages()
    #lets_roll_into_images()