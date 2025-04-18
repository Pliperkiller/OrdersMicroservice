from abc import ABC, abstractmethod
from src.domain.entities.order_item import OrderItem

class CreateOrderUsecase(ABC):
    @abstractmethod
    def create_order(self, client_id:int, order_items:list[OrderItem]):
        pass

