from flask import Flask
from flask_cors import CORS
from src.app.routes.AppRoutes import AppRoutes
from src.utils.constants.ServerConstants import ROOT_TEMPLATES, ROOT_STATIC

class Server:
    
    def __init__(self) -> None:
        self.app = Flask(__name__, template_folder=ROOT_TEMPLATES, static_folder=ROOT_STATIC)
        CORS(self.app)
        self.routes = AppRoutes(app=self.app,)
        
    def run(self, port = 5555):
        self.app.run(port=port)
        
    def getApp(self):
        return self.app
    
    def verifyDefaultCamera(self):
        return 0