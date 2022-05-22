- hypervisor = provides virtual interfaces between hardware and software
  - need a separate virtual machine with an Operating System for each app
- containers are on top of the operating system instead of being bundled with the operating system
- containers are isolated, startup quickly and include all application code and depedencies

- Containers write to a scratch space that is not accessible by other containers 
- Named Volumes enable you to persist data between containers without dealing with where the data is stored on the host
- Bind mounts enable you to specify the path on the host and the mount point for the containers
- Containers on the same docker network can talk to each other
