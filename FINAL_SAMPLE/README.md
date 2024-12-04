# Final Project Sample Files

This directory contains sample files that will help you build your final microservices project.

Included are:

* `Dockerfile`: A Dockerfile that illustrates the multi-stage build concept. In this example, the entire application you write is copied to the base container, and then each sub-container runs the specified microservice.

    > Note that this is **not** optimal way to build microservices. Typically, you would copy *only* the files needed for each specific microservice to each sub-container.

* `compose-testing.yml`: A Docker Compose file showing how to define your microservices. In this file, each microservice is exposed on its own port for testing purposes. **This is NOT your final deliverable compose file - it is only to help you test your services!**

* `compose-with-traefik.yml`: A Docker Compose file similar to the above, but incorporating the Traefik reverse proxy. In this example, the individual microservices are not exposed directly to the Internet; they are only accessible via the Traefik proxy, which is able to both merge all the services into one virtual "server" as well as potentially impose access restrictions, load balancing and more. **This file, modified for your project, is for your deliverable.**

    > For either compose file, you should rename it to `compose.yml` in your project directory before trying to use it. While you can use `docker compose -f some-other-filename.yml ...`, this is cumbersome and prone to errors or frustration. `compose.yml` is the default filename that Docker Compose will always search for.

* `service.py`: An extremely minimal Hello World Python Flask service. It simply returns Hello World when a `GET` request is made to `/hello`. **You MAY NOT use this service as-is, but you can use it as a template to build your own services.**
