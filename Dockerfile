FROM python:3.11-bullseye
WORKDIR /app
COPY . .
RUN pip install --upgrade pip
RUN pip install --upgrade pip setuptools
RUN pip install thinc
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["uvicorn", "server:app"]
