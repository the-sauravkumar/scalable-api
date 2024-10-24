import json
import pytest
from app.models import User

def test_register(client, db_init):
    """Test user registration"""
    response = client.post('/api/auth/register', 
        json={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'TestPass123!'
        }
    )
    assert response.status_code == 201
    data = json.loads(response.data)
    assert 'user' in data
    assert data['user']['username'] == 'testuser'

def test_register_duplicate_username(client, db_init):
    """Test registration with duplicate username"""
    # First registration
    client.post('/api/auth/register', 
        json={
            'username': 'testuser',
            'email': 'test1@example.com',
            'password': 'TestPass123!'
        }
    )
    
    # Second registration with same username
    response = client.post('/api/auth/register', 
        json={
            'username': 'testuser',
            'email': 'test2@example.com',
            'password': 'TestPass123!'
        }
    )
    assert response.status_code == 409

def test_login_success(client, db_init):
    """Test successful login"""
    # Register user
    client.post('/api/auth/register', 
        json={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'TestPass123!'
        }
    )
    
    # Login
    response = client.post('/api/auth/login',
        json={
            'username': 'testuser',
            'password': 'TestPass123!'
        }
    )
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'token' in data

def test_login_invalid_credentials(client, db_init):
    """Test login with invalid credentials"""
    response = client.post('/api/auth/login',
        json={
            'username': 'nonexistent',
            'password': 'WrongPass123!'
        }
    )
    assert response.status_code == 401