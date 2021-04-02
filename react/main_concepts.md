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



- controlled components = forms whose single source of truth is stored in component state
 
- do not try to sync state between react components, all state should have a single source of truth in the highest parent component that needs that state

- use [react developer tools](https://github.com/facebook/react/tree/master/packages/react-devtools) to inspect props and move up the component hierarchy tree

- if something can be derived from existing props or state, do not store it as state, calculate it when it is needed.

> At Facebook, we use React in thousands of components, and we haven’t found any use cases where we would recommend creating component inheritance hierarchies.

- if you ensure that your react components are following the single responsibility principle and the props/state are statically typed, not using inheritance is a real benefit.