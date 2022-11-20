FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
COPY /backend/requirements.txt /backend/
RUN pip install -r /backend/requirements.txt
COPY ./model /model/
COPY ./bacckend /backend