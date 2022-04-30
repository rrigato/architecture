- cluster = collection of tasks or services
- task = docker container
- service = maintain a desired number of tasks within a cluster

- Using an ALB with ecs maps a dynamic port number so that multiple tasks can be listening on the same port and the same instance can be routed too
  - you still need a nat gateway if ecs is running in a private subnet

- tasks = instantiation of a task definition

