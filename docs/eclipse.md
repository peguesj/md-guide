## Information about the PlantUML Eclipse Plugin


The Eclipse Plugin is developed and maintained by
[Hallvard Trætteberg](https://github.com/hallvard)
*(many thanks for his work!)*.

Like the core library PlantUML itself, it is *open source* and the plugin is distributed under EPL license.

The source code [is hosted on GitHub](https://github.com/hallvard/plantuml).


## How to use it?
First, you have to display the *PlantUML View* (click the *Window* menu):

![](eclipse103.png)

This view displays automatically the class you are working on:

![](eclipse104.png)

If you write some comment in *PlantUML language*, the corresponding diagram is automatically displayed.
And if you have several comments with diagrams, it selects the one the cursor is in.

![](eclipse105.png)

In the *Preferences* Windows, you can also set up [GraphViz path if needed](graphviz-dot):

![](eclipse107.png)


## How to install it?


To install the plugin, you have to:
* Go to **Help/Software Update/Find and install...** or **Help/Install new software...**
* Create (if needed) or choose the following site as update site: ``http://hallvard.github.io/plantuml/``\n![](eclipse101.png)
* Select PlantUML features:\n![](eclipse102.png)
* Restart Eclipse


## How to improve it?

The plugin is not limited to Java source file, it also works with *Ecore**/Xcore*
files.

So that you can see the corresponding class diagram in a view side-by-side the *Ecore**/Xcore*
editor :

![](xwordfeud-plantuml.png)

If you want to support other file types, you can implement a new extension to do so.
You can have a look at
[the current xcore implementation](https://github.com/hallvard/plantuml/tree/master/net.sourceforge.plantuml.xcore).


