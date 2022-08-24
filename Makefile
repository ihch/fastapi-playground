PROJECT = fastapi

all: Dockerfile
	docker build -t $(PROJECT) .

run:
	docker run -p 8000:8000 -v $(shell pwd)/openapi:/src/openapi $(PROJECT)

export-openapi:
	docker run --rm -v $(shell pwd)/openapi:/src/openapi -it fastapi python main.py
