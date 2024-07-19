FROM python:3.9-slim
RUN pip install flask
COPY . /app
WORKDIR /app
EXPOSE 8080
CMD ["python", "app.py"]
