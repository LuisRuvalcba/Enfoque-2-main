#define TRIGGER_PIN 2
#define ECHO_PIN 3

void setup() {
  Serial.begin(9600);
  pinMode(TRIGGER_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
}

void loop() {
  long duration, distancia;
  
  // Generar un pulso corto en el pin de trigger
  digitalWrite(TRIGGER_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIGGER_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIGGER_PIN, LOW);
  
  // Medir la duración del pulso de eco
  duration = pulseIn(ECHO_PIN, HIGH);
  
  // Calcular la distancia en centímetros
  distancia = duration * 0.034 / 2;
  
  // Mostrar la distancia medida en el monitor serial
  Serial.print("Distancia: ");
  Serial.print(distancia);
  Serial.println(" cm");
  
  delay(1000);  // Esperar 1 segundo antes de la próxima lectura
}
