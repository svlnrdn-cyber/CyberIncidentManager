
from enums import IncidentPriority, IncidentStatus
from incident_repository import IncidentRepository
from incident_factory import IncidentFactory
from priority_calculator import PriorityCalculator
from priority_strategy import StandardPriorityStrategy
from incident_service import IncidentService
from incident_report_service import IncidentReportService


class CyberIncidentManager:
    def __init__(self):
        self.repository = IncidentRepository()
        self.service = IncidentService(self.repository)

        calculator = PriorityCalculator(StandardPriorityStrategy())
        self.calculator = calculator
        self.report_service = IncidentReportService(calculator)

    def list_incidents(self, records=None):
        if records is None:
            records = self.service.list_all()

        if not records:
            print("Gösterilecek olay bulunmuyor.")
            return

        for index, incident in enumerate(records, start=1):
            print(f"\n--- Olay {index} ---")
            incident.show_info()

            score = self.calculator.calculate(incident)
            print("Öncelik puanı:", score)
            print("Risk seviyesi:", self.calculator.risk_level(score))
            print("-" * 40)

    def add_incident(self):
        print("\n1. Zararlı Yazılım")
        print("2. Yetkisiz Erişim")
        incident_type = input("Olay türü: ").strip()

        if incident_type not in ("1", "2"):
            print("Geçersiz olay türü.")
            return

        title = input("Olay başlığı: ").strip()
        description = input("Olay açıklaması: ").strip()

        if not title or not description:
            print("Başlık ve açıklama boş bırakılamaz.")
            return

        try:
            priority_number = int(input("Önem (1-Düşük, 2-Orta, 3-Yüksek, 4-Kritik): "))
            impact = int(input("Etki (1-5): "))
            urgency = int(input("Aciliyet (1-5): "))

            if not 1 <= priority_number <= 4:
                print("Önem seviyesi 1-4 arasında olmalı.")
                return

            if not 1 <= impact <= 5 or not 1 <= urgency <= 5:
                print("Etki ve aciliyet 1-5 arasında olmalı.")
                return

            incident = IncidentFactory.create(
                incident_type,
                title,
                description,
                IncidentPriority(priority_number),
                impact,
                urgency
            )

            self.service.add(incident)
            print("Olay kaydedildi.")

        except ValueError as error:
            print("Giriş hatası:", error)

    def search_incident(self):
        keyword = input("Aranacak olay başlığı: ").strip()

        if not keyword:
            print("Arama alanı boş bırakılamaz.")
            return

        self.list_incidents(self.service.search(keyword))

    def update_status(self):
        records = self.service.list_all()

        if not records:
            print("Güncellenecek olay bulunmuyor.")
            return

        self.list_incidents(records)

        try:
            number = int(input("Olay numarası: "))
            if not 1 <= number <= len(records):
                print("Geçersiz olay numarası.")
                return

            print("1. Yeni")
            print("2. İnceleniyor")
            print("3. Çözüldü")
            choice = input("Yeni durum: ").strip()

            statuses = {
                "1": IncidentStatus.NEW,
                "2": IncidentStatus.INVESTIGATING,
                "3": IncidentStatus.RESOLVED
            }

            if choice not in statuses:
                print("Geçersiz durum.")
                return

            self.service.update_status(number - 1, statuses[choice])
            print("Olay durumu güncellendi.")

        except ValueError:
            print("Lütfen geçerli bir sayı girin.")

    def delete_incident(self):
        records = self.service.list_all()

        if not records:
            print("Silinecek olay bulunmuyor.")
            return

        self.list_incidents(records)

        try:
            number = int(input("Silinecek olay numarası: "))
            if not 1 <= number <= len(records):
                print("Geçersiz olay numarası.")
                return

            confirmation = input("Silinsin mi? (e/h): ").strip().lower()
            if confirmation == "e":
                self.service.delete(number - 1)
                print("Olay silindi.")
            else:
                print("Silme iptal edildi.")

        except ValueError:
            print("Lütfen geçerli bir sayı girin.")

    def show_report(self):
        report = self.report_service.create_report(
            self.service.list_all()
        )

        print("\n=== GÜVENLİK OLAYLARI RAPORU ===")
        print("Toplam olay:", report["toplam_olay"])
        print("Çözülen olay:", report["cozulmus_olay"])
        print("Açık olay:", report["acik_olay"])
        print("\nRisk dağılımı:")

        for risk, count in report["risk_dagilimi"].items():
            print(f"{risk}: {count}")

    def sort_incidents(self):
        records = sorted(
            self.service.list_all(),
            key=self.calculator.calculate,
            reverse=True
        )
        self.list_incidents(records)

    def run(self):
        while True:
            print("\n=== CYBER INCIDENT MANAGER ===")
            print("1. Olayları listele")
            print("2. Yeni olay ekle")
            print("3. Önceliğe göre sırala")
            print("4. Olay ara")
            print("5. Olay durumunu güncelle")
            print("6. Olay sil")
            print("7. Rapor göster")
            print("8. Çıkış")

            choice = input("Seçiminiz: ").strip()

            if choice == "1":
                self.list_incidents()
            elif choice == "2":
                self.add_incident()
            elif choice == "3":
                self.sort_incidents()
            elif choice == "4":
                self.search_incident()
            elif choice == "5":
                self.update_status()
            elif choice == "6":
                self.delete_incident()
            elif choice == "7":
                self.show_report()
            elif choice == "8":
                print("Program kapatılıyor.")
                break
            else:
                print("1 ile 8 arasında bir seçenek girin.")


if __name__ == "__main__":
    app = CyberIncidentManager()
    app.run()
