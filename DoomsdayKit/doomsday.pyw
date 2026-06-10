from tkinter import *
import tkinter as tk
from tkinter import ttk
from pdf2image import convert_from_path
from PIL import Image, ImageTk
import os
import colorsys

firePDFs = ["BuildAFire.pdf","FireStartingMethods.pdf"]
foodPDFs = ["AutumnBerries.pdf","mushrooms.pdf"]
shelterPDFs = ["knots.pdf","roofing.pdf"]
waterPDFs = ["WaterNice+Nasty.pdf","WaterSafety.pdf"]
medicalPDFs = ["WildFirstAid.pdf","GeneralMedicalInfo.pdf"]

#PDF_PATH = "/home/doomsday/Desktop/DoomsdayKit/BuildAFire.pdf"
PDF_PATH = 'pdfs/placeholderPDF.pdf'

sizes = ["1600x900","800x450","1024x600"]

root = tk.Tk()
root.geometry("1024x600")
root.resizable(False,False)
root.update()

widgetWidth = int(root.winfo_width()/50)
widgetHeight = int(root.winfo_height()/50)

homeWidgetWidth = int(root.winfo_width()/6)
homeWidgetHeight = int(root.winfo_height()/6)
homeTitleWidth = int(root.winfo_width()/2)
homeTitleHeight = int(root.winfo_height()/2)
#  #path is the rpi path
#survBtnImg = Image.open('/home/doomsday/Desktop/DoomsdayKit/imgs/survivalBtnImg.png').resize((homeWidgetWidth,homeWidgetWidth))
survBtnImg = Image.open('imgs/survivalBtnImg.png').resize((homeWidgetWidth,homeWidgetWidth))
survBtnImg = ImageTk.PhotoImage(survBtnImg)
#settingsBtnImg = Image.open('/home/doomsday/Desktop/DoomsdayKit/imgs/settingsBtnImg.png').resize((homeWidgetWidth,homeWidgetWidth))
settingsBtnImg = Image.open('imgs/settingsBtnImg.png').resize((homeWidgetWidth,homeWidgetWidth))
settingsBtnImg = ImageTk.PhotoImage(settingsBtnImg)
#exitBtnImg = Image.open('/home/doomsday/Desktop/DoomsdayKit/imgs/exitBtnImg.png').resize((homeWidgetWidth,homeWidgetWidth))
exitBtnImg = Image.open('imgs/exitBtnImg.png').resize((homeWidgetWidth,homeWidgetWidth))
exitBtnImg = ImageTk.PhotoImage(exitBtnImg)
#rainbowBtnImg = Image.open('/home/doomsday/Desktop/DoomsdayKit/imgs/rainbowBtnImg.png').resize((homeWidgetWidth,homeWidgetWidth))
rainbowBtnImg = Image.open('imgs/rainbowBtnImg.png').resize((homeWidgetWidth,homeWidgetWidth))
rainbowBtnImg = ImageTk.PhotoImage(rainbowBtnImg)
#doomsdayTitleImg = Image.open('/home/doomsday/Desktop/DoomsdayKit/imgs/doomsdayTitleImg.png').resize((homeTitleWidth,homeTitleHeight))
doomsdayTitleImg = Image.open('imgs/doomsdayTitleImg.png').resize((homeTitleWidth-int(homeTitleWidth/10),homeTitleHeight-int(homeTitleHeight/10)))
doomsdayTitleImg = ImageTk.PhotoImage(doomsdayTitleImg)

waterBtnImg = Image.open('imgs/waterBtnImg.png').resize((homeWidgetWidth,homeWidgetWidth))
waterBtnImg = ImageTk.PhotoImage(waterBtnImg)
shelterBtnImg = Image.open('imgs/shelterBtnImg.png').resize((homeWidgetWidth,homeWidgetWidth))
shelterBtnImg = ImageTk.PhotoImage(shelterBtnImg)
foodBtnImg = Image.open('imgs/foodBtnImg.png').resize((homeWidgetWidth,homeWidgetWidth))
foodBtnImg = ImageTk.PhotoImage(foodBtnImg)
medicalBtnImg = Image.open('imgs/medicalBtnImg.png').resize((homeWidgetWidth,homeWidgetWidth))
medicalBtnImg = ImageTk.PhotoImage(medicalBtnImg)
fireBtnImg = Image.open('imgs/fireBtnImg.png').resize((homeWidgetWidth,homeWidgetWidth))
fireBtnImg = ImageTk.PhotoImage(fireBtnImg)

enterBtnImg = Image.open('imgs/enterBtnImg.png').resize((homeWidgetWidth,homeWidgetWidth))
enterBtnImg = ImageTk.PhotoImage(enterBtnImg)


pageChoice = 0

def closeSystem():
    os._exit(1)
def clear():
    for widget in root.winfo_children():
        widget.destroy()


hue = 0

def rainbowRoom():
    clear()
    timeWasteLbl = tk.Label(root,text='Congrats You Just\nWasted Your Time!',font=('Helvetica',20),fg='#ffffff',bg='#272727').place(rely=0.3,relx=0.5,anchor='center')
    homeBtn = tk.Button(root,image=exitBtnImg,bd=0,bg='#272727',activebackground='#272727',command=homeBtnFunc).place(relx=0.5,rely=0.8,anchor='center')

def fireBtnFunc():
    global PDF_PATH
    tempList = []
    for x in range(len(firePDFs)):
        tempList.append('pdfs/fire/'+firePDFs[x])
    if PDF_PATH not in tempList:
        PDF_PATH = 'pdfs/placeholderPDF.pdf'
    del tempList
    pdfChoice = StringVar()
    clear()
    backBtn = tk.Button(root, image=exitBtnImg, bd=0,activebackground='#272727',background='#272727', command=survivalBtn).place(relx=0,rely=0,anchor='nw')
    topFillerLbl = tk.Label(root,text='\n',bg='#272727').pack()
    instructionLabel = tk.Label(root,text='Choose the desired PDF in the dropdown\nbelow and click the confirm button on the right once to continue',background='#272727',fg='#FFFFFF',font=('Helvetica', 16)).pack()
    pdfBtn = ttk.Combobox(root,textvariable=pdfChoice)
    pdfBtn['values'] = tuple(firePDFs)
    #pdfBtn.current(1)
    pdfBtn.pack()
    def selectPDFFunc():
        global PDF_PATH
        if str(pdfChoice.get()) not in firePDFs:
            pdfChoice.set("BuildAFire.pdf")
        try:
            pdf = pdfChoice.get()
        except:
            pass
        PDF_PATH = 'pdfs/fire/'+pdf
        del pdf
        clear()
        fireBtnFunc()
    selectPDF = tk.Button(root, image=enterBtnImg,command=selectPDFFunc,bg='#272727',activebackground='#272727',border=0).place(relx=1,rely=0,anchor='ne')

    fillerLbl = tk.Label(root, text='',font=('Arial',int(homeWidgetWidth-(homeWidgetWidth/1.5))),background='#272727').pack()
    displayPDF()

def foodBtnFunc():
    global PDF_PATH
    tempList = []
    for x in range(len(foodPDFs)):
        tempList.append('pdfs/food/'+foodPDFs[x])
    if PDF_PATH not in tempList:
        PDF_PATH = 'pdfs/placeholderPDF.pdf'
    del tempList
    pdfChoice = StringVar()
    clear()
    backBtn = tk.Button(root, image=exitBtnImg, bd=0,activebackground='#272727',background='#272727', command=survivalBtn).place(relx=0,rely=0,anchor='nw')
    topFillerLbl = tk.Label(root,text='\n',bg='#272727').pack()
    instructionLabel = tk.Label(root,text='Choose the desired PDF in the dropdown\nbelow and click the confirm button on the right once to continue',background='#272727',fg='#FFFFFF',font=('Helvetica', 16)).pack()
    pdfBtn = ttk.Combobox(root,textvariable=pdfChoice)
    pdfBtn['values'] = tuple(foodPDFs)
    #pdfBtn.current(1)
    pdfBtn.pack()
    def selectPDFFunc():
        global PDF_PATH
        if str(pdfChoice.get()) not in foodPDFs:
            pdfChoice.set("AutumnBerries.pdf")
        try:
            pdf = pdfChoice.get()
        except:
            pass
        PDF_PATH = 'pdfs/food/'+pdf
        del pdf
        clear()
        foodBtnFunc()
    selectPDF = tk.Button(root, image=enterBtnImg,command=selectPDFFunc,bg='#272727',activebackground='#272727',border=0).place(relx=1,rely=0,anchor='ne')

    fillerLbl = tk.Label(root, text='',font=('Arial',int(homeWidgetWidth-(homeWidgetWidth/1.5))),background='#272727').pack()
    displayPDF()

def shelterBtnFunc():
    global PDF_PATH
    tempList = []
    for x in range(len(shelterPDFs)):
        tempList.append('pdfs/shelter/'+shelterPDFs[x])
    if PDF_PATH not in tempList:
        PDF_PATH = 'pdfs/placeholderPDF.pdf'
    del tempList
    pdfChoice = StringVar()
    clear()
    backBtn = tk.Button(root, image=exitBtnImg, bd=0,activebackground='#272727',background='#272727', command=survivalBtn).place(relx=0,rely=0,anchor='nw')
    topFillerLbl = tk.Label(root,text='\n',bg='#272727').pack()
    instructionLabel = tk.Label(root,text='Choose the desired PDF in the dropdown\nbelow and click the confirm button on the right once to continue',background='#272727',fg='#FFFFFF',font=('Helvetica', 16)).pack()
    pdfBtn = ttk.Combobox(root,textvariable=pdfChoice)
    pdfBtn['values'] = tuple(shelterPDFs)
    #pdfBtn.current(1)
    pdfBtn.pack()
    def selectPDFFunc():
        global PDF_PATH
        if str(pdfChoice.get()) not in shelterPDFs:
            pdfChoice.set("knots.pdf")
        try:
            pdf = pdfChoice.get()
        except:
            pass
        PDF_PATH = 'pdfs/shelter/'+pdf
        del pdf
        clear()
        shelterBtnFunc()
    selectPDF = tk.Button(root, image=enterBtnImg,command=selectPDFFunc,bg='#272727',activebackground='#272727',border=0).place(relx=1,rely=0,anchor='ne')

    fillerLbl = tk.Label(root, text='',font=('Arial',int(homeWidgetWidth-(homeWidgetWidth/1.5))),background='#272727').pack()
    displayPDF()

def waterBtnFunc():
    global PDF_PATH
    tempList = []
    for x in range(len(waterPDFs)):
        tempList.append('pdfs/water/'+waterPDFs[x])
    if PDF_PATH not in tempList:
        PDF_PATH = 'pdfs/placeholderPDF.pdf'
    del tempList
    pdfChoice = StringVar()
    clear()
    backBtn = tk.Button(root, image=exitBtnImg, bd=0,activebackground='#272727',background='#272727', command=survivalBtn).place(relx=0,rely=0,anchor='nw')
    topFillerLbl = tk.Label(root,text='\n',bg='#272727').pack()
    instructionLabel = tk.Label(root,text='Choose the desired PDF in the dropdown\nbelow and click the confirm button on the right once to continue',background='#272727',fg='#FFFFFF',font=('Helvetica', 16)).pack()
    pdfBtn = ttk.Combobox(root,textvariable=pdfChoice)
    pdfBtn['values'] = tuple(waterPDFs)
    #pdfBtn.current(1)
    pdfBtn.pack()
    def selectPDFFunc():
        global PDF_PATH
        if str(pdfChoice.get()) not in waterPDFs:
            pdfChoice.set("WaterSafety.pdf")
        try:
            pdf = pdfChoice.get()
        except:
            pass
        PDF_PATH = 'pdfs/water/'+pdf
        del pdf
        clear()
        waterBtnFunc()
    selectPDF = tk.Button(root, image=enterBtnImg,command=selectPDFFunc,bg='#272727',activebackground='#272727',border=0).place(relx=1,rely=0,anchor='ne')

    fillerLbl = tk.Label(root, text='',font=('Arial',int(homeWidgetWidth-(homeWidgetWidth/1.5))),background='#272727').pack()
    displayPDF()

def medicalBtnFunc():
    global PDF_PATH
    tempList = []
    for x in range(len(medicalPDFs)):
        tempList.append('pdfs/medical/'+medicalPDFs[x])
    if PDF_PATH not in tempList:
        PDF_PATH = 'pdfs/placeholderPDF.pdf'
    del tempList
    pdfChoice = StringVar()
    clear()
    backBtn = tk.Button(root, image=exitBtnImg, bd=0,activebackground='#272727',background='#272727', command=survivalBtn).place(relx=0,rely=0,anchor='nw')
    topFillerLbl = tk.Label(root,text='\n',bg='#272727').pack()
    instructionLabel = tk.Label(root,text='Choose the desired PDF in the dropdown\nbelow and click the confirm button on the right once to continue',background='#272727',fg='#FFFFFF',font=('Helvetica', 16)).pack()
    pdfBtn = ttk.Combobox(root,textvariable=pdfChoice)
    pdfBtn['values'] = tuple(medicalPDFs)
    #pdfBtn.current(1)
    pdfBtn.pack()
    def selectPDFFunc():
        global PDF_PATH
        if str(pdfChoice.get()) not in medicalPDFs:
            pdfChoice.set("WildFirstAid.pdf")
        try:
            pdf = pdfChoice.get()
        except:
            pass
        PDF_PATH = 'pdfs/medical/'+pdf
        del pdf
        clear()
        medicalBtnFunc()
    selectPDF = tk.Button(root, image=enterBtnImg,command=selectPDFFunc,bg='#272727',activebackground='#272727',border=0).place(relx=1,rely=0,anchor='ne')

    fillerLbl = tk.Label(root, text='',font=('Arial',int(homeWidgetWidth-(homeWidgetWidth/1.5))),background='#272727').pack()
    displayPDF()

def survivalBtn():
    clear()
    fireBtn = tk.Button(root, image=fireBtnImg, bd=0,activebackground='#272727', command=fireBtnFunc)
    fireBtn.config(bg='#272727')
    fireBtn.place(x=0,y=0,anchor='nw')

    foodBtn = tk.Button(root, image=foodBtnImg, bd=0,activebackground='#272727',command=foodBtnFunc)
    foodBtn.config(bg='#272727')
    foodBtn.place(relx=0.5,y=0,anchor='n')

    medicalBtn = tk.Button(root, image=medicalBtnImg, bd=0,activebackground='#272727', command=medicalBtnFunc)
    medicalBtn.config(bg='#272727')
    medicalBtn.place(relx=1.0,y=0,anchor='ne')

    waterBtn = tk.Button(root, image=waterBtnImg, bd=0,activebackground='#272727', command=waterBtnFunc)
    waterBtn.config(bg='#272727')
    waterBtn.place(x=0, rely=1.0,anchor='sw')

    shelterBtn = tk.Button(root, image=shelterBtnImg, bd=0,activebackground='#272727', command=shelterBtnFunc)
    shelterBtn.config(bg='#272727')
    shelterBtn.place(relx=1.0, rely=1.0,anchor='se')

    homeBtn = tk.Button(root, image=exitBtnImg, bd=0,activebackground='#272727', command=homeBtnFunc)
    homeBtn.config(bg='#272727')
    homeBtn.place(relx=0.5,rely=1,anchor='s')


def displayPDF():

    #clear()
    #homeButton = tk.Button(root, text="Home", command=homeBtnFunc).pack()
    #btn_1 = tk.Button(root, text="Food").pack()
    #btn_2 = tk.Button(root, text="Shelter").pack()
    #btn_3 = tk.Button(root, text="Water").pack()
    #btn_4 = tk.Button(root, text="Medical").pack()
    
    pages = convert_from_path(PDF_PATH, dpi=150)
    
    canvas = tk.Canvas(root,background='#272727')
    
    
    scroll_y = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)

    frame = ttk.Frame(canvas)
    
    # put frame inside canvas
    canvas_frame = canvas.create_window((0, 0), window=frame, anchor="nw")

    # Source - https://stackoverflow.com/q/17355902

    for x in range(len(pages)):
        # convert PIL image → Tk image
        img = ImageTk.PhotoImage(pages[x].resize((int(root.winfo_height()*1.5),int(root.winfo_width()*1.5))))
        # display image in Tkinter
        label = ttk.Label(frame, image=img,anchor='center')
        label.image = img
        label.pack()


    # update scroll region
    def configure_frame(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame.bind("<Configure>", configure_frame)

    # configure canvas scrolling
    canvas.configure(yscrollcommand=scroll_y.set,background='#272727')

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
    global sizeChoice
    sizeChoice = StringVar()
    clear()
    
    def setSize():
        global sizeChoice
        if str(sizeChoice.get()) not in sizes:
            sizeChoice.set("1024x600")
        try:
            size = sizeChoice.get()
        except:
            pass
        root.geometry(str(size))
        del size
    
    infoLbl = tk.Label(root,text='The drop down below allows you to change the resolution of this program.\nThen press the button beneath to confirm.',bd=0,bg='#272727',font=('Helvetica',15),fg='#ffffff').pack(pady=20)
    sizeBtn = ttk.Combobox(root,textvariable=sizeChoice)
    sizeBtn['values'] = tuple(sizes)
    sizeBtn.current(1)
    sizeBtn.pack(pady=20)
    submitSize = tk.Button(root, image=enterBtnImg, command= setSize,bd=0,bg='#272727',activebackground='#272727').place(relx=0.85,rely=0.5,anchor='e')
    homeButton = tk.Button(root, image=exitBtnImg, command=homeBtnFunc,bd=0,bg='#272727',activebackground='#272727').place(relx=0.15,rely=0.5,anchor='w')
    

def homeBtnFunc():
    

    global survBtnImg,settingsBtnImg,exitBtnImg,rainbowBtnImg,doomsdayTitleImg

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
    doomsdayLbl = tk.Label(root,image=doomsdayTitleImg, bd=0,activebackground='#272727')
    doomsdayLbl.config(bg='#272727')
    doomsdayLbl.place(relx=0.5,rely=0.5,anchor=CENTER)
    

homeBtnFunc()

root.mainloop()
