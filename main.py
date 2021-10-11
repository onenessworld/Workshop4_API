from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)
rider_data = {'R0': 'Karim', 'R1': 'Manuja', 'R2': 'Phil'}  # Contains ID:Name of riders.


# Resource supporting GET method with no parameters.
class SampleResource(Resource):
    def get(self):
        sample_response = "SampleResource got GET request."
        return sample_response


# Concrete example of RiderResource supporting GET method with rider ID query parameter.
class RiderResource(Resource):
    def get(self):
        get_parser = reqparse.RequestParser()  # From flask library.
        get_parser.add_argument('id', type=str)  # Expect a query param called "id". Replicate this line for each query param.
        args = get_parser.parse_args()  # Stores value of "id" (and any other query params), defaults to None.
        if args.id in rider_data:  # Check if "id" exists.
            sample_response = "Rider with ID *%s* is *%s*" % (args.id, rider_data[args.id])
        else:  # Provided "id" doesn't exist, return a useful message.
            sample_response = "Rider ID *%s* doesn't exist, legal values are: %s"\
                              % (args.id, list(rider_data.keys()))
        return sample_response


# http://localhost:5000/sample_route
api.add_resource(SampleResource, '/sample_route')  # add_resource method maps a url/route to a resource.

# http://localhost:5000/rider
# http://localhost:5000/rider?id=R5
api.add_resource(RiderResource, '/rider')


if __name__ == "__main__":
    app.run()  # Runs web app @ http://localhost:5000 by default for me.
