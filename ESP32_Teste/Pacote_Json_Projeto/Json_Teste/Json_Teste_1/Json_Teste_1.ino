#include <ArduinoJson.h>

void setup() {
  // put your setup code here, to run once:
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(LED_BUILTIN, HIGH);
  delay(2000);
  digitalWrite(LED_BUILTIN, LOW);
  delay(2000);

  // Teste 1 do Json apenas para entendimento e organização do Json 
  // Não contém váriaveis ainda para o conteúdo das perguntas e respostas será elaborado nos próximos códigos
  
  StaticJsonDocument<8096> dados_sentimentos;

  // Exemplo de Json com Array
  JsonArray verbais_array = dados_sentimentos.createNestedArray("perguntas_verbais");
  
  JsonObject verbal_1 = verbais_array.createNestedObject();
  verbal_1["pergunta"] = "Oque Você está sentindo hoje ?";
  verbal_1["resposta"] = "Resposta do usuário captada no microfone";

  JsonObject verbal_2 = verbais_array.createNestedObject();
  verbal_2["pergunta"] = "Oque foi desafiador para você hoje?";
  verbal_2["resposta"] = "Resposta do usuário captada no microfone";

  // Exemplo de Json com somente Objeto

  JsonObject alternativa_obj = dados_sentimentos.createNestedObject("perguntas_alternativas");
  alternativa_obj["pergunta"] = "Você gosta de Trabalhar na Softtek";
  alternativa_obj["resposta"] = "Resposta pelo botão sim ou não";

  serializeJsonPretty(dados_sentimentos, Serial);
}
