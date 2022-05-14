# Django-datesAPI
A simple Django REST API storing data in PostgreSQL database and interacting with http://numbersapi.com. The API is deployed to Heroku at https://dashboard.heroku.com/apps/django-dates-api.

## Technologies
### Why Django
I chose Django because:
- it has a perfect library for creating REST APIs - Django REST Framework
- it has a large community and there are many great resources available on the Internet (documentation, tutorials, problems solved by other developers)
- it is a framework I wanted to learn so it was a perfect opportunity to do this

### Why PostgreSQL
I chose PostgreSQL because:
- it is the most preferred database for Django
- it is one of the fastest growing database management systems, alongside its NoSQL brother MongoDB
- I wanted to learn it too
- it is compatible with Heroku

## Requirements
[Docker](https://www.docker.com/get-docker)

You need to be able to at least run the ```docker-compose``` command. If you are using Windows you can download Docker Desktop.

## Usage
I highly recommend using [Postman](https://www.postman.com/downloads/) for sending requests. You can also use its [web app](https://go.postman.co/home) if you don't want to install it.

### Endpoints
- POST /dates (requires a json with month and day)
- DELETE /dates/{id} (requires authorization by passing the correct X-API-KEY)
- GET /dates
- GET /popular

You can make requests to local server as well as to the deployed app on Heroku.

### Local
Open ```settings.py```, scroll to ```DATABASES = { ...``` and make sure the ```'HOST'``` is set to ```'localhost'```. Then open your command line or terminal in the root folder and run

```docker-compose up```

First build may take some time but after that it launches quickly. Now you can send some requests.

To stop the container press ```Ctrl+C```.

### Heroku
You can send requests without any configuration.
