from dataclasses import dataclass


@dataclass
class TypeEnforce:
    int_value: int



if __name__ == "__main__":
    import logging
    import os
    from time import strftime
    os.environ["AWS_REGION"] = "us-east-1"
    logging.basicConfig(
        format=("%(levelname)s | %(asctime)s.%(msecs)03d" +
            strftime("%z") + " | %(message)s"
        ),
        datefmt="%Y-%m-%dT%H:%M:%S", 
        level=logging.INFO
    )
    myClass = TypeEnforce(int_value=5)
    #残念 does not type enforce　
    myClass.int_value = "str"
    print(myClass)

