# main.py

#Importa o programa e a função que realiza a leitura serial

from serial_reader import read_serial

#Verifica se o arquivo que está sendo executado é o main.py "Principal"

if __name__ == "__main__":
    print("Executa o programa leitura serial")
    read_serial()