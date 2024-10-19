FROM tiangolo/uvicorn-gunicorn:python3.10

ARG MODE

ENV MODE=${MODE}

COPY ./requirements/base.txt .
RUN pip install -r base.txt

ARG COZE_API_TOKEN
ARG COZE_BOT_ID

ENV COZE_API_TOKEN = $COZE_API_TOKEN
ENV COZE_BOT_ID = $COZE_BOT_ID

COPY ./scripts /app
COPY ./ /app
WORKDIR /app
