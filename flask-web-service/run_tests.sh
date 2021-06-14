# ensure the cwd contains the application code
cd "$( dirname "${BASH_SOURCE[0]}" )"

# use codecov to generate code coverage reports
pytest --cov=.
