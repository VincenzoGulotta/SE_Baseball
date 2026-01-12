from dataclasses import dataclass

@dataclass
class Team:
    id: int
    code: str
    name: str
    salary: float

    def __str__(self):
        return f"{self.code} ({self.name})"

    def __eq__(self, other):
        return self.code == other.code and self.name == other.name

    def __hash__(self):
        return hash(self.code)