from src.domain.entities.order import Order
from abc import ABC, abstractmethod

class OrderService(ABC):

    @abstractmethod
    def create_order(self, order: Order):
        pass
    @abstractmethod
    def delete_order(self, order_id):
        pass
    
    @abstractmethod
    def get_order(self, order_id):
        pass
    
    @abstractmethod
    def get_all_orders(self):
        pass
    
    @abstractmethod
    def update_order(self, order_id, order):
        pass
    
    @abstractmethod
    def update_order_status(self, order_id, new_status):
        pass