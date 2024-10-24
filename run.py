from app import create_app, db
from app.models import User

app = create_app()

@app.cli.command("init-db")
def init_db():
    """Initialize the database."""
    db.create_all()
    
    # Create admin user if it doesn't exist
    admin = User.query.filter_by(username='admin').first()
    if not admin:
        admin = User(
            username='admin',
            email='admin@example.com',
            password='Admin123!',
            is_admin=True
        )
        db.session.add(admin)
        db.session.commit()
        print('Admin user created successfully.')
    print('Database initialized successfully.')

if __name__ == '__main__':
    app.run()