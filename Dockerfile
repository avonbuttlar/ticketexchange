FROM python:3.11

WORKDIR /fastapi

COPY ./backend/requirements.txt /backend/requirements.txt
COPY ./backend /fastapi/backend
COPY ./frontend /fastapi/frontend

ENV PYTHONPATH=/fastapi

RUN pip install --no-cache-dir -r /backend/requirements.txt

CMD ["uvicorn", "backend.root:app", "--host", "0.0.0.0", "--port", "5000"]
