"""SharePoint API client for document retrieval."""

from typing import List

import time


class SharePointClient:
    """Simple SharePoint API client skeleton."""

    def __init__(self, base_url: str, credentials: dict) -> None:
        self.base_url = base_url
        self.credentials = credentials

    def list_documents(self) -> List[str]:
        """Return a list of document URLs from SharePoint."""
        raise NotImplementedError

    def download_document(self, url: str) -> bytes:
        """Download document content and return as bytes."""
        raise NotImplementedError

    def watch_for_updates(self, callback, poll_interval: int = 60) -> None:
        """Continuously poll for document updates and invoke callback."""

        known = set(self.list_documents())
        while True:
            try:
                current = set(self.list_documents())
                added = current - known
                if added:
                    callback(list(added))
                known = current
                time.sleep(poll_interval)
            except Exception as e:
                print(f"SharePoint watch error: {e}")


class DummySharePointClient(SharePointClient):
    """Client returning canned data for testing."""

    def __init__(self) -> None:
        super().__init__("https://sharepoint.example.com", {})

    def list_documents(self) -> List[str]:
        return [
            "https://sharepoint.example.com/docs/doc1.txt",
            "https://sharepoint.example.com/docs/doc2.txt",
        ]

    def download_document(self, url: str) -> bytes:
        return b"Dummy document contents for " + url.encode()
