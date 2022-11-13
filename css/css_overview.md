```css
div ul{
/*ul inside a div*/
}```

```css
h1 + p{
/*p directly after an h1*/
}```

```css
h1, p {
/*h1 and p tags*/
}```

```css
div.class-name{
/*div with class of class-name*/
}```

```css
a:hover{
/*changes css based on hover state*/
}```




- floated elements are always ```display:block```
- float = element is taken out of the normal layout flow and stuck to the left or right of its parent container
  - any content that would come below the floated element in a normal flow would wrap around it inline
  
- ```display:flex``` = element this is applied to acts like a ```display:block``` but its children are flex items

# tables
- ```thead th:nth-child(n)``` selects the nth child that is a ```th``` for the ```thead``` parent
  - ```nth-child``` also takes ```even``` and ```odd``` parameters
- ```border-collapse:collapse``` makes sure there is no spacing between table elements
