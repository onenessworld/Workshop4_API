# Workshop 4

In this workshop, we'll be extending our previous project into an API.

Make sure to have these dependencies added to your project interpreter in PyCharm.

 1. [Flask](https://flask.palletsprojects.com/en/1.1.x/)
 2. [Flask-RESTful](https://flask-rescful.readthedocs.io/en/latest/)
 3. [flask-mongoengine](https://docs.mongoengine.org/projects/flask-mongoengine/en/latest/)

 <b> Flask </b> is a framework that allows us to easily setup a web server with Python. It's a bit minimalistic, so to make it work better for our needs we add Flask-RESTful, which introduces a lot of helpful methods to handle creating a REST API. Flask-mongoengine is the same as the mongoengine we've used previously; it just adds a little more code to integrate mongoengine with our Flask app.
 ## Routing 
By default, Flask supports routing with '@' decorators
```
@app.route('/')
def hello_world():
    return 'Hello World!'
```

This means that our server will return 'Hello World!' whenever we make an GET call on localhost:5000/
