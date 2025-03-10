## Emacs
From the original work by [Zhang Weize](http://zhangweize.wordpress.com/2010/09/20/update-plantuml-mode), [plantuml-mode](https://github.com/skuro/plantuml-mode) supports editing and previewing PlantUML diagrams all within Emacs, optionally also integrating with [Org-Babel](http://orgmode.org/worg/org-contrib/babel).

[Luca Greco](http://twitter.com/lucagreco) has shared a set of
[standalone helpers](http://gist.github.com/547521) to edit, render, preview PlantUML code from Emacs.



## Org-Babel
[Org-Babel](http://orgmode.org/worg/org-contrib/babel) now
natively supports [blocks of plantuml code](http://eschulte.github.io/babel-dev/DONE-integrate-plantuml-support.html).

### Napkin
[ob-napkin](https://github.com/pinetr2e/ob-napkin) package is available from MELPA.

``ob-napkin`` supports Python syntax for sequence diagrams along with the plain plantuml code. Note that it uses Plantuml server, which means that it does not require to install JAR file and usually faster than invoking JVM.


## Emacs Org-Mode

1.) Download ``plantuml.jar`` from [official download page](https://plantuml.com/download) and save it at ``/home/you/path/to/plantuml.jar``

2.) install ``plantuml-mode`` via melpa.

3.) in ``*scratch*`` execute 
```
(setq org-plantuml-jar-path (expand-file-name "/home/you/path/to/plantuml.jar"))
(add-to-list 'org-src-lang-modes '("plantuml" . plantuml))
(org-babel-do-load-languages 'org-babel-load-languages '((plantuml . t)))
```
4.) put some uml in your org file e.g.
```
#+begin_src plantuml :file my-diagram.png
title Authentication Sequence

Alice->Bob: Authentication Request
note right of Bob: Bob thinks about it
Bob->Alice: Authentication Response
#+end_src
```
5.) export e.g. with ``C-c C-e h o``


### ob-plantuml.el (obsolete)
You can also use PlantUML with [Emacs org-mode](http://orgmode.org).

You will find the needed macro at the following address [http://www.emacswiki.org/emacs/IanYang](http://www.emacswiki.org/emacs/IanYang)

Once installed, embed PlantUML code in Emacs org-mode is used
like this:
```
#+BEGIN_UML
Alice -> Bob: Authentication Request
Bob --> Alice: Authentication Response
#+END_UML
```
While the org file is exported to HTML or other formats, PlantUML is called to generate image and replace the block in place.

Thanks to Ian Yang for the work done.

This method, however, is considered obsolete:
> ;; OBSOLETED, use ob-plantuml.el bundled in org instead.
( A citation from [https://www.emacswiki.org/emacs/org-export-blocks-format-plantuml.el](https://www.emacswiki.org/emacs/org-export-blocks-format-plantuml.el) )


