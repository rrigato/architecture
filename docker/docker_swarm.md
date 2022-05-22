- Have a single replica service in docker swarm to take advantage of secrets and configs

- managers = manage membership and delegation
- workers = run swarm services
- service = defintion of tasks to run on worker or manager nodes
- node = instance of docker engine running in the swarm
- task = docker container managed by the swarm


- each node in a docker swarm is a docker daemon
- docker daemon is responsible for managing containers and interacting with the host os
- services can access any node of the same docker swarm cluster
- service specification options:
    - published port
    - CPU/memory limits
    - rolling update policy
    - number of replicas

- global replica = 1 task per node
- replicated service = total number of tasks across all nodes
- tasks are independent containers of the service image that terminates when the container terminates or fails