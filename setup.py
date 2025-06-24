# setup.py
from setuptools import setup, find_packages

setup(
    name="qrcode-wifi",
    version="0.1.0",
    description="Gere QR Codes em A4 para redes Wi-Fi com logo e texto.",
    author="Thomaz Romano",
    url="https://github.com/romanozamoth/qrcode-wifi",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "qrcode",
        "pillow",
        "pytest"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
