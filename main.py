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