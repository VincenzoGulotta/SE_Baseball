from dataclasses import dataclass

@dataclass
class Team:
    team_id: int
    code: str
    name: str
    salary: float

    def __str__(self):
        return f"[{self.code}] ({self.name})"

    def __repr__(self):
        return f"[{self.code}] ({self.name})"

    def __eq__(self, other):
        return self.team_id == other.team_id

    def __hash__(self):
        return hash(self.team_id)

