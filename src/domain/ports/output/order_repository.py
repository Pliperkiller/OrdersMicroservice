from abc import ABC, abstractmethod
from src.domain.entities.order import Order

class OrderRepository(ABC):
    @abstractmethod
    def create(self, order:Order):
        pass

    @abstractmethod
    def get_by_id(self, order_id:int):
        pass

    @abstractmethod
    def update(self, order_id : int ,order:Order):
        pass

    @abstractmethod
    def delete(self, order_id:int):
        pass

    @abstractmethod
    def get_all(self):
        pass