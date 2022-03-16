# Testing for the website 'Drone Digest'

The following document outlines all testing carried out on the website 'Drone Digest'

During the construction process, the Dev Tools functionality of Chrome was used to test CSS code initially, where it was then tweaked to the desired outcome.

## Table of Contents

 1. [Validator testing](#validator-testing)
    * [HTML](#html)
    * [CSS](#css)
    * [Lighthouse](#lighthouse)
    * [Javascript](#javascript)
    * [Pep8](#pep8)
2. [Manual testing](#manual-testing)
    * [Responsive testing](#responsive-testing)
    * [Element testing](#element-testing)



## Validator testing

To view testing images please click on each individual hyperlink. These files can also be found in the [testing images](/testing/testing-images) folder.

### HTML

All HTML pages were passed through for testing via [W3C](https://validator.w3.org/) and the results are as follows:

1. [base.html](/testing/testing-images/base-html.png)

* Twelve errors were generated, but these were all caused by curly variable brackets so can be ignored.

2. [confirm-delete.html](/testing/testing-images/confirm-delete-html.png)

* Five errors were generated. Error four regarding form action was caused by a blank string. An attempt was made to fix using a "/" but this broke the file routing so was left untouched. All other errors were caused by curly variable brackets so can be ignored.

3. [home.html](/testing/testing-images/home-html.png)
 
 * Again the majority of errors were caused by curly variable braces. Errors 11 and 12 stating open elements were incorrect and had been closed correctly. Error five regarding the button however was fixed by using a snippet of javascript to set a href location on the button instead of using the a tag that had been wrapping the button. It was retested and passed validation.

 4. [new-thread.html](/testing/testing-images/new-thread-html.png)

 * Error four regarding form action was caused by a blank string. An attempt was made to fix using a "/" but this broke the file routing so was left untouched.. All other errors were caused by curly variable brackets so can be ignored.

 5. [signup-logon.html](/testing/testing-images/sign-up-html.png)

 * Five errors were caused again due to curly brackets and were ignored. Errors 4 and 6 regarding form action were caused by a blank string. An attempt was made to fix using a "/" but this broke the file routing so was left untouched.. Errors 8 and 9 were amended by adding an ID attribute to both form controls. Test was reran and errors were gone. 

 6. [threads.html](/testing/testing-images/threads-html.png)

 * The four errors found here were caused by curly brackets and could be ignored.


<br>

[Back to top](#table-of-contents)

<br>

### CSS

The CSS was tested using [Jigsaw](https://jigsaw.w3.org/css-validator/).

![CSS Results](/testing/testing-images/css.png)

One error was found were there was a space between the digit and the px value. This was deleted, retested and passed. 

<br>

[Back to top](#table-of-contents)

<br>

### Lighthouse

The site was tested for accessibility, performance and best practise using Google's [Lighthouse](https://developers.google.com/web/tools/lighthouse) tool. The results were as follows:

![Homepage](/testing/testing-images/homepage.JPG)

![Log On/Register Pages](/testing/testing-images/logon.JPG)

![Create Thread]()

![Thread Window](/testing/testing-images/thread.JPG)

![Confirm Delete](/testing/testing-images/confirm.jpg)

All tests were found to be within acceptable parameters.


<br>

[Back to top](#table-of-contents)

<br>

### Javascript

![JS Testing](/testing/testing-images/js.jpg)

Three warnings were received for missing semi-colons. These were amended, retested and passed. The warning around 'let' was ignored.


<br>

[Back to top](#table-of-contents)

<br>































