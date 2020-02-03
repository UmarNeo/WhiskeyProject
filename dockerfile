FROM tiangolo/uwsgi-nginx-flask:python3.5

RUN pip install flask
RUN pip install flask-cors
RUN pip install pandas
RUN pip install sklearn


WORKDIR /app/
COPY . .


#CMD uwsgi --master --http 0.0.0.0:80 --wsgi-file /app/app.py --callable app --processes 2 --threads 2 --stats 127.0.0.1:9292 --socket-timeout 6000 --http-timeout 6000

#CMD python app.py
