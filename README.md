# ci-practice

A small Python project for learning CI/CD with GitHub Actions.

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py --demo      # show a short demo of the cleaner functions
python main.py --version   # show the version
```

## Run the tests

```bash
pytest
```

## Version

The version number lives in one place only: `version.py`.

```python
__version__ = "1.0.0"
```

We use Semantic Versioning: `MAJOR.MINOR.PATCH`.

- **PATCH** (1.0.0 → 1.0.1): a bug fix.
- **MINOR** (1.0.1 → 1.1.0): a new feature that does not break old code.
- **MAJOR** (1.1.0 → 2.0.0): a change that breaks old code.

### How to see the version

```bash
python main.py --version
```

Output:

```
ci-practice version 1.0.0
```

### How to release a new version

1. Change the number in `version.py`, for example to `"1.0.1"`.
2. Run the tests: `pytest`.
3. Commit the change:
   ```bash
   git add version.py
   git commit -m "Bump version to 1.0.1"
   git push
   ```
4. Create a tag. The tag is the version with a `v` in front:
   ```bash
   git tag v1.0.1
   ```
5. Push the tag:
   ```bash
   git push origin v1.0.1
   ```

When the tag reaches GitHub, the **Release** workflow starts. It runs the
tests, checks that the tag matches `version.py`, and creates a GitHub Release.
If the tag and `version.py` are different, the workflow fails and no release
is made.
