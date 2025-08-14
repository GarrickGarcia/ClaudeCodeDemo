import arcpy

# Demo geodatabase workspace
arcpy.env.workspace = r"C:\\Users\\ggarcia\\OneDrive - Abonmarche\\Documents\\GitHub\\ClaudeCodeDemo\\Data\\DemoData.gdb"

# Feature class name
fc = "wMain"

# Get count and print
count = int(arcpy.management.GetCount(fc)[0])
print(f"wMain feature count: {count}")