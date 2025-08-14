---
aliases: ["bugged", "create-bug"]
description: "Creates a bugged ArcPy script that calculates water main lengths by material"
---

Create the file `bugged_arcpy.py` at the repository root with a logical bug that causes the script to fail. 

The script should calculate total water main length by material type but has a bug where it incorrectly tries to access the Shape_Length field using attribute notation instead of index notation in the cursor.

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
        
        # BUG: Incorrectly trying to access field by name instead of index
        # This will cause AttributeError: 'tuple' object has no attribute 'Shape_Length'
        material_lengths[material] += row.Shape_Length

# Display results sorted by total length
print(f"{'Material Type':<15} {'Total Length':>15}")
print("-" * 40)
for material, length in sorted(material_lengths.items(), key=lambda x: x[1], reverse=True):
    print(f"{material:<15} {length:>15,.2f} ft")

print("-" * 40)
print(f"{'TOTAL':<15} {sum(material_lengths.values()):>15,.2f} ft")
print(f"\nTotal materials analyzed: {len(material_lengths)}")
```

After creating the file, respond with:
"Created bugged_arcpy.py with attribute access error (row.Shape_Length instead of row[1])"