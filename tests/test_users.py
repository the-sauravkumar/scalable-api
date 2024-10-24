import json
import pytest
from flask_jwt_extended import create_access_token

@pytest.fixture
def admin_token(app):
    """Create admin token for testing"""
    with app.app_context():
        return create_access_token(identity=1, additional_claims={'is_admin': True})

@pytest.fixture
def user_token(app):
    """Create regular user token for testing"""
    with app.app_context():
        return create_access_token(identity=2, additional_claims={'is_admin': False})

def test_get_users_admin(client, db_init, admin_token):
    """Test getting all users as admin"""
    response = client.get('/api/users/',
        headers={'Authorization': f'Bearer {admin_token}'}
    )
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'users' in data

def test_get_users_unauthorized(client, db_init, user_token):
    """Test getting all users as non-admin"""
    response = client.get('/api/users/',
        headers={'Authorization': f'Bearer {user_token}'}
    )
    assert response.status_code == 403

def test_get_user_profile(client, db_init, user_token):
    """Test getting own user profile"""
    response = client.get('/api/users/2',
        headers={'Authorization': f'Bearer {user_token}'}
    )
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'user' in data

def test_update_user(client, db_init, user_token):
    """Test updating user profile"""
    response = client.put('/api/users/2',
        headers={'Authorization': f'Bearer {user_token}'},
        json={
            'email': 'newemail@example.com'
        }
    )
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['user']['email'] == 'newemail@example.com'

def test_delete_user_admin(client, db_init, admin_token):
    """Test deleting user as admin"""
    response = client.delete('/api/users/2',
        headers={'Authorization': f'Bearer {admin_token}'}
    )
    assert response.status_code == 200

def test_delete_user_unauthorized(client, db_init, user_token):
    """Test deleting user as non-admin"""
    response = client.delete('/api/users/1',
        headers={'Authorization': f'Bearer {user_token}'}
    )
    assert response.status_code == 403