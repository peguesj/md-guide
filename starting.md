## Quick Start Guide to PlantUML

For those interested in an initial exploration of PlantUML, we recommend using an online platform that directly supports PlantUML.

Explore it on our [online server](https://www.plantuml.com/plantuml).


## Local Installation Procedure

After trying the online version, if you're considering a more comprehensive local environment, a [local installation of PlantUML](faq-install) is suggested. Before installation, ensure the following prerequisites are met:

**Java:** PlantUML requires Java to be installed on your machine.

- Check if Java is already installed: ```java -version```. The minimum version needed is Java 8.

- If not installed, download and install it from the official [Java website](https://www.oracle.com/java/technologies) or through package managers like `apt` for Ubuntu, `brew` for macOS, etc.

**GraphViz**: Needed only for some diagrams.

- **Linux**: You'll find mode information [here](graphviz-dot) about GraphViz installation
- **Windows**: A compiled version of GraphViz is embedded within PlantUML, eliminating the need for a separate installation. However, if needed, you can acquire a standalone version [here](graphviz-dot)

Once ready, [download the plantuml.jar file](download) and execute it to access PlantUML’s [graphical user interface](gui). No further unpacking or installation procedures are needed.


## Command Line Operations

For those familiar with command line interfaces or intending to [integrate PlantUML with scripting or documentation platforms](running), PlantUML offers a convenient [command line syntax](command-line). Follow these steps:

1. **Compose a Text File**: Document your PlantUML commands. Here's a sample `sequenceDiagram.txt`:
```
@startuml
Alice -> Bob: test
@enduml
```

2. **Execute the File**: Process the aforementioned text file:
```
java -jar plantuml.jar sequenceDiagram.txt
```

3. **Alternative**: Launch the [Graphical User Interface](gui) and select the directory that contains the text files:
```
java -jar plantuml.jar -gui
```

Upon execution, a `sequenceDiagram.png` containing the sequence diagram will be generated.

Explore PlantUML to further your diagramming capabilities.


## Using Docker

Using [Docker](https://docker.com) to test PlantUML provides an isolated environment without requiring a direct installation of PlantUML or its dependencies on your machine.

### Instructions

1. **Pull the PlantUML Docker Image**

   There's an official [Docker image for PlantUML](https://hub.docker.com/r/plantuml/plantuml-server) available on Docker Hub.

```
docker pull plantuml/plantuml-server:jetty
```

   This command pulls the [PlantUML server image](https://hub.docker.com/r/plantuml/plantuml-server) using Jetty as the server.

2. **Run the PlantUML Server Container**

   Once the image is downloaded, you can run a container based on this image.

```
docker run -d -p 8080:8080 plantuml/plantuml-server:jetty
```

   This command does the following:

* ``-d``: Runs the container in detached mode.
* ``-p 8080:8080``: Maps port 8080 of the container to port 8080 on your host machine.

3. **Access PlantUML Server**

   Once the container is running, you can access the PlantUML server in your browser by visiting ``http://localhost:8080/``.


   You should see the PlantUML server's user interface, which allows you to type PlantUML code and see the visual representation on the fly.

4. **Test Your PlantUML Code**

   In the PlantUML server interface:

* Type or paste your PlantUML code into the provided text area.
* As you type or modify the code, the diagram on the right should update automatically.

5. **Stop the Container (when done)**

   When you're done testing your PlantUML diagrams, you might want to stop the running Docker container. First, identify the container ID:

```
docker ps
```

   This command lists all running containers. Look for the ``plantuml/plantuml-server:jetty`` image in the list and note the container ID.

   Now, you can stop the container:

```
docker stop [CONTAINER_ID]
```

   Replace ``[CONTAINER_ID]`` with the ID of your running PlantUML container.

6. **Remove the Container (optional)**

   If you want to remove the container entirely:

```
docker rm [CONTAINER_ID]
```

   This command removes the stopped container from your machine.


## PlantUML Integration Capabilities

Over the years (since 2009!), the tool has been integrated with a [variety of platforms and tools](running), offering users flexibility and ease of use.

Here's a summary of PlantUML's integration capabilities.

- **IDE Integration**:
  - [IntelliJ IDEA](https://plugins.jetbrains.com/plugin/7017-plantuml-integration): Plugins like "PlantUML integration" let you view and edit PlantUML diagrams directly within the IDE.
  - [Eclipse](eclipse): The "PlantUML Eclipse Plugin" allows for the same in the Eclipse IDE.
  - [VS Code](https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml): Extensions like "PlantUML" facilitate diagram preview and other features in Visual Studio Code.
  - Others: [NetBeans](https://plugins.netbeans.apache.org/?search=plantuml), and more.

- **Version Control System Integration**:
  - Git: With certain extensions, you can view PlantUML diagrams in repositories without needing to render them first.
  - [GitLab](https://docs.gitlab.com/ee/administration/integration/plantuml.html) have PlantUML integration to view UML diagrams in markdown files directly.
  - There is a [Github action](https://github.com/marketplace/actions/generate-plantuml) that generates UML diagrams and pushes them to your repository.

- **Documentation and Wiki Tools**:
  - [Confluence](https://marketplace.atlassian.com/search?query=plantuml): With the "PlantUML for Confluence" plugin, you can embed UML diagrams directly into your Confluence pages.
  - [Markdown](https://blog.anoff.io/2018-07-31-diagrams-with-plantuml/): PlantUML supports the embedding of diagrams in markdown, which can then be rendered by many platforms that support extended markdown.

- **Continuous Integration/Continuous Deployment (CI/CD)**:
  - Some CI/CD tools and platforms allow for the automated generation and rendering of PlantUML diagrams as part of the build or documentation process.

- **Browser Extensions**:
  - There are [browser extensions](https://chrome.google.com/webstore/detail/plantuml-visualizer/ffaloebcmkogfdkemcekamlmfkkmgkcf) that can render PlantUML diagrams directly within web pages, especially useful for platforms where native integration doesn't exist.

- **Other Tools**:
  - [Doxygen](https://www.doxygen.nl/manual/config.html#cfg_dot_uml): A documentation generator tool, Doxygen, has PlantUML integration to generate UML diagrams from annotated source code.
  - [Sphinx](https://pypi.org/project/sphinxcontrib-plantuml/): The Python documentation generator has plugins to integrate PlantUML diagrams.
  - [AsciiDoc](https://github.com/asciidoctor/asciidoctor-diagram): With the `asciidoctor-diagram` extension, you can embed PlantUML diagrams in AsciiDoc documents.

- **Cloud Platforms**:
  - Certain cloud platforms like [GitLab](https://docs.gitlab.com/ee/administration/integration/plantuml.html) provide native integration with PlantUML, allowing for rendering diagrams directly in repositories or wikis.

- **Docker**:
   - [Docker Image for PlantUML](https://hub.docker.com/r/plantuml/plantuml): There's a Docker image for PlantUML, which makes it easy to run PlantUML in a containerized environment for various purposes.


## PlantUML Language Reference Guide

For an in-depth understanding of PlantUML, the [PlantUML Language Reference Guide](guide) is available.

This guide provides comprehensive insights into the language, from basic syntax to advanced techniques. It's a valuable resource for all users. Acquire your copy and expand your diagramming knowledge.


