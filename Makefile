PROJECT = fastapi

all: Dockerfile
	docker build -t $(PROJECT) .

run:
	docker run -p 8000:8000 $(PROJECT)

export-openapi:
	python3 src/main.py
