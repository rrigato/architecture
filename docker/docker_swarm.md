- Have a single replica service in docker swarm to take advantage of secrets and configs

- managers = manage membership and delegation
- workers = run swarm services
- service = defintion of tasks to run on worker or manager nodes
- node = instance of docker engine running in the swarm
- task = docker container managed by the swarm