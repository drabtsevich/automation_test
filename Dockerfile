FROM python:3.11-slim

# System dependencies for playwright
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    gnupg \
    libglib2.0-0 \
    libnss3 \
    libfontconfig1 \
    libxcb1 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libasound2 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libxshmfence1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

# install python deps
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# install playwright browsers
RUN playwright install --with-deps

# default command to run tests
CMD ["pytest", "--alluredir=allure-results"]