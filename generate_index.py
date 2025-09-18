import os

# Repo info
GITHUB_USER = "naveenupreti"
REPO_NAME = "Python-Notes"
BRANCH = "main"

SECTIONS = ["Notes", "Programs", "Syllabus", "Ebooks"]
BASE_URL = f"https://cdn.jsdelivr.net/gh/{GITHUB_USER}/{REPO_NAME}@{BRANCH}"

def make_link(path):
    view_url = f"{BASE_URL}/{path}"
    download_url = f"{view_url}?raw=true"
    return view_url, download_url

def generate_html():
    html = [
        "<!DOCTYPE html>",
        "<html>",
        "<head>",
        "  <meta charset='UTF-8'>",
        "  <title>Python Notes Repository</title>",
        "  <style>",
        "    body { font-family: Arial; margin: 20px; }",
        "    h2 { color: #2c3e50; }",
        "    ul { list-style-type: none; padding-left: 20px; }",
        "    li { margin: 5px 0; }",
        "    a { text-decoration: none; color: #2980b9; margin-right: 10px; }",
        "    .download { background: #27ae60; color: white; padding: 3px 7px; border-radius: 5px; font-size: 12px; }",
        "  </style>",
        "</head>",
        "<body>",
        "  <h1>Python Notes Repository</h1>"
    ]

    for section in SECTIONS:
        if not os.path.exists(section):
            continue
        html.append(f"<h2>{section}</h2><ul>")
        for root, _, files in os.walk(section):
            for file in sorted(files):
                rel_path = os.path.join(root, file).replace("\\", "/")
                view_url, download_url = make_link(rel_path)
                html.append(
                    f"<li>{file} "
                    f"<a href='{view_url}' target='_blank'>View</a>"
                    f"<a class='download' href='{download_url}' download>Download</a></li>"
                )
        html.append("</ul>")

    html.extend(["</body>", "</html>"])
    return "\n".join(html)

if __name__ == "__main__":
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(generate_html())
    print("✅ index.html generated successfully!")
