FROM python:3

ADD pythontest.py /

RUN pip install --upgrade pip
RUN pip install pystrich
RUN pip install psycopg2
RUN pip install pandas
RUN pip install Flask
RUN pip install Flask-Cors

CMD [ "python", "./pythontest.py" ]