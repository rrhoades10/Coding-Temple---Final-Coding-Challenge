from app import create_app, cli, db

from app.blueprints.auth.models import User

app = create_app()
cli.register(app)

@app.shell_context_processor
def make_context():
    return dict(db=db, User=User)