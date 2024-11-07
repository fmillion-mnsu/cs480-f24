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

## Phase 2: ...

The rest of the project phases will be posted as we progress through this project.
