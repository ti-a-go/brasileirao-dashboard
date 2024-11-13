import pandas as pd
import seaborn as sns
import streamlit as st



url = "https://raw.githubusercontent.com/adaoduque/Brasileirao_Dataset/refs/heads/master/campeonato-brasileiro-full.csv"

data = pd.read_csv(url)

team = "Bahia"

def get_result(winner: str) -> str:
    if winner == team:
        return "Vitória"
    if winner == "-":
        return "Empate"
    return "Derrota"

def get_team_data(data: pd.DataFrame, team: str) -> pd.DataFrame:
    team_data = data.copy().query(f"mandante == '{team}' or visitante == '{team}'")
    team_data["resultado"] = team_data["vencedor"].apply(get_result)
    return team_data[["vencedor", "resultado"]]

def get_team_result_frequency(team_data: pd.DataFrame) -> pd.DataFrame:
    freq = team_data["resultado"].value_counts().reset_index()
    freq.columns = ["Resultado", "Quantidade"]
    return freq

team_results = get_team_result_frequency(get_team_data(data, "Bahia"))

st.title("Campeonato Brasileiro de Futebol")

st.dataframe(data)

st.header("Resultados do Time")

st.dataframe(team_results)