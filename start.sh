# To do away with all that __pycache__ noise

set -e
export PYTHONDONTWRITEBYTECODE=1
export PYTHONUNBUFFERED=1
python3 main.py