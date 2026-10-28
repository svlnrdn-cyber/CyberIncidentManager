
import unittest

from enums import IncidentPriority, IncidentStatus
from incident_types import MalwareIncident, UnauthorizedAccessIncident
from priority_calculator import PriorityCalculator
from priority_strategy import CriticalAssetStrategy


class TestCyberIncidentManager(unittest.TestCase):

    def setUp(self):
        self.calculator = PriorityCalculator()
        self.incident = MalwareIncident(
            "Test Zararlı Yazılım",
            "Test açıklaması",
            IncidentPriority.HIGH,
            4,
            3
        )

    def test_incident_title(self):
        self.assertEqual(self.incident.title, "Test Zararlı Yazılım")

    def test_incident_description(self):
        self.assertEqual(self.incident.description, "Test açıklaması")

    def test_incident_priority(self):
        self.assertEqual(self.incident.priority, IncidentPriority.HIGH)

    def test_default_status_is_new(self):
        self.assertEqual(self.incident.status, IncidentStatus.NEW)

    def test_update_status(self):
        self.incident.update_status(IncidentStatus.INVESTIGATING)
        self.assertEqual(
            self.incident.status,
            IncidentStatus.INVESTIGATING
        )

    def test_resolved_status(self):
        self.incident.update_status(IncidentStatus.RESOLVED)
        self.assertEqual(self.incident.status, IncidentStatus.RESOLVED)

    def test_priority_calculation(self):
        score = self.calculator.calculate(self.incident)
        self.assertEqual(score, 59)

    def test_risk_level_high(self):
        score = self.calculator.calculate(self.incident)
        self.assertEqual(
            self.calculator.risk_level(score),
            "Yüksek Risk"
        )

    def test_malware_incident_type(self):
        self.assertEqual(
            self.incident.incident_type(),
            "Zararlı Yazılım"
        )

    def test_unauthorized_access_type(self):
        incident = UnauthorizedAccessIncident(
            "Şüpheli Giriş",
            "Olağan dışı giriş",
            IncidentPriority.CRITICAL,
            5,
            5
        )
        self.assertEqual(
            incident.incident_type(),
            "Yetkisiz Erişim"
        )

    def test_invalid_impact(self):
        with self.assertRaises(ValueError):
            MalwareIncident(
                "Test",
                "Açıklama",
                IncidentPriority.HIGH,
                6,
                3
            )

    def test_invalid_status(self):
        with self.assertRaises(ValueError):
            self.incident.update_status("Bilinmeyen durum")

    def test_standard_strategy(self):
        score = self.calculator.calculate(self.incident)
        self.assertEqual(score, 59)

    def test_critical_asset_strategy(self):
        calculator = PriorityCalculator(CriticalAssetStrategy())
        score = calculator.calculate(self.incident)
        self.assertEqual(score, 71)


if __name__ == "__main__":
    unittest.main(verbosity=2)
