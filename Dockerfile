FROM python:3.10-slim
RUN apt-get update && apt-get install -y chromium chromium-driver curl unzip && apt-get clean
ENV CHROME_BIN=/usr/bin/chromium
ENV PATH=$PATH:/usr/bin
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /app
WORKDIR /app
CMD ["python", "run_ui_test.py"]
