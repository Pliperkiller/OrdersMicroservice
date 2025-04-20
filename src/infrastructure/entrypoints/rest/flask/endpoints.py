# src/interfaces/routes/order_routes.py
from flask import Blueprint, request, jsonify
from src.infrastructure.entrypoints.rest.controllers.order_controller import OrderController
from src.application.services.order_service import OrderService
from src.infrastructure.adapters.repositories.pg_order_item_repository import PgOrderItemRepository
from src.infrastructure.adapters.repositories.pg_order_repository import PgOrderRepository
from src.infrastructure.adapters.repositories.pg_product_repository import PgProductRepository
from src.infrastructure.database.models.table_base_model import db

order_blueprint = Blueprint('orders', __name__)

order_service = OrderService(
    order_repository=PgOrderRepository(),
    order_item_repository=PgOrderItemRepository(),
    product_repository=PgProductRepository()
)
order_controller = OrderController(order_service)

@order_blueprint.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    response, status = order_controller.create_order(data)
    return jsonify(response), status

@order_blueprint.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    response, status = order_controller.get_order(order_id)
    return jsonify(response), status

@order_blueprint.route('/orders/<int:order_id>/status', methods=['PUT'])
def update_order_status(order_id):
    data = request.get_json()
    response, status = order_controller.update_order_status(order_id, data)
    return jsonify(response), status

@order_blueprint.route('/orders', methods=['GET'])
def get_all_orders():
    response, status = order_controller.get_all_orders()
    return jsonify(response), status

@order_blueprint.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    response, status = order_controller.delete_order(order_id)
    return jsonify(response), status

@order_blueprint.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "API is running"}), 200

@order_blueprint.route('/health/db', methods=['GET'])
def database_health_check():
    try:
        db.session.execute('SELECT 1')
        return jsonify({"status": "Database connection is healthy"}), 200
    except Exception as e:
        return jsonify({"status": "Database connection failed", "error": str(e)}), 500