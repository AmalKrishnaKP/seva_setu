import enum
 

 
class JobStatusEnum(str, enum.Enum):
    POSTED = "POSTED"
    ACCEPTED = "ACCEPTED"
    STARTED = "STARTED"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"
 

 