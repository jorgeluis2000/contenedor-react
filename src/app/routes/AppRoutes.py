from flask import Flask, render_template, Response, jsonify, request
from src.utils.function.ColorTransform import hex_to_rgb, rgbToHsv, rgbToBgr

class AppRoutes:

    def __init__(self, app: Flask) -> None:
        self.app = app
        self.router()

    def router(self):

        @self.app.after_request
        def add_header(response: Response) -> Response:
            response.headers['Cache-Control'] = 'no-store'
            return response

        @self.app.route('/api/wave/<string:name>')
        def wave_someone(name) -> Response:
            return jsonify({
                "ok": True,
                "message": f'Hola {name}'
            })

        @self.app.route('/api/wave')
        def get_wave() -> Response:
            return jsonify({
                "ok": True,
                "message": "Hola mundo!!"
            })

        @self.app.route('/')
        def pagina():
            return render_template('index.html')
            

