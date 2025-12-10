import customtkinter as CTK

# Configurações de Aparência
CTK.set_appearance_mode('dark')

# Criação da Janela Principal
App = CTK.CTk()
App.title('Sistema - Lista de Casamento')
App.geometry('320x550')

# Lista para armazenar Convidados
Lista_Familia = []

# Título
Label_Titulo_App = CTK.CTkLabel(App, text='Lista de Casamento')
Label_Titulo_App.pack(pady=10)



# Campos de Entrada
Campo_Ele = CTK.CTkEntry(App, placeholder_text = 'Digite o Nome do Convidado -> Ele:')
Campo_Ele.pack(pady=10)
    
Campo_Ela = CTK.CTkEntry(App, placeholder_text = 'Digite o Nome do Convidado -> Ela:')
Campo_Ela.pack(pady=10)

Campo_Filhos = CTK.CTkEntry(App, placeholder_text = 'Quant. Filhos:')
Campo_Filhos.pack(pady=10)

# Função de Cadastro
def Creat_Cad():
    Ele = Campo_Ele.get().strip()
    Ela = Campo_Ela.get().strip()
    Filhos_Inp = Campo_Filhos.get().strip()
    
    # Validação de Filhos
    try:
        Filhos_Int = int(Filhos_Inp) if Filhos_Inp else 0
        
        if Filhos_Int < 0:
            Label_Status.configure(text="❗ Filhos não pode ser negativo", text_color="red")
            return

    except ValueError:
        Label_Status.configure(text="Erro: Digite apenas números em Filhos", text_color="red")
        return
    
    # Validações de Nomes
    if not Ele and Ela:
        Label_Status.configure(text="❗ Preencha pelo menos um dos campos (Ele ou Ela)", text_color="yellow")
        return
    
    # Salvar na Lista
    Lista_Familia.append

# Opções do Menu
Botao_Cad = CTK.CTkButton(App, text='Cadastrar Convidados', command=Creat_Cad, text_color='blue')
Botao_Cad.pack(pady=10)

# Iniciar Aplicação
App.mainloop()