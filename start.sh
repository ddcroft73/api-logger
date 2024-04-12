# To do away with all that __pycache__ noise, or not.  I don't really know why i bothered.
set -e
export PYTHONDONTWRITEBYTECODE=1
export PYTHONUNBUFFERED=1
python3 main.py