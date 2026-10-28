
from abc import ABC, abstractmethod


class PriorityStrategy(ABC):
    @abstractmethod
    def calculate(self, incident):
        pass


class StandardPriorityStrategy(PriorityStrategy):
    def calculate(self, incident):
        return (
                10 * incident.priority.value
                + 5 * incident.impact
                + 3 * incident.urgency
        )


class CriticalAssetStrategy(PriorityStrategy):
    def calculate(self, incident):
        return (
                10 * incident.priority.value
                + 8 * incident.impact
                + 3 * incident.urgency
        )
