from credit_risk.data.contracts import Dataset, DataStage
from pathlib import Path


class Registry:

    def __init__(self):
        self._storage: dict[str, Dataset] = {}

    def register(self, dataset: Dataset):
        if dataset.name in self._storage:
            raise ValueError("Dataset has already been registered.")

        self._storage[dataset.name] = dataset

    def get(self, name) -> Dataset:
        if name in self._storage:
            return self._storage[name]
        raise ValueError("Dataset has not been registered yet.")

    def names(self) -> list[str]:
        return list(self._storage.keys())


def build_default_registry() -> Registry:
    PROJECT_ROOT = Path.cwd().parent
    registry = Registry()

    registry.register(
        Dataset(
            name="lending_club_accepted_raw",
            source="Kaggle - Lending Club",
            stage=DataStage.RAW,
            path=PROJECT_ROOT / Path("data/raw/lending_club_accepted.csv"),
            tags=("lending_club", "accepted", "raw"),
        )
    )

    registry.register(
        Dataset(
            name="lending_club_rejected_raw",
            source="Kaggle - Lending Club",
            stage=DataStage.RAW,
            path=PROJECT_ROOT / Path("data/raw/lending_club_rejected.csv"),
            tags=("lending_club", "rejected", "raw"),
        )
    )

    return registry
