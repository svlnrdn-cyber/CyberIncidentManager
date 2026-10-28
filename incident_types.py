
from security_incident import SecurityIncident


class MalwareIncident(SecurityIncident):
    def incident_type(self):
        return "Zararlı Yazılım"
    def show_info(self):
        print("Olay türü: Zararlı Yazılım")
        super().show_info()


class UnauthorizedAccessIncident(SecurityIncident):
    def incident_type(self):
        return "Yetkisiz Erişim"
    def show_info(self):
        print("Olay türü: Yetkisiz Erişim")
        super().show_info()
