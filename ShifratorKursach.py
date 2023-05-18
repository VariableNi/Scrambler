from customtkinter import *
import customtkinter as CTk
from tkinter import *
from PIL import Image, ImageTk

mainFrame = CTk.CTk()
mainFrame.title("Scrambler")
mainFrame.geometry("800x600")
CTk.set_appearance_mode("dark")

shifr = ['0000', '0001', '0011', '0201', '1012', '2003', '4020', '3022', '1115', '2115', '3016', 
         '5114', '3333', '4117', '4514', '5550', '2257', '9224', '6336', '8722', '5555', '7077', 
         '5665', '7772', '6666', '7765', '8855', '9990', '7777']

alphabet = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
                 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', ',']

ShifrWord = ""
deShifrWord = ""

def ShifFrame():

    shifButton.place(relx=100, rely=100)
    deShifButton.place(relx=100, rely=100)
    Word.place(relx=0.5, rely=0.5, anchor=CENTER)
    encryptButton.place(relx=0.5, rely=0.6, anchor=CENTER)
    trashButton.place(relx=0.61, rely=0.5, anchor=CENTER)
    BackButton.place(relx=0.09, rely=0.04, anchor=CENTER)

def deShifFrame():

    shifButton.place(relx=100, rely=100)
    deShifButton.place(relx=100, rely=100)
    Word.place(relx=0.5, rely=0.5, anchor=CENTER)
    deEncryptButton.place(relx=0.5, rely=0.6, anchor=CENTER)
    trashButton.place(relx=0.61, rely=0.5, anchor=CENTER)
    BackButton.place(relx=0.09, rely=0.04, anchor=CENTER)

def Encrypt():
    WordOfUser = Word.get().lower()
    global ShifrWord

    for i in range(0, len(WordOfUser)):
        for j in range(0, len(alphabet)):

            if WordOfUser[i] == alphabet[j]:
                ShifrWord = ShifrWord + shifr[j]

    LabelShifrWord.insert(END, ShifrWord)
    LabelShifrWord.place(relx=0.5, rely=0.2, anchor=CENTER)
    ShifrWord = ""

def deEncrypt():
    WordOfUser = Word.get()
    WordOfUser = list(WordOfUser)
    global deShifrWord
    findSymbol = ""
    findSymbolInt = 0


    if len(WordOfUser) == 4:
        findSymbolInt = int(WordOfUser[0]) + int(WordOfUser[1]) + int(WordOfUser[2]) + int(WordOfUser[3])
        LabelShifrWord.insert(END, alphabet[findSymbolInt])
        LabelShifrWord.place(relx=0.5, rely=0.2, anchor=CENTER)
        deShifrWord = ""
        findSymbolInt = 0
        findSymbol = ""


    elif len(WordOfUser) >= 8:

        for i in range(0, len(WordOfUser)):
            findSymbolInt = findSymbolInt + int(WordOfUser[i])
            findSymbol = findSymbol + WordOfUser[i]

            if len(findSymbol) == 4:

                for j in range(0, len(shifr)):
                    if findSymbol == shifr[j]:
                        deShifrWord = deShifrWord + alphabet[j]
                        findSymbol = ""

        LabelShifrWord.insert(END, deShifrWord)
        LabelShifrWord.place(relx=0.5, rely=0.2, anchor=CENTER)
        deShifrWord = ""
        findSymbolInt = 0
        findSymbol = ""

    else:
        LabelShifrWord.insert(END, "Text size < 4 or size not % 2")
        LabelShifrWord.place(relx=0.5, rely=0.2, anchor=CENTER)
        deShifrWord = ""
        findSymbolInt = 0
        findSymbol = ""

def Back():

    shifButton.place(relx=0.4, rely=0.5, anchor=CENTER)
    deShifButton.place(relx=0.6, rely=0.5, anchor=CENTER)
    Word.place(relx=100, rely=0.5, anchor=CENTER)
    encryptButton.place(relx=100, rely=0.6, anchor=CENTER)
    deEncryptButton.place(relx=100, rely=100, anchor=CENTER)
    trashButton.place(relx=100, rely=100, anchor=CENTER)
    BackButton.place(relx=100, rely=100, anchor=CENTER)
    LabelShifrWord.place(relx=100, rely=100)
    Word.delete(0, END)
    LabelShifrWord.delete(1.0, END)

def Trash():

    Word.delete(0, END)
    LabelShifrWord.delete(1.0, END)

shifButton = CTkButton(master=mainFrame, text="Scrambler", text_color="white", command=ShifFrame)
deShifButton = CTkButton(master=mainFrame, text="Decoder", text_color="white", command=deShifFrame)
Word = CTkEntry(master=mainFrame, text_color="white")
encryptButton = CTkButton(master=mainFrame, text="Encrypt", text_color="white", command=Encrypt)
deEncryptButton = CTkButton(master=mainFrame, text="DeEncrypt", text_color="white", command=deEncrypt)
trashButton = CTkButton(master=mainFrame, text="⌫", width=20, height=20, bg_color="#242422", fg_color="#242422", command=Trash)
BackButton = CTkButton(master=mainFrame, text="Back", text_color="white", command=Back)
LabelShifrWord = CTkTextbox(master=mainFrame, text_color="white", width=500, height=200)

shifButton.place(relx=0.4, rely=0.5, anchor=CENTER)
deShifButton.place(relx=0.6, rely=0.5, anchor=CENTER)

mainFrame.mainloop()