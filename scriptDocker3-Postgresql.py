import subprocess
import sys
import time

def manage_postgres_container():
    # Verifica se o container existe
    container_exists = subprocess.run(
        ["docker", "ps", "-a", "--filter", "name=meu_postgres", "--format", "{{.Names}}"],
        capture_output=True,
        text=True
    ).stdout.strip() == "meu_postgres"

    if container_exists:
        resposta = input("Container 'meu_postgres' já existe. Deseja recriá-lo? (yes/no): ").lower()
        
        if resposta == "yes":
            print("Removendo container existente...")
            subprocess.run(["docker", "rm", "-f", "meu_postgres"], check=True)
        elif resposta == "no":
            print("Utilizando container existente...")
            # Verifica se está rodando
            status = subprocess.run(
                ["docker", "ps", "--filter", "name=meu_postgres", "--format", "{{.Status}}"],
                capture_output=True,
                text=True
            ).stdout.strip()
            
            if not status:
                print("Iniciando container...")
                subprocess.run(["docker", "start", "meu_postgres"], check=True)
            
            enter_postgres_shell()
            return
        else:
            print("Opção inválida. Saindo.")
            return

    # Inicia novo container
    try:
        print("Iniciando novo container PostgreSQL...")
        subprocess.run([
            "docker", "run", "-d",
            "--name", "meu_postgres",
            "-p", "5432:5432",
            "-e", "POSTGRES_PASSWORD=senha123",
            "-e", "POSTGRES_USER=postgres",
            "-e", "POSTGRES_DB=postgres",
            "-v", "pg_data:/var/lib/postgresql/data",  # Volume para persistência
            "postgres:latest"
        ], check=True)
        
        print("\nContainer iniciado com sucesso!")
        print("Aguardando PostgreSQL inicializar...")
        
        # Espera o PostgreSQL ficar pronto
        time.sleep(5)
        wait_for_postgres()
        
        enter_postgres_shell()
        
    except subprocess.CalledProcessError as e:
        print(f"Erro: {e.stderr}")
        sys.exit(1)

def wait_for_postgres():
    """Aguarda até que o PostgreSQL esteja pronto para aceitar conexões"""
    while True:
        result = subprocess.run([
            "docker", "exec", "meu_postgres",
            "pg_isready", "-U", "postgres"
        ], capture_output=True, text=True)
        
        if "accepting connections" in result.stdout:
            break
        time.sleep(1)

def enter_postgres_shell():
    print("\nIniciando sessão PSQL...")
    print("Comandos básicos do PostgreSQL:")
    print(" - CREATE DATABASE...")
    print(" - CREATE TABLE...")
    print(" - INSERT INTO...")
    print(" - SELECT * FROM...")
    print(" - DROP TABLE...")
    print("Digite '\\q' para sair\n")
    
    # Entra no shell interativo
    subprocess.run([
        "docker", "exec", "-it",
        "meu_postgres",
        "psql", "-U", "postgres"
    ])

if __name__ == "__main__":
    manage_postgres_container()