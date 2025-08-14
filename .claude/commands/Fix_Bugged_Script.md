---
aliases: ["fix-bug", "debug"]
description: "Fixes the logical bug in bugged_arcpy.py"
---

Fix the logical bug in `bugged_arcpy.py` by following these specific steps:

## The Bug
The script tries to access the Shape_Length field using attribute notation (`row.Shape_Length`) instead of index notation (`row[1]`). This causes an AttributeError because SearchCursor returns tuples, not objects with attributes.

## How to Fix

1. First, read the current `bugged_arcpy.py` file
2. Identify the bug on line 30: `material_lengths[material] += row.Shape_Length`
3. Fix it by using the correct index notation

## The Fix
Replace line 30 from:
```python
material_lengths[material] += row.Shape_Length
```

With:
```python
material_lengths[material] += row[1]
```

## Complete Fixed Script
Write the following exact content to `bugged_arcpy.py`:

```python
"""
Water Main Length by Material Report
Calculates total pipe length for each material type in the water distribution system.
"""
import arcpy

# Set workspace to demo geodatabase
arcpy.env.workspace = r"C:\\Users\\ggarcia\\OneDrive - Abonmarche\\Documents\\GitHub\\ClaudeCodeDemo\\Data\\DemoData.gdb"

# Feature class to analyze
fc = "wMain"

print("Water Main Infrastructure Summary")
print("=" * 40)

# Dictionary to store lengths by material
material_lengths = {}

# Process all water mains
with arcpy.da.SearchCursor(fc, ["MATERIAL", "Shape_Length"]) as cursor:
    for row in cursor:
        material = row[0]
        
        # Initialize material in dictionary if not present
        if material not in material_lengths:
            material_lengths[material] = 0
        
        # FIXED: Using correct index notation to access Shape_Length
        material_lengths[material] += row[1]

# Display results sorted by total length
print(f"{'Material Type':<15} {'Total Length':>15}")
print("-" * 40)
for material, length in sorted(material_lengths.items(), key=lambda x: x[1], reverse=True):
    print(f"{material:<15} {length:>15,.2f} ft")

print("-" * 40)
print(f"{'TOTAL':<15} {sum(material_lengths.values()):>15,.2f} ft")
print(f"\nTotal materials analyzed: {len(material_lengths)}")
```

After fixing, respond with:
"Fixed bugged_arcpy.py - now correctly uses index notation (row[1]) to access Shape_Length"