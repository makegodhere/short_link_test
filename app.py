from flask import Flask
from flask_restplus import Api
from config.settings import DEBUG, HOST, PORT, BLUEPRINTS, SQLALCHEMY_DATABASE_URI
from config.db import db, ma

app = Flask(
    import_name=__name__
)

# Инициализируем базу данных и схемы Marshmallow
app.config.update({
    'SQLALCHEMY_DATABASE_URI': SQLALCHEMY_DATABASE_URI,
})
db.init_app(app)
ma.init_app(app)

# Инициализируем API
# Требуется организация верисонности API, скорее всего это проще сделать на уровне улов и ресурсов каждого аппа
api = Api(app)

# Импортируем аппы приложения
for blueprint in BLUEPRINTS:
    # Импортируем апп
    module = getattr(__import__(f'{blueprint}.app', fromlist=['blueprint']), 'blueprint')
    app.register_blueprint(
        blueprint=module
    )

    # Импортируем модели и схемы аапов
    models = __import__(f'{blueprint}.models')
    schemas = __import__(f'{blueprint}.schemas')

    # Импортируем урлы аппов
    urls = getattr(__import__(f'{blueprint}.urls', fromlist=['urls']), 'urls')
    for url in urls:
        api.add_resource(*url)


if __name__ == '__main__':
    app.debug = DEBUG
    app.run(
        host=HOST,
        port=PORT,
    )
