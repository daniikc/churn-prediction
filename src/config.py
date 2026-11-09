from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DATA_RAW= ROOT / "data" / "raw"
DATA_PROCESSED=ROOT / "data" / "processed"
RAW_FILE=DATA_RAW/"telco_raw.csv"
PROCESSED_FILE= DATA_PROCESSED / "telco_clean.csv"
