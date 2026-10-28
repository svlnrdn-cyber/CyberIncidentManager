
from priority_strategy import StandardPriorityStrategy


class PriorityCalculator:
    def __init__(self, strategy=None):
        self.strategy = strategy or StandardPriorityStrategy()

    def calculate(self, incident):
        return self.strategy.calculate(incident)

    def risk_level(self, score):
        if score >= 65:
            return "Kritik Risk"
        elif score >= 45:
            return "Yüksek Risk"
        elif score >= 25:
            return "Orta Risk"
        else:
            return "Düşük Risk"
