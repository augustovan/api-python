from flask import Flask
from flask_restplus import Api

class Server():
    def __init__(self, ):
        self.app = Flask(__name__)
        self.api = Api(self.app,
            version='1.0',
            title='Sample Book API',
            description='A simple book API',
            doc='/docs'
        )

    def run(self, ):
        self.app.run(
            debug=True,
            port=5000
        )

server = Server()