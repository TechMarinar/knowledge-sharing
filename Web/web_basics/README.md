# Getting Comfortable with Web Basics

## HTML Form

    <form action="mailto:abc@xyz.com" method="post" enctype="text/plain">
    ...
    <input type="submit" name="">
    </form>

## CSS

**Styling:**

    hr {
        border-style: none;
        border-top-style: dotted;
        border-color: grey;
        border-width: 5px;
        width: 5%;
    }

    img:hover {
        background-color: gold;
    }

**Margin, Border, Padding**

    p {
        display: inline-block;
        width: 100px;
    }

    img {
        position: relative;
        left: 30px;
    }

    body {
        margin: 0;
    }

    .div-container {
        position: relative;
        width: 300px;
        height: 300px;
    }

    .div-class1 {
        display: inline-block;
        position: relative;
        right: 100px;
    }

    //Relative to its parent element
    .div-class2 {
        position: absolute;
        right: 100px;
        top: 100px;
    }

    //Always fixed on the screen at the same position
    .class-fixed {
        positioin: fixed;
        top: 0;
    }

* Display: block | inline | inline-block | none
* Common inline elements: <span> | <img> | <a>
* Position: static | relative | **absolute** | fixed
* Coordinates: top | bottom | left | right

**Center Align**

    //If element doesn't have a width set
    body {
        margin: 0;
        text-align: center;
        font-family: "Helvetica Neue",Helvetica,Arial,sans-serif
    }

    //If it's a block element and has its width set
    h1 {
        width: 10%;
        margin: 0 auto;
    }

**Font**

    body {
        font-family: "Helvetica Neue",Helvetica,Arial,sans-serif
    }

    h1 {
        margin-top: 0;
        font-size: 100%;
        font-family: 'Montserrat', sans-serif;
        font-weight: normal;
        <!-- line-height: 2; -->
    }

* 1em = 16 px = 100% = 1rem
* 1rem //Does not get affected by upstream size changes. Use this.

**Floating**

Use `float` only to wrap text and not for positioning.

    <div class="skill-row">
        <img class="code-img" src="" alt="">
        <h3>heading3</h3>
        <p class="code-skill-description">Paragraph</p>
    </div>

    .code-img {
        width: 25%;
        float: left;
        margin-right: 30px;
    }

    //No wrapping on the left
    .code-skill-description {
        clear: left;
    }

**Rotate**

    style="transform: rotate(30deg);"

## Bootstrap

1. Copy and paste bootstrap CDN in <head> section
2. Copy and paste javascript at the bottom of <body> element

## Bootstrap Grid Layout

    <div class="row">
        <div class="col-md-6">Val1</div>
        <div class="col-md-3">Val2</div>
        <div class="col-md-3">Val3</div>
    </div>

    <div class="row">
        <div class="col-lg-3 col-md-4 col-sm-6">Val1</div>
        <div class="col-lg-3 col-md-4 col-sm-6">Val2</div>
        <div class="col-lg-3 col-md-4 col-sm-6">Val3</div>
        <div class="col-lg-3 col-md-4 col-sm-6">Val4</div>
    </div>

## References

* colorhunt.co
* https://developer.mozilla.org/en-US/docs/Web/CSS/color_value
* devdocs.io
* www.favicon.cc
* markusvogl.com
* codepen.io
* www.cssfontstack.com
* fonts.google.com
* www.flaticon.com
* giphy.com
* https://www.frontendmentor.io/
* www.codeply.com
* ui-patterns.com/patterns
* dribbble.com
* sneakpeekit.com
* balsamiq.cloud