import pandas as pd
import matplotlib.pyplot as plt

# Configurações iniciais
aporte_mensal = 400  # Valor investido mensalmente
preco_cota = 9.33  # Preço médio da cota
dividend_yield = 0.009  # 0.9% ao mês (9 centavos por cota)
meses = 12  # Período da simulação

saldo = 0
cotas = 0
dados = []

# Simulação do investimento
for mes in range(1, meses + 1):
    cotas_compradas = aporte_mensal / preco_cota
    cotas += cotas_compradas
    saldo += aporte_mensal
    
    dividendos = cotas * preco_cota * dividend_yield
    cotas += dividendos / preco_cota  # Reinvestindo dividendos

    dados.append([mes, f"R$ {saldo:.2f}", f"{cotas:.2f} cotas", f"R$ {dividendos:.2f}"])

# Criando DataFrame e exportando para Excel
df = pd.DataFrame(dados, columns=["Mês", "Saldo Acumulado", "Total de Cotas", "Dividendos"])
df.to_excel("investimento_fii.xlsx", index=False)

# Gráfico de crescimento do investimento
plt.figure(figsize=(10, 5))
plt.plot(df["Mês"], df["Saldo Acumulado"].str.replace("R$", "").astype(float), marker='o', label="Saldo Acumulado")
plt.xlabel("Meses")
plt.ylabel("Valor (R$)")
plt.title("Simulação de Investimento em FIIs")
plt.legend()
plt.grid()
plt.show()

print("Planilha criada: investimento_fii.xlsx")
