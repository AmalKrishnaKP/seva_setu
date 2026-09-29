import enum
 

 
class JobStatusEnum(str, enum.Enum):
    POSTED = "POSTED"
    ACCEPTED = "ACCEPTED"
    STARTED = "STARTED"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"
 

class AuditTagEnum(str, enum.Enum):
    WORKER = "WORKER"
    SECURITY = "SECURITY"
    ADMIN = "ADMIN"
    CATEGORY ="CATEGORY"
    BADGE ="BADGE"
    CUSTOMER = "CUSTOMER"
class LanguageEnum(str,enum.Enum):
    MAL="MAL"
    ENG="ENG"
    TAM="TAM"
    TEL="TEL" 
    HIN="HIN"
