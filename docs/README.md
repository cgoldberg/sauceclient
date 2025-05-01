# Generating the sauceclient Docs

----

## Local Configuration

The following packages are required to build the documentation:

- `sphinx`
- `sphinx_rtd_theme`

You can install them with:

```
pip install -r docs/requirements_doc.html
```

To generate the docs:

- from the main `sauceclient` directory, run:

```
sphinx-build -b html docs html
```

Documentation will be generated in the `sauceclient/html` directory.

----

## Publishing to "Read the Docs"

There is a [job configured][rtd-job] on the "Read the Docs" platform that
publishes new documentation on every commit to the `master` branch of the
GitHub Repo.

Configuration for the publishing job is located at: `docs/.readthedocs.yaml`

Documentation is hosted at: https://sauceclient.readthedocs.io

[rtd-job]: https://app.readthedocs.org/projects/sauceclient
