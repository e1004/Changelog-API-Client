from dataclasses import dataclass
from datetime import date
from typing import Self

from realerikrani.baseclient import BaseClient

from .model import Version, VersionsPage


@dataclass
class ChangelogClient:
    http_client: BaseClient

    def create_version(self: Self, version_number: str) -> Version:
        url = f"{self.http_client.url}/versions"
        response = self.http_client.post(
            url, data={"version_number": version_number}
        ).json()
        return Version.make(response["version"])

    def delete_version(self: Self, version_number: str) -> Version:
        url = f"{self.http_client.url}/versions/{version_number}"
        response = self.http_client.delete(url).json()
        return Version.make(response["version"])

    def release_version(self: Self, version_number: str, released_at: date) -> Version:
        url = f"{self.http_client.url}/versions/{version_number}"
        response = self.http_client.patch(
            url, data={"released_at": released_at.isoformat()}
        ).json()
        return Version.make(response["version"])

    def read_versions(
        self: Self, page_size: int | None, page_token: str | None
    ) -> VersionsPage:
        url = f"{self.http_client.url}/versions"

        if page_size:
            url += f"?page_size={page_size}"
        if page_token and page_size:
            url += f"&page_token={page_token}"
        elif page_token:
            url += f"?page_token={page_token}"

        response = self.http_client.get(url).json()
        return VersionsPage(
            versions=[Version.make(v) for v in response["versions"]],
            prev_token=response["previous_token"],
            next_token=response["next_token"],
        )
