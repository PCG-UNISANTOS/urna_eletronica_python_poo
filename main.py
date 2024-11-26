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