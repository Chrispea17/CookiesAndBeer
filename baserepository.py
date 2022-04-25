from abc import ABC, abstractmethod
from typing import List

from recommendations import Recommendation

class BaseRepository(ABC):

    @abstractmethod
    def add_one(recommendation) -> int:
        raise NotImplementedError("Derived classes must implement add_one")

    @abstractmethod
    def add_many(recommendations) -> int:
        raise NotImplementedError("Derived classes must implement add_many")

    @abstractmethod
    def delete_one(recommendation) -> int:
        raise NotImplementedError("Derived classes must implement delete_one")

    @abstractmethod
    def delete_many(recommendations) -> int:
        raise NotImplementedError("Derived classes must implement delete_many")

    @abstractmethod
    def update(recommendation) -> int:
        raise NotImplementedError("Derived classes must implement update")

    @abstractmethod
    def update_many(recommendations) -> int:
        raise NotImplementedError("Derived classes must implement update_many")

    @abstractmethod
    def find_first(query) -> Recommendation:
        raise NotImplementedError("Derived classes must implement find_first")

    @abstractmethod
    def find_all(query) -> list[Recommendation]:
        raise NotImplementedError("Derived classes must implement find_all")