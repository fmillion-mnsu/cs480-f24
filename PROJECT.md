# CS 480 - Cloud Computing - Final Project Fall 2024

The final project for this course is a cumulative, multi-phase project that will involve designing, building and deploying a simple application optimized for deployment in a cloud computing environment.

The various aspects that this project will cover include:

* Working with cloud service APIs
* Microservices
* Containers
* Cloud storage (S3)
* Load balancing and reverse proxying

## Phase 1: Planning

For Phase 1, you will plan your application. This project is open-ended and you may decide what your program will be and what scope it will cover, as long as it fulfills the requirements of this project. The core requirements for your application design are:

* The application must involve **at least three (3) microservices** not counting any frontend, database or proxy server.
* The microservices should be Web applications - typically backend Web APIs.
* At least one of your microservices should involve storing data in block storage via S3. This can be as simple as "receive files from a user and provide a list of those files".

Write a very minimal "RAD" (requirements analysis document) for your proposed project. 

> Please note that you will not be expected to actually fully implement an application - a skeleton proof-of-concept is suitable for this project. THe focus of this project is learning about various cloud computing functions, not on developing web APIs. That being said, some experience with API development is definitely valuable!

As part of this process, start to think about the API each of your microservices will expose - both to external consumers of the API as well as "inter-service" communication amongst the microservices. Think about how you'll pass data between services when necessary - will you require explicit restricted API calls, will you simply depend on a database or file store, or will you use a hybrid approach? Document this in your "mini-RAD".

## Phase 2: Development

In this phase, you will **write your microservices** in a language of your choice. Python is a good choice if you want to write quickly, since you can write each microservice in a single file. For common code, you can import another file that contains common functions into each microservice. **The example files for this project assume you're writing in Python** - if you are using another language/framework, such as ASP.NET or Node, you will want to do your own research for how to easily implement each service separately.

If your microservices need shared data, you have a few options:

* Write a common functions file that contains access to a database. This could even just be as simple as a text file on disk, a CSV file that is read and processed each time, or an SQLite database. Don't worry about getting too elaborate with hosted database servers for this project (unless you really want to!)
* Ensure that no microservice depends on data handled by another microservice. For example, a Login service should generate a JWT or a similar token that other services can decrypt and access independently.
* Write code for handling the database or file in each microservice. This is not ideal and is not a good pattern for long-term maintainability, so I advise against it.

## Phase 3: Packaging

In this phase, you will produce container images for *each* of your microservices. 

You can accomplish this using just one Dockerfile by using named targets. Alternatively you can use multiple Dockerfiles. However, writing one Dockerfile with targets allows you to optimize your build by doing things such as installing requirements only once, and then building individual containers off of that "intermediate" container.

The [sample files](FINAL_SAMPLE/) for the project will illustrate a Dockerfile that builds multiple Python application services.

**Test** each service independently using Postman or a similar API testing tool by running each built container and running appropriate queries against it. The sample files contain comments with details to help you with this process.

> **Hint**: If you do decide to use a shared database file or SQLite database, make sure you provide a **volume mount** for each container when running it, so they can all access the same data file!

## Phase 4: Setting up a Compose stack

In this phase, you will setup a Docker Compose file that runs *all* of your microservices at once, as a single "unit". Compose files represent a collection of services that can interact with each other. Compose also offers a lightweight version of features offered by more advanced orchestration tools - for example, Compose can run multiple *replicas* of each service for load balancing or redundancy. 

> **Note**: In production environments, such functionalities are typically managed by a more powerful container orchestration framework such as Kubernetes, or by a platform-specific orchestration system designed by and for a particular cloud infrastructure or service.

The [sample files](FINAL_SAMPLE) contain an example Compose file that will illustrate how to set up a stack.

## Phase 5: Adding the Reverse Proxy and Final Testing

The final phase of the project is to add in a configuration for a **reverse proxy**, which will provide a single virtual "server" that offers all of the endpoints provided by your microservices at one place. 

The file `compose-with-traefik.yml` in the [sample fies](FINAL_SAMPLE) illustrates how to add the Traefik proxy to your Compose file. Additionally, you need to provide a Traefik configuration file. You can essentially use the one in the samples as-is, but you may need to make slight modifications if you choose to use different paths for your data files.

## Deliverable

Your final deliverable consists of the following:

* Your planning documentation ("mini-RAD")
* All source code for your individual microservices
* Compose file that will build and run your services and the Traefik proxy
