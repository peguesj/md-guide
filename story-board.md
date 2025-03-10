## User Story Board 

This diagram can represent User Story Maps as used in agile software development: Activity> User Task> Story, and their allocation into Sprints (see this tutorial on [User Story Mapping](https://www.aha.io/roadmapping/guide/release-management/what-is-user-story-mapping), a [Quick Reference](http://www.jpattonassociates.com/wp-content/uploads/2015/03/story_mapping.pdf), or the whole [Story Mapping](https://www.jpattonassociates.com/story-mapping/) site).

In the future it may support other agile terminology, eg Epic> Story> Task, and their allocation into Releases (FixVersions).

It is very rudimentary for now, and we hope to add:

- Colors
- Text wrapping in the boxes
- Labels in the left margin
- Links to detailed story descriptions

Please comment in [issue #423](https://github.com/plantuml/plantuml/issues/423) "Incubation of user story board"


## Desired Diagram

The target (desired) diagram looks something like this.

![](https://user-images.githubusercontent.com/4921146/102212806-aefd8480-3ecd-11eb-8d71-e2e16fe1d10a.png)


## Current Implementation

The current implementation looks like this.
The components of a board are made out as an indented list.

First a tiny board:

```plantuml
@startboard
A1
+U1.1
++S1 R1
++S1 R2 
+U1.2
A2
@endboard
```

Now a more realistic board: 

```plantuml
@startboard
Activity 1
+User Task 1a
++Story 1 Release 1
++Story 2 Release 1
+User Task 1b
++Story 3 Release 1
+++Story 4 Release 1
++++Story 5 Release 2

Activity 2
+User Task 2
+++Story 6 Release 1
+++Story 7 Release 1
+++Story 8 Release 2
Activity 3

+User Task 3
++++Story 9 Release 2
++++Story 10 Release 3
@endboard
```


