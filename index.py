#Importar as bibliotecas
from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
import DataBaser



#Criar Nossa Janela
jan = Tk()
jan.title("EasyBeach - Painel de acesso")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 0.9)
jan.iconbitmap(default="icons/logoIcon.ico")
#--------------------------------------------Carregando Imagens-----------------
logo = PhotoImage(file="icons/logo.png")
#--------Widgets---------------------------------------------------------------
LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50, y=100)
#---------------------------------------------------------------------------------------------------------------------
UserLabel = Label(RightFrame, text='Usuário:', font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150, y=110)

#----------------------------------------------------------------------------------------------------------------------

SenhaLabel = UserLabel = Label(RightFrame, text="Senha:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
SenhaLabel.place(x=5, y=150)

SenhaEntry = ttk.Entry(RightFrame, width=30, show="*")
SenhaEntry.place(x=150, y=160)

def Login():
     Usuario =  UserEntry.get()
     Senha = SenhaEntry.get()

     DataBaser.cursor.execute("""
     SELECT * FROM Usuarios 
     WHERE (Usuario = ? AND Senha = ?)
     """, (Usuario, Senha))

     print("Selecionado")
     verifyLogin = DataBaser.cursor.fetchone()
     if (Usuario in verifyLogin and Senha in verifyLogin):
          messagebox.showinfo(title="Informações de Login", message="Acesso confirmado!")
     else:   
        messagebox.showinfo(title="Informações de Login", message="Acesso negado, verifique seu cadastro!")

#Botões
LoginButton = ttk.Button(RightFrame, text="Login", width=20, command="Login")
LoginButton.place(x=129, y=225)

def Registro():
    #Removendo os buttons da página 
    LoginButton.place(x=5000)
    RegistroButton.place(x=5000)
    #Inserindo Widgets de Cadastro
    NomeLabel = Label(RightFrame, text="Nome:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
    NomeLabel.place(x=5, y=5)

    NomeEntry = ttk.Entry(RightFrame, width=39)
    NomeEntry.place(x=101, y=16)

    EmailLabel = Label(RightFrame, text="Email:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
    EmailLabel.place(x=5, y=55)

    EmailEntry = ttk.Entry(RightFrame, width=39)
    EmailEntry.place(x=100, y=66)


    def RegistroDataBase():

        Nome =  NomeEntry.get()
        Email = EmailEntry.get()
        Usuario = UserEntry.get()
        Senha = SenhaEntry.get() 

        if (Nome == "" and Email == "" and Usuario == "" and Senha == ""):
             messagebox.showerror(title="Erro no Registro", message="Preencha os campos que faltam!")
        elif(Usuario == "" and Senha == ""):
             messagebox.showerror(title="Erro no Registro", message="Preencha os campos Usuário e Senha!")
        elif(Nome == "" and Email == ""):
             messagebox.showerror(title="Erro no Registro", message="Preencha os campos Nome e Email!")
        elif(Email == "" and Usuario == ""):
             messagebox.showerror(title="Erro no Registro", message="Preencha os campos Usuário e Email!")
        elif(Nome == "" and Senha == ""):
             messagebox.showerror(title="Erro no Registro", message="Preencha os campos Nome e Senha!")
        elif(Email == "" and Senha == ""):
             messagebox.showerror(title="Erro no Registro", message="Preencha os campos Email e Senha!")
        elif(Nome == "" and Usuario == ""):
             messagebox.showerror(title="Erro no Registro", message="Preencha os campos Usuário e Nome!")
        elif (Nome == ""):
             messagebox.showerror(title="Erro no Registro", message="Preencha o campo Nome!")
        elif (Email == ""):
             messagebox.showerror(title="Erro no Registro", message="Preencha o campo Email")
        elif (Usuario == ""):
             messagebox.showerror(title="Erro no Registro", message="Preencha o campo Usuário!")
        elif(Senha == ""):
             messagebox.showerror(title="Erro no Registro", message="Preencha o campo Senha!")
        else:
                DataBaser.cursor.execute("""
                INSERT INTO Usuarios(Nome, Email, Usuario, Senha) VALUES(?, ?, ?, ?)
                """,(Nome, Email, Usuario, Senha)) 

                DataBaser.conn.commit()
                messagebox.showinfo(title="Informações de Registro", message="Registrado com sucesso")


    Registro = ttk.Button(RightFrame, text="Registrar", width=20, command=RegistroDataBase)
    Registro.place(x=125, y=225)

    def BackToLogin():
    #Removendo Widgets de cadastro
          NomeLabel.place(x=5000)
          NomeEntry.place(x=5000)
          EmailLabel.place(x=5000)
          EmailEntry.place(x=5000)
          Registro.place(x=5000)
          Back.place(x=5000)
 #Trazendo de volta os idgets de login
    LoginButton.place(x=125)
    RegistroButton.place(x=125)



    Back = ttk.Button(RightFrame, text="Voltar", width=20, command=BackToLogin)
    Back.place(x=125, y=260)

RegistroButton = ttk.Button(RightFrame, text="Registrar", width=20, command=Registro)
RegistroButton.place(x=130, y=260)



jan.mainloop()