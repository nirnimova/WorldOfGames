FROM python:3.11.3-slim
COPY *.py /app/
COPY Scores.txt /app/
COPY templates/* /app/templates/
RUN pip install flask
CMD python /app/MainScores.py