- [introduction](#introduction)
- [chapter_3](#chapter_3)
- [chapter_4](#chapter_4)
- [chapter_11](#chapter_11)
- [chapter_13](#chapter_13)
- [ch14_dom_browser_api](#ch14_dom_browser_api)
- [ch15_event_handlers](#ch15_event_handlers)
- [web_design_and_ajax](#web_design_and_ajax)
- [jquery](#jquery)
- [js_runtime_context_scope](#js_runtime_context_scope)
- [web_architecture](#web_architecture)
# introduction
- session storage = only accessible within the same tab, removed on tab close, 5 mb
- local storage = 10 mb, never expires and stored in browser

```javascript
# template expression
`This is a string with ${a_variable}` 
```
- && (logical and), || (logical or), !(logical not)

- NaN cannot be compared to itself
- ```&&``` and ```||``` use short circuit evaluation 
- logicalExpression ? trueEvaluation : falseEvaluation;
- functions with no return value return undefined
- functions with the function keyword are hoisted to the top of the code
- arrow functions
```javascript
const arrowFunction = (paramOne, paramTwo) =>{
    //statements
};
```
- The following are equilvalent
```javascript
const square1 = (x) => { return x*x; };
const square2 = x => x*x;
```

- call stack keeps track of context of nested function calls

```javascript
function power (base, defaultValue=2){

}
```

# chapter_3
- two types of functions
  - functions that are idempotent (called with the same arguements you get the same result)
  - functions that depend on the global scope/context

- elements of an array are its properties where the property name is the index value
- reading a property key that does not exist on an object returns undefined

```javascript
"x" in {x: "hello", y:, "world"}; //true

Object.keys({x:0, y:1}); // ["x", "y"]

typeof []; //"object"

[1, 2, 3].includes(2); // true

for(let arrayElement of [1, 2, 3]){
    console.log(arrayElement); // 1 2 3
}

"hello".indexof("o"); // 4

function myFunction(...varName){
    //passes any number of args
} 
```

- ```let``` or ```const``` prevents a variable from binding to the global namespace

- destructuring
```javascript
//myName will have value of 1
let {myName} = { myName: 1, x: 2 };
```

# chapter_4
```javascript
//converts object to JSON
JSON.stringify();
//reads JSON and returns an Object
JSON.parse();

//[3, 4]
[1, 2, 3, 4].filter((x) =>{ return(x > 2)});

//provides hints on what should/should'nt be provided to javascript
"use strict"; 

//true
[1] instanceof Array;
```

- map function = apply a function to each element of the array 

- all JS objects have an Object.prototype which passes common functionality to functions like .toString()
- protoypes are static 
- encapsulation and polymorphism decouple, while inheritance tightly couples

# chapter_11
- INI file = ; and blank lines ignored
  - [] = new sections

- exports in commonJS are not available in the local scope
- ES modules can export functions, classes or let/const
- if something can be done with a function, use a function instead of going through the rituals of moving your objects through various states
- Promise = class that is an asyncoronous actions whose ```.then``` method returns the result to the callback from the promise 

- Promise can be resolved(succeded) or rejected(failed)
- ```Promise.All()``` returns an array of resolved promises
  - if any of the resolved promises in the array failed, the whole 
  ```javascript 
  Promise.All()
  ``` 
  fails
- async function returns a promise
```javascript
// yields the result of the async function
await async_func_call();

//arrow function can be made async
['url1.example.com', 'url2.example.com', 'url3.example.com'].map(async hostname =>{
    return(await axios.get(hostname));

});
```

# chapter_13

``` html
<!--Block elements = take up the whole width of the document-->
<h1></h1>
<p></p>

<!--inline elements = rendered on the same line as the surrounding text-->
<b></b>
<a></a>
```

``` css
/*applies to p elements with id main and classes a and b*/
p#main.a.b{}
/*applies to all a tags inside of p tags*/
p a {}
```
- sandboxing = limitations to underlying resources placed on .js files by the browser
- when multiple css rules have the same property selector, the most recently read rule wins

# ch14_dom_browser_api
- The document object model (DOM) is an api that allows scripts to access and update the contents of a web page while loaded in the browser

- HTML5 common javascript API's
 - geolocation = where the user is location
 - localStorage = stores data even after the browser is closed
 - sessionStorage = keeps info while the browser tab is open
 - history = items from the browser history

- Always consider the cross compatibility implications when using newer browser javascript APIS

- you can modify the browser history call stack

- Key-value pairs in objects are unordered

- Date object stores the number of milliseconds since the epoch


# ch15_event_handlers
- window.addEventListener = register a callback handler taht is called when an event occurs
- the most specific event handler is called first

```javascript
//stop the event from propagating to the parent node event
event.stopPropagation()

//Prevents the default action such as link, down arrow from occurring
event.preventDefault()

//reference to end a timeout early
let x = setTimeout(() =>{
  console.log('hello');

}, 500);
clearTimeout(x);


setInterval(() =>{
  console.log('prints every 2 seconds');
}, 2000);


```
- common events:
  - mousedown event = click down on mouse
  - mouseup event = release click of a mouse
  - click event = mouseup followed by a mouse down
  - touch event for touchscreens
  - focus/blur = when user moves from or to the browser tab/window
  - load = fires when the document/image is loaded
  - beforeunload = fires before the page is closed to prevent user from losing work
  - submit = fired when a button of type="submit" is clicked on a form



# web_design_and_ajax

- Draw a site map on a paper where every page is represented
- Sketch the information needed for each page on a piece of paper before beginning the design

- Keep your primary navigation bar the same across all of the content on your site

- When the browser comes across a ```html <script>``` tag it will stop processing the page and wait for the script to finish processing

# jquery
- jQuery plugins = extensions for jQuery where you first include jquery and then include the plugin
  - plugins are just IIFE (immediately invoked function expressions) that you can assign to ```HTML $.fn.<plugin_name>``` and then are invoke with ```HTML $('<some_selector>').<plugin_name>(function_arguements)```


# js_runtime_context_scope
- js has both global and function level context/scope

- each execution context (function or global) has its own variables object that holds variables/functions/parameters

- nested functions can access their parents variables but parent functions cannot access the variables of functions they invoke
- There are 7 types of built in JS errors, each with a name and a message

- optimizing is only useful when you have code that is already taking a lot of time
- 
# web_architecture
- HTML is responsible for structuring content, CSS is responsible for presentation, and javascript is responsible for behaviors
- Editing HTML/CSS should not necessitate updating your JS scripts and vice-versa