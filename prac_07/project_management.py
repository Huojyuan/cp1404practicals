"""Project Management Program
Estimated time: 3.5 hours
"""

from project import Project
from datetime import datetime
import pickle

FILENAME = "projects.txt"
PKLNAME = "projects.pkl"


def main():
    projects = load_projects_pickle(PKLNAME)
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    menu = "- (L)oad projects\n" \
           "- (S)ave projects\n" \
           "- (D)isplay projects\n" \
           "- (F)ilter projects by date\n" \
           "- (A)dd new project\n" \
           "- (U)pdate project\n" \
           "- (Q)uit"
    choice = input(menu + "\n>>> ").lower()

    while choice != "q":
        if choice == "l":
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Filename: ")
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_project(projects)
        elif choice == "u":
            update_project(projects)
        else:
            print("Invalid choice")
        choice = input(menu + "\n>>> ").lower()

    save = input(f"Would you like to save to {PKLNAME}? (y or yes to confirm) ").lower()
    if save in ['y', 'yes']:
        save_projects_pickle(PKLNAME, projects)

    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Load project data from a tab-delimited file."""
    projects = []
    with open(filename, "r") as file:
        next(file)  # Skip header
        for line in file:
            parts = line.strip().split('\t')
            name = parts[0]
            start_date = parts[1]
            priority = parts[2]
            cost_estimate = parts[3]
            completion_percentage = parts[4]
            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project)
    return projects


def load_projects_pickle(filename):
    """Load projects from a binary file using pickle."""
    try:
        with open(filename, "rb") as file:
            projects = pickle.load(file)
        print(f"{len(projects)} projects loaded from {filename}")
        return projects
    except (FileNotFoundError, EOFError):
        print("No file found or file is empty. Starting with empty project list.")
        return []


def save_projects(filename, projects):
    """Save project data to a tab-delimited file."""
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            line = f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t" \
                   f"{project.cost_estimate}\t{project.completion_percentage}\n"
            file.write(line)
    print(f"{len(projects)} projects saved to {filename}")


def save_projects_pickle(filename, projects):
    """Save projects to a binary file using pickle."""
    with open(filename, "wb") as file:
        pickle.dump(projects, file)
    print(f"{len(projects)} projects saved to {filename}")


def display_projects(projects):
    """Display incomplete and complete projects, sorted by priority."""
    incomplete = sorted([p for p in projects if not p.is_complete()])
    complete = sorted([p for p in projects if p.is_complete()])

    print("Incomplete projects:")
    for p in incomplete:
        print(f"  {p}")
    print("Completed projects:")
    for p in complete:
        print(f"  {p}")


def filter_projects_by_date(projects):
    """Show projects starting after a given date."""
    date_str = input("Show projects that start after date (dd/mm/yy): ")
    try:
        filter_date = datetime.strptime(date_str, "%d/%m/%Y").date()
        filtered = sorted([p for p in projects if p.start_date > filter_date], key=lambda p: p.start_date)
        for p in filtered:
            print(p)
    except ValueError:
        print("Invalid date format")


def add_project(projects):
    """Prompt the user for new project details and add it to the list."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $")
    completion = input("Percent complete: ")

    try:
        new_project = Project(name, start_date, priority, cost_estimate, completion)
        projects.append(new_project)
        print("Project added.")
    except Exception as e:
        print(f"Error adding project: {e}")


def update_project(projects):
    """Display projects and prompt user to update one."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    try:
        choice = int(input("Project choice: "))
        project = projects[choice]
        print(project)
        new_completion = input("New Percentage: ")
        if new_completion:
            project.completion_percentage = int(new_completion)
        new_priority = input("New Priority: ")
        if new_priority:
            project.priority = int(new_priority)
    except (ValueError, IndexError):
        print("Invalid selection or input")


if __name__ == "__main__":
    main()
