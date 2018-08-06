from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app import create_app

app = create_app('app.config')
app.config.from_object('app.config')

migrate = Migrate(app)
manager = Manager(app)
manager.add_command("runserver",
                    Server(host='0.0.0.0',
                           port=12341,
                           use_debugger=True))

if __name__ == '__main__':
    manager.run()