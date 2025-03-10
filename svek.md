## Current architecture: Svek

This current architecture (which codename is **Svek**) uses **Graphviz/Dot** to compute *nodes position*. The drawing itself is fully done in Java.

The main advantage is that, since PlantUML does the drawing, the software is now less dependent of Graphviz/Dot.

The code is also simpler, because the two steps (node computation *then* graphical rendering) are clearly separated.

With this architecture, Graphviz/Dot generates a simplified SVG output
(whatever is the actual output format need by the user), and those simplified SVG data are parsed by PlantUML.
The drawing is then done by PlantUML.


## Svek on debug mode [option debugsvek]

You can keep the intermediate *dot file* and the *simplified SVG output*, with the `debugsvek` option.

With this option:
```
java -jar plantuml.jar -debugsvek filename.puml
```

We can keep the 2 intermediate files:
- `filename_svek.dot`
- `filename_svek.svg`

*[Ref. [QA-4420](https://forum.plantuml.net/4420/)]*


