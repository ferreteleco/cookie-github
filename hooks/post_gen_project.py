"""Post-generate hook for cookiecutter."""

import logging
from pathlib import Path
from shutil import rmtree


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


if __name__ == "__main__":

    logging.basicConfig(level=logging.DEBUG, format="%(message)s")
    LOG = logging.getLogger("post_gen_project")
    remove_unwanted_templates()
    change_line_endings_crlf_to_lf()
