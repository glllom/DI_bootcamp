from flask_migrate import Migrate

from project import create_app, db

if __name__ == '__main__':
	app = create_app()
	migrate = Migrate(app, db)
	db.create_all(app=app)

	app.run(debug=True, port=5500)
