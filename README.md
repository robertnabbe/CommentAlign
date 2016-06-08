CommentAlign for SublimeText 3
==============================
A simple plugin for SublimeText 3 that columnizes the inline comments in your code to improve readability. The column will start after the _longest_ line in your code/selection. Make sure you've set the syntax for your document as this plugin will rely on that.

Usage
-----

`CommentAlign` will work with or without a selected region. To align your inline comments, press '**CTRL + ALT + ]**' on Windows and Linux; for OSX use the '**CMD + OPTION + ]**' to trigger the plugin.

Example
-------

The following code example:

    var a = "hey", 
	    b = "there",
	    some_arr = []; //initialize

	(function() { //run code when doc is ready
	    some_arr.push(a); //push first variable to  array
	    some_arr.push(b + ", kid!"); //something random..

	    if (a[1]=="e") {
	        a[1] == "a"; //change e to a, because why not?
	        some_arr.push(a); //push altered variable to array
	    }
	})();

..will be converted to:

    var a = "hey", 
        b = "there",
        some_arr = [];               //initialize

    (function() {                    //run code when doc is ready
        some_arr.push(a);            //push first variable to  array
        some_arr.push(b + ", kid!"); //something random..

        if (a[1]=="e") {
            a[1] == "a";             //change e to a, because why not?
            some_arr.push(a);        //push altered variable to array
        }
    })();


Install
-------

To install, simply clone this git repository to your packages directory.
	
	git clone https://github.com/robertnabbe/CommentAlign.git

Notes
-----

- Feel free to change the keymap combination to your liking;
- Currently only languages that use '**//**' for inline comments (e.g. C, C++, C#, CSS, Java, JavaScript, PHP, etc.) are supported;