from project.core import create_app
from project.settings.constants import FLASK_HOST, FLASK_PORT

app = create_app()

if __name__ == "__main__":
    app.run(host=FLASK_HOST, port=FLASK_PORT)
