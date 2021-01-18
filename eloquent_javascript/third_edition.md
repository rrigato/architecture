- [introduction](#introduction)
- [chapter_3](#chapter_3)
- [chapter_4](#chapter_4)
- [chapter_5](#chapter_5)
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

# chapter_5