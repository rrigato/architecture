> Dynamic, highly parameterized software is harder to understand and build than more static software

- program to an interface not an implementation
- dynamic binding = which implementation of the same polymorphic interface is dispatched to at runtime based on values that are not known at development time
    - Example = multiple classes with the same method interface but different implementations are chosen based on system config at runtime