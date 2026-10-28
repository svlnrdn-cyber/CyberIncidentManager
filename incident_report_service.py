
class IncidentReportService:
    def __init__(self, priority_calculator):
        self.priority_calculator = priority_calculator

    def create_report(self, incidents):
        total = len(incidents)
        resolved = sum(
            1 for incident in incidents
            if incident.status.value == "Çözüldü"
        )

        risk_counts = {
            "Kritik Risk": 0,
            "Yüksek Risk": 0,
            "Orta Risk": 0,
            "Düşük Risk": 0
        }

        for incident in incidents:
            score = self.priority_calculator.calculate(incident)
            risk = self.priority_calculator.risk_level(score)
            risk_counts[risk] += 1

        return {
            "toplam_olay": total,
            "cozulmus_olay": resolved,
            "acik_olay": total - resolved,
            "risk_dagilimi": risk_counts
        }
