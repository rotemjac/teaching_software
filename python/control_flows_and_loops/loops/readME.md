

break, continue, pass
break and continue are like other prograqm languages.
pass is unique, and basically doesn't do anything. 
From stackoverflow:
Since the pass keyword doesn't do anything, it's only useful when you syntactically 
need an indented suite, but don't want to do anything.
A common example is if you want to ignore some exception, you use except SomeException: pass. 
There are many other use cases as well. You wouldn't strictly need a 
keyword for this, since you could use any other statement that doesn't do 
anything (e.g. 0 is a perfectly valid statement that doesn't have an effect), but having 
a keyword for this allows you to be more explicit about not wanting to do anything.
