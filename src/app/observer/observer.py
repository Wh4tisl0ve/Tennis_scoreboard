from __future__ import annotations
from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def notify_subscribers(self):
        pass

    @abstractmethod
    def attach(self, observer: Observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        pass


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject):
        pass
