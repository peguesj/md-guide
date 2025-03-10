## lua

This page is used to provide some idea on how [lua](https://github.com/luaj/luaj) could be used instead of the current preprocessor.

For example, how would you change this:

```
@startuml
!function foo()
  !return "hello foo"
!endfunction
Bob -> Alice : foo()
@enduml
```

or

```
@startuml
!procedure define_actor($name)
  actor $name
!endprocedure

define_actor(Bob)

Bob -> Alice : hello
@enduml
```


