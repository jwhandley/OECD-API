# OECD API

This is a simple package for downloading datasets from the OECD API and loading them as pandas dataframes or saving them as CSVs.

## Command line usage

```bash
python3 oecd_api.py -d {OECD dataset code} -f {OECD API filter} -o {output filename}
```

## Using as an import

```python
from oecd_api import get_data, parse_data

oecd_code = "QNA"
filter = None

xml = get_data(oecd_code, filter)
df = parse_data(xml)

df.head()
```
