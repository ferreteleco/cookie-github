"""Post-generate hook for cookiecutter."""

import logging
from pathlib import Path
from shutil import rmtree, copytree


class Color:
    """Simple colors for print without external libraries."""

    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARK_CYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


def change_line_endings_crlf_to_lf():
    for path in Path(".").glob("**/*"):
        if path.is_file():
            data = path.read_bytes()
            lf_data = data.replace(b"\r\n", b"\n")
            path.write_bytes(lf_data)


def remove_issue_templates_if_selected(delete_flag: bool):
    """Removes the generated issue templates file if selected to do so in project config."""

    if delete_flag:
        LOG.info("Skipping issue templates files generation ...")
        path = Path("./ISSUE_TEMPLATE")
        rmtree(path)


def remove_pr_templates_if_selected(delete_flag: bool):
    """Removes the generated PR template file if selected to do so in project config."""

    if delete_flag:
        LOG.info("Skipping PR templates file generation ...")
        path = Path("./pull_request_template.md")
        path.unlink()


def add_ci_actions_for_language(language: str):
    """Adds CI action(s) for the target language, if applicable."""

    if language != "none":
        LOG.info("Adding %s actions with default config...", language)

        destination = Path("workflows")
        ci_workflow_files_path = Path("_", language, "workflows")
        copytree(ci_workflow_files_path, destination, dirs_exist_ok=True)

        print("\n\n#############################################################")
        print("#                                                           #")
        print(
            f"# {Color.BOLD}{Color.BLUE}Please review gen. checklist in order to adjust CI config{Color.END} #"
        )
        print("#                                                           #")
        print("#############################################################\n\n")

    else:
        LOG.info("Skipping CI Actions files generation (no language specified)")


def add_composite_actions_for_language(language: str):
    """Adds CI composite action(s) for the target language, if applicable."""

    destination = Path("actions")
    if language == "python":
        ci_composite_actions_files_path = Path("_", language, "actions")
        copytree(ci_composite_actions_files_path, destination, dirs_exist_ok=True)
    elif language == "none":
        LOG.info(
            "Skipping CI composite Actions files generation (no language specified)"
        )
    else:
        LOG.info(
            "Skipping CI composite Actions files generation (not required for %s)",
            language,
        )


def clean():
    """Remove files and folders only needed as input for generation."""
    LOG.info("Removing input data folder ...")
    rmtree("_")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(message)s")
    LOG = logging.getLogger("post_gen_project")

    ISSUES_DELETE_FLAG = not {{cookiecutter.add_issue_templates}}
    remove_issue_templates_if_selected(ISSUES_DELETE_FLAG)
    PR_DELETE_FLAG = not {{cookiecutter.add_PR_template}}
    remove_pr_templates_if_selected(PR_DELETE_FLAG)

    TARGET_LANGUAGE = "{{cookiecutter.target_language}}".lower()
    add_ci_actions_for_language(TARGET_LANGUAGE)
    add_composite_actions_for_language(TARGET_LANGUAGE)
    clean()
    change_line_endings_crlf_to_lf()
