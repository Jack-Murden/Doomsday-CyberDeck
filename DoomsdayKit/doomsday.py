from tkinter import *
import tkinter as tk
from tkinter import ttk
from pdf2image import convert_from_path
from PIL import Image, ImageTk
import os
import colorsys

PDFs = ["BuildAFire.pdf"]

#PDF_PATH = "/home/doomsday/Desktop/DoomsdayKit/BuildAFire.pdf"
PDF_PATH = PDFs[0]

root = tk.Tk()
root.geometry("800x450")
root.resizable(False,False)
root.update()

widgetWidth = int(root.winfo_width()/50)
widgetHeight = int(root.winfo_height()/50)

pageChoice = 0

homeWidgetWidth = int(root.winfo_width()/6)
homeWidgetHeight = int(root.winfo_height()/6)
homeTitleWidth = int(root.winfo_width()/2)
homeTitleHeight = int(root.winfo_height()/2)
#survBtnImg = Image.open('/home/doomsday/Desktop/DoomsdayKit/survivalBtnImg.png').resize((homeWidgetWidth,homeWidgetWidth))
survBtnImg = Image.open('survivalBtnImg.png').resize((homeWidgetWidth,homeWidgetWidth))
survBtnImg = ImageTk.PhotoImage(survBtnImg)
#settingsBtnImg = Image.open('/home/doomsday/Desktop/DoomsdayKit/settingsBtnImg.png').resize((homeWidgetWidth,homeWidgetWidth))
settingsBtnImg = Image.open('settingsBtnImg.png').resize((homeWidgetWidth,homeWidgetWidth))
settingsBtnImg = ImageTk.PhotoImage(settingsBtnImg)
#exitBtnImg = Image.open('/home/doomsday/Desktop/DoomsdayKit/exitBtnImg.png').resize((homeWidgetWidth,homeWidgetWidth))
exitBtnImg = Image.open('exitBtnImg.png').resize((homeWidgetWidth,homeWidgetWidth))
exitBtnImg = ImageTk.PhotoImage(exitBtnImg)
#rainbowBtnImg = Image.open('/home/doomsday/Desktop/DoomsdayKit/rainbowBtnImg.png').resize((homeWidgetWidth,homeWidgetWidth))
rainbowBtnImg = Image.open('rainbowBtnImg.png').resize((homeWidgetWidth,homeWidgetWidth))
rainbowBtnImg = ImageTk.PhotoImage(rainbowBtnImg)
#doomsdayTitleImg = Image.open('/home/doomsday/Desktop/DoomsdayKit/doomsdayTitleImg.png').resize((homeTitleWidth,homeTitleHeight))
doomsdayTitleImg = Image.open('doomsdayTitleImg.png').resize((homeTitleWidth,homeTitleHeight))
doomsdayTitleImg = ImageTk.PhotoImage(doomsdayTitleImg)


def closeSystem():
    os._exit(1)
def clear():
    for widget in root.winfo_children():
        widget.destroy()

hue = 0

def rainbowRoom():
    clear()
    homeButton = tk.Button(root, text="Home", command=homeBtn,bd=0).place(rely=0.85,relx=0.5,anchor=CENTER)
    
    def rgb_bg():
        global hue
        r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
        color = f'#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}'

        root.config(bg=color)

        hue += 0.002
        if hue >= 1:
            hue = 0

        root.after(10, rgb_bg)

    rgb_bg()


def survivalBtn():

    clear()
    homeButton = tk.Button(root, text="Home", command=homeBtn).pack()
    btn_1 = tk.Button(root, text="Food").pack()
    btn_2 = tk.Button(root, text="Shelter").pack()
    btn_3 = tk.Button(root, text="Water").pack()
    btn_4 = tk.Button(root, text="Medical").pack()

    pages = convert_from_path(PDF_PATH, dpi=150)
    
    canvas = tk.Canvas(root)
    
    scroll_y = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)

    frame = ttk.Frame(canvas)
    
    # put frame inside canvas
    canvas_frame = canvas.create_window((0, 0), window=frame, anchor="nw")

    
    for x in range(len(pages)):
        # convert PIL image → Tk image
        img = ImageTk.PhotoImage(pages[x])
        # display image in Tkinter
        label = ttk.Label(frame, image=img)
        label.image = img
        label.pack()


    # update scroll region
    def configure_frame(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame.bind("<Configure>", configure_frame)

    # configure canvas scrolling
    canvas.configure(yscrollcommand=scroll_y.set)

    canvas.pack(side="left", fill="both", expand=True)
    scroll_y.pack(side="right", fill="y")


def sizeChange(element):
    global widgetWidth, widgetHeight
    val = element.get()
    root.geometry(val)
    root.update()
    widgetWidth = int(root.winfo_width()/50)
    widgetHeight = int(root.winfo_height()/50)
    
def settingsBtn():
    sizeChoice = StringVar()
    clear()
    homeButton = tk.Button(root, text="Home", command=homeBtn).pack()
    sizeBtn = ttk.Combobox(root,textvariable=sizeChoice)
    sizeBtn['values'] = ('1600x900', '800x450', '400x225','1024x600')
    sizeBtn.current(1)
    sizeBtn.pack()
    submitSize = tk.Button(root, text="Apply Size", command= lambda: sizeChange(sizeBtn)).pack()
    

def homeBtn():
    clear()
    root.config(bg='#272727')
    root.update()
    #top left
    survBtn = tk.Button(root, image=survBtnImg, command=survivalBtn, bd=0,activebackground='#272727')
    survBtn.config(bg='#272727')
    survBtn.place(x=0,y=0,anchor='nw')

    #top right
    settingsBtn1 = tk.Button(root, text="Settings", command=settingsBtn, image=settingsBtnImg, bd=0,activebackground='#272727')
    settingsBtn1.config(bg='#272727')
    settingsBtn1.place(relx=1.0,y=0,anchor='ne')

    #bottom left
    rainbowBtn = tk.Button(root,text="Rainbow", command=rainbowRoom, image=rainbowBtnImg, bd=0,activebackground='#272727')
    rainbowBtn.config(bg='#272727')
    rainbowBtn.place(x=0, rely=1.0, anchor="sw")

    #bottom right
    exitBtn = tk.Button(root, text="Exit", command=closeSystem, image=exitBtnImg, bd=0,activebackground='#272727')
    exitBtn.config(bg='#272727')
    exitBtn.place(relx=1.0, rely=1.0, anchor="se")

    #dead center
    doomsdayLbl = tk.Label(root,image=doomsdayTitleImg,font=("Comic Sans MS", 30, "bold"), bd=0,fg='#782222',activebackground='#272727')
    doomsdayLbl.config(bg='#272727')
    doomsdayLbl.place(relx=0.5,rely=0.5,anchor=CENTER)
    

homeBtn()

root.mainloop()
