
from enum import Enum


class IncidentPriority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4


class IncidentStatus(Enum):
    NEW = "Yeni"
    INVESTIGATING = "İnceleniyor"
    RESOLVED = "Çözüldü"
