Collection of architecture notes I have from books, news feeds, online tech talks.

The goal is to slim down the source material into the smallest amount of actionable information

- [static_security_scan](#static_security_scan)


# static_security_scan

1) Create a virtual environment and install dependencies:

```bash
python -m venv avenv
source avenv/bin/activate
pip install -r requirements/requirements-dev.txt
```


2) implement to ensure no secrets are commited locally:

setup a baseline where all tracked files will be compared to:
```bash
detect-secrets scan > .secrets.baseline
```

compare all tracked files to baseline the ```results``` key should be ```{}``` if no secrets are present
```bash
detect-secrets scan

detect-secrets scan | \
python3 -c "import sys, json; print(json.load(sys.stdin)['results'])"
```
```powershell
(detect-secrets scan | ConvertFrom-Json).results
```