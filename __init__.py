import flask
import app as flaskapp


if __name__ == '__main__':
    app = flaskapp.create_app()
    app.run(
        host='0.0.0.0',
        port=8080
    )