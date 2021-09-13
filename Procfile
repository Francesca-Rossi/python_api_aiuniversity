web: gunicorn -w 3 -k uvicorn.workers.UvicornWorker --preload main:app --bind 0.0.0.0:$PORT
