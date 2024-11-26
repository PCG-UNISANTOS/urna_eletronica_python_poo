import tkinter as tk
import tkinter as tk
from tkinter import messagebox
import pickle
from common import Eleitor, Candidato

FILE_ELEITORES = 'eleitores.pkl'
FILE_CANDIDATOS = 'candidatos.pkl'
FILE_VOTOS = 'votos.pkl'


#salvar dados no arquivo pkl
def carregar_dados(arquivo):
    try:
        with open(arquivo, 'rb') as arq:
            return pickle.load(arq)
    except FileNotFoundError:
        return {}


def salvar_dados(arquivo, dados):
    with open(arquivo, 'wb') as arq:
        pickle.dump(dados, arq)

eleitores = carregar_dados(FILE_ELEITORES)
candidatos = carregar_dados(FILE_CANDIDATOS)
votos = carregar_dados(FILE_VOTOS)

#tela de cadastro eleitor/candidato
def tela_cadastro():
    def salvar_eleitor():
        try:
            titulo = int(entry_titulo.get())
            nome = entry_nome.get()
            RG = entry_rg.get()
            CPF = entry_cpf.get()
            secao = int(entry_secao.get())
            zona = int(entry_zona.get())

            if titulo in eleitores:
                raise Exception("Título já existente!")

            eleitores[titulo] = Eleitor(nome, RG, CPF, titulo, secao, zona)
            salvar_dados(FILE_ELEITORES, eleitores)
            messagebox.showinfo("Sucesso", "Eleitor cadastrado com sucesso!")
            limpar_campos()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def salvar_candidato():
        try:
            numero = int(entry_titulo.get())
            nome = entry_nome.get()
            RG = entry_rg.get()
            CPF = entry_cpf.get()

            if numero in candidatos:
                raise Exception("Número já existente!")

            candidatos[numero] = Candidato(nome, RG, CPF, numero)
            salvar_dados(FILE_CANDIDATOS, candidatos)
            messagebox.showinfo("Sucesso", "Candidato cadastrado com sucesso!")
            limpar_campos()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def limpar_campos():
        entry_titulo.delete(0, tk.END)
        entry_nome.delete(0, tk.END)
        entry_rg.delete(0, tk.END)
        entry_cpf.delete(0, tk.END)
        entry_secao.delete(0, tk.END)
        entry_zona.delete(0, tk.END)

    cadastro = tk.Tk()
    cadastro.title("Cadastro de Eleitores e Candidatos")
    cadastro.geometry("400x300")

    tk.Label(cadastro, text="Título/Número:").grid(row=0, column=0, padx=10, pady=5)
    entry_titulo = tk.Entry(cadastro)
    entry_titulo.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(cadastro, text="Nome:").grid(row=1, column=0, padx=10, pady=5)
    entry_nome = tk.Entry(cadastro)
    entry_nome.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(cadastro, text="RG:").grid(row=2, column=0, padx=10, pady=5)
    entry_rg = tk.Entry(cadastro)
    entry_rg.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(cadastro, text="CPF:").grid(row=3, column=0, padx=10, pady=5)
    entry_cpf = tk.Entry(cadastro)
    entry_cpf.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(cadastro, text="Seção:").grid(row=4, column=0, padx=10, pady=5)
    entry_secao = tk.Entry(cadastro)
    entry_secao.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(cadastro, text="Zona:").grid(row=5, column=0, padx=10, pady=5)
    entry_zona = tk.Entry(cadastro)
    entry_zona.grid(row=5, column=1, padx=10, pady=5)

    btn_eleitor = tk.Button(cadastro, text="Salvar Eleitor", command=salvar_eleitor)
    btn_eleitor.grid(row=6, column=0, padx=10, pady=10)

    btn_candidato = tk.Button(cadastro, text="Salvar Candidato", command=salvar_candidato)
    btn_candidato.grid(row=6, column=1, padx=10, pady=10)

    btn_limpar = tk.Button(cadastro, text="Limpar Campos", command=limpar_campos)
    btn_limpar.grid(row=7, column=0, columnspan=2, pady=10)

    cadastro.mainloop()

#tela da urna eletrônica
def tela_urna():
    eleitor_atual = {"titulo": None, "nome": None}#infos do eleitor atual
    urna_window = tk.Tk()
    urna_window.title("Urna Eletrônica")
    urna_window.geometry("600x400")
    urna_window.resizable(False, False)#para que não redimencione a tela

    #grava o voto digitado
    voto_digitado = tk.StringVar()
    
    #mostra o candidato enquanto o usuário digita
    candidato_atual = tk.StringVar(value="Candidato:")  

    #configurações de grid para a janela principal
    urna_window.rowconfigure(0, weight=1)
    urna_window.columnconfigure(0, weight=1)
    urna_window.columnconfigure(1, weight=1)

    def iniciar_votacao():
        #confere o título do eleitor para habilitar a votação
        try:
            titulo = int(entry_titulo.get())
            if titulo in eleitores:
                eleitor_atual["titulo"] = titulo
                eleitor_atual["nome"] = eleitores[titulo].get_nome()
                lbl_eleitor["text"] = f"Eleitor: {eleitor_atual['nome']}"
                lbl_status["text"] = "Status: Liberado para votar"
                habilitar_teclado()
                
                #limpa o número digitado
                voto_digitado.set("")  
            else:
                raise Exception("Eleitor não encontrado!")
        except ValueError:
            messagebox.showerror("Erro", "Título inválido! Insira apenas números.")
        except Exception as e:
            lbl_eleitor["text"] = "Eleitor não encontrado!"
            lbl_status["text"] = f"Status: {e}"

    def registrar_voto():
        #registra o voto
        numero = voto_digitado.get()
        try:
            if numero.isdigit() and int(numero) in candidatos:
                candidato = candidatos[int(numero)]
                votos[int(numero)] = votos.get(int(numero), 0) + 1
                lbl_status["text"] = f"Voto registrado: {candidato.get_nome()}"
            elif numero == "BRANCO":
                votos["BRANCO"] = votos.get("BRANCO", 0) + 1
                lbl_status["text"] = "Voto registrado: BRANCO"
            elif numero == "NULO":
                votos["NULO"] = votos.get("NULO", 0) + 1
                lbl_status["text"] = "Voto registrado: NULO"
            else:
                raise Exception("Número inválido ou candidato não encontrado!")
            
            #salva o voto no arquivo .pkl
            salvar_dados(FILE_VOTOS, votos)             
            messagebox.showinfo("Sucesso", "Voto registrado com sucesso!")
            
            #limpa tela para próximo eleitor
            limpar_voto()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def adicionar_numero(numero):
        #concatena o número digitado nos botões
        if eleitor_atual["titulo"] is None:
            messagebox.showwarning("Atenção", "Valide o eleitor antes de votar!")
            return

        #add o número digitado
        voto_digitado.set(voto_digitado.get() + str(numero))
        #atualiza a prévia do voto
        lbl_preview["text"] = f"Voto: {voto_digitado.get()}"  

        #exibe o nome do candidato
        try:
            numero_atual = int(voto_digitado.get())
            if numero_atual in candidatos:
                candidato_atual.set(f"Candidato: {candidatos[numero_atual].get_nome()}")
            else:
                candidato_atual.set("Candidato: Não encontrado")
        except ValueError:
            candidato_atual.set("Candidato: Não encontrado")

    def limpar_voto():
        #limpa campo de visualização do voto e do candidato
        voto_digitado.set("")
        candidato_atual.set("Candidato:")
        lbl_preview["text"] = "Voto:"

    def habilitar_teclado():
        #habiliata os botões para votar após a confirmação do eleitor
        for widget in frame_teclado.winfo_children():
            widget.config(state="normal")