
## Nesneye Yönelik Tasarım ve SOLID

- **Single Responsibility Principle (SRP):** IncidentService olay işlemlerini, IncidentRepository veri saklamayı, IncidentReportService rapor oluşturmayı üstlenir.
- **Open/Closed Principle (OCP):** Yeni olay türleri SecurityIncident sınıfından türetilebilir. Yeni öncelik hesaplama stratejileri PriorityStrategy sınıfından türetilebilir.
- **Liskov Substitution Principle (LSP):** MalwareIncident ve UnauthorizedAccessIncident, SecurityIncident nesnesi beklenen yerlerde kullanılabilir.
- **Dependency Inversion Principle (DIP):** PriorityCalculator, hesaplama yöntemini doğrudan kendi içinde tanımlamak yerine PriorityStrategy üzerinden kullanır.

## Tasarım Desenleri

- **Factory Pattern:** IncidentFactory, olay türüne göre uygun güvenlik olayı nesnesini oluşturur.
- **Strategy Pattern:** PriorityStrategy, farklı öncelik hesaplama yöntemlerinin birbirinin yerine kullanılmasını sağlar.
