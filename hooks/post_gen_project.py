"""Post-generate hook for cookiecutter."""

import logging
from pathlib import Path
from shutil import rmtree, copytree


class color:
    """Simple colors for print without external libraries."""
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARK_CYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def change_line_endings_crlf_to_lf():
    for path in Path(".").glob("**/*"):
        if path.is_file():
            data = path.read_bytes()
            lf_data = data.replace(b"\r\n", b"\n")
            path.write_bytes(lf_data)


def remove_unwanted_templates():

    if not {{ cookiecutter.add_issue_templates }}:
        LOG.info("Skipping issue templates files generation ...")
        path = Path("./ISSUE_TEMPLATE")
        rmtree(path)

    if not {{ cookiecutter.add_PR_template }}:
        LOG.info("Skipping PR templates file generation ...")
        path = Path("./pull_request_template.md")
        path.unlink()


def add_ci_action_unit_tests_runner():
    """Adds a CI action for running unit tests, if applicable"""

    target_language = "{{cookiecutter.project_language}}"

    if {{cookiecutter.add_ci_action_unit_tests_runner}}:

        if target_language.lower() != "other":

            LOG.info("Adding action for running unit tests (workflows folder) with default config...")

            destination = Path("workflows")
            ci_test_workflow_files_path = Path("_", "workflows", target_language)
            copytree(ci_test_workflow_files_path, destination)

            print("\n\n######################################################################")
            print("#                                                                    #")
            print(f"# {color.BOLD}{color.BLUE}Please review gen. checklist in order to adjust CI UT basic action{color.END} #")
            print("#                                                                    #")
            print("######################################################################\n\n")

        else:
            LOG.info("CI action for running unit tests file generation is not defined for %s language. Skipping...", target_language)

    else:
        LOG.info("Skipping CI action for running unit tests file generation")


def clean():
    """Remove files and folders only needed as input for generation."""
    LOG.info("Removing input data folder ...")
    rmtree("_")


if __name__ == "__main__":

    logging.basicConfig(level=logging.DEBUG, format="%(message)s")
    LOG = logging.getLogger("post_gen_project")
    remove_unwanted_templates()
    add_ci_action_unit_tests_runner()
    clean()
    change_line_endings_crlf_to_lf()
