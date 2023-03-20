.PHONY: start
start:
	uvicorn main:app --port 9001 --forwarded-allow-ips=*

.PHONY: format
format:
	black .
	isort .