- ```CMD``` and ENTRYPOINT define what command gets executed when running a container
- ENTRYPOINT should be used when running the container as an executable
- ENTRYPOINT <command_name> <arguement_0>
    - gets executed as ```/bin/sh -c <command_name> <arguement_0> ```

- ENTRYPOINT ["<command_name>", "<arguement_0>", "<arguement_1>"]
    - gets executed as ```<command_name> <arguement_0> <arguement_1> ```