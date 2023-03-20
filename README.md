# Cookiecutter project for GitHub configuration templates

This repository can be used for adding Github Actions and templates to an existing project.

## Version

Current version is 1.2.1 and was set according to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Project's version should be updated, when applicable:

- In this very file.
- In the CHANGELOG.md file.
- In the CHANGES.md file.

## Usage

In order to start a new project, install [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/)
and run the following command:

```bash
$ cookiecutter https://github.com/ferreteleco/cookie-github.git
```

It will create the appropriate .github folder in your project directory (wherever you invoke
cookiecutter).

**NOTE:** it can also be cloned using GIT over SSH, if properly configured in your account.

**NOTE:** after the repository is downloaded, the template can be used again without downloading it
again. In order to do so, simply specify template name as argument for cookiecutter:

```bash
$ cookiecutter cookie-github
```

If more than one target language is desired (Python and C++ for example), the cookiecutter can be
run again with the *-f* option, in order to select a new target language and add it to the base
folder:

```bash
# First call. Folder gets created. Select python options, for example.
$ cookiecutter https://github.com/ferreteleco/cookie-github.git
# Second call, Folder already exists. If python was selected again, contents will be overwritten.
# If C++ is selected (for example) new CI files, related with C++ development, will be added.
$ cookiecutter -f https://github.com/ferreteleco/cookie-github.git
```

IMPORTANT: PR and Issue templates option overwrites every time, so if they are wanted, should be
marked as true in the last call to cookiecutter. The CI specific options are managed differently and
this is not an issue (it can be set to true or false in successive calls without erasing previous 
calls generated data).


**NOTE:** alternatively, you can use [Cookieninja](https://github.com/cookieninja-generator/cookieninja),
forked and more updated version of Cookiecutter with backward compatibility.

## Variables

Variables allow to customize your project. After running one of the previous cookiecutter commands,
you will be prompted to fill in the following values:

- **add_issue_templates:** this flags controls wether or not to add issue templates in the generated
  folder.
- **add_PR_template:** this flags controls wether or not to add a PR template in the generated
  folder.
- **add_ci_action_unit_tests:** this variable controls whether or not to create an action to
  run unit tests in the repository. The available actions are:
    - cpp, which creates an action for Catch2 based unit tests, built using CMake.
    - python, which creates an action for Python code unit tests, executed with pytest over a
      project built with Poetry.
    - none, which does not generate any action.
- **add_ci_action_auto_release:** this variable controls whether or not to create an action to
  generate dev releases (pre-releases, tagged with "latest" tag), triggered on pushes to master
  branch. The available actions are:
    - python, which creates an action for Python releases, building assets after pytest test
      execution in a project built with Poetry.
    - none, which does not generate any action.
- **add_ci_action_tagged_release:** this variable controls whether or not to create an action to
  generate tagged releases (releases, semver tagged), triggered on "v*.*.*" tags pushed. The
  available actions are:
    - python, which creates an action for Python releases, building assets after pytest test
      execution in a project built with Poetry.
    - none, which does not generate any action.

**NOTE:** Each added action will be accompanied of a markdown checklist, stating the changes /
configuration required to fine tune it.

## Contributing

If you want to contribute to this template, feel free to do so! Create a new branch to work in, and
open a pull request when you are done! It will be reviewed and merged into master by one of the
maintainers as soon as possible.

## Authors

- [Andrés Ferreiro González](https://github.com/ferreteleco)

## Maintainer

- [Andrés Ferreiro González](https://github.com/ferreteleco)
