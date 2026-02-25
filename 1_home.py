import streamlit as st
import pandas as pd
import webbrowser


#Configurando a página do aplicativo
st.set_page_config(
    page_title='Home',
    page_icon=':house:',
    layout='wide'
)


#Lendo a base de dados
if 'data' not in st.session_state:
    df_data = pd.read_csv('archive/CLEAN_FIFA23_official_data.csv', index_col=0)
    df_data = df_data[df_data['Contract Valid Until'] >= 2023]  # datetime.today().year
    df_data = df_data[df_data['Value(£)'] > 0]
    df_data.sort_values(by='Overall', ascending=False, inplace=True)
    st.session_state['data'] = df_data

st.write('# FIFA23 OFFICIAL DATASET! :soccer:')

st.sidebar.markdown('Desenvolvido por Wander A. Martins')

button = st.button('Acesse os dados no Kaggle')
if button:
    webbrowser.open_new_tab('https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data')

st.markdown(
    """
    O conjunto de dados sobre jogadores de futebol de 2017 a 2023 fornece informações abrangentes
    sobre jogadores profissionais de futebol. O conjunto de dados contém uma ampla gama de atributos,
    incluindo dados demográficos dos jogadores, características físicas, estatísticas de jogo,
    detalhes de contratos e afiliações a clubes.
    
    Com mais de **17.000 registos**, este conjunto de dados oferece um recurso valioso para analistas,
    investigadores e entusiastas do futebol interessados em explorar vários aspectos do mundo do futebol,
    pois permite estudar os atributos dos jogadores, métricas de desempenho, avaliação de mercado,
    análise de clubes, posicionamento dos jogadores e desenvolvimento dos jogadores ao longo do tempo.
"""
)

