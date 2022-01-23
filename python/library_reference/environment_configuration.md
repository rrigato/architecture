
# PYTHONPYCACHEPREFIX

- redirects ```*.pyc``` files to a separate folder instead of placing in the typical ```__pycache__``` directory within your project 

```bash
export PYTHONPYCACHEPREFIX="$HOME/Documents/project_pycache"
```

```powershell
$env:PYTHONPYCACHEPREFIX="${HOME}\\Documents\\project_pycache"
```

https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPYCACHEPREFIX