![Work in Progress](https://img.shields.io/badge/status-in--progress-orange)

# QR Code WiFi Generator

Gere QR codes estilizados para redes Wi-Fi com suporte a logo e saída em tamanho A4 (ideal para impressão).

## Requisitos
```bash
pip install -r requirements.txt
```

## Exemplo de Uso
```bash
python examples/example_run.py
```
_________________
### Parâmetros
```bash
ssid: Nome da rede Wi-Fi
password: Senha
security: WPA (padrão), WEP ou "" (sem senha)
hidden: True/False
logo_path: Caminho para o logo opcional
```
 or
### .env file
```bash
ssid="WifiTest"
password="PassTest"
security="WPA" #(padrão), "WEP" ou "" (sem senha)
hidden=False # or True
logo_path="assets\logo-test.png" # Opcional
font_path="assets\fonts\DejaVuSans-Bold.ttf"
```

_________________
## 📁 Project Structure
```bash
qrcode-wifi/
├── src/
│   └── wifiqrcode_gen/
│       ├── __init__.py
│       └── generator.py
├── assets/
│   ├── logo-test.png
│   └── fonts/
│       └──DejaVuSans-Bold.ttf
├── examples/
│   └── example_run.py
├── tests/
│   └── test_generator.py
├── requirements.txt
├── setup.py
├── README.md
├── .gitignore
├── .env
└── LICENSE
```