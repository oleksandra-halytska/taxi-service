FROM python:3.11


WORKDIR /app

# Install any OS packages needed to run Chromium
RUN apt-get update && apt-get install -y \
    libnss3 \
    libxss1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    wget \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

RUN pip install playwright
RUN playwright install
RUN playwright install --with-deps

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .



EXPOSE 8000


CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
