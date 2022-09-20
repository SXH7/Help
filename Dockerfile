FROM python:3.10
WORKDIR /main
COPY requirements.txt /main/
RUN pip install -r requirements.txt
COPY . /bot
CMD python main.py
