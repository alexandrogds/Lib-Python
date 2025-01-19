import time

import threading

from pynput.mouse import Button, Controller as mouse

from pynput.keyboard import Listener, KeyCode, Key, Controller as keyboard

delay = 2

button = Button.left

# start_stop_key = KeyCode(char='s')
start_stop_key = KeyCode(char='x')

exit_key = KeyCode(char='v')

class ClickMouse(threading.Thread):

    def __init__(self, delay, button):

        super(ClickMouse, self).__init__()

        self.delay = delay

        self.button = button

        self.running = False

        self.program_running = True

    def start_clicking(self):

        self.running = True
        # mouse.press(self.button)

    def stop_clicking(self):

        self.running = False
        # mouse.release(self.button)

    def exit(self):

        self.stop_clicking()

        self.program_running = False

    def runing(self,params):
                directions = [Key.space,'a','d','w','s']
                powerups=['1','2','3','4']

                keys = [Key.space,'a','d','w','s','1','2','3','4']


                # for _ in powerups:
                # for _ in [x for x in [z for z in [powerups,directions]]]:
                for _ in keys:
                    keyboard.press(_)
                    time.sleep(0.3)
                    keyboard.release(_)

    def run(self):

        self.randoms = 0

        print('starting program')

        while self.program_running:

            while self.running:
		
                self.runing([])

            time.sleep(0.1)

        print('totals random.randints generateds is',self.randoms)

mouse = mouse()
keyboard = keyboard()

click_thread = ClickMouse(delay, button)

click_thread.start()

def on_press(key):
    running = False

    if key == start_stop_key:

        if click_thread.running or running:

            click_thread.stop_clicking()
            running = False
            # Controller().release(Button.left)
        else:

            click_thread.start_clicking()
            running = True
            # Controller().press(Button.left)

    elif key == exit_key:

        click_thread.exit()

        listener.stop()

with Listener(on_press=on_press) as listener:

    listener.join()