import streamlit as st
import pandas as pd  # Importa pandas para manipulação de dados em forma de DataFrame

# Função principal da Página 3
def main():
    # Define o título da página
    st.title("Página 3")
    # Adiciona uma descrição da página
    st.write("Esta é a terceira página do aplicativo.")
    
    # Exibe uma tabela de dados na página
    st.write("Aqui está uma tabela de dados:")
    
    # Cria um dicionário com dados para a tabela
    data = {
        'Coluna A': [1, 2, 3],   # Dados da Coluna A
        'Coluna B': [4, 5, 6],   # Dados da Coluna B
        'Coluna C': [7, 8, 9]    # Dados da Coluna C
    }
    
    df = pd.DataFrame(data)   # Converte o dicionário em um DataFrame do pandas
    st.table(df)              # Exibe o DataFrame como uma tabela na aplicação Streamlit
