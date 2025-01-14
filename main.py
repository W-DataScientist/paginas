import streamlit as st

# Função para a página inicial
def home():
    # Define o título da página
    st.title("Página Inicial")
    # Adiciona uma mensagem de boas-vindas
    st.write("Bem-vindo ao meu aplicativo multipágina!")
    # Instruções para navegação
    st.write("Use a barra lateral para navegar entre as páginas.")

# Dicionário que mapeia os nomes das páginas para suas respectivas funções
paginas = {
    "Página Inicial": home,  # Mapeia "Página Inicial" para a função home()
    "Página 2": "pages.page_2",  # Mapeia "Página 2" para o arquivo page_2.py
    "Página 3": "pages.page_3"   # Mapeia "Página 3" para o arquivo page_3.py
}

# Cria um menu de navegação na barra lateral usando radio buttons
st.sidebar.title("Navegação")
# Permite ao usuário selecionar uma página do menu
pagina_selecionada = st.sidebar.radio("Selecione uma página", paginas.keys())

# Exibe a página selecionada
if pagina_selecionada == "Página Inicial":
    home()  # Chama a função da página inicial
else:
    # Importa e executa a função da página selecionada dinamicamente
    page = __import__(paginas[pagina_selecionada], fromlist=[''])
    page.main()  # Chama a função main() do módulo importado
