import streamlit as st
import numpy as np  # Importa numpy para gerar dados aleatórios

# Função principal da Página 2
def main():
    # Define o título da página
    st.title("Página 2")
    # Adiciona uma descrição da página
    st.write("Esta é a segunda página do aplicativo.")
    
    # Adiciona um gráfico de linha à página
    st.write("Aqui está um gráfico de linha:")
    
    data = np.random.randn(10, 2)  # Gera um array de dados aleatórios com 10 linhas e 2 colunas
    st.line_chart(data)  # Plota os dados gerados como um gráfico de linha
