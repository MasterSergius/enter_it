# basic commands, use with Dockerfile

IMAGE:=fastapi_example
CONTAINER:=fastapi_example_container
HOST_PORT:=8000
CONTAINER_PORT:=8000

.PHONY: image
image:
	docker build . -t ${IMAGE}

.PHONY: clean
clean:
	docker rm -f ${CONTAINER}
	docker image rm -f ${IMAGE}

.PHONY: run
run: clean image
	docker run -d --name ${CONTAINER} -p ${HOST_PORT}:${CONTAINER_PORT} ${IMAGE}

.PHONY: stop
stop:
	docker stop ${CONTAINER}

.PHONY: shell
shell:
	docker run -i -p ${HOST_PORT}:${CONTAINER_PORT} -t ${IMAGE} /bin/bash


# advanced commands, docker-compose stuff, up and down all services

DOCKER_COMPOSE_FILE="docker-compose.yml"

.PHONY: compose-build
compose-build:
	docker compose -f ${DOCKER_COMPOSE_FILE} build

.PHONY: all-up
all-up: compose-build
	docker compose -f ${DOCKER_COMPOSE_FILE} up -d

.PHONY: all-down
all-down:
	docker compose -f ${DOCKER_COMPOSE_FILE} down --remove-orphans

.PHONY: db-shell
db-shell:
	@DB_CONTAINER_ID=$$(docker compose -f ${DOCKER_COMPOSE_FILE} ps -q db); \
	if [ -z "$$DB_CONTAINER_ID" ]; then \
		echo "Error: 'db' service container not found or not running. Please ensure it's up (make up)."; \
	else \
		docker exec -it $$DB_CONTAINER_ID bash; \
	fi

.PHONY: app-shell
app-shell:
	@APP_CONTAINER_ID=$$(docker compose -f ${DOCKER_COMPOSE_FILE} ps -q app); \
	if [ -z "$$APP_CONTAINER_ID" ]; then \
		echo "Error: 'app' service container not found or not running. Please ensure it's up (make up)."; \
	else \
		docker exec -it $$APP_CONTAINER_ID bash; \
	fi
