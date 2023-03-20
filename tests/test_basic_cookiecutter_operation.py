"""
test_basic_cookiecutter_operation.py

Maintainer Andrés Ferreiro González (andres.ferreiro.glez@gmail.com)
Created @ Monday, 20th March 2023 1:27:53 pm

Copyright (c) 2023 Andrés Ferreiro González
All Rights Reserved
"""

from setupconfig import gen_path_temp_dir, remove_temp_dir, run_cookiecutter


def test_bake_folder_default():
    """Basic cookiecutter test for baking a .github folder with default settings"""

    temp_path = gen_path_temp_dir()
    result = run_cookiecutter(temp_path)

    assert result["exit_code"] == 0
    assert result["project_dir"].stem == ".github"
    assert result["project_dir"].is_dir()

    remove_temp_dir(temp_path)


def test_bake_folder_pr_template_only():
    """Basic cookiecutter test for baking a .github folder with custom settings, generating a PR
    template only."""

    temp_path = gen_path_temp_dir()
    extra_context = {
        "add_issue_templates": False,
        "add_PR_template": True,
        "add_ci_action_unit_tests": "none",
        "add_ci_auto_release": "none",
        "add_ci_tagged_release": "none",
    }
    result = run_cookiecutter(temp_path, extra_context=extra_context)

    assert result["exit_code"] == 0
    assert result["project_dir"].stem == ".github"
    assert result["project_dir"].is_dir()

    # 2, because .gitattributes is also generated
    assert len(list(result["project_dir"].rglob("*.*"))) == 2
    assert result["project_dir"].joinpath("pull_request_template.md").is_file()

    remove_temp_dir(temp_path)
