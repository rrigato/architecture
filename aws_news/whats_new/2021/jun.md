- cloudformation modules enable you to have cloudformation resources that can be reused across stacks

- modules can take parameter inputs and have their resources referenced using ```!ref```

- When creating a logical resource from a module you use the following naming convention in the template using the module:
```organization::service::usecase::MODULE```



- Aws Sam has built in templates for TensorFlow, PyTorch, XGBoost, and Scikit-Learn machine learning pipelines


