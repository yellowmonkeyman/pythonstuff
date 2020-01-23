import keyboard 

running = True

while (running == True):  
    try:
        if keyboard.is_pressed('up'): 
            print('You Pressed Walked North!')
            running = False
        elif keyboard.is_pressed('down'): 
            print('You Pressed Walked South!')
            running = False
        elif keyboard.is_pressed('left'): 
            print('You Pressed Walked West!')
            running = False 
        elif keyboard.is_pressed('right'): 
            print('You Pressed Walked East!')
            running = False
        elif keyboard.is_pressed('a'): 
            print('You Pressed A!')
            running = False
    except:
        break