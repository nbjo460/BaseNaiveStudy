FROM python:3.12

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY excell/ excell/
COPY csv/ csv/
COPY Python/ Python/
COPY server/ server/
COPY templates/ templates/
COPY static/ static/
CMD ["uvicorn", "server.run_server:app", "--host", "0.0.0.0", "--port", "8002"]





