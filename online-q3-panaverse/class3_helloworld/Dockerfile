FROM python:3.12
ADD ./pyproject.toml /code/
ADD ./class3_helloworld /code/class3_helloworld/
WORKDIR /code
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install
CMD ["poetry", "run", "uvicorn", "class3_helloworld.main:app", "--host", "0.0.0.0", "--reload"]