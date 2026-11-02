# CI Practice Project

## About
A small Python project for learning CI/CD with GitHub Actions.
The code is simple on purpose. The goal is to learn pipelines, tests, and releases.

## Files
- `cleaner.py`: small helper functions (remove_duplicates, clean_name, average)
- `test_cleaner.py`: pytest tests for those functions
- `.github/workflows/ci.yml`: runs tests on every push and pull request
- `.github/workflows/release.yml`: creates a GitHub Release when I push a tag like v1.0.0

## Commands
- Install: `pip install -r requirements.txt`
- Run tests: `pytest`
- Check style: `flake8 .` (only if flake8 is in requirements.txt)

## Rules
- Every new function needs at least one pytest test.
- Run `pytest` before saying a task is finished.
- Keep the code simple. No new libraries unless I approve.
- Use Semantic Versioning for tags (v1.0.0, v1.0.1, v1.1.0).

## Git rules
- Never run `git push` or create tags without asking me first.
- Work on a new branch for each feature, not directly on main.
- Write short, clear commit messages.

## How to talk to me
- I am a beginner learning CI/CD.
- Use simple English and short sentences.
- Explain what you changed and why, step by step.
- When you edit a YAML file, explain each new line.
- If I ask, you can explain in Sinhala too.