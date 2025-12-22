# app/enums/status_enum.py
from enum import Enum

# For Blog
class BlogStatus(str, Enum):
    Draft = "Draft"
    Published = "Published"

# For Category / Tag
class Status(str, Enum):
    Active = "Active"
    Inactive = "Inactive"
    Draft = "Draft"
