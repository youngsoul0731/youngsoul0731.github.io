# Yuanshuo Zhang’s Homepage

Personal academic website: https://youngsoul0731.github.io/

Adapted from [Jingbo Wang’s homepage](https://github.com/wangjingbo1219/wangjingbo1219.github.io). Attribution is retained in the page footer and [TEMPLATE_CREDITS.md](TEMPLATE_CREDITS.md).

## Structure

```text
index.html              Page content — edit this file directly
styles.css              Styling and responsive layouts
main.js                 Navigation interactions
images/avatar.jpg       Personal portrait
icons/                  Site icon
projects/               Research figures, organized by topic and project
about.html, about/      Compatibility redirects for old URLs
.github/workflows/      Static GitHub Pages deployment
```

The site uses plain HTML, CSS, and JavaScript, matching the reference template’s structure. It has no Jekyll, Ruby, package installation, or content-generation dependency. Paper content is written directly in `index.html`.

## Preview and publish

Run `python3 -m http.server 8001 --bind 127.0.0.1` from this folder and open http://127.0.0.1:8001/ (or open `index.html` directly).

Push changes to `main` to publish through the static Pages workflow. The workflow uploads only the website files. `.nojekyll` also supports serving the static site without Jekyll processing.
