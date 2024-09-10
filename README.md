# blaaskaak.nl

This is the repository for the [blaaskaak.nl](https://blaaskaak.nl) website.

This README will guide you through the process of setting up the site locally
and provide a brief overview of how Hugo, the site builder, works.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Hugo](https://gohugo.io/getting-started/installing/) (Prebuilt binaries
  recommended)

## Getting Started

Follow these steps to get the site up and running on your local machine:

1. **Clone the Repository**

    ```sh
    git clone git@github.com:CoenPrins/blaaskaak.git
    cd blaaskaak
    ```

2. TODO: first build event list?

2. **Start the Hugo Server**

    Run the following command to start the local Hugo development server:

    ```sh
    hugo server
    ```

3. **Open in Browser**

    Open your web browser and navigate to `http://localhost:1313` to view the site.

## How Hugo Works

Hugo is a static site generator that builds your site from content, normally
written in Markdown, but we do HTML, and templates written in HTML. Here's a
brief overview of the key components:

- **Assets**: The css and javascript of the website. Only loaded if included in
  the code, see the [Hugo Docs](https://gohugo.io/functions/resources/get/).
- **Content**: Write the content of the website in the `content/` directory.
  Each file represents a page.
  > [!TIP]
  > Give your file a good name, because its name is converted to the title of
  > that page: `over-ons.html` becomes `/over-ons/` in the url and `Over ons`
  > in the title!
- **Templates**: Define the structure and layout of your site using HTML
  templates in the `layouts/` directory. These templates determine how your
  content is rendered.
- **Static Files**: These files are copied to the output folder during build.
  No processing is done (hence; static).
- **Configuration**: Configure your site using the `hugo.toml` file. This
  file contains settings such descriptions of Blaaskaak, and the url to certain
  images.

## Resources

For more information on Hugo, check out the following resources:

- [Hugo Documentation](https://gohugo.io/documentation/)
