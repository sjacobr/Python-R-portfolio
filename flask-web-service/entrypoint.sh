# ensure the cwd contains the application code
cd "$( dirname "${BASH_SOURCE[0]}" )"

flask run -h 0.0.0.0 -p 80

