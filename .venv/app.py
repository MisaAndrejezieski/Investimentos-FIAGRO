import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd

def calcular_investimento():
    try:
        # Obtendo valores da interface
        aporte_mensal = float(entry_aporte.get())
        taxa_rendimento_mensal = float(entry_rendimento.get()) / 100
        dividend_yield = float(entry_dividend.get()) / 100
        meses = int(entry_meses.get())

        cotas = 0
        saldo = 0
        dados = []

        for mes in range(1, meses + 1):
            cotas_compradas = aporte_mensal / 10  # Supondo preço médio da cota = R$ 10
            cotas += cotas_compradas
            saldo += aporte_mensal
            rendimento = saldo * taxa_rendimento_mensal
            dividendos = cotas * 10 * dividend_yield  # Dividendos = cotas * preço médio * yield
            cotas += dividendos / 10  # Reinveste dividendos na compra de novas cotas
            saldo += rendimento  # Aplica o rendimento sobre o saldo

            dados.append([mes, f'R$ {aporte_mensal:.2f}', f'R$ {saldo:.2f}', f'{cotas:.2f} cotas'])

        # Criando planilha Excel
        df = pd.DataFrame(dados, columns=["Mês", "Aporte Mensal", "Saldo Acumulado", "Total de Cotas"])
        df.to_excel("dados/investimento_fiis.xlsx", index=False)

        messagebox.showinfo("Sucesso", "Planilha criada: dados/investimento_fiis.xlsx")

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

# Criando interface gráfica
root = tk.Tk()
root.title("Simulador de Investimento FIIs")
root.geometry("400x250")

# Layout da interface
ttk.Label(root, text="Aporte Mensal (R$):").grid(row=0, column=0, padx=10, pady=5)
entry_aporte = ttk.Entry(root)
entry_aporte.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(root, text="Rendimento (% ao mês):").grid(row=1, column=0, padx=10, pady=5)
entry_rendimento = ttk.Entry(root)
entry_rendimento.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(root, text="Dividend Yield (% ao mês):").grid(row=2, column=0, padx=10, pady=5)
entry_dividend = ttk.Entry(root)
entry_dividend.grid(row=2, column=1, padx=10, pady=5)

ttk.Label(root, text="Duração (meses):").grid(row=3, column=0, padx=10, pady=5)
entry_meses = ttk.Entry(root)
entry_meses.grid(row=3, column=1, padx=10, pady=5)

ttk.Button(root, text="Calcular", command=calcular_investimento).grid(row=4, columnspan=2, pady=10)

root.mainloop()
