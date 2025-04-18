from enum import Enum


class SeniorityLevel(str, Enum):
    JUNIOR = "Junior"
    SEMI_SENIOR = "Semi-Senior"
    SENIOR = "Senior"
    MANAGER_OR_ABOVE = "Manager or Above"
