from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app.models import User
from app import db
from app.utils.decorators import admin_required
from app.utils.validators import validate_email, validate_password

users_bp = Blueprint('users', __name__)

@users_bp.route('/', methods=['GET'])
@jwt_required()
@admin_required
def get_users():
    try:
        users = User.query.all()
        return jsonify({
            'users': [user.to_dict() for user in users]
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@users_bp.route('/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    try:
        current_user_id = get_jwt_identity()
        claims = get_jwt()
        
        if current_user_id != user_id and not claims.get('is_admin'):
            return jsonify({'error': 'Unauthorized access'}), 403
        
        user = User.query.get_or_404(user_id)
        return jsonify({'user': user.to_dict()})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@users_bp.route('/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    try:
        current_user_id = get_jwt_identity()
        claims = get_jwt()
        
        if current_user_id != user_id and not claims.get('is_admin'):
            return jsonify({'error': 'Unauthorized access'}), 403
        
        user = User.query.get_or_404(user_id)
        data = request.get_json()
        
        if 'email' in data:
            if not validate_email(data['email']):
                return jsonify({'error': 'Invalid email format'}), 400
            existing_user = User.query.filter_by(email=data['email']).first()
            if existing_user and existing_user.id != user_id:
                return jsonify({'error': 'Email already exists'}), 409
            user.email = data['email']
        
        if 'password' in data:
            is_valid, msg = validate_password(data['password'])
            if not is_valid:
                return jsonify({'error': msg}), 400
            user.password = data['password']
        
        if 'is_active' in data and claims.get('is_admin'):
            user.is_active = data['is_active']
        
        db.session.commit()
        return jsonify({
            'message': 'User updated successfully',
            'user': user.to_dict()
        })
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@users_bp.route('/<int:user_id>', methods=['DELETE'])
@jwt_required()
@admin_required
def delete_user(user_id):
    try:
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'})
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500