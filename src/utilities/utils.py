# -*- coding: utf-8 -*-
#**********************************************************************************
# content        = utils.py functions
# version        = 1.1.0
# date           = 06-09-2025
#
# how to         = gets imported automatically from notebooks
# dependencies   = Python 3, pandas, difflib, numpy, scipy, pathlib
# todos          = good for now
# license        = MIT
# author         = Enrico Vaccari <e.vaccari99@gmail.com>
#**********************************************************************************

# -------------------------------------------------------------------
# LIBRARIES (for utils.py)
# -------------------------------------------------------------------

# --- Standard library ---
from pathlib import Path
from typing import Union

# --- Third-party: core scientific ---
import difflib
import numpy as np
import pandas as pd
from scipy.stats import shapiro  # used elsewhere if needed


# -------------------------------------------------------------------
# FUNCTIONS
# -------------------------------------------------------------------

def get_project_root() -> Path:
    """
    Walk up from current working directory until we find a repo marker
    or a 'data' folder. Falls back to CWD if nothing is found.
    """
    candidates = ("pyproject.toml", "requirements.txt", ".git")
    here = Path.cwd().resolve()
    for p in (here, *here.parents):
        if any((p / m).exists() for m in candidates) or (p / "data").exists():
            return p
    return here

# -------------------------------------------------------------------

def load_dataset(file_path: Union[str, Path]) -> pd.DataFrame:
    """
    Load a dataset from CSV or Excel into a pandas DataFrame.

    Parameters
    ----------
    file_path : str | Path
        Path to the CSV (.csv) or Excel (.xlsx/.xls) file.

    Returns
    -------
    pd.DataFrame
        The loaded dataset.

    Raises
    ------
    FileNotFoundError
        If the file does not exist.
    ValueError
        If the extension is not supported.
    """
    file_path = Path(file_path).resolve()
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    suffix = file_path.suffix.lower()
    if suffix == ".csv":
        print("Data loaded correctly!")
        return pd.read_csv(file_path, sep=";")
    elif suffix in (".xlsx", ".xls"):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Use '.csv', '.xlsx', or '.xls'.")

# -------------------------------------------------------------------

def save_dataset(dataset: pd.DataFrame, relative_path: Union[str, Path]) -> Path:
    """
    Save a dataset under <PROJECT_ROOT>/data/<relative_path>.

    Parameters
    ----------
    dataset : pd.DataFrame
        DataFrame (or Series) to save.
    relative_path : str | Path
        Subfolder and filename relative to <PROJECT_ROOT>/data,
        e.g. 'processed/04_X_train.xlsx' or 'outputs/results.csv'.

    Notes
    -----
    - Always writes inside the 'data' folder at project root.
    - Creates subfolders if they don't exist.
    - Supports .xlsx and .csv formats.

    Returns
    -------
    Path
        The full path where the file was saved.
    """
    project_root = get_project_root()
    data_root = project_root / "data"

    path = (data_root / Path(relative_path)).resolve()
    path.parent.mkdir(parents=True, exist_ok=True)

    if path.suffix.lower() == ".xlsx":
        dataset.to_excel(path, index=False)
    elif path.suffix.lower() == ".csv":
        dataset.to_csv(path, index=False)
    else:
        raise ValueError("Unsupported file format. Use '.xlsx' or '.csv'.")

    print(f"File saved at: {path}")

# -------------------------------------------------------------------

def explore_dataset(dataset: pd.DataFrame) -> None:
    """
    Print a quick textual summary of a dataset.

    Parameters
    ----------
    dataset : pd.DataFrame
        The dataset to explore.
    """
    print("HEADER ----------------------------------------------------------------")
    print(dataset.head(5))

    print("\nINFO ------------------------------------------------------------------")
    # dataset.info() prints to stdout and returns None
    dataset.info()

    print("\nCOLUMN TYPES -----------------------------------------------------------")
    print(dataset.dtypes)

    print("\nROWS AND COLUMNS NUMBER -----------------------------------------------")
    print(f"Rows: {dataset.shape[0]}")
    print(f"Columns: {dataset.shape[1]}")

# -------------------------------------------------------------------

def mece_check(df, label_col="label"):
    """
    Check if labels are mutually exclusive and exhaustive (MECE).
    
    - Mutually Exclusive: no row has more than one label.
    - Collectively Exhaustive: no row is missing a label.
    
    Returns True if both conditions hold, False otherwise.
    Prints diagnostic messages.
    """
    # 1. Check missing labels
    missing = df[label_col].isna().any()
    
    # 2. Check overlapping labels:
    # group by index → count unique labels
    overlap = (
        df.groupby(df.index)[label_col]
        .nunique()
        .gt(1)  # >1 unique label per row
        .any()
    )
    
    if overlap:
        print("❌ Overlapping label assignments detected.")
    if missing:
        print("❌ Unlabelled rows present.")
    if not (overlap or missing):
        print("✅ Labels are MECE.")
    
    return not (overlap or missing)

# -------------------------------------------------------------------


def fuzzy_scan(columns, keywords, cutoff=0.7):
    """
    Scan a list of columns for sensitive attributes with fuzzy matching.
    
    Parameters
    ----------
    columns : list
        List of dataset column names
    keywords : list
        Sensitive keywords to search for
    cutoff : float
        Similarity threshold (0 to 1). Higher = stricter.
    
    Returns
    -------
    matches : dict
        Mapping of keyword → matched columns
    """
    matches = {}
    for kw in keywords:
        close = difflib.get_close_matches(kw, [c.lower() for c in columns], cutoff=cutoff)
        if close:
            matches[kw] = close
    return matches

# -------------------------------------------------------------------
