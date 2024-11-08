from routes.api import api_router


def boot(app):
    app.include_router(api_router, prefix="")

    if app.debug:
        for route in app.routes:
            print({'path': route.path, 'name': route.name, 'methods': route.methods})
