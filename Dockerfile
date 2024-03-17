FROM python:3.11-bullseye
WORKDIR /app
COPY . .
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y ffmpeg
RUN pip install --upgrade pip && \
    pip install --upgrade pip setuptools && \
    pip install thinc && \
    pip install --no-cache-dir -r requirements.txt
EXPOSE 8081
CMD ["uvicorn", "server:app", "--port", "8081"]
