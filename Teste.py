import os
import shutil
import time

# Diretórios (substitua pelo caminho correto no seu ambiente)
diretorio_origem = "/home/valcann/backupsFrom"
diretorio_destino = "/home/valcann/backupsTo"
diretorio_logs = "/home/valcann"

# Arquivos de log
log_origem = os.path.join(diretorio_logs, "backupsFrom.log")
log_destino = os.path.join(diretorio_logs, "backupsTo.log")

# Timestamp de 3 dias atrás
tres_dias_atras = time.time() - (3 * 24 * 60 * 60)

def listar_arquivos(diretorio, arquivo_log):
    """Lista os arquivos no diretório e salva no arquivo de log."""
    with open(arquivo_log, "w") as log:
        for raiz, _, arquivos in os.walk(diretorio):
            for arquivo in arquivos:
                caminho_arquivo = os.path.join(raiz, arquivo)
                try:
                    estatisticas = os.stat(caminho_arquivo)
                    data_criacao = time.ctime(estatisticas.st_ctime)
                    data_modificacao = time.ctime(estatisticas.st_mtime)
                    tamanho = estatisticas.st_size
                    log.write(f"{arquivo}, {tamanho} bytes, Criado: {data_criacao}, Modificado: {data_modificacao}\n")
                except Exception as e:
                    log.write(f"Erro ao acessar {caminho_arquivo}: {e}\n")

def limpar_e_copiar_arquivos(origem, destino):
    """Remove e copia arquivos com base na data de criação."""
    if not os.path.exists(destino):
        os.makedirs(destino)

    with open(log_destino, "w") as log:
        for raiz, _, arquivos in os.walk(origem):
            for arquivo in arquivos:
                caminho_arquivo = os.path.join(raiz, arquivo)
                try:
                    data_criacao = os.path.getctime(caminho_arquivo)
                    if data_criacao > tres_dias_atras:
                        os.remove(caminho_arquivo)
                    else:
                        caminho_destino = os.path.join(destino, arquivo)
                        shutil.copy2(caminho_arquivo, caminho_destino)
                        log.write(f"Copiado: {arquivo} para {caminho_destino}\n")
                except Exception as e:
                    log.write(f"Erro ao processar {caminho_arquivo}: {e}\n")

def principal():
    """Executa as ações principais."""
    # Verificar se os diretórios existem
    if not os.path.exists(diretorio_origem):
        print(f"Erro: Diretório de origem '{diretorio_origem}' não encontrado.")
        return
    if not os.path.exists(diretorio_destino):
        os.makedirs(diretorio_destino)
    
    # Listar arquivos no diretório de origem
    listar_arquivos(diretorio_origem, log_origem)

    # Limpar e copiar arquivos
    limpar_e_copiar_arquivos(diretorio_origem, diretorio_destino)

if __name__ == "__main__":
    principal()
