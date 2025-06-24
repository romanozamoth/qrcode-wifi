import pytest
from PIL import Image
from wifiqrcode_gen.generator import (
    generate_wifi_qr,
    build_full_image,
    create_a4_image
)

# --- TESTE SIMPLES DE GERAR QR
def test_generate_wifi_qr_returns_image():
    ssid = "TestSSID"
    password = "TestPassword"
    qr_img = generate_wifi_qr(ssid, password)
    assert isinstance(qr_img, Image.Image)
    assert qr_img.size[0] > 0 and qr_img.size[1] > 0


# --- TESTE DO BLOCO COMPLETO
def test_build_full_image_returns_image():
    ssid = "TestSSID"
    password = "TestPassword"
    qr_img = generate_wifi_qr(ssid, password)
    bloco_img = build_full_image(qr_img, ssid, password)
    assert isinstance(bloco_img, Image.Image)
    assert bloco_img.size[1] > qr_img.size[1]  # Deve incluir faixa superior/inferior


# --- TESTE DA IMAGEM FINAL EM A4
def test_create_a4_image_dimensions():
    ssid = "TestSSID"
    password = "TestPassword"
    qr_img = generate_wifi_qr(ssid, password)
    bloco_img = build_full_image(qr_img, ssid, password)
    a4_img = create_a4_image(bloco_img)
    assert a4_img.size == (2480, 3508)
