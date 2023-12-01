from tkinter import *
from tkinter import ttk
from tkinter import font
from PIL import ImageTk





def goBack():
    processFrame.grid_forget()
    processFrame.pack_forget()
    menuFrame.grid(row=0,column=0,columnspan=1, **gridDict)
    menuFrame.pack_propagate(0)

def calculRedirect():
    calculButton.configure(text='Canvas Calcul (WIP)',state=DISABLED)
def processRedirect():
    processFrame.grid(row=0,column=0,columnspan=1, **gridDict)
    processFrame.pack_propagate(0)
    menuFrame.grid_forget()
    menuFrame.pack_forget()


if __name__ == "__main__":
    global main
    main = Tk()
    main.title('Rec Room Printer')

    main.geometry("360x400")
    main.resizable(False, False)

    style = ttk.Style()
    style.theme_use('clam')

    main.iconbitmap('source/logo.ico')

    gridDict = {"sticky": "nswe", "padx":0, "pady":0}

    police_personnalisee = font.Font(family="Helvetica", size=9)

    # Créer un style pour les boutons ttk
    style = ttk.Style()
    style.configure('Custom.TButton', font=police_personnalisee)

    # 1 = True
    debugMode=0
    if debugMode == 1:
        debugBorder = {"borderwidth":1, "relief": "solid"}
    else:
        debugBorder = {}


    class menu:
        global menuFrame
        menuFrame = Frame(main,width=350,height=185, **debugBorder)
        menuFrame.grid(row=0,column=0,columnspan=1, **gridDict)
        menuFrame.pack_propagate(0)

        menuFrame.grid_rowconfigure(0, weight=2, minsize=19)
        menuFrame.grid_rowconfigure(1, weight=1, minsize=315)
        menuFrame.grid_rowconfigure(2, weight=0)
        menuFrame.grid_columnconfigure(0, weight=1)

        class header:
            topImageFrame = Frame(menuFrame,width=350, **debugBorder)
            topImageFrame.grid(row=0,column=0,columnspan=1, **gridDict)

            topImageImg = ImageTk.PhotoImage(file="source/header.png")

            item = Canvas(topImageFrame, height=54, width=350, **debugBorder)
            item.grid(row=0,column=0, **gridDict)
            item.create_image(5,5,anchor='nw', image=topImageImg)


        class buttons:
            buttonsFrame = Frame(menuFrame, height=54,width=350, **debugBorder)
            buttonsFrame.grid(row=1,column=0,columnspan=1, **gridDict)
            buttonsFrame.pack_propagate(0)

            global calculButton
            calculButton = ttk.Button(buttonsFrame, text="Canvas Calcul", takefocus=False, command=calculRedirect, width=20,style='Custom.TButton')
            calculButton.configure(state=NORMAL)
            calculButton.pack(pady=(95,10))

            processButton = ttk.Button(buttonsFrame, text="Print Process", takefocus=False, command=processRedirect, width=20,style='Custom.TButton')
            processButton.configure(state=NORMAL)
            processButton.pack(pady=10)


        class footer:
            footerFrame = Frame(menuFrame, height=30,width=350, **debugBorder)
            footerFrame.grid(row=2,column=0,columnspan=1, **gridDict)
            footerFrame.pack_propagate(0)

            creditText = Label(footerFrame,text="Made by James",font=("Helvetica", 10))
            creditText.pack()
    
    class printProcess:
        global processFrame
        processFrame = Frame(main,width=360,height=185, **debugBorder)

        processFrame.grid_rowconfigure(0, weight=0, minsize=50)
        processFrame.grid_rowconfigure(1, weight=1, minsize=290)
        processFrame.grid_rowconfigure(2, weight=2, minsize=60)
        processFrame.grid_columnconfigure(0, weight=1)
        processFrame.grid_columnconfigure(1, weight=1)

        class title:
            titleFrame = Frame(processFrame,width=360, **debugBorder)
            titleFrame.grid(row=0,column=0,columnspan=2,**gridDict)
            titleFrame.pack_propagate(0)

            goBackButton = ttk.Button(titleFrame,text="Go back",takefocus=False,command=goBack)
            goBackButton.grid(row=0,column=0,pady=10,padx=(10,5))

            titleText = Label(titleFrame,text="Print Process",**debugBorder)
            titleText.grid(row=0,column=1,pady=10,padx=5)

        class parameters:
            parametersFrame = Frame(processFrame,width=360, **debugBorder)
            parametersFrame.grid(row=1,column=0,columnspan=2, **gridDict)
            parametersFrame.grid_propagate(0)

        class generateButton:
            generateFrame = Frame(processFrame,width=360, **debugBorder)
            generateFrame.grid(row=2,column=0,columnspan=2, **gridDict)
            generateFrame.pack_propagate(0)



    main.mainloop()