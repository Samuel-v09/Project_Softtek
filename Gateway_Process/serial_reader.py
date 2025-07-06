#serial_reader.py

# Importa as bibliotecas necessárias
import serial
import serial.tools.list_ports
import json
import time

#Função que encontra a porta serial do ESP32
def find_port(baudrate=115200):

    print("Procurando dispositivo ESP32...")
    
    portas = serial.tools.list_ports.comports()
    for porta in portas:
        try:
            #Abre uma conexão rápida para ver se consegue um feedback do dispositivo
            with serial.Serial(porta.device, baudrate, timeout=2) as ser:

                # Se for possível ler alguma linha significa que o dispositivo foi encontrado
                if ser.readline():
                    print(f"Dispositivo localizado na porta '{porta.device}'")
                    return porta.device
        except serial.SerialException:
            # Se a porta estiver ocupada ou der qualquer tipo de erro, é realizada a próxima tentativa
            continue
    print("ERRO: Não foi encontrado o dispositivo, analise a conexão.")
    return None

# Organiza o processo e realiza a leitura de dados
def read_serial():

    porta_esp = find_port()

    if not porta_esp:
        print("Não foi possível conectar o dispositivo ou seja dispositivo não encontrado")
        return

    try:
        # Após encontra a porta é aberta a conexão
        with serial.Serial(porta_esp, 115200, timeout=1) as conexao_serial:
            print("Comunicação Iniciada")

            # Loop para ler os dados de forma continua
            while True:
                # Faz a leitura da linha, realiza a conversão de bytes para texto e remove os espaços
                linha = conexao_serial.readline().decode('utf-8', errors='ignore').strip()

                # Se a linha não estiver vazia processa o JSON
                if linha:
                    try:
                        dados = json.loads(linha)
                        print("\n")
                        print("Dados Recebidos com Sucesso")
                        print(dados)
                        print("\n")

                    # Se o Json não estiver ok avisa e continua fazendo a leitura
                    except json.JSONDecodeError:
                        print("Dado mal recebido ou formatação incorreta")

    except KeyboardInterrupt:
        # Função para interromper o programa Ctrl+C
        print("Programa Encerrado pelo Operador")

    except serial.SerialException:
        #Analisa erros de conexão
        print("Erro de conexão serial")

