import pandas as pd

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
