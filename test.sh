#/usr/bin/bash

echo --------------------Run Tests--------------------
echo "🔬  Running pytest tests…" &&
. venv/bin/activate
export $(cat .env | xargs)
pytest -v --cov=api --exitfirst
echo "👌  OK!"
echo --------------------Finished Test Run--------------------