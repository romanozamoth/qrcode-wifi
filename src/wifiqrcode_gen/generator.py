# src/wifiqrcode_gen/generator.py
import os
import qrcode
from PIL import Image, ImageDraw, ImageFont
from typing import Optional
from pathlib import Path

def load_default_logo(size: int = 70) -> ImageFont.FreeTypeFont:
    try:
        logo_path = os.getenv("logo_path",None)
        if not logo_path:
            base_dir = Path(__file__).resolve().parents[2]
            logo_path = base_dir / "assets/logo-test.png"
        return logo_path
    except Exception as e:
        print(f"[AVISO] Não foi possível carregar o logo personalizado.\nCriando imagem sem Logo.\nErro: {e}")
        return None

def load_default_font(size: int = 70) -> ImageFont.FreeTypeFont:
    try:
        font_path = os.getenv("font_path",None)
        if not font_path:
            base_dir = Path(__file__).resolve().parents[2]
            font_path = base_dir / "assets/fonts/DejaVuSans-Bold.ttf"
        return ImageFont.truetype(str(font_path), size)
    except Exception as e:
        print(f"[AVISO] Não foi possível carregar a fonte personalizada.\nUsando fonte padrão.\nErro: {e}")
        return ImageFont.load_default()

def generate_wifi_qr(ssid: str, password: str, security: str = "WPA", hidden: bool = False) -> Image.Image:
    wifi_config = f"WIFI:T:{security};S:{ssid};P:{password};H:{'true' if hidden else 'false'};;"
    qr = qrcode.QRCode(
        version=6,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=30,
        border=4,
    )
    qr.add_data(wifi_config)
    qr.make(fit=True)
    return qr.make_image(fill_color="black", back_color="white").convert('RGB')


def build_full_image(qr_img: Image.Image, ssid: str, password: str) -> Image.Image:
    qr_width, qr_height = qr_img.size
    faixa_sup = int(qr_height * 0.15)
    faixa_inf = int(qr_height * 0.15)
    bloco_h = faixa_sup + qr_height + faixa_inf
    bloco_img = Image.new("RGB", (qr_width, bloco_h), "white")
    draw = ImageDraw.Draw(bloco_img)

    bloco_img.paste(qr_img, (0, faixa_sup))

    # Texto
    try:
        font = load_default_font()
    except IOError:
        font = ImageFont.load_default()

    text = f"Rede: {ssid}\nSenha: {password}"
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    tx = (qr_width - tw) // 2
    ty = faixa_sup + qr_height + (faixa_inf - th) // 2

    draw.rectangle([(0, faixa_sup + qr_height), (qr_width, bloco_h)], fill="black")
    draw.text((tx, ty), text, font=font, fill="white")

    # Logo
    logo_path=load_default_logo()
    if logo_path:
        try:
            logo = Image.open(logo_path).convert("RGBA")
            max_w, max_h = qr_width, faixa_sup
            ratio = min(max_w / logo.width, max_h / logo.height)
            logo = logo.resize((int(logo.width * ratio), int(logo.height * ratio)), Image.LANCZOS)
            lx = (qr_width - logo.width) // 2
            ly = (faixa_sup - logo.height) // 2
            bloco_img.paste(logo, (lx, ly), logo)
        except FileNotFoundError:
            print(f"[AVISO] Logo não encontrado: {logo_path}")

    return bloco_img


def create_a4_image(bloco_img: Image.Image) -> Image.Image:
    a4_width, a4_height = 2480, 3508
    final_img = Image.new("RGB", (a4_width, a4_height), "white")
    pos_x = (a4_width - bloco_img.width) // 2
    pos_y = (a4_height - bloco_img.height) // 2
    final_img.paste(bloco_img, (pos_x, pos_y))
    return final_img


def generate_wifi_qr_image(
    ssid: str,
    password: str,
    security: str = "WPA",
    hidden: bool = False,
    output_path: str = "wifi_qr_code_a4.png"
) -> None:
    qr = generate_wifi_qr(ssid, password, security, hidden)
    bloco = build_full_image(qr, ssid, password)
    final = create_a4_image(bloco)
    final.save(output_path)
    print(f"QR Code salvo em {output_path}")
