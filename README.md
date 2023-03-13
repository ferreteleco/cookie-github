# Cookiecutter project for GitHub configuration templates

This repository can be used for adding Github Actions and templates to an existing project.

## Version

Current version is 1.2.0 and was set according to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Project's version should be updated, when applicable:

- In this very file.
- In the changelog.

## Usage

In order to start a new project, install [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/)
and run the following command:

```bash
$ cookiecutter https://github.com/ferreteleco/cookie-github.git
```

It will create the appropriate .github folder in your project directory (wherever you invoke
cookiecutter).

NOTE: it can also be cloned using GIT over SSH, if properly configured in your account.

NOTE1: after the repository is downloaded, the template can be used again without downloading it
again. In order to do so, simply specify template name as argument for cookiecutter:

```bash
$ cookiecutter cookie-github
```

NOTE: alternatively, you can use [Cookieninja](https://github.com/cookieninja-generator/cookieninja),
forked and more updated version of Cookiecutter with backward compatibility.

## Variables

Variables allow to customize your project. After running one of the previous cookiecutter commands,
you will be prompted to fill in the following values:

- **add_issue_templates:** this flags controls wether or not to add issue templates in the generated
  folder.
- **add_PR_template:** this flags controls wether or not to add a PR template in the generated
  folder.
- **project_language:** This variable choice serves to select the main project language, and it is
  aligned with the actions that will be later opt to be created.
- **add_ci_action_unit_tests_runner:** this variable controls whether or not to create an action to
  run unit tests in the repository. The available actions (per project_language variable) are:
    - cpp, which creates an action for Catch2 based unit tests, built using CMake.
    - python, which creates an action for Python code unit tests, executed with pytest over a
      project built with Poetry.
    - other, which does not generate any action.

## Contributing

If you want to contribute to this template, feel free to do so! Create a new branch to work in, and
open a pull request when you are done! It will be reviewed and merged into master by one of the
maintainers as soon as possible.

## Authors

- [Andrés Ferreiro González](https://github.com/ferreteleco)

## Maintainer

- [Andrés Ferreiro González](https://github.com/ferreteleco)
