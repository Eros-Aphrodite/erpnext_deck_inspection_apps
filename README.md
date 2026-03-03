### Deck Inspections

Deck inspection management

### Goals

- Provide a **single, easy-to-complete Deck Inspection form** for deck renovation and inspection scope checks
- Capture **contact details**, **date**, **responsible user**, and **tags** for each inspection
- Track workflow status: **New** → **In Progress** → **Done**
- Organize inspection details by **Deck** and **Roof** tabs
- Allow free-form **notes** for documenting findings and specifications

### What's included

- `Deck Inspection` DocType with Details (contact, date, status, notes) and tabbed layout (Deck, Roof)
- Desk route shortcut to open the DocType at `/app/deck-inspection`

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app deck_inspections
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/deck_inspections
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### CI

This app can use GitHub Actions for CI. The following workflows are configured:

- CI: Installs this app and runs unit tests on every push to `develop` branch.
- Linters: Runs [Frappe Semgrep Rules](https://github.com/frappe/semgrep-rules) and [pip-audit](https://pypi.org/project/pip-audit/) on every pull request.


### License

mit
