FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBFFERED 1

WORKDIR /app

#Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

#Copy the current directory
COPY . /app/

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000", "--noreload" ]
