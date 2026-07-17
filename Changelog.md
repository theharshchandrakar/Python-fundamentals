# Changelog

## July 17, 2026

### Conversion
- Converted all 20 `.ipynb` files to `.py` format
- Created `convert_ipynb_to_py.py` for automated markdown-to-comment conversion

### Folder Organization
- Created "Jupyter Files" folder and moved all `.ipynb` files
- Created "Python Scripts" folder and moved all `.py` files including conversion script

### Bug Fixes

| File | Issue | Fix |
|------|-------|-----|
| Task2 | ValueError crash on string-to-int conversion | Wrapped in try-except block |
| Task5 | Blocking `input()` statements | Replaced with default values |
| Task6 | Incorrect "tuple" comments in list operations | Changed to "list" |
| Task9 | Variable scope error (`year` vs `y` parameter) | Corrected to use parameter `y` |
| Task9 | Blocking `input()` in palindrome test | Replaced with default "racecar" |
| Task10 | Lambda using wrong variable (`num%2` vs `x%2`) | Corrected to use `x` |
| Task11 | FileExistsError on log.txt creation | Added file cleanup check |
| Task12 | Multiple blocking `input()` statements | Replaced with default values |
| Task17 | Jupyter magic command `%pip install` | Replaced with subprocess call |

### Verification
- All 20 task files tested successfully
- No syntax or runtime errors
- All Jupyter dependencies removed
- Markdown content properly commented

### Git
- Committed: "Convert all .ipynb files to .py with proper formatting and fix conversion errors"
- Pushed to main branch
