from views import index, name

def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/name', name)
    