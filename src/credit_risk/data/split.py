import pandas as pd
from sklearn.model_selection import train_test_split
from pathlib import Path


def split_dataframe(
    df: pd.DataFrame,
    target_col: str,
    train_size: float = 0.7,
    val_size: float = 0.15,
    test_size: float = 0.15,
    random_state: int = 42,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    if not (0 < train_size < 1 and 0 < val_size < 1 and 0 < test_size < 1):
        raise ValueError("train_size, val_size, and test_size must be between 0 and 1.")

    if (train_size + val_size + test_size) != 1:
        raise ValueError("train_size + val_size + test_size must sum to 1.0.")

    if target_col not in df.columns:
        raise ValueError("Target column not found.")

    if (df[target_col].isna()).sum() > 0:
        raise ValueError("Null value found in target column.")

    train, temp = train_test_split(
        df,
        train_size=train_size,
        stratify=df[target_col],
        random_state=random_state,
    )

    val_ratio_in_temp = val_size / (val_size + test_size)

    val, test = train_test_split(
        temp,
        train_size=val_ratio_in_temp,
        stratify=temp[target_col],
        random_state=random_state,
    )

    return (train, val, test)


def save_splits(
    train_df: pd.DataFrame,
    val_df: pd.DataFrame,
    test_df: pd.DataFrame,
    output_dir: Path = Path("data/interim"),
    prefix: str = "",
) -> tuple[Path, Path, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)

    train_path = output_dir / Path(f"{prefix}train.csv")
    val_path = output_dir / Path(f"{prefix}val.csv")
    test_path = output_dir / Path(f"{prefix}test.csv")

    train_df.to_csv(train_path, index=False)
    val_df.to_csv(val_path, index=False)
    test_df.to_csv(test_path, index=False)

    return (train_path, val_path, test_path)


def split_and_save(
    df: pd.DataFrame,
    target_col: str,
    train_size: float = 0.7,
    val_size: float = 0.15,
    test_size: float = 0.15,
    output_dir: Path = Path("data/interim"),
    random_state: int = 42,
    prefix: str = "",
) -> tuple[Path, Path, Path]:
    train, val, test = split_dataframe(
        df, target_col, train_size, val_size, test_size, random_state
    )

    return save_splits(train, val, test, output_dir, prefix)
