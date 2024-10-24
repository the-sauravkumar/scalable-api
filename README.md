# scalable-api

A simple authentication API built with Flask, providing user management features, JWT authentication, and email functionalities for password reset.

## Project Structure

```
flask-auth-api/
├── .env                    # Environment variables
├── .gitignore              # Git ignore file
├── README.md               # Project documentation
├── requirements.txt        # Project dependencies
├── config.py               # Configuration settings
├── run.py                  # Application entry point
├── tests/                  # Test directory
│   ├── __init__.py
│   ├── test_auth.py        # Authentication tests
│   └── test_users.py       # User management tests
└── app/                    # Application package
    ├── __init__.py        # App initialization
    ├── models/             # Database models
    │   ├── __init__.py
    │   └── user.py
    ├── routes/             # API routes
    │   ├── __init__.py
    │   ├── auth.py
    │   └── users.py
    ├── utils/              # Utility functions
    │   ├── __init__.py
    │   ├── validators.py
    │   └── decorators.py
    ├── schemas/            # API schemas
    │   ├── __init__.py
    │   └── user.py
    └── templates/          # Email templates (optional)
        └── reset_password.html
```

## Features

- User registration and login with JWT authentication
- Password reset functionality via email
- User data validation
- Test cases for authentication and user management

## Getting Started

### Prerequisites

- Python 3.7 or higher
- `pip` (Python package installer)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/the-sauravkumar/scalable-api.git
   cd scalable-api
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and configure your environment variables:
   ```plaintext
   SECRET_KEY=your_secret_key
   DATABASE_URL=sqlite:///users.db
   JWT_SECRET_KEY=your_jwt_secret_key
   MAIL_SERVER=smtp.gmail.com
   MAIL_PORT=587
   MAIL_USE_TLS=true
   MAIL_USERNAME=your_email@gmail.com
   MAIL_PASSWORD=your_email_password
   MAIL_DEFAULT_SENDER=your_email@gmail.com
   ```

### Running the Application

To start the Flask application, run:
```bash
python run.py
```

The API will be available at `http://127.0.0.1:5000`.

### Running Tests

To run the tests, ensure the virtual environment is activated and run:
```bash
pytest tests/
```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request for any improvements or fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Saurav Kumar
```

You can copy this content directly into your `README.md` file. Let me know if you need any more modifications!
