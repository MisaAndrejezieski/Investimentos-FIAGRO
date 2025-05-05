import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd

# Criando a janela principal
root = tk.Tk()
root.title("Investimentos em Fundos Imobiliários")

# Lista de entradas
entries = {}

def salvar_dados():
    """Obtém os dados da interface e salva em um arquivo Excel"""
    mes = entries["Mês"].get()
    valor_investido = float(entries["Valor Investido (R$)"].get())
    preco_cota = float(entries["Preço da Cota (R$)"].get())
    rendimento_por_cota = float(entries["Rendimento por Cota (R$)"].get())
    
    quantidade_cotas = valor_investido / preco_cota
    dividendos_recebidos = quantidade_cotas * rendimento_por_cota

    # Criar ou atualizar a planilha
    novo_dado = pd.DataFrame([[mes, valor_investido, preco_cota, quantidade_cotas, dividendos_recebidos]], 
                             columns=["Mês", "Valor Investido (R$)", "Preço da Cota (R$)", "Quantidade de Cotas", "Dividendos Recebidos (R$)"])
    
    try:
        df_existente = pd.read_excel("investimentos_fundos_imobiliarios.xlsx")
        df_atualizado = pd.concat([df_existente, novo_dado], ignore_index=True)
    except FileNotFoundError:
        df_atualizado = novo_dado
    
    df_atualizado.to_excel("investimentos_fundos_imobiliarios.xlsx", index=False)

    messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")

# Criando os campos de entrada
campos = ["Mês", "Valor Investido (R$)", "Preço da Cota (R$)", "Rendimento por Cota (R$)"]

for i, campo in enumerate(campos):
    ttk.Label(root, text=campo).grid(row=i, column=0, padx=10, pady=5)
    entrada = ttk.Entry(root)
    entrada.grid(row=i, column=1, padx=10, pady=5)
    entries[campo] = entrada

# Botão para salvar os dados
ttk.Button(root, text="Salvar Dados", command=salvar_dados).grid(row=len(campos), column=0, columnspan=2, pady=10)

# Executando a interface
root.mainloop()
