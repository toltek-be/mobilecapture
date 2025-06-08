FROM python:3.10-slim

# Installation de dépendances système
RUN apt-get update && apt-get install -y \
    wget unzip curl gnupg \
    fonts-liberation libnss3 libxss1 libasound2 libx11-xcb1 \
    libxcomposite1 libxdamage1 libxrandr2 libgbm1 xdg-utils \
    libgconf-2-4 libgtk-3-0 libxext6 libxi6 libxtst6 libxrender1 libxcb1 \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Installer Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get update && apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb

# Installer ChromeDriver (version compatible avec Chrome stable)
RUN CHROME_VERSION=$(google-chrome --version | grep -oP '\d+\.\d+\.\d+') && \
    CHROMEDRIVER_VERSION=$(curl -s "https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json" | \
    python3 -c "import sys, json; print(json.load(sys.stdin)['channels']['Stable']['version'])") && \
    wget -O chromedriver.zip https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/${CHROMEDRIVER_VERSION}/linux64/chromedriver-linux64.zip && \
    unzip chromedriver.zip && \
    mv chromedriver-linux64/chromedriver /usr/bin/chromedriver && \
    chmod +x /usr/bin/chromedriver && \
    rm -rf chromedriver.zip chromedriver-linux64

# Installer Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Ajouter le script
COPY script.py .

# Créer le dossier de sortie
RUN mkdir -p /screenshots

# Exécution du script par défaut
CMD ["python", "script.py"]

