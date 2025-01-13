from dataclasses import dataclass
from datetime import date
from uuid import UUID


@dataclass(slots=True)
class Version:
    created_at: date
    project_id: UUID
    number: str
    id: UUID
    released_at: date | None

    @classmethod
    def make(cls: type["Version"], data: dict) -> "Version":
        return cls(
            id=UUID(data["id"]),
            project_id=UUID(data["project_id"]),
            number=data["number"],
            created_at=date.fromisoformat(data["created_at"]),
            released_at=(
                date.fromisoformat(data["released_at"])
                if data["released_at"] is not None
                else None
            ),
        )


@dataclass(slots=True)
class VersionsPage:
    versions: list[Version]
    prev_token: str | None
    next_token: str | None
