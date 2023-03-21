"""
test_custom_solutions.py

Maintainer Andrés Ferreiro González (andres.ferreiro.glez@gmail.com)
Created @ Monday, 20th March 2023 1:27:53 pm

Copyright (c) 2023 Andrés Ferreiro González
All Rights Reserved
"""

from setupconfig import gen_path_temp_dir, remove_temp_dir, run_cookiecutter


def test_bake_folder_existing():
    """Basic cookiecutter test for baking a .github folder with default settings and then add extra
    files calling again with the equivalent of -f option"""

    temp_path = gen_path_temp_dir()
    extra_context = {
        "add_issue_templates": False,
        "add_PR_template": True,
        "target_language": "python",
        "ci-runner": "ubuntu-20.04",
    }
    result = run_cookiecutter(temp_path, extra_context=extra_context)

    assert result["exit_code"] == 0
    assert result["project_dir"].stem == ".github"
    assert result["project_dir"].is_dir()

    assert len(list(result["project_dir"].rglob("*.*"))) == 7

    extra_context_2 = {
        "add_issue_templates": True,
        "add_PR_template": True,
        "target_language": "cpp",
        "ci-runner": "ubuntu-20.04",
    }
    result_2 = run_cookiecutter(
        temp_path, extra_context=extra_context_2, overwrite_contents_if_exist=True
    )

    assert result_2["exit_code"] == 0
    assert result_2["project_dir"].stem == ".github"
    assert result_2["project_dir"].is_dir()

    assert result_2["project_dir"].joinpath("pull_request_template.md").is_file()
    assert result_2["project_dir"].joinpath("ISSUE_TEMPLATE").is_dir()
    assert result_2["project_dir"].joinpath("workflows/ci-tests-python.yml").is_file()
    assert result_2["project_dir"].joinpath("workflows/ci-tests-cpp.yml").is_file()

    remove_temp_dir(temp_path)
