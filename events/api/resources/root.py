from flask_restful import Resource


class RootResource(Resource):
    def get(self):
        return {"status": "OK", "version": "v.0.1"}
