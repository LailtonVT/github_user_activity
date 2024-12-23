# GitHub User Activity CLI

Este é um projeto simples de CLI em Python que utiliza a API do GitHub para buscar e exibir as atividades recentes de um usuário.

- https://roadmap.sh/projects/github-user-activity



## Funcionalidades

- Aceita o nome de usuário do GitHub como argumento.
- Busca as 25 atividades mais recentes do usuário.
- Exibe informações sobre commits, issues e estrelas de repositórios.

## Requisitos

- Python 3.x

## Como usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/github-user-activity-cli.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd github-user-activity-cli
   ```

3. Torne o script executável:
   ```bash
   chmod +x github_activity.py
   ```

4. Execute o script com o nome de usuário do GitHub como argumento:
   ```bash
   python3 github_activity.py <username>
   ```

## Exemplo de Uso

```bash
$ python3 github_activity.py octocat
Atividades recentes de octocat:
- Pushed 2 commits to octocat/Hello-World
- Opened a new issue in octocat/Spoon-Knife
- Starred octocat/Hello-World
```

## Licença

Este projeto está licenciado sob a Licença MIT.