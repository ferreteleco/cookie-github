"""
setupconfig.py

Maintainer Andrés Ferreiro González (andres.ferreiro.glez@gmail.com)
Created @ Monday, 20th March 2023 1:27:53 pm

Copyright (c) 2023 Andrés Ferreiro González
All Rights Reserved
"""

from pathlib import Path
from shutil import rmtree
from typing import Dict, Union
from uuid import uuid4

from cookiecutter.generate import generate_context
from cookiecutter.main import cookiecutter
from cookiecutter.prompt import prompt_for_config


def gen_path_temp_dir() -> Path:
    """Generates a temporary dir (under /tmp) where to create a project and inspect it.

    Returns:
        Path: Generated path.
    """

    base_path = Path("/tmp/pytest-cookie-github")
    uuid = uuid4().hex
    test_path = base_path.joinpath(uuid)

    return test_path


def remove_temp_dir(path_to_remove: Path):
    """Removes the given input directory and its contents.

    Args:
        path_to_remove (Path): Path to be removed.
    """

    rmtree(path_to_remove)


def run_cookiecutter(
    path: Path,
    extra_context: Union[None, Dict] = None,
    overwrite_contents_if_exist: bool = False,
) -> Dict:
    """Runs cookiecutter on the current directory (should be base project dir) and returns both
    its context and the generated output directory, if any.

    Args:
        path (Path): Path where to place the generated cookiecutter.
        extra_content(Dict): A dictionary of context that overrides default and user configuration.
        overwrite_contents_if_exist (bool, optional): Flag controlling the operation if folder
        exist when running cookiecutter. Defaults to False.

    Returns:
        Dict: Dictionary with the generated results: context, generated path, exit code and
        exception (if any).
    """

    result = {
        "exception": None,
        "exit_code": -1,
        "project_dir": None,
        "context": None,
    }

    # Render the context, so it can be returned.
    context = prompt_for_config(
        generate_context(
            context_file=str("cookiecutter.json"), extra_context=extra_context
        ),
        no_input=True,
    )

    # Run cookiecutter to generate a new project
    generated_dir = cookiecutter(
        template=".",
        output_dir=str(path),
        no_input=True,
        overwrite_if_exists=overwrite_contents_if_exist,
        extra_context=extra_context,
    )

    result["project_dir"] = Path(generated_dir)
    result["context"] = context
    result["exit_code"] = 0
    result["exception"] = None

    return result
