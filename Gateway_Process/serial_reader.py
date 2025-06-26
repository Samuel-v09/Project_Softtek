# Importa as bibliotecas necessárias
import serial
import serial.tools.list_ports
import json
import time

class serial_reader:
    """
    Gerencia a comunicação serial com o Arduino de forma robusta.
    """
    def __init__(self, baudrate=115200, timeout=1):
        """
        Método construtor, executado quando um objeto 'serial_reader' é criado.
        """
        self.port = None
        self.baudrate = baudrate
        self.timeout = timeout
        self.connection = None
        print("INFO: serial_reader inicializado.")

    def find_device_port(self):
        """
        Varre todas as portas seriais e tenta encontrar o dispositivo automaticamente.
        """
        print("INFO: Procurando dispositivo na porta serial...")
        ports = serial.tools.list_ports.comports()
        
        if not ports:
            print("ERRO: Nenhuma porta serial encontrada.")
            return None

        for port_info in ports:
            try:
                # Tenta abrir e fechar a porta para ver se ela é válida e se está disponível
                with serial.Serial(port_info.device, self.baudrate, timeout=0.2) as ser:
                    time.sleep(2) # Dá tempo para o ESP enviar o primeiro dado
                    line = ser.readline()
                    if line:
                        print(f"INFO: Dispositivo encontrado na porta '{port_info.device}'")
                        self.port = port_info.device
                        return self.port
            except serial.SerialException:
                # Se a porta estiver ocupada ou der erro, apenas ignora e tenta a próxima
                continue
        
        print("ERRO: Não foi possível encontrar um dispositivo respondendo. Verifique a conexão do cabo USB.")
        return None

    def connect(self):
        """
        Estabelece a conexão definitiva com a porta encontrada.
        """
        if not self.port:
            self.find_device_port()
        
        if self.port:
            try:
                self.connection = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
                print(f"INFO: Conexão estabelecida com sucesso em '{self.port}'.")
                return True
            except serial.SerialException as e:
                print(f"ERRO: Falha ao conectar em '{self.port}': {e}")
                self.connection = None
                return False
        return False

    def disconnect(self):
        """
        Fecha a conexão serial de forma segura.
        """
        if self.connection and self.connection.is_open:
            self.connection.close()
            print(f"INFO: Conexão com a porta '{self.port}' fechada.")

    def read_json_data(self):
        """
        Lê uma linha da porta serial, decodifica o texto e o transforma em um objeto Python.
        Este é o coração da leitura de dados.
        """
        # Primeiro, verifica se a conexão existe e está aberta.
        if not self.connection or not self.connection.is_open:
            print("AVISO: Tentativa de leitura sem uma conexão ativa.")
            return None

        try:
            # 1. Lê uma linha de texto da porta serial (espera até encontrar o "enter")
            # 2. .decode('utf-8') converte os bytes recebidos em texto legível
            # 3. .strip() remove espaços ou linhas em branco do começo e do fim
            line = self.connection.readline().decode('utf-8').strip()
            
            # Se a linha não estiver vazia...
            if line:
                # ...tenta converter o texto JSON em um dicionário Python.
                return json.loads(line)
                
        except json.JSONDecodeError:
            # Captura erro se o texto recebido não for um JSON válido.
            print(f"AVISO: Dado recebido não é um JSON válido: '{line}'")
        except UnicodeDecodeError:
            # Captura erro se o Arduino enviar algum caractere "estranho".
            print("AVISO: Recebido um caractere inválido que não pôde ser decodificado.")
        except serial.SerialException as e:
            # Captura erro se o cabo for desconectado durante o uso.
            print(f"ERRO: A conexão serial foi perdida: {e}")
            self.disconnect() # Tenta fechar a conexão "quebrada"
        
        # Se qualquer erro ocorrer, a função retorna None (nulo).
        return None

    def __enter__(self):
        """
        Executado no início do bloco 'with'. Tenta conectar.
        """
        self.connect()
        return self # Retorna o próprio objeto para ser usado dentro do 'with'

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Executado automaticamente no final do bloco 'with', garantindo que a conexão seja fechada.
        """
        self.disconnect()






       



