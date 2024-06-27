FROM python:3.12
WORKDIR /code
COPY . /code/
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install
CMD ["poetry", "run", "uvicorn", "class4_helloworld.main:app", "--reload"]