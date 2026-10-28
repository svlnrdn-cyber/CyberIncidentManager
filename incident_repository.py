
import json
from pathlib import Path

from enums import IncidentPriority, IncidentStatus
from incident_types import MalwareIncident, UnauthorizedAccessIncident


class IncidentRepository:
    def __init__(self, file_path=None):
        # Dosya yolu, programın çalıştırıldığı dizine değil,
        # bu Python dosyasının bulunduğu proje dizinine bağlıdır.
        if file_path is None:
            project_folder = Path(__file__).resolve().parent
            file_path = project_folder / "data" / "incidents.json"

        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

    def save_all(self, incidents):
        data = []

        for incident in incidents:
            data.append({
                "title": incident.title,
                "description": incident.description,
                "priority": incident.priority.name,
                "impact": incident.impact,
                "urgency": incident.urgency,
                "type": incident.incident_type(),
                "status": incident.status.name
            })

        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def load_all(self):
        if not self.file_path.exists():
            return []

        with self.file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        incidents = []

        for item in data:
            priority = IncidentPriority[item["priority"]]
            impact = item.get("impact", 3)
            urgency = item.get("urgency", 3)

            if item["type"] == "Zararlı Yazılım":
                incident = MalwareIncident(
                    item["title"],
                    item["description"],
                    priority,
                    impact,
                    urgency
                )
            elif item["type"] == "Yetkisiz Erişim":
                incident = UnauthorizedAccessIncident(
                    item["title"],
                    item["description"],
                    priority,
                    impact,
                    urgency
                )
            else:
                continue

            status_name = item.get("status", "NEW")
            incident.update_status(IncidentStatus[status_name])
            incidents.append(incident)

        return incidents
