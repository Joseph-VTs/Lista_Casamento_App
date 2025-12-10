"""
    Config.py
"""
Reset = '\033[0m'
Black = '\033[1;30m'
Red = '\033[1;31m'
Green = '\033[1;32m'
Yellow = '\033[1;33m'
Ciano = '\033[1;36m'
White = '\033[1;37m'

import os
def Limpar_Terminal():
    while True:
        Resposta = input(f"❗ Aperte {Yellow}ENTER{Reset} para Continuar...")
        
        if Resposta == '':
            break
        else:
            print(f"❗ Apenas aperte {Yellow}ENTER{Reset}... 🙃")
            
    os.system('cls' if  os.name == 'nt' else 'clear')



"""
    Validacoes.py
"""
def Ent_Nomes(Act = "Vazio" ,Sexo = 'Vazio'):
    while True:
        Entrada = input(f"{Act} o Nome do Convidado -> {Sexo}: ").title().strip()
        
        # -1 -> Encerra
        if Entrada.strip() == "-1":
            return "-1"
        
        # Enter salva como Vazio
        if Entrada.strip() == "":
            return ""
        
        # Nome not Número
        if Entrada.isdigit():
            print(f"{Yellow}Nome não pode ser Números. Verifique... 🙃{Reset}")
            continue
        
        if not Entrada.replace(" ", "").isalpha():
            print(f"{Yellow}Nome deve conter apenas letras. Verifique... 🙃{Reset}")
            continue
        
        # Tamanho do Nome == 3 letras
        if len(Entrada.strip()) < 3:
            print(f"{Yellow}Nome está muito pequeno. Verifique... 🙃{Reset}")
            continue
            
        # if passou nas validações -> Retorna    
        return Entrada.strip()



"""
    CRUD.py
"""
Lista_Familia = []

# Função principal -> Salvar Convidados
def Def_Init(Ele: str, Ela: str, Filhos: int):
    
    Next_Index = len(Lista_Familia)
    
    Dic_Familia = {
        "Ele": Ele,
        "Ela": Ela,
        "Filhos": Filhos
    }
    
    Set_Familia = {
        'Index': Next_Index,
        'Familia': Dic_Familia
    }
    
    Lista_Familia.append(Set_Familia)

# Criando novos Convidados
def Creat_Cad():
    while True:
        Limpar_Terminal()
        print("-1 para retornar ao Menu")
        
        # Campo Ele
        while True:
            Ele = Ent_Nomes("Digite", "Ele").strip()
            if Ele == "-1":
                print("Saindo...")
                return
            if Ele == "" or Ele:
                break
            print("❗ Erro (Campo Ele), Verifique... 🙃")
        
        # Campo Ela
        while True:
            Ela = Ent_Nomes("Digite", "Ela").strip()
            if Ela == "-1":
                print("Saindo...")
                return
            if Ela == "" or Ela:
                break
            print("❗ Erro (Campo Ela), Verifique... 🙃")
        
        # Pelo menos um campo precisa estar preenchido
        if not Ele.strip() and not Ela.strip():
            print("❗ Pelo menos um dos campos deve ser preenchido.")
            continue
        
        # Campo Filhos
        while True:
            Filhos = input("Quant. Filhos: ").strip()
            if Filhos == "-1":
                print("Saindo...")
                return
            try:
                Filhos = int(Filhos)
                if Filhos < 0:
                    print("❗ Filhos não podem ser Negativos. Verifique... 🙃")
                    continue
                break  # válido
            except ValueError:
                print("Erro (Filhos) -> Digite apenas números inteiros")
                continue
        
        # Salva na lista
        Def_Init(Ele, Ela, Filhos)
        print(f"{Green}✅ Convidado salvo com sucesso!{Reset}")
        print(f"{Black}-{Reset}" * 71)
        
        # Mostra o último cadastrado
        Item = Lista_Familia[-1]
        Index = Item['Index']
        Ele_1 = Item['Familia']['Ele']
        Ela_1 = Item['Familia']['Ela']
        Filhos_1 = Item['Familia']['Filhos']

        print(
            f"{Ciano}|{Reset} {Index:<7}",
            f"{Ciano}|{Reset} {Ele_1:<17}",
            f"{Ciano}|{Reset} {Ela_1:<17}",
            f"{Ciano}|{Reset} {Filhos_1:<7}"
        )
        print(f"{Black}-{Reset}" * 71)



def Read_Convidados():
    while True:
        Limpar_Terminal()
        print(f"{Ciano}-{Reset}" * 71)
        print(
            f"{Ciano}|{Reset} {'Index':<7}",
            f"{Ciano}|{Reset} {'Eles':<17}",
            f"{Ciano}|{Reset} {'Elas':<17}",
            f"{Ciano}|{Reset} {'Filhos':<7}"
        )
        print(f"{Ciano}-{Reset}" * 71)
        
        # Criar variaveis, para conjuntos. Totais finais
        Total_Filhos = 0
        Total_Casais = 0
        Total_Convidados = 0
        
        for Item in Lista_Familia:
            
            Interno_1 = Item['Index'] # Ops 1
            Index = Interno_1
            Ele = Item['Familia']['Ele'] # Ops 2
            Ela = Item['Familia']['Ela']
            Filhos = Item['Familia']['Filhos']
            
            print(
                f"{Ciano}|{Reset} {Index:<7}",
                f"{Ciano}|{Reset} {Ele:<17}",
                f"{Ciano}|{Reset} {Ela:<17}",
                f"{Ciano}|{Reset} {Filhos:<7}"
            )
            print(f"{Black}-{Reset}" * 71)
            
            Total_Filhos += Filhos
            
            # Vazio += 0
            if Ele.strip():
                Total_Convidados += 1
                
            if Ela.strip():
                Total_Convidados += 1
                
            if Ele.strip() and Ela.strip():
                Total_Casais += 1
            
        # Totais Finais
        print(
            "\n\nTotais dos Convidados",
            f"\nTotal de Filhos: {Total_Filhos}",
            f"\nTotal de Casais: {Total_Casais}",
            f"\nTotal de Adultos: {Total_Convidados}",
            f"\nTotal Final dos Convidados: {Total_Convidados + Total_Filhos}"
        )
        print(f"{Black}-{Reset}" * 71)
        
        try:
            Exit = int(input("Digite (-1) para voltar ao Menu Principal: "))
            if Exit == -1:
                break
            else:
                print("Para sair, Digite (-1)")
        except ValueError:
            print("❗ Erro (Lista), Opção Inválida")
            continue

# Editar Convidados
def Update():
    while True:
        Limpar_Terminal()
        print("Edição por Index - ID")
        print("digitar (ENTER mantém o valor antigo).")
        print("Digite (-1) para voltar ao Menu Principal")
        print(f"{Black}-{Reset}" * 71)
        
        # Validação se Lista está vazia ou possui itens
        if len(Lista_Familia) == 0:
            print("Lista está Vazia...")
            break
        
        # Buscar por Index
        try:
            Edit = int(input("Digite o Index: "))
            if Edit == -1:
                break

        except ValueError:
            print("❗ Erro (Update), Opção Inválida")
            continue
        
        # if Index for maior ou menor que a lista == Inválido
        if Edit < 0 or Edit >= len(Lista_Familia):
            print("❗ Index Inválido...")
            continue
        
        Item = Lista_Familia[Edit]
        Index = Item['Index']
        Ele_Atual = Item['Familia']['Ele']
        Ela_Atual = Item['Familia']['Ela']
        Filhos_Atual = Item['Familia']['Filhos']
        
        print(f"{Black}-{Reset}" * 71)
        print(
            f"{Ciano}|{Reset} {'Index':<7}",
            f"{Ciano}|{Reset} {'Ele':<17}",
            f"{Ciano}|{Reset} {'Ela':<17}",
            f"{Ciano}|{Reset} {'Filhos':<7}"
        )
        
        print(f"{Black}-{Reset}" * 71)
        print(
            f"{Ciano}|{Reset} {Index:<7}",
            f"{Ciano}|{Reset} {Ele_Atual:<17}",
            f"{Ciano}|{Reset} {Ela_Atual:<17}",
            f"{Ciano}|{Reset} {Filhos_Atual:<7}"
        )
        print(f"{Black}-{Reset}" * 71)
        
        # Atualizando nomes
        Ele = Ent_Nomes("Atualizar", "Ele")
        if Ele == "-1":
            return
        
        Ela = Ent_Nomes("Atualizar", "Ela")
        if Ela == "-1":
            return
        
        try:
            Filhos = input("Nova quantidade de Filhos (ENTER mantém): ")
            Filhos = int(Filhos) if Filhos.strip() else Filhos_Atual
            
            if Filhos < 0:
                print(f"{Yellow}❗ Filhos não podem ser Negativos. Mantendo valor antigo.{Reset}")
                Filhos = Filhos_Atual

        except ValueError:
            print(f"{Yellow}❗ Entrada inválida para Filhos, manteremos o valor atual.{Reset}")
            Filhos = Filhos_Atual
        
        # if for == Vazio, mantém o valor
        if Ele.strip():
            Item['Familia']['Ele'] = Ele
            
        if Ela.strip():        
            Item['Familia']['Ela'] = Ela
            
        Item['Familia']['Filhos'] = Filhos
        
        print(f"{Black}-{Reset}" * 71)
        print(f"{Green}✅ Convidado atualizado com sucesso!{Reset}")
        print(
            f"{Ciano}|{Reset} {Index:<7}",
            f"{Ciano}|{Reset} {Item['Familia']['Ele']:<17}",
            f"{Ciano}|{Reset} {Item['Familia']['Ela']:<17}",
            f"{Ciano}|{Reset} {Item['Familia']['Filhos']:<7}"
        )
        print(f"{Black}-{Reset}" * 71)



"""
    Iniciar.py
"""
def Iniciar():
    while True:
        Limpar_Terminal()
        print("App Lista de Casamentos | v1.0")
        print(f"{Black}-{Reset}" * 71)
        print(f"| {Ciano}7{Reset} - Editar")
        print(f"| {Ciano}8{Reset} - Lista")
        print(f"| {Ciano}9{Reset} - Cadastrar")
        print(f"| {Ciano}0{Reset} - Sair")
        print(f"{Black}-{Reset}" * 71)
        
        try:
            OPS = int(input("💢 Digite uma Opção: "))
        except ValueError:
            print("❗ Erro (Menu), Opção Inválida")
            continue
        
        match OPS:
            case 0: print("Saindo..."); break
            
            case 7: Update()
            # case 8: print("Lista de Convidados")
            case 8: Read_Convidados()
            # case 9: print("Cadastrar")
            case 9: Creat_Cad()
            
            case _: print("❗ Opção Inválida")

if __name__ == '__main__':
    Iniciar()