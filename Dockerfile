FROM python:3.9

WORKDIR /workdir/app

COPY ./requirements.txt /workdir/requirements.txt

RUN python3 -m pip install --upgrade pip &&\
    python3 -m pip install --no-cache-dir -r /workdir/requirements.txt

COPY ./app /workdir/app

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "80"]