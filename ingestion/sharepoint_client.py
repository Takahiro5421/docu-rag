"""SharePoint API client for document retrieval."""

from typing import List


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
