
class IncidentService:
    def __init__(self, repository):
        self.repository = repository
        self.incidents = self.repository.load_all()

    def list_all(self):
        return list(self.incidents)

    def add(self, incident):
        self.incidents.append(incident)
        self.repository.save_all(self.incidents)

    def delete(self, index):
        if not 0 <= index < len(self.incidents):
            raise IndexError("Geçersiz olay numarası.")

        deleted = self.incidents.pop(index)
        self.repository.save_all(self.incidents)
        return deleted

    def search(self, keyword):
        keyword = keyword.casefold()

        return [
            incident for incident in self.incidents
            if keyword in incident.title.casefold()
        ]

    def update_status(self, index, status):
        if not 0 <= index < len(self.incidents):
            raise IndexError("Geçersiz olay numarası.")

        self.incidents[index].update_status(status)
        self.repository.save_all(self.incidents)
