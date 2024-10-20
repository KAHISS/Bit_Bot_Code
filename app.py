from customtkinter import *
from bit_bot_code import BitBotCode
from tkinter import messagebox


class App:
    def __init__(self):
        self.root = CTk()
        self.root.title("Bit Bot Code")
        self.root.geometry("360x400")
        self.widgets()
        self.root.mainloop()

    def widgets(self):
        CTkLabel(self.root, text='Login', font=("Arial", 23)).place(x=155, y=10)
        self.inputEmail = CTkEntry(self.root, placeholder_text='Insira seu e-mail', width=160*2, height=40)
        self.inputEmail.place(x=20, y=50)
        self.inputPassword = CTkEntry(self.root, placeholder_text='Insira sua senha', width=160*2, height=40, show="*")
        self.inputPassword.place(x=20, y=110)
        CTkLabel(self.root, text="_"*25, font=("Arial", 23)).place(x=19, y=150)

        CTkLabel(self.root, text='Início', font=("Arial", 23)).place(x=155, y=185)
        self.inputInit = CTkEntry(self.root, placeholder_text='Insira o link de início', width=160*2, height=40)
        self.inputInit.place(x=20, y=220)
        CTkLabel(self.root, text='Fim', font=("Arial", 23)).place(x=165, y=265)
        self.inputEnd = CTkEntry(self.root, placeholder_text='Insira o link de início', width=160*2, height=40)
        self.inputEnd.place(x=20, y=300)
        CTkButton(self.root, width=320, height=40, command=self.initBot, text='Iniciar', font=('Arial', 21)).place(x=20, y=351)


    def initBot(self):
        if not "" in [self.inputEmail.get(), self.inputPassword.get(), self.inputInit.get(), self.inputEnd.get()]:
            bot = BitBotCode()
            bot.login(self.inputEmail.get(), self.inputPassword.get())
            bot.checkClass(self.inputInit.get(), self.inputEnd.get())
        else:
            messagebox.showerror("Error", "Preencha todos os campos")

if __name__ == "__main__":
    app = App()
