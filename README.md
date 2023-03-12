# Cookiecutter project for GitHub configuration templates

This repository can be used for adding Github Actions and templates to an existing project.

## Version

Current version is 0.1.0 and was set according to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Project's version should be updated, when applicable:

- In this very file.

## Usage

In order to start a new project, install [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) and run the following command:

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