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

"<head>

#index do power app
#     <title>Quadro Interativo</title>
# </head>

# <div style='font-family: Arial, sans-serif; background: linear-gradient(90deg, rgb(218, 227, 245) 16.62%, #5C95FF 200%); margin: 0; padding: 0;'>
#     <header style='background: #ffffff; box-shadow: 0 .125rem .25rem #000000; padding: 20px;'>
#         <div style='display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;'>
#             <h1 style='font-size: 1.50rem; margin: 0; color: #0056b3; font-weight: bold; text-align: center; flex: 1;'>Quadro Interativo</h1>
#             <nav>
#                 <a style='color: #007bff; text-decoration: none; font-size: 150%;' href='https://kimberlyclark.sharepoint.com/:x:/r/Sites/H945/Suzano/Quadro%20Interativo/WIPES/Troca%20de%20Turno%20WW.xlsx?d=w21258b47a4c844cd9b9859a354013d72&csf=1&web=1&e=VzSu7g' target='_blank'>Troca de Turno</a>
#                 <a style='color: #007bff; text-decoration: none; font-size: 150%;' href='#'>Tutorial</a>
#                 <a style='color: #007bff; text-decoration: none; font-size: 150%;' href='#'>Sugestão & Erro</a>
#                 <a style='color: #007bff; text-decoration: none; font-size: 150%;' href='https://kimberlyclark.sharepoint.com/Sites/H945/'>Portal de Melhoria Continua</a>
#             </nav>
#         </div>
#     </header>

#     <main style='margin: 20px;'>
#         <section style='display: flex; flex-wrap: wrap;'>
#             <div style='flex: 0 0 calc(20% - 20px); margin: 10px; min-width: 200px; box-sizing: border-box;'>
#                 <h2 style='font-size: 1.50rem; color: #007bff;'>EHS</h2>
#                 <button style='display: block; width: 100%; margin-top: 10px; padding: 10px; border-radius: 15px; background-color: #0046CA; color: white; border: none; cursor: pointer; font-size: 1rem;'>Botão 1A</button>
#                 <button style='display: block; width: 100%; margin-top: 10px; padding: 10px; border-radius: 15px; background-color: #0046CA; color: white; border: none; cursor: pointer; font-size: 1rem;'>Botão 1B</button>
#                 <!-- Adicione mais botões aqui -->
#             </div>
#             <div style='flex: 0 0 calc(20% - 20px); margin: 10px; min-width: 200px; box-sizing: border-box;'>
#                 <h2 style='font-size: 1.50rem; color: #007bff;'>Coluna 2</h2>
#                 <button style='display: block; width: 100%; margin-top: 10px; padding: 10px; border-radius: 15px; background-color: #0046CA; color: white; border: none; cursor: pointer; font-size: 1rem;'>Botão 2A</button>
#                 <button style='display: block; width: 100%; margin-top: 10px; padding: 10px; border-radius: 15px; background-color: #0046CA; color: white; border: none; cursor: pointer; font-size: 1rem;'>Botão 2B</button>
#                 <!-- Adicione mais botões aqui -->
#             </div>
#             <div style='flex: 0 0 calc(20% - 20px); margin: 10px; min-width: 200px; box-sizing: border-box;'>
#                 <h2 style='font-size: 1.50rem; color: #007bff;'>Coluna 3</h2>
#                 <!-- Adicione mais botões aqui -->
#             </div>
#             <div style='flex: 0 0 calc(20% - 20px); margin: 10px; min-width: 200px; box-sizing: border-box;'>
#                 <h2 style='font-size: 1.50rem; color: #007bff;'>Coluna 4</h2>
#                 <!-- Adicione mais botões aqui -->
#             </div>
#             <div style='flex: 0 0 calc(20% - 20px); margin: 10px; min-width: 200px; box-sizing: border-box;'>
#                 <h2 style='font-size: 1.50rem; color: #007bff;'>Coluna 5</h2>
#                 <!-- Adicione mais botões aqui -->
#             </div>
#         </section>
#     </main>
# </body>
# </html>"
