
from incident_types import MalwareIncident, UnauthorizedAccessIncident


class IncidentFactory:
    @staticmethod
    def create(incident_type, title, description, priority, impact, urgency):
        if incident_type == "1":
            return MalwareIncident(
                title, description, priority, impact, urgency
            )

        if incident_type == "2":
            return UnauthorizedAccessIncident(
                title, description, priority, impact, urgency
            )

        raise ValueError("Geçersiz güvenlik olayı türü.")
