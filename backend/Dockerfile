FROM python:3.8
WORKDIR /backend

# Install app reqs and copy src
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

CMD python main.py