FROM python:3.10-slim as builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY main.py requirements.txt ./
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

# RUN python -m pip show requests


# Final stage
FROM python:3.10-slim-buster

WORKDIR /app

COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .
COPY --from=builder /app/main.py .

RUN python -m venv venv
# Enable venv
# ENV VIRTUAL_ENV venv  
ENV PATH="venv/bin:$PATH" 
RUN which python
# RUN . venv/bin/activate


RUN pip install --no-cache /wheels/*
