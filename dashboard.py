import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt


sns.set_theme()
st.set_page_config(layout="wide")

url = "https://raw.githubusercontent.com/adaoduque/Brasileirao_Dataset/refs/heads/master/campeonato-brasileiro-full.csv"

data = pd.read_csv(url)


def get_result(winner: str, team: str) -> str:
    if winner == team:
        return "Vitória"
    if winner == "-":
        return "Empate"
    return "Derrota"

def get_team_data(data: pd.DataFrame, team: str) -> pd.DataFrame:
    team_data = data.copy().query(f"mandante == '{team}' or visitante == '{team}'")
    team_data["resultado"] = team_data["vencedor"].apply(get_result, team=team)
    return team_data[["vencedor", "resultado"]]

def get_team_result_frequency(team_data: pd.DataFrame) -> pd.DataFrame:
    freq = team_data["resultado"].value_counts().reset_index()
    freq.columns = ["Resultado", "Quantidade"]
    return freq


st.title("Campeonato Brasileiro de Futebol")

st.dataframe(data)

teams = data["mandante"].unique()

# st.write(teams)

selected_team = st.selectbox(
    "Escolha o seu time",
    tuple(teams)
)

team_results = get_team_result_frequency(get_team_data(data, selected_team))

fig, ax = plt.subplots()

colors = ["limegreen", "gold", "tomato"]

team_results.sort_values(by="Resultado", inplace=True, ascending=False)

ax = sns.barplot(y=team_results["Quantidade"], hue=team_results["Resultado"], palette=colors)

title = f"{selected_team}\nTotal de Jogos: {team_results['Quantidade'].sum()}"

ax.set_title(title, fontsize=30)
ax.set_ylabel(None)
ax.set(yticklabels=[])


for i in ax.containers:
  ax.bar_label(i, fontsize=20, padding=-25)

st.pyplot(fig)

plt.close()

# fig.savefig("output.png", bbox_inches="tight")
