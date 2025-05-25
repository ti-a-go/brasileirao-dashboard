import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

from helpers import get_team_data, get_team_result_frequency

sns.set_theme()
st.set_page_config(layout="wide")

def fetch_data():
    url = "https://raw.githubusercontent.com/adaoduque/Brasileirao_Dataset/refs/heads/master/campeonato-brasileiro-full.csv"
    return pd.read_csv(url)


def render_title():

    page_title = "Campeonato Brasileiro de Futebol"

    st.title(page_title)


def render_data(data):
    st.dataframe(data)




def render_team_result(data, save_fit=False):
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

    if save_fit:
        fig.savefig("output.png", bbox_inches="tight")



def main():
    data = fetch_data()
    render_title()
    render_data(data)
    render_team_result(data)

if __name__ == "__main__":
    main()