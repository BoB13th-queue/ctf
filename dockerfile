FROM alpine:3.20.3

RUN apk add --no-cache python3 py3-pip

ADD ./requirements.txt /back/requirements.txt
WORKDIR /back
RUN \
python3 -m venv .venv &&\
source .venv/bin/activate &&\
pip install -r requirements.txt

ADD . /back

CMD ["/bin/sh", "-c", ". .venv/bin/activate && python3 main.py"]