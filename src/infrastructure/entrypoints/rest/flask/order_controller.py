from flask import Blueprint, request, jsonify
from src.domain.entities.order_item import OrderItem
from application.services.order_service import OrderService
order_blueprint = Blueprint('orders', __name__)

class OrderController:
    def __init__(self, order_service : OrderService):
        self.order_service = order_service
        
    def register_routes(self, blueprint):
        @blueprint.route('/orders', methods=['POST'])
        def create_order():
            data = request.get_json()
            client_id = data.get('client_id')
            items = data.get('items', [])
            
            if not client_id or not items:
                return jsonify({'error': 'Se requiere client_id y e items'}), 400
            
            order_items = []
            for item in items:
                product_id = item.get('productId')
                amount = item.get('amount')
            
                order_item = OrderItem(item_id=item_id, amount=amount)
                order_items.append(order_item)                

            
            order = self.order_service.create_order(client_id, items)
            return jsonify(order.to_dict()), 201
        
        @blueprint.route('/orders/<int:order_id>', methods=['GET'])
        def get_order(order_id):
            order = self.order_service.get_order(order_id)
            if not order:
                return jsonify({'error': 'Pedido no encontrado'}), 404
            return jsonify(order.to_dict()), 200
        
        @blueprint.route('/orders/<int:order_id>/status', methods=['PUT'])
        def update_order_status(order_id):
            data = request.get_json()
            new_status = data.get('status')
            
            if not new_status:
                return jsonify({'error': 'Se requiere el estado nuevo'}), 400
            
            order = self.order_service.update_order_status(order_id, new_status)
            if not order:
                return jsonify({'error': 'Pedido no encontrado o estado inválido'}), 404
            
            return jsonify(order.to_dict()), 200
        
        @blueprint.route('/orders', methods=['GET'])
        def get_all_orders():
            orders = self.order_service.get_all_orders()
            return jsonify([order.to_dict() for order in orders]), 200
            
        @blueprint.route('/orders/<int:order_id>/items/<int:item_id>', methods=['PUT'])
        def update_order_item(order_id, item_id):
            data = request.get_json()
            amount = data.get('amount')
            
            if not amount:
                return jsonify({'error': 'Se requiere la cantidad'}), 400
                
            item = self.order_service.update_order_item(order_id, item_id, amount)
            if not item:
                return jsonify({'error': 'Pedido o item no encontrado'}), 404
                
            return jsonify(item.to_dict()), 200
            
        @blueprint.route('/orders/<int:order_id>/items/<int:item_id>', methods=['DELETE'])
        def remove_order_item(order_id, item_id):
            result = self.order_service.remove_order_item(order_id, item_id)
            if not result:
                return jsonify({'error': 'Pedido o item no encontrado'}), 404
                
            return jsonify({'message': 'Item eliminado correctamente'}), 200