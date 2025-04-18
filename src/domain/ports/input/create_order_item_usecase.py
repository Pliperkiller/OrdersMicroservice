from abc import ABC, abstractmethod
from src.domain.entities.order_item import OrderItem

class CreateOrderItemUsecase(ABC):
    @abstractmethod
    def create_order_item(self, order_id ,order_item:OrderItem):
        pass
