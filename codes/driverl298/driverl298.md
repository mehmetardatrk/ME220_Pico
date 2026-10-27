### ⚙️ L298N Motor Sürücü Bağlantı Tablosu

| L298N Sürücü Pini | Bağlantı Yeri | Açıklama |
| :--- | :--- | :--- |
| **12V / VCC** | Harici Pil / Güç Kaynağı (+) | Motor beslemesi (6V–12V) |
| **GND** | Harici Pil (-) & Pico GND (Pin 38) | Ortak Toprak (GND) hattı şarttır |
| **ENA** | Pico GP16 (Pin 21) | Motor A hız kontrolü (PWM) |
| **IN1** | Pico GP17 (Pin 22) | Motor A yön pini 1 |
| **IN2** | Pico GP18 (Pin 24) | Motor A yön pini 2 |
| **OUT1 & OUT2** | DC Motor Klemensleri | Motora giden iki kablo |
