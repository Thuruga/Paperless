import git
from bs4 import BeautifulSoup
import os

# Clonar o repositório
repo_url = 'https://github.com/Thuruga/Paperless.git'
repo_dir = #r'path\to\repo_clone\place'
repo = git.Repo.clone_from(repo_url, repo_dir)

# Caminho do arquivo HTML dentro do repositório
caminho_arquivo_html = os.path.join(repo_dir, 'index.html')

# Ler o conteúdo do arquivo HTML
with open(caminho_arquivo_html, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Criar um objeto BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Manipular o HTML (exemplo: alterar o texto de um elemento)
elemento = soup.find('h1')
elemento.string = 'Novo Título'

# Salvar as alterações de volta no arquivo
with open(caminho_arquivo_html, 'w', encoding='utf-8') as file:
    file.write(str(soup))

# Fazer o commit das alterações
repo.index.add([caminho_arquivo_html])
repo.index.commit('Alterado o título do elemento h1')

# Empurrar as alterações para o repositório remoto
origin = repo.remote(name='origin')
origin.push()

print('Alterações feitas e empurradas para o repositório remoto.')
