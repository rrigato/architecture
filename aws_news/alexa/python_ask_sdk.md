- ```handler_input.response_builder.ask()``` = if you want to keep the session open and re-prompt the user with a new question

- ```SkillBuilder().lambda_handler()``` = returns a function that you should specifiy as your lambda handler in your function configuration that can handle an alexa skills kit invocation event

- request and exception handlers are processed from top to bottom
```python
alexa_skill = SkillBuilder()
alexa_skill.add_request_handler(FirstIntentHandlerProcessed())
alexa_skill.add_request_handler(SecondIntentHandlerProcessed())
alexa_skill.add_request_handler(ThirdIntentHandlerProcessed())

alexa_skill.add_exception_handler(CatchAllExceptionHandler())
```
