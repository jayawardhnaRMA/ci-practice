import re
import subprocess
import sys
from pathlib import Path

from version import __version__

PROJECT_DIR = Path(__file__).parent


def test_version_looks_like_semver():
    # MAJOR.MINOR.PATCH, for example 1.0.0
    assert re.fullmatch(r"\d+\.\d+\.\d+", __version__)


def test_main_version_flag_prints_same_version():
    result = subprocess.run(
        [sys.executable, "main.py", "--version"],
        cwd=PROJECT_DIR,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert result.stdout.strip() == f"ci-practice version {__version__}"
