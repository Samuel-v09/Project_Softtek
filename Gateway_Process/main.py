# serial_gateway/main.py

# Do nosso ficheiro "serial_reader", importamos a classe "serial_reader"
from serial_reader import serial_reader
import time

def run_gateway():
    """
    Função principal que orquestra o gateway para teste.
    Ela cria uma instância do nosso leitor serial e o coloca para funcionar.
    """
    print("INFO: [1] A iniciar o programa principal de teste...")
    
    # Cria uma instância (um objeto) do nosso leitor serial inteligente.
    print("INFO: [2] Criando instância do serial_reader...")
    handler = serial_reader(baudrate=115200)

    print("INFO: [3] Entrando no bloco with handler...")
    # O 'with' é um bloco de código seguro. Ele vai executar o método
    # handler.connect() no início e o handler.disconnect() no final, automaticamente.
    with handler:
        print("INFO: [4] Entrou no bloco with. Verificando conexão...")
        # Se a conexão falhar (handler.connection continuar como None), avisamos e paramos.
        if not handler.connection:
            print("CRÍTICO: Não foi possível iniciar o gateway. Verifique a conexão e tente novamente.")
            return

        print("\n--- Gateway de Comunicação Iniciado ---")
        print("A escutar dados do ESP. Pressione Ctrl+C para parar.")

        # Loop infinito para continuar a escutar os dados.
        while True:
            try:
                print("INFO: [5] Chamando handler.read_json_data()...")
                # Pede ao nosso handler para ler e processar os dados da porta serial.
                dados_recebidos = handler.read_json_data()

                # Se a função retornou dados válidos (não nulos), exibe-os na tela.
                if dados_recebidos:
                    print("\n-------------------------------------------")
                    print(f"[DADO RECEBIDO E PROCESSADO COM SUCESSO]")
                    print(dados_recebidos)
                    print("-------------------------------------------")
                    
            except KeyboardInterrupt:
                # Este bloco é ativado quando você pressiona Ctrl+C no terminal,
                # permitindo encerrar o programa de forma limpa.
                print("\nINFO: A encerrar o gateway a pedido do utilizador.")
                break
            except Exception as e:
                # Captura qualquer outro erro inesperado que possa acontecer no loop.
                print(f"ERRO INESPERADO no loop principal: {e}")
                time.sleep(5) # Espera um pouco antes de tentar novamente.

# Esta é uma convenção em Python. O código abaixo só é executado
# quando corremos o ficheiro "main.py" diretamente.
if __name__ == "__main__":
    run_gateway()