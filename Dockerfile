FROM python:3.6
RUN apt-get update && apt-get install -y \
		gcc \
		gettext \
		sqlite3 \
	--no-install-recommends && rm -rf /var/lib/apt/lists/*

ENV DJANGO_VERSION 2.2.1
RUN pip3 install psycopg2 django=="$DJANGO_VERSION"
RUN mkdir -p /djangotest
COPY . /djangotest
EXPOSE 8000
