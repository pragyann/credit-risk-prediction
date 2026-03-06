"""Lending Club data source access layer.

Current scope is intentionally simple: datasets are already downloaded and
registered locally, so this module only returns dataset contracts from the
registry.

In a full production ingestion flow, this layer would include logic to fetch
data from remote sources (for example download from an API/server), verify
integrity, and persist files into the local raw-data area.
"""

from credit_risk.data.contracts import Dataset
from credit_risk.data.registry import Registry


class LendingClubDataSource:
    """Provide access to Lending Club raw dataset contracts."""

    def __init__(self, registry: Registry):
        self.dataset = registry.get("lending_club_accepted_raw")

    def get_raw(self) -> Dataset:
        """Return the raw accepted-loans dataset contract."""
        return self.dataset
