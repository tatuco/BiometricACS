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