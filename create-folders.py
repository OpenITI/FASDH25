import os

top_level = "./python_exercises/lesson_7.1/"
student_repos = "mARkdown/"

for team_folder in os.listdir(student_repos):
    team_readme_dir = os.path.join(top_level, team_folder)
    if not os.path.exists(team_readme_dir):
        os.makedirs(team_readme_dir)
    team_readme_path = os.path.join(team_readme_dir, "README.md")
    readme_text = "## {} Python Lesson 7.1\nUse this folder for writing and testing scripts related to lesson 7.1".format(team_folder)
    with open(team_readme_path, "w") as f:
        f.write(readme_text)

