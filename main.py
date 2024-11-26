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