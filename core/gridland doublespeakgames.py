import time

import threading

from pynput.mouse import Button, Controller as mouse

from pynput.keyboard import Listener, KeyCode, Controller as keyboard


import pyautogui

import PIL

from PIL import ImageGrab

import os

import subprocess


delay = 2

button = Button.left

# start_stop_key = KeyCode(char='s')
start_stop_key = KeyCode(char='x')
run_key_program_two = KeyCode(char='q')

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
    def run_program_two(self):

        self.program_two([])

    def stop_clicking(self):

        self.running = False
        # mouse.release(self.button)

    def exit(self):

        self.stop_clicking()

        self.program_running = False

    def print_coord(self,coord):
        color = self.image.getpixel(coord)
        def rgb_to_hex(rgb):
            return '%02x%02x%02x' % rgb
        hexx = rgb_to_hex(color)
        comand="perl -e 'foreach $a(@ARGV){print \"\\e[48:2::\".join(\":\",unpack(\"C*\",pack(\"H*\",$a))).\"m \\e[49m \"};print \" \"'"
        comand+=f" \"{hexx}\""
        os.system(comand)
        print(color,end=' ')
        print(coord)
        time.sleep(0.05)

    def starting(self,params):
        self.primeiro_slot={
            'coords':{
                'superiores':[(504,264),(504,263),(504,262),(504,261)],
                'inferiores':[(504,307),(504,308),(504,309),(504,310)],
                'esquerdas':[(479,300),(480,300),(481,300),(482,300)],
                'direitas':[(525,300),(526,300),(527,300),(528,300)],
            }
        }
        self.slot={
            'deltas':{
                'x':self.primeiro_slot['coords']['direitas'][1][0]-self.primeiro_slot['coords']['esquerdas'][1][0],
                'y':self.primeiro_slot['coords']['inferiores'][1][1]-self.primeiro_slot['coords']['superiores'][1][1]
            },
            'bordas':{
                'x':531-self.primeiro_slot['coords']['direitas'][1][0],
                'y':313-self.primeiro_slot['coords']['inferiores'][1][1]
            },
            'colors':{
                'bordas':{
                    'esquerdas':[],
                    'direitas':[],
                    'superiores':[],
                    'inferiores':[]
                }
            },
            'coords':{
                'cantos':{
                    'esquerdos':{
                        'superior':(),
                        'inferior':()
                    },
                    'direitos':{
                        'superior':(),
                        'inferior':()
                    }
                }
            },
            'quantidades':{'x':8,'y':8}
        }
        self.espada={
            'deltas':{
                'x':512-self.primeiro_slot['coords']['esquerdas'][1][0],
                'y':282-self.primeiro_slot['coords']['superiores'][1][1]
            },
            'color':{
                'color':(54,54,54),
                'range':{
                    'min':40,
                    'max':65
                }
            }
        }
        self.espadas={
            'quantidades':0
        }
        self.slots=[]
        self.slots.append(self.primeiro_slot)
        for x in range(self.slot['quantidades']['x']):
            for y in range(self.slot['quantidades']['y']):
                aux={
                    'coords':{
                        'esquerdas':[],
                        'direitas':[],
                        'superiores':[],
                        'inferiores':[],
                    }
                }
                for __ in aux['coords']:
                    for _ in self.primeiro_slot['coords'][__]:
                        aux['coords'][__].append((\
                            _[0]+self.slot['deltas']['x']*x\
                            +self.slot['bordas']['x']*x,\
                            _[1]+self.slot['deltas']['y']*y\
                            +self.slot['bordas']['y']*y))
                self.slots.append(aux)

    def program_two(self,params):

        self.image = ImageGrab.grab()

        for x in range(self.slot['quantidades']['x']):
            for y in range(self.slot['quantidades']['y']):
                # print(_['coords'])
                aux=[None,None]
                aux[0]=self.slots[self.slot['quantidades']['y']*x+y]['coords']['esquerdas'][1][0]+self.espada['deltas']['x']
                aux[1]=self.slots[self.slot['quantidades']['y']*x+y]['coords']['superiores'][1][1]+self.espada['deltas']['y']
                coord=(aux[0],aux[1])
                # if self.image.getpixel(coord) == self.espada['color']:
                print(x,y)
                self.print_coord(coord)
                if self.image.getpixel(coord)[0]>self.espada['color']['range']['min'] and \
                    self.image.getpixel(coord)[1]<self.espada['color']['range']['max']:
                    self.espadas['quantidades']+=1
                    print('ok')

        print(self.espadas['quantidades'])


    def runing(self,params):
        # screenshot = pyautogui.screenshot()
        time.sleep(0.05)
        # print(pyautogui.position())

        # color = image.getpixel((x, y))

        self.image = ImageGrab.grab()
        coord=pyautogui.position()
        self.print_coord(coord)

        coords=[]
        for coord in coords:
            self.print_coord(coord)

        # width, height = self.image.size
        # for x in range(width):
        #     for y in range(height):
        #         coord=(x,y)
        #         if self.image.getpixel(coord) == None:
        #             pass
                # image.putpixel( (x,y), new_color)

    def run(self):

        self.randoms = 0

        print('starting program')
        self.starting([])

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

    if key == start_stop_key:

        if click_thread.running:

            click_thread.stop_clicking()
            # Controller().release(Button.left)
        else:

            click_thread.start_clicking()
            # Controller().press(Button.left)

    elif key == run_key_program_two:
        click_thread.run_program_two()
    elif key == exit_key:

        click_thread.exit()

        listener.stop()

with Listener(on_press=on_press) as listener:

    listener.join()