# main.py
# Ponto de entrada do programa

import os
from organizer import organize_files

def main():
    print("=== Organizador Automático de Arquivos ===")
    folder_path = input("Digite o caminho da pasta que deseja organizar: ").strip()

    if not os.path.isdir(folder_path):
        print("❌ Caminho inválido. Verifique e tente novamente.")
        return

    organize_files(folder_path)
    print("✅ Organização concluída com sucesso!")

if __name__ == "__main__":
    main()

