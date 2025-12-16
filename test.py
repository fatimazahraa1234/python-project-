import matplotlib.pyplot as plt
import pandas as pd

# 1. Chargement (Correction du nom de fichier potentiel)

df = pd.read_csv("Telco_Cusomer_Churn.csv")

# 2. Vérification
print(df.head())

# 3. Calcul (Correction: on utilise 'df', pas 'self.df')
global_churn = df["Churn"].value_counts()

# 4. Visualisation
plt.figure(figsize=(7, 7))

colors = ['#66b3ff', '#ff9999']
explode = (0, 0.1)

plt.pie(
    global_churn,
    labels=global_churn.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    explode=explode,
    shadow=True,
    textprops={'fontsize': 14}
)

plt.title("Taux de Désabonnement Global (Global Churn Rate)", fontsize=16)
plt.axis('equal')
plt.show()