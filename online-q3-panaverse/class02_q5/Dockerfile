FROM python:3.12
COPY . /code/
WORKDIR /code/
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install
CMD ["poetry", "run", "uvicorn", "class02_q5.main:app", "--reload"]