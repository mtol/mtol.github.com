# Linden Mackenzie Tolhurst

## Prerequisites

    pip install pelican ghp-import

## Instructional

**Gah, what's going on here?** This static website is generated using  [Pelican], as configured in `pelicanconf.py` and `publishconf.py`. There are two primary branches:

* `source`: where the source for the website is, including the Pelican configuration files; and
* `master`: where the built website is uploaded to to be rendered by [Github Pages][ghp]

Any work done should be done in the `source` branch. The directory structure is as follows:

* `pages`: the pages that consitute the website;
* `theme`: where the page templates reside; and
* `output`: the build directory, where the generated HTML is stored.

The `content` directory, per a typical Pelican setup, is for blog posts which is not currently used.

You can build the project by running `make`, and export it using `make github` which builds into the `output` directory and pushes its contents to `master` using [`ghp-import`][ghp-import].

[pelican]: http://docs.getpelican.com "Pelican"
[ghp-import]: https://github.com/davisp/ghp-import "davisp/ghp-import"
[ghp]: http://pages.github.com/
