
from dataclasses import dataclass, field
from enums import IncidentPriority, IncidentStatus


@dataclass
class SecurityIncident:
    title: str
    description: str
    priority: IncidentPriority
    impact: int = 3
    urgency: int = 3
    status: IncidentStatus = field(default=IncidentStatus.NEW)

    def __post_init__(self):
        if not 1 <= self.priority.value <= 4:
            raise ValueError("Önem seviyesi 1 ile 4 arasında olmalıdır.")

        if not 1 <= self.impact <= 5:
            raise ValueError("Etki 1 ile 5 arasında olmalıdır.")

        if not 1 <= self.urgency <= 5:
            raise ValueError("Aciliyet 1 ile 5 arasında olmalıdır.")

    def incident_type(self):
        return "Genel Olay"

    def update_status(self, new_status):
        if not isinstance(new_status, IncidentStatus):
            raise ValueError("Geçersiz olay durumu.")

        self.status = new_status

    def show_info(self):
        print("Olay başlığı:", self.title)
        print("Açıklama:", self.description)
        print("Önem seviyesi:", self.priority.name)
        print("Etki:", self.impact)
        print("Aciliyet:", self.urgency)
        print("Durum:", self.status.value)
