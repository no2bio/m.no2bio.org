##m.no2bio.org
[![Feel free to fork the QR code too :)](https://raw.github.com/thedod/m.no2bio.org/master/html/img/qr-m.no2bio.png)](http://m.no2bio.org)

The `html/` folder contains the static files you see in the actual [mobile portal](http://m.no2bio.org) [not necessarily the newest version].
The html files inside it were generated with `make-m.py` (see below), but if you want to suggest better html design and don't want to dive into the templates (not too hard, but maybe you don't), feel free to simply edit one or more pages at `html/` and pull-request it (including all css+js needed), and we'll try to "templatize" it.

At the moment, [bootstrap 3](http://getbootstrap.com/) is used, but feel free to use whatever responsive framework you have in mind. Go ahead. Dazzle us with something exotic.

**Even if your design doesn't become out "mainstream" theme, it may end up as an unofficial theme on our site, so don't hesitate to suggest something "too wild"**

###Generating html from templates [optional]
* First time, do `git submodule update --init`. This would fetch [pystache](https://github.com/defunkt/pystache), python library for [mustache](http://mustache.github.io/) templates.
* You can edit [menu.csv](https://github.com/thedod/m.no2bio.org/blob/master/menu.csv) with a spreadsheet program (or even a text editor). The semantics are explained at [menu.csv.doc.md](https://github.com/thedod/m.no2bio.org/blob/master/menu.csv.doc.md).
* Do `python make-m.py`

### Customizing iframed "applets"
Some of the pages in the portal show iframes containing "applets". They're all responsive, but if you design your own theme, maybe you'd want to theme them with a similar look:

* [Updates](http://m.no2bio.org/updates.html) (aka "the widget") ([gist](https://gist.github.com/thedod/6028657)).
* [Bloggers for privacy](http://m.no2bio.org/bloggers.html) ([gist](https://gist.github.com/thedod/5912762)).
* [Contact](http://m.no2bio.org/contact.html) ([repo](https://github.com/thedod/whatmail)).

