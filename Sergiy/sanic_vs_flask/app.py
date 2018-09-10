from sanic import Sanic, response


def create_app():
    app = Sanic()

    register_routes(app)

    return app

def register_routes(app):

    @app.route('/')
    async def test(request):
        return response.text('Hello, World!')

    @app.route('/calc')
    async def calc(request):
        my_list = [x for x in range(10000)]
        return response.json({'list': my_list}, status=200)
