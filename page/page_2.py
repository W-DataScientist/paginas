import streamlit as st
import numpy as np  # Importa numpy para gerar dados aleatórios

# Função principal da Página 2
def main():
    # Define o título da página
    st.title("Página 2")
    
    # Adiciona uma descrição da página
    st.write("Esta é a segunda página do aplicativo.")
    
    # Texto explicativo sobre a Página 2
    st.write("""
        Nesta página, você encontrará um gráfico de linha que ilustra dados gerados aleatoriamente.
        O gráfico pode ser utilizado para visualizar tendências ou padrões em conjuntos de dados.
        Você pode modificar a lógica para incluir dados reais ou outros tipos de visualizações conforme necessário.
    """)
    
    # Exemplo de gráfico simples
    st.write("Aqui está um gráfico de linha:")
    
    data = np.random.randn(10, 2)  # Gera um array de dados aleatórios com 10 linhas e 2 colunas
    st.line_chart(data)  # Plota os dados gerados como um gráfico de linha
