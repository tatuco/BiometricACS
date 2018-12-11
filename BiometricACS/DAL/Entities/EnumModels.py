import enum


class CamerasVector(enum.Enum):
    enter = 'enter'
    exit = 'exit'


class AccountRole(enum.Enum):
    viewer = 'viewer'
    technical_engineer = 'technical_engineer'
    
    
class EmployeeStatus(enum.Enum):
    working = 'working'
    trainees = 'trainees'
    vacation = 'vacation'
    dismissed = 'dismissed'


class EventVisit(enum.Enum):
    entered = 'entered'
    entered_by_hand_pass = 'entered by hand pass'
    out = 'out'
    out_by_hand_pass = 'went out by hand pass'
