### Materials for lecture 15: Docker

How to setup docker and run app

1. Install Docker (and docker-compose) then start docker service: https://www.docker.com/get-started/
2. Use Dockerfile to play with single image/container. Use docker-compose for multiple containers that should be within a same network.
3. Setup database: create table `users` (you may use `init_migration.sql`):
   - enter shell to db container (use command `make db-shell`)
   - enter postgresql shell `psql -U myuser user_database`
   - copy-paste content of `init_migration.sql` and press enter
   - you may exit container with ctrl+d
3. Use `make` for your convenience with single docker image:
   - make image: build docker image
   - make run: run image instance in a container
   - make stop: stop running container
   - make clean: remove container and image, so next build starts from scratch
   - make shell: enter shell (bash) within running container for debug purposes
4. Use `make` for your convenience with docker-compose (note, on some platforms it might be `docker-compose`, on others `docker compose`). Thus, make changes in Makefile if needed:
   - make compose-build: build images based on docker-compose.yml file
   - make all-up: start fastapi example app and db server
   - make all-down: stop fastapi example app and db server
   - make db-shell: enter shell (bash) of container with db server
   - make app-shell: enter shell (bash) of container with fastapi example app
5. Access swagger docs: http://localhost:8000/docs

### Your Homework

1. Add more functionality to fastapi app. For example: get user by id, delete user.
2. Don't save passwords as a plain text! Use hash.
3. Improve makefile. For example, add command to execute sql query.
4. Update README with your changes.
