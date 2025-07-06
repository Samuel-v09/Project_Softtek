#include <ArduinoJson.h>

void setup()
{
  // put your setup code here, to run once:
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(115200);
}

void loop()
{
  // put your main code here, to run repeatedly:
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);

  // Teste 2 do Json, já testado Json esse código é o teste para enviar para o python estabelecer essa comunicação é fundamental para as próximas etapas
  // Não contém váriaveis ainda para o conteúdo das perguntas e respostas será elaborado nos próximos códigos

  StaticJsonDocument<8096> dados_sentimentos;

  // Exemplo de Json com Array

  // Perguntas Verbais Oficial

  JsonArray verbais_array = dados_sentimentos.createNestedArray("perguntas_verbais");

  JsonObject verbal_1 = verbais_array.createNestedObject();
  verbal_1["pergunta"] = "Qual foi o ponto alto do seu dia e o que o tornou significativo?";
  verbal_1["resposta"] = "Resposta do usuário captada no microfone";

  JsonObject verbal_2 = verbais_array.createNestedObject();
  verbal_2["pergunta"] = "Descreva o maior desafio que você enfrentou hoje e como se sentiu ao lidar com ele?";
  verbal_2["resposta"] = "Resposta do usuário captada no microfone";

  JsonObject verbal_3 = verbais_array.createNestedObject();
  verbal_3["pergunta"] = "Lembre-se de um momento hoje em que você precisou de explicar algo ou de entender uma explicação. Como foi essa experiência?";
  verbal_3["resposta"] = "Resposta do usuário captada no microfone";

  JsonObject verbal_4 = verbais_array.createNestedObject();
  verbal_4["pergunta"] = "Houve alguma tarefa ou momento hoje que te deu uma sensação especial de 'trabalho bem feito'?";
  verbal_4["resposta"] = "Resposta do usuário captada no microfone";

  // Perguntas Alternativas

  JsonArray alternativa_array = dados_sentimentos.createNestedArray("perguntas_alternativas");

  JsonObject alternativa_5 = alternativa_array.createNestedObject();
  alternativa_5["pergunta"] = "No geral, você diria que o seu dia de trabalho hoje foi satisfatório?";
  alternativa_5["resposta"] = "Resposta pelo botão sim ou não";

  JsonObject alternativa_6 = alternativa_array.createNestedObject();
  alternativa_6["pergunta"] = "Você sentiu que teve energia suficiente para cumprir as suas tarefas de hoje?";
  alternativa_6["resposta"] = "Resposta pelo botão sim ou não";

  JsonObject alternativa_7 = alternativa_array.createNestedObject();
  alternativa_7["pergunta"] = "Você sente que conseguiu ser produtivo(a) na maior parte do tempo hoje?";
  alternativa_7["resposta"] = "Resposta pelo botão sim ou não";

  JsonObject alternativa_8 = alternativa_array.createNestedObject();
  alternativa_8["pergunta"] = "A sua carga de trabalho hoje pareceu-lhe justa e equilibrada?";
  alternativa_8["resposta"] = "Resposta pelo botão sim ou não";

  JsonObject alternativa_9 = alternativa_array.createNestedObject();
  alternativa_9["pergunta"] = "Hoje, você sentiu-se valorizado(a) pelo seu trabalho ou pelas suas contribuições?";
  alternativa_9["resposta"] = "Resposta pelo botão sim ou não";

  JsonObject alternativa_10 = alternativa_array.createNestedObject();
  alternativa_10["pergunta"] = "Você sentiu que a comunicação com a sua equipa hoje foi clara e eficaz?";
  alternativa_10["resposta"] = "Resposta pelo botão sim ou não";

  JsonObject alternativa_11 = alternativa_array.createNestedObject();
  alternativa_11["pergunta"] = "Os desafios que você enfrentou hoje foram, na sua maioria, do tipo que te estimulam a crescer?";
  alternativa_11["resposta"] = "Resposta pelo botão sim ou não";

  JsonObject alternativa_12 = alternativa_array.createNestedObject();
  alternativa_12["pergunta"] = "Você conseguiu fazer pausas adequadas para descansar a mente durante o dia de hoje?";
  alternativa_12["resposta"] = "Resposta pelo botão sim ou não";

  // Exemplo de Json com somente Objeto vou utilizar esse modelo nos estilos de roupas

  JsonObject alternativa_obj = dados_sentimentos.createNestedObject("Roupas");
  alternativa_obj["pergunta"] = "Você gosta de Trabalhar na Softtek";
  alternativa_obj["resposta"] = "Resposta pelo botão sim ou não";

  serializeJson(dados_sentimentos, Serial); // Pega o conteúdo trasnforma em String de Texto para enviar pela porta serial

  Serial.println(); // Nova linha aqui o Python entende que terminou a mensagem

  delay(5000); // Delay necessário para não lotar a porta serial
}
