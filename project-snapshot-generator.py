import os

def export_project_snapshot(
    root_dir="C:\csv-cleaner",                 # ← This is the path to your project root
    output_file="csv-cleaner_snapshot.txt"  # ← This is the output file name
):
    with open(output_file, "w", encoding="utf-8") as out:
        for folder, subfolders, files in os.walk(root_dir):
            
            # Skip virtual environments and caches
            if "venv" in folder or "__pycache__" in folder or ".git" in folder:
                continue

            out.write(f"\n=== FOLDER: {folder} ===\n")

            for file in files:
                path = os.path.join(folder, file)
                out.write(f"\n--- FILE: {path} ---\n")
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        out.write(f.read())
                except:
                    out.write("[Binary or unreadable file skipped]\n")

if __name__ == "__main__":
    export_project_snapshot("C:\csv-cleaner")  # ← This means “current folder”
