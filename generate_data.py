import os
import json

# Base folders in your repo
SYLLABUS_FOLDER = "Syllabus"
NOTES_FOLDER = "Notes"
PROGRAMS_FOLDER = "Programs"
ASSIGNMENTS_FOLDER = "Assignments"
EBOOKS_FOLDER = "ebooks"

# Helper function to list files with relative paths
def list_files(folder):
    if not os.path.exists(folder):
        return []
    return [f"{folder}/{f}" for f in sorted(os.listdir(folder)) if os.path.isfile(os.path.join(folder, f))]

# Helper function to list files inside units (UNIT-1, UNIT-2, etc.)
def list_unit_files(base_folder):
    units = {}
    if not os.path.exists(base_folder):
        return units
    for unit in sorted(os.listdir(base_folder)):
        unit_path = os.path.join(base_folder, unit)
        if os.path.isdir(unit_path):
            units[unit] = [f"{unit_path}/{f}" for f in sorted(os.listdir(unit_path)) if os.path.isfile(os.path.join(unit_path, f))]
    return units

# Build data dictionary
data = {
    "syllabus": list_files(SYLLABUS_FOLDER),
    "notes": list_unit_files(NOTES_FOLDER),
    "programs": list_unit_files(PROGRAMS_FOLDER),
    "assignments": list_unit_files(ASSIGNMENTS_FOLDER),
    "ebooks": list_files(EBOOKS_FOLDER)
}

# Write data.json
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("data.json has been successfully generated!")
