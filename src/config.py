from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DATA_RAW= ROOT / "data" / "raw"
DATA_PROCESSSED=ROOT / "data" / "processed"
RAW_FILE=DATA_RAW/"telco_raw.csv"
