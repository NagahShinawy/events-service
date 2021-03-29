from flask_restful import Resource


class UserResource(Resource):

    def get(self):
        return {"data": [
            {
                "user": "test",
                "email": "test@test.com"
            }
        ]}