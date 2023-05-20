FROM python:3.11.3-slim
COPY *.py /app/
COPY Scores.txt /app/
COPY templates/* /app/templates/
COPY tests/* /app/tests/
RUN pip install -r requirements.txt

# Download and install ChromeDriver
RUN wget -q https://chromedriver.storage.googleapis.com/$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip -O /tmp/chromedriver.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    rm /tmp/chromedriver.zip

CMD python /app/MainScores.py