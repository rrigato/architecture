# [main concepts doc](https://reactjs.org/docs/hello-world.html)

> React embraces the fact that rendering logic is inherently coupled with other UI logic: how events are handled, how the state changes over time, and how the data is prepared for display

> Instead of artificially separating technologiesby putting markup and logic in separate files, React separates concerns with loosely coupled units called “components” that contain both

- JSX is an extension of JavaScript 
- JSX is xss (cross site scripting) safe because react DOM escapes any characters before rendering them
- react elements are immutable

- react focuses on how the ui should look at a given moment instead of how it changes over time
- components take props as an argument and return a react element  
 
- always start react components with a capital letter.
- props are read only
- all react components must be pure = do not modify props and invoking with the same input props provides the same output react element
  
- I like how the components for buttons, forms, etc. can be used, but I am terrified of the nesting/types that can be passed to props.
    - I could see this resulting in a lot of global scope being passed around, I strongly prefer having clear inputs with type and name defined


> In React apps, whether a component is stateful or stateless is considered an implementation detail of the component that may change over time. You can use stateless components inside stateful components, and vice versa.

- Testability could be a concern if you have a react component violating the single responsibility principle
  
- mounting = life cycle event describing when a react component is rendered to the DOM 

- this.setState is asynchronous 


> React synthetic events do not work exactly the same as native events


> You have to be careful about the meaning of this in JSX callbacks. In JavaScript, class methods are not bound by default.


- Concerning that react components are coupled to js classes you have to deal with problems like these?