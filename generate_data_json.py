import os
import json

# Root folder of your repo
ROOT_FOLDER = "."

# UNITs list
UNITS = ["UNIT-1", "UNIT-2", "UNIT-3", "UNIT-4", "UNIT-5"]

# Top-level folder mapping
FOLDER_MAP = {
    "syllabus": "Syllabus",
    "notes": "Notes",
    "programs": "Programs",
    "assignments": "Assignments",
    "ebooks": "ebooks",
    "exampapers": "ExamPapers"
}

# Load existing data.json if it exists
data_json_path = os.path.join(ROOT_FOLDER, "data.json")
if os.path.exists(data_json_path):
    with open(data_json_path, "r", encoding="utf-8") as f:
        old_data = json.load(f)
else:
    old_data = {}

# Helper: preserve "hidden" flags
def preserve_hidden(old_list, new_list):
    old_dict = {item["path"]: item for item in old_list}
    result = []
    for item in new_list:
        path = item["path"]
        if path in old_dict and "hidden" in old_dict[path]:
            item["hidden"] = True
        result.append(item)
    return result

# Scan files in a folder
def scan_files(folder):
    if not os.path.exists(folder):
        return []
    files = []
    for item in sorted(os.listdir(folder)):
        path = os.path.join(folder, item).replace("\\", "/")
        if os.path.isfile(path):
            files.append({"path": path})
    return files

# Scan UNIT folders
def scan_units(base_folder, old_units_data):
    units_dict = {}
    for unit in UNITS:
        unit_folder = os.path.join(base_folder, unit)
        new_files = scan_files(unit_folder)
        old_files = old_units_data.get(unit, []) if old_units_data else []
        units_dict[unit] = preserve_hidden(old_files, new_files)
    return units_dict

# Build new data.json structure
data = {}

# Syllabus
data["syllabus"] = preserve_hidden(old_data.get("syllabus", []), scan_files(FOLDER_MAP["syllabus"]))

# Notes, Programs, Assignments (grouped by UNIT)
data["notes"] = scan_units(FOLDER_MAP["notes"], old_data.get("notes", {}))
data["programs"] = scan_units(FOLDER_MAP["programs"], old_data.get("programs", {}))
data["assignments"] = scan_units(FOLDER_MAP["assignments"], old_data.get("assignments", {}))

# ebooks and exampapers (flat lists, preserve hidden)
data["ebooks"] = preserve_hidden(old_data.get("ebooks", []), scan_files(FOLDER_MAP["ebooks"]))
data["exampapers"] = preserve_hidden(old_data.get("exampapers", []), scan_files(FOLDER_MAP["exampapers"]))

# Save updated data.json
with open(data_json_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("data.json updated successfully with hidden flags preserved!")
