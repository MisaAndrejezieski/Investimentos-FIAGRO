import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd

def calcular_investimento():
    try:
        # Obtendo valores da interface
        aporte_mensal = float(entry_aporte.get())
        taxa_juros_mensal = float(entry_juros.get()) / 100
        meses = int(entry_meses.get())

        dados = []
        saldo = 0

        for mes in range(1, meses + 1):
            saldo += aporte_mensal
            saldo *= (1 + taxa_juros_mensal)
            dados.append([mes, f'R$ {aporte_mensal:.2f}', f'R$ {saldo:.2f}'])

        # Criando DataFrame e salvando em Excel
        df = pd.DataFrame(dados, columns=["Mês", "Aporte Mensal", "Saldo Acumulado"])
        df.to_excel("dados/investimento_fiagro.xlsx", index=False)

        messagebox.showinfo("Sucesso", "Planilha criada: dados/investimento_fiagro.xlsx")
    
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

# Criando janela principal
root = tk.Tk()
root.title("Simulador de Investimento FIAGRO")
root.geometry("350x200")

# Layout da interface
ttk.Label(root, text="Aporte Mensal (R$):").grid(row=0, column=0, padx=10, pady=5)
entry_aporte = ttk.Entry(root)
entry_aporte.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(root, text="Taxa de Juros (% ao mês):").grid(row=1, column=0, padx=10, pady=5)
entry_juros = ttk.Entry(root)
entry_juros.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(root, text="Duração (meses):").grid(row=2, column=0, padx=10, pady=5)
entry_meses = ttk.Entry(root)
entry_meses.grid(row=2, column=1, padx=10, pady=5)

ttk.Button(root, text="Calcular", command=calcular_investimento).grid(row=3, columnspan=2, pady=10)

root.mainloop()
