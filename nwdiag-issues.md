## Network diagram issues (nwdiag-issues)

This page lists issues on [nwdiag](nwdiag).


## Example *OK* on group of Peer networks [fixed on V1.2023.3beta4] [[#89FB89#FIXED]]

### Group on first
```plantuml
@startuml
nwdiag {
    internet [ shape = cloud];
    internet -- router;

    group {
      color = "pink";
      app;
      db;
    }

    network proxy {
        router;
        app;
    }

    network default {
    	app;
        db;
    }
}
@enduml
```

### Group on second
```plantuml
@startuml
nwdiag {
    internet [ shape = cloud];
    internet -- router;

    network proxy {
        router;
        app;
    }

    group {
      color = "pink";
      app;
      db;
    }

    network default {
    	app;
        db;
    }
}
@enduml
```

### Group on third
```plantuml
@startuml
nwdiag {
    internet [ shape = cloud];
    internet -- router;

    network proxy {
        router;
        app;
    }
    network default {
    	app;
        db;
    }
    group {
      color = "pink";
      app;
      db;
    }
}
@enduml
```

*[Ref. [Issue#408](https://github.com/plantuml/plantuml/issues/408) and [QA-12655](https://forum.plantuml.net/12655/nwdiag-overlapp-problem-with-3-newtorks?show=12661#c12661)]*


## Example *KO* with shape

1. Overlap of label for folder
1. Hexagon shape is missing

```plantuml
@startuml
nwdiag {
network Network {
Folder [shape = folder]
Hexagon [shape = hexagon]
}
}
@enduml
```

```plantuml
@startuml
nwdiag {
network Network {
Folder [shape = folder, description = "Test, long long label\nTest, long long label"]
Hexagon [shape = hexagon, description = "Test, long long label\nTest, long long label"]
}
}
@enduml
```


## Borderline cases of nwdiag (test of number lines)

### Element or Server

* How many adress lines before overlap? *[Hints: 7 (tested on V1.2021.8)]*

```plantuml
@startuml
nwdiag {
network Network {
server0 [address = "Adress_line_1\nAdress_line_2\nAdress_line_3\nAdress_line_4\nAdress_line_5\nAdress_line_6\nAdress_line_7\nAdress_line_8\nAdress_line_9"]
server1 [address = "Adress_line_1\nAdress_line_2\nAdress_line_3\nAdress_line_4\nAdress_line_5\nAdress_line_6\nAdress_line_7"]
}
}
@enduml
```


### Network

* How many adress lines before overlap? *[Hints: 7 or 16]*

```plantuml
@startuml
nwdiag {
network Network1 {
address = "Adress_line_1\nAdress_line_2\nAdress_line_3\nAdress_line_4\nAdress_line_5\nAdress_line_6\nAdress_line_7\nAdress_line_8\nAdress_line_9"
server
}
network Network2 {
address = "Adress_line_1\nAdress_line_2\nAdress_line_3\nAdress_line_4\nAdress_line_5\nAdress_line_6\nAdress_line_7\nAdress_line_8\nAdress_line_9"
server
}
}
@enduml
```
```plantuml
@startuml
nwdiag {
network Network1 {
address = "Adress_line_1\nAdress_line_2\nAdress_line_3\nAdress_line_4\nAdress_line_5\nAdress_line_6\nAdress_line_7\nAdress_line_8\nAdress_line_9\nAdress_line_10\nAdress_line_11\nAdress_line_12\nAdress_line_13\nAdress_line_14\nAdress_line_15\nAdress_line_16\nAdress_line_17"
server [address = "\nAdress_line_1\nAdress_line_2\nAdress_line_3\nAdress_line_4\nAdress_line_5\nAdress_line_6\nAdress_line_7\n"]
}
network Network2 {
address = "Adress_line_1\nAdress_line_2\nAdress_line_3\nAdress_line_4\nAdress_line_5\nAdress_line_6\nAdress_line_7\nAdress_line_8\nAdress_line_9\nAdress_line_10\nAdress_line_11\nAdress_line_12\nAdress_line_13\nAdress_line_14\nAdress_line_15\nAdress_line_16\nAdress_line_17"
server
}
}
@enduml
```


## Example *OK* with incoming server (e.g. the Internet or Web) [fixed on V1.2023.3beta4] [[#89FB89#FIXED]]

```plantuml
@startuml
nwdiag {
  web1 [shape = cloud]
  web2 [shape = cloud]
}
@enduml
```

```plantuml
@startuml
nwdiag {
  web1 [shape = cloud]
  web2 [shape = cloud]

  network {
    web1
    web2
  }
}
@enduml
```

```plantuml
@startuml
nwdiag {
  web1 [shape = cloud]
  web2 [shape = cloud]

  network {
    web1
    web2
    appli
  }
  network {
    appli
    db [shape = database]
  }
}
@enduml
```

- Q?: What is the line on the top of web2 ?  [fixed on V1.2023.3beta4]


## Minimal *OK* example... [fixed on V1.2023.3beta4] [[#89FB89#FIXED]]

```plantuml
@startuml
nwdiag {
  a
  b
}
@enduml
```

```plantuml
@startuml
nwdiag {
  ok
  ko
}
@enduml
```

```plantuml
@startuml
nwdiag {
  1
  2
  network {
   1
   2
   3
   4
  }
}
@enduml
```

```plantuml
@startuml
nwdiag {
  1
  2
  3
  6
  network 1 {
   1
   2
   3
   4
   5
   6
  }
  network 2 {
   1
   2
   3
   4
  }
}
@enduml
```


## Other internal networks (stretched) examples [[#89FB89#FIXED]] on V1.2023.9

```plantuml
@startuml
nwdiag {
  network {
    a;
    b;
    c;
  }
  a -- 1
  b -- 2
  c -- 3
}
@enduml
```

```plantuml
@startuml
nwdiag {
  network {
    a;
    b;
    c;
  }
  b -- 2
  c -- 3
}
@enduml
```


## Example *KO* on of Peer networks


```plantuml
@startuml
nwdiag {
    Internet [shape = cloud]
    Internet -- A
}
@enduml
```

VS

```plantuml
@startuml
nwdiag {
    Internet [shape = cloud]
    Internet -- A
    Internet -- B
}
@enduml
```


## OK: Example with 3 or more groups [[#89FB89#FIXED]]
```plantuml
@startuml
nwdiag {
  group {
    color = "#FFaaaa";
    web01;
    db01;
  }
  group {
    color = "#aaFFaa";
    web02;
    db02;
  }
  group {
    color = "#aaaaFF";
    web03;
    db03;
  }

  network dmz {
      web01;
      web02;
      web03;
  }
  network internal {
      web01;
      db01 ;
      web02;
      db02 ;
      web03;
      db03;
  }
}
@enduml
```
*[Ref. [QA-13138](https://forum.plantuml.net/13138)]*

```plantuml
@startuml
nwdiag {
  group {
    color = "#FFaaaa";
    web01;
    db01;
  }
  group {
    color = "#aaFFaa";
    web02;
    db02;
  }
  group {
    color = "#aaaaFF";
    web03;
    db03;
  }
  group {
    color = "#aaFFFF";
    web04;
    db04;
  }

  network dmz {
      web01;
      web02;
      web03;
      web04;
  }
  network internal {
      web01;
      db01 ;
      web02;
      db02 ;
      web03;
      db03;
      web04;
      db04;
  }
}
@enduml
```

▶ Seems to be corrected on V1.2021.10beta4-5+ *(but only on **opposite layout**)*


## Example *OK* on Goup of Peer networks between networks [fixed on V1.2023.3beta4] [[#89FB89#FIXED]]
 
### Group first: OK
```plantuml
@startuml
nwdiag {
  group group02 {
    color = palegreen
    a02;
    a01;
  }
  network net01 {
    a01;
  }
  a01 -- a02;
  network net02 {
    a02;
  }
}
@enduml
```

### Group at the end: OK (1.2023.3beta4)
```plantuml
@startuml
nwdiag {
  network net01 {
    a01;
  }
  a01 -- a02;
  network net02 {
    a02;
  }
  group group02 {
    color = pink
    a02;
    a01;
  }
}
@enduml
```


## Test of Peer networks

### No link
```plantuml
@startuml
nwdiag {
c1 [ shape = cloud];
c2 [ shape = cloud];
network nw {
  a;
  b;
}
}
@enduml
```

### On up
```plantuml
@startuml
nwdiag {
c1 [ shape = cloud];
c2 [ shape = cloud];
c1 -- a;
c2 -- b;
network nw {
  a;
  b;
}
}
@enduml
```

### On down
```plantuml
@startuml
nwdiag {
network nw {
  a;
  b;
}
c1 [ shape = cloud];
c2 [ shape = cloud];
a -- c1;
b -- c2;
}
@enduml
```

### Up/Down
```plantuml
@startuml
nwdiag {
c1 [ shape = cloud];
c2 [ shape = cloud];
c1 -- a;
network nw {
  a;
  b;
}
b -- c2;
}
@enduml
```


### KO but perhaps not realistic [[#C90000#KO]]
```plantuml
@startuml
nwdiag {
network nw {
  a;
  b;
}
c1 [ shape = cloud];
c2 [ shape = cloud];
c1 -- a;
c2 -- b;
}
@enduml
```

### KO but perhaps not realistic [[#C90000#KO]]
```plantuml
@startuml
nwdiag {
c1 [ shape = cloud];
c2 [ shape = cloud];
c1 -- a;
network nw {
  a;
  b;
}
c2 -- b;
}
@enduml
```

### KO (2 nw) but perhaps not realistic [[#C90000#KO]]
```plantuml
@startuml
nwdiag {
c1 [ shape = cloud];
c2 [ shape = cloud];
c1 -- a;
network nw {
  a;
  b;
}
b -- c2;
network nx {
b
}
}
@enduml
```


### KO : how to manage multiple peers [[#C90000#KO]]
```plantuml
@startuml
nwdiag {
c1 [ shape = cloud];
c1 -- a;
c1 -- b;
}
@enduml
```

### Up
```plantuml
@startuml
nwdiag {
c1 [ shape = cloud];
network nw {
  c1;
  a;
  b;
}
}
@enduml
```

### Down
```plantuml
@startuml
nwdiag {
network nw {
  c1;
  a;
  b;
}
c1 [ shape = cloud];
}
@enduml
```


### Other remarks ("What about...") [[#C90000#KO]]
```plantuml
@startuml
nwdiag {
c1 [ shape = cloud];
c2 [ shape = cloud];
c1 -- a;
c2 -- b;
network nw {
  a;
  b;
}
}
@enduml
```
```plantuml
@startuml
nwdiag {
c1 [ shape = cloud];
c2 [ shape = cloud];
c1 -- a;
b -- c2;
network nw {
  a;
  b;
}
}
@enduml
```

*[Ref. [QA-17932](https://forum.plantuml.net/17932/nwdiag-possible-misbehavior)]*


