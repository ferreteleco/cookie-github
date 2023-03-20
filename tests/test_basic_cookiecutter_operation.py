"""
test_basic_cookiecutter_operation.py

Maintainer Andrés Ferreiro González (andres.ferreiro.glez@gmail.com)
Created @ Monday, 20th March 2023 1:27:53 pm

Copyright (c) 2023 Andrés Ferreiro González
All Rights Reserved
"""


def test_bake_folder_default(cookies):
    """Basic cookiecutter test for baking a .github folder with default settings"""

    result = cookies.bake()

    assert result.exit_code == 0
    assert result.exception is None

    assert result.project_path.name == ".github"
    assert result.project_path.is_dir()
