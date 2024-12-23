import sys
import urllib.request
import json

def fetch_github_activity(username):
    url = f"https://api.github.com/users/{username}/events"

    try:
        # Fazendo a requisicao para o endpoint
        with urllib.request.urlopen(url) as response:
            data = response.read()
            events = json.loads(data)

            # Verificando se ha eventos disponiveis
            if not events:
                print(f"Nenhuma atividade recente encontrada para o usuario {username}")
                return
            print(f"Atividades recentes de {username} no GitHub:")
            for event in events[:25]: # Exibe o maximo de 10 eventos
                action = event.get('type', 'Unknown event')
                repo = event.get('repo', {}).get('name', 'Unknown repo')

                # Formata os eventos mais comuns
                if action ==  "PushEvent":
                    commits = len(event.get('payload', {}).get('commits', []))
                    print(f"- Pushed {commits} commits to {repo}")
                elif action == "IssuesEvent":
                    action_type = event.get('payload', {}).get('action', 'Unknown action')
                    print(f"- {action_type} issue on {repo}")
                elif action == "WatchEvent":
                    print(f"- Starred {repo}")
                else:
                    print(f"- {action} on {repo}")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"Usuario {username} nao encontrado")
        else:
            print(f"Erro ao acessar a API do GitHub: {e.reason}")
    except Exception as e:
        print(f"Erro inesperado: {str(e)}")

def main():
    if len(sys.argv) != 2:
        print("Uso: python github_activity.py <username>")
        sys.exit(1)

    username = sys.argv[1]
    fetch_github_activity(username)
if __name__ == "__main__":
    main()
