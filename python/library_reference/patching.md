- patch where an object is looked up not where it is defined
- patches return a ```MagicMock``` object
- patching temporarily changes the name that an object points to with a different one


- patch a dict for ```os.environ``` example:
```python
from unittest.mock import patch
import os

@patch.dict(os.environ, {"mock_key": "new_value3"})
def test_patch_os_environ(self):
    """implementation os.environ will be patched"""
    pass
```