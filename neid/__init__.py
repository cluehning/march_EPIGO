"""
NEID - simple, robust analysis utilities.

This package is intentionally minimal and "fail-proof":
- flat layout (no src/ import surprises)
- defensive imports with helpful error messages
- strong typing and clear APIs
"""

from __future__ import annotations

from .analysis import (
    build_feature_matrix,
    normalize_matrix,
    shannon_entropy,
    spectrum_1d,
)
from .config import Config, load_config
from .io import (
    ensure_dir,
    read_csv,
    read_json,
    read_npy,
    read_parquet,
    read_yaml,
    write_csv,
    write_json,
    write_npy,
    write_parquet,
)

__all__ = [
    "Config",
    "build_feature_matrix",
    "ensure_dir",
    "load_config",
    "normalize_matrix",
    "read_csv",
    "read_json",
    "read_npy",
    "read_parquet",
    "read_yaml",
    "shannon_entropy",
    "spectrum_1d",
    "write_csv",
    "write_json",
    "write_npy",
    "write_parquet",
]

__version__ = "0.1.0"
