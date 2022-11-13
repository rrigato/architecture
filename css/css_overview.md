```css
div ul{
/*ul inside a div*/
}
```

```css
h1 + p{
/*p directly after an h1*/
}
```

```css
h1, p {
/*h1 and p tags*/
}
```

```css
div.class-name{
/*div with class of class-name*/
}
```

```css
a:hover{
/*changes css based on hover state*/
}
```

- at rules 
```css
@media(min-width: 750px)
div{
/*how browser should behave based on screen width of at least 750 px*/
}
```

- outer ```display:block``` type = box will break to newline, width/height respected
- outer ```display:inline``` = no new line, width/height ignored
- ```display:inline-block``` = width, height, padding and margin are respected without the box going to a newline



- floated elements are always ```display:block```
- float = element is taken out of the normal layout flow and stuck to the left or right of its parent container
  - any content that would come below the floated element in a normal flow would wrap around it inline
  
- ```display:flex``` = element this is applied to acts like a ```display:block``` but its children are flex items

# tables
- ```thead th:nth-child(n)``` selects the nth child that is a ```th``` for the ```thead``` parent
  - ```nth-child``` also takes ```even``` and ```odd``` parameters
- ```border-collapse:collapse``` makes sure there is no spacing between table elements
