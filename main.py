from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)


# Minimal Resource supporting GET method.
class HelloWorld(Resource):
    def get(self):
        return "Hello, World!"


# Resource supporting GET method with parameters.
class SampleResource(Resource):
    def get(self):
        get_parser = reqparse.RequestParser()  # From flask library.
        get_parser.add_argument('sample_param', type=str)  # Expect a query param called "sample_param".
        args = get_parser.parse_args()  # Stores value of sample param, defaults to None.
        sample_response = "GET parameter *sample_param* got value: *%s*" % args.sample_param
        return sample_response


# Resource supporting GET method with optional resource ID.
class AnotherResource(Resource):
    def get(self, resource_id=None):
        if resource_id:  # If resource ID is provided, GET matching resource.
            sample_response = "GET with resource ID: *%s*" % resource_id
        else:  # Else, print an error or GET all resources.
            sample_response = "GET with no resource ID: this is either an error, or an opportunity to display all " \
                              "available resource. "
        return sample_response


# http://localhost:5000/
api.add_resource(HelloWorld, '/')

# http://localhost:5000/sample_route
# http://localhost:5000/sample_route?sample_param=some_random_value
api.add_resource(SampleResource, '/sample_route')

# http://localhost:5000/another_route
# http://localhost:5000/another_route/some_resource_id
api.add_resource(AnotherResource, '/another_route', '/another_route/<string:resource_id>')


if __name__ == "__main__":
    app.run()  # Runs web app @ http://localhost:5000 by default for me.
