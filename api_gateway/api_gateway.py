from elasticsearch import Elasticsearch
from flask_restful import Resource, Api
from flask import Flask, Response, make_response, json


app = Flask(__name__)
api = Api(app)

es = Elasticsearch(
    cloud_id="CS6200_Final_Project:dXMtd2VzdC0xLmF3cy5mb3VuZC5pbyQ4NmM4OTlmMTgxMTc0MjgzODdlN2E0NTMxNWVlYTFjMiQxNGZhZDc5NzhmNGU0N2UyOGMwNDIxYTEyYzVjZDFjNA==",
    http_auth=("elastic", "zC9IE0Nh8xek7eJAxVo02mZM"),
)


class ElasticsearchProxy(Resource):
    def get(self, query):
        res = es.search(
            index='s&p500',
            body={
                "query": {
                    "match": {
                        "title": query
                    }
                }
            },
            size=1000
        )
        return Response(
            json.dumps(res['hits']['hits']),
            headers={'Access-Control-Allow-Origin': '*'}
        )


api.add_resource(ElasticsearchProxy, '/<string:query>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
