---
description: Write a predefined Python script that prints the feature count of wMain in the demo geodatabase (static content, same every time)
allowed-tools:
  - Bash
---

Ignore any provided arguments. Always (re)create the file `count_wMain_features.py` at the repository root with EXACTLY the following content (overwrite if it exists). Do not alter or template anything—verbatim copy only. This intentionally keeps the script extremely simple for demo purposes.

```python
import arcpy

# Demo geodatabase workspace
arcpy.env.workspace = r"C:\\Users\\ggarcia\\OneDrive - Abonmarche\\Documents\\GitHub\\ClaudeCodeDemo\\Data\\DemoData.gdb"

# Feature class name
fc = "wMain"

# Get count and print
count = int(arcpy.management.GetCount(fc)[0])
print(f"wMain feature count: {count}")
```

After writing the file, respond with exactly one short line:
Created count_wMain_features.py (static demo script)

(If content already identical, respond with: count_wMain_features.py already up to date)
