import sys
import os
import shutil


# Para usar esse arquivo basta executar o comando passando os seguintes argumentos:
# python renomear_arquivos.py FOLDER_DESEJA_RENOMEAR FOLDER_DESTINO NUM_INICIAL


FOLDER_PARA_RENOMEAR = sys.argv[1]  # String
FOLDER_DESTINO = sys.argv[2]  # String
TYPE_ANOMALY = sys.argv[3]  # String
NUM_INICIAL = int(sys.argv[4])  # Integer
FOLDER_TMP = 'tmp'

if not os.path.exists(FOLDER_DESTINO):
    print(f"Criando folder -> {FOLDER_DESTINO}...")
    os.mkdir(FOLDER_DESTINO) 


def unir_path_arquivos(path_arquivo, nomes_arquivos):
    path_arquivos = []
    for nome_arquivo in nomes_arquivos:
        path_arquivos.append(os.path.join(path_arquivo, nome_arquivo))
    return path_arquivos


def copiar_todos_arquivos_da_pasta(pasta_origem, pasta_destino):
    print("Criando uma pasta temporária...")
    if not os.path.exists(FOLDER_TMP):
        print(f"Criando folder -> {FOLDER_TMP}...")
        os.mkdir(FOLDER_TMP) 

    nomes_arquivos = os.listdir(FOLDER_PARA_RENOMEAR)
    for nome_arquivo in nomes_arquivos:
        shutil.copyfile(os.path.join(pasta_origem, nome_arquivo), 
                        os.path.join(FOLDER_TMP, nome_arquivo))
    


def renomear_todos_arquivos(folder_input, folder_output, numero_inicial):
    print("Renomeando os arquivos da pasta destino...")
    nomes_arquivos_para_renomear = os.listdir(folder_input)
    nomes_com_path_arquivos_para_renomear = unir_path_arquivos(folder_input, nomes_arquivos_para_renomear)
    i = numero_inicial
    for nome_com_path_arquivo_para_renomear in nomes_com_path_arquivos_para_renomear:
        os.rename(nome_com_path_arquivo_para_renomear, os.path.join(folder_output, f'{TYPE_ANOMALY}{i:07}.png'))
        i += 1

    print(f'Removendo folder temporária...')
    #shutil.rmtree(FOLDER_TMP, ignore_errors=True)

    print(f'Processo finalizado!\nSeus arquivos foram renomeados e movidos para = {FOLDER_DESTINO}')


if __name__ == "__main__":
    #copiar_todos_arquivos_da_pasta(FOLDER_PARA_RENOMEAR, FOLDER_DESTINO)
    renomear_todos_arquivos(FOLDER_PARA_RENOMEAR, FOLDER_DESTINO, NUM_INICIAL)
