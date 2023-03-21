# Import required libraries
from tkinter import *
from PIL import ImageTk, Image
from tkinter.ttk import *
import time as t
from threading import *
from pymem import *
import multiprocessing
import os



minecraft = multiprocessing.Process()
mcchildprocesses = multiprocessing.active_children()



print('Starting...')
print('Tape v4 Client developed by Pythonify')
print('Ready to begin')

def pause(secs):
    init_time = time()
    while time() < init_time+secs: pass




# Create an instance of tkinter window
win = Tk()

# Define the geometry of the window
win.geometry("700x500")




frame = Frame(win, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)



win.title('Tape v4 Injector')





# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open('requiredfiles\\Tape v4.png'))

# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack()
  




# Progress bar widget
progress = Progressbar(frame, orient = HORIZONTAL,
              length = 450, mode = 'determinate')

def bar():
    progress['value'] += 1

def autoprogress():
    for e in range(100):
        bar()
        pause(0.1)
  
# Function responsible for the updation
# of the progress bar value




from time import time








from tkinter.messagebox import showinfo





progress.pack(pady = 10)

s = Style()
s.configure('mcfont', font=('minecraft'))

def optionsmenu():
    optionswindow = Tk()
    optionswindow.geometry('300x200')
    optionswindow.title('Options')
    minecraftfont = Style()
    minecraftfont.configure('minecraftfont', font=('minecraft'))
    optionstext = Label(optionswindow, text='Options', font=('minecraft', 25))
    optionstext.pack()
    def closewindow():
        optionswindow.destroy()
    closeoptionswindow = Button(optionswindow, text='Close', style='minecraftfont', command=closewindow)
    closeoptionswindow.pack(pady=10)
    c1 = Checkbutton(optionswindow, text='Verbose Mode',variable=toggle_verbose, onvalue='True', offvalue='False')
    c1.pack()



def verbosetext():
    t.sleep(1)
    print('''
SENT REACH !
SENT GUI !
SENT CLIENTCONNECT !
SENT AIMASSIST !
SENT SERVER !
SENT CLIENT !
SENT PYTHON !
SENT KEYBIND !
SENT KEYBINDS !
SENT KEYPROCESSOR !
SENT MINECRAFT !
Connecting to clients...
''')
    t.sleep(1)
    print('Connected to 1.7.10')
    t.sleep(0.3)
    print('Connected to 1.8.9')
    t.sleep(0.1)
    print('Connected to 1.12.2')
    print('Injecting...')



def operation():
    label.config(text='Initializing...')
    if progress['value'] <= 100:
        label.config(text='Initializing...')
        if toggle_verbose == 'True':
            verbosetext()
        else:
            pass
        for r in range(100):
            bar()
            progress.update()
            label.config(text='Injecting, ' + str(progress['value']) + '%')
            t.sleep(0.1)
        label.config(text='Done! You can now close this window.')
        progress.stop()
    else:
        pass

ismcrunning = 'true'

def check_minecraft():
    try:
        minecraftcheck = Pymem('javaw.exe')
        minecraftcheck
        ismcrunning = 'true'
        ismcrunning
    except:
        label.config(text='Minecraft must be running.')
        ismcrunning = 'false'

def inject_dlls():
    os.system('requiredfiles\\Injector.exe --process-name javaw.exe --inject NullDLL64.dll')

def injection():
        if ismcrunning == 'true':
            inject_dlls()
            operation()
        else:
            label.config(text='Minecraft must be running')



label = Label(frame, text = "Waiting to start", font = "Segoe")  
label.pack()
        
def closewindow():
    exit()

closebutton = Button(frame, text='Exit', command=closewindow)
closebutton.pack(pady=10)

toggle_verbose = 'False'




options = Button(frame, text='Options', command=optionsmenu)
options.pack()
            









  
# This button will initialize
# the progress bar
injectbutton = Button(frame, text = 'Inject', command = injection).pack(pady = 10)



















  
# infinite loop
mainloop()

frame.mainloop()

win.mainloop()
