FROM python:3.7.5

WORKDIR /vvwo

RUN pip install pipenv
COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install

COPY . .

ENTRYPOINT ["pipenv", "run"]
CMD ["python", "main.py"]
