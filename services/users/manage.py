# services/users/manage.py

from flask.cli import FlaskGroup

from project import app

cli = FlaskGroup(app)


@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session_commit()


if __name__ == '__main__':
    cli()