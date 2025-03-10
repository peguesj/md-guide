# wiki.md

## Overview

This project provides a comprehensive reference guide for PlantUML, including various diagram types and their usage. The main file, `wiki.html`, serves as the entry point for the guide, rendering markdown content and providing interactive features such as code highlighting and diagram rendering.

## How It Works

1. **Markdown Files**: The content is organized into multiple markdown files, each representing a different section or diagram type. These files are listed in the `toc.js` file, which maps titles to their respective markdown files.
2. **HTML Rendering**: The `wiki.html` file loads and renders the markdown content using the `marked` library for markdown parsing and `Prism.js` for syntax highlighting.
3. **Interactive Features**: The HTML file includes buttons for rendering PlantUML diagrams and copying code snippets. These features are implemented using JavaScript functions defined within the HTML file.
4. **Table of Contents**: The `toc_table.md` file provides a structured table of contents, which is generated and updated using the `transform_toc.py` and `update_toc_mappings.py` scripts.

## Prerequisites

- **Python 3.x**: Required for running the `transform_toc.py` and `update_toc_mappings.py` scripts.
- **Node.js**: Required for running the `marked` library and other JavaScript dependencies.
- **Internet Connection**: The project relies on external libraries hosted on CDNs, such as Bootstrap, Prism.js, and marked.

## Dependencies

- **Bootstrap 5**: For styling and responsive design.
- **Prism.js**: For syntax highlighting.
- **marked**: For markdown parsing.
- **pako**: For PlantUML encoding.
- **jQuery**: For DOM manipulation and event handling.

## Setup

1. **Clone the Repository**:
    ```sh
    git clone <repository-url>
    cd /md-guide
    ```

2. **Install Python Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the Python Scripts**:
    - To transform the table of contents:
        ```sh
        python transform_toc.py
        ```
    - To update the TOC mappings:
        ```sh
        python update_toc_mappings.py
        ```

4. **Open `wiki.html` in a Browser**:
    - Simply open the `wiki.html` file in your preferred web browser to view the rendered content.

## Usage

- **Navigating the Guide**: Use the sidebar to navigate through different sections of the guide.
- **Rendering Diagrams**: Click the "Render" button next to PlantUML code blocks to generate diagrams.
- **Copying Code**: Click the "Copy" button to copy code snippets to the clipboard.
- **Back to Top**: Use the "Back to Top" button to quickly scroll to the top of the page.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your fork.
5. Create a pull request to the main repository.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

