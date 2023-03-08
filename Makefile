# run:
# 	uvicorn main:app --port 8080 --reload
run:

	docker compose up -d


start:

	uvicorn main:app --port 8080 --reload
