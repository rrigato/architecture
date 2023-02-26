- dockerfile = text file of steps to build an image when invoking docker build

- each command in a Dockerfile creates a new read-only layer which is the difference from the previously run layer
- multi-stage build = when you have separate build and runtime dependencies 
    - multiple ```FROM``` statements in a Dockerfile
- running an image to create a container creates a writable layer on top of the read-only built layers
- ```ENTRYPOINT``` sets the images main command, ```CMD``` can provide default arguements if none are provided for the docker run statment

- ```FROM <base_image> AS <build_stage_name>``` to enable multi stage builds

- ```ARG``` = not persisted to final writable layer of image, only available when building an image
- ```ENV``` = peristed for all build layers and writable runtime containeraw

- Shared docker tag = reference multiple architectures 
- simple docker tag references 1 architecture