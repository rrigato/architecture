> React embraces the fact that rendering logic is inherently coupled with other UI logic: how events are handled, how the state changes over time, and how the data is prepared for display

> Instead of artificially separating technologiesby putting markup and logic in separate files, React separates concerns with loosely coupled units called “components” that contain both

- JSX is an extension of JavaScript 
- JSX is xss (cross site scripting) safe because react DOM escapes any characters before rendering them
- react elements are immutable

- react preferences focuses on how the ui should look at a given moment instead of how to change it over time
- components take props as an argument and return a react element  - Is the props JS object mutable by different components? 
- always start react components with a capital letter.
- props are read only
- all react components must be pure = do not modify props and invoking with the same input provides the same output
- I like how the components for buttons, forms, etc. can be used, but I am terrified of the nesting/types that can be passed to props.
  - - I could see this resulting in a lot of global scope being passed around, I strongly prefer having clear inputs with type and name defined