##m.no2bio.org
[![Feel free to fork the QR code too :)](https://raw.github.com/thedod/m.no2bio.org/master/html/img/qr-m.no2bio.png)](http://m.no2bio.org)

The `html/` folder contains static files that are [more or less] what you see in the actual [mobile portal](http://m.no2bio.org).
At the moment, [bootstrap 3](http://getbootstrap.com/) is used, but feel free to use whatever responsive framework you have in mind. Go ahead. Dazzle us with something.

###Phase 1: Static html (easily doable now)
This is a straitforward static html job, and if your pull-request's good - it may become our official skin (or perhaps an "unofficial" one available at `m.no2bio.org/skins/yourskin`).

Note that most of the pages simply contain iframes (that are responsive, but perhaps don't match your theme).
In the future this portal would [hopefully] contain lots of non-iframe content, but these specific pages would keep their "iframed applet" structure, mainly because these "applets" are also embedded [in](http://no2bio.org/bloggers/#bloggers-for-privacy) [other](http://no2bio.org/contact/)
[places](http://codepen.io/thedod/full/jAqLd).

###Phase 2: Blog integration and static html generation
Once we decide on a framework, we will start generating the content of `html/` automatically from:

* A config file (csv, json that would eventually come from a couchapp, etc.) defining the static part of the menu, as well as what to take from the blog.
* The blog's [JSON API](ihttps://wordpress.org/plugins/json-api/).

I believe this will be done as a cron jon in python with [mustache](http://mustache.github.io/) templates, but feel free to suggest alternatives (as long as the result is static html).

###Phase 3: Customizing iframed "applets"
If you want to customize the iframed "applets" themselves (i.e. they clash with the rest of the look),
here's where you can get the code and make it match your "main" theme.

* [Updates](http://m.no2bio.org/updates.html) (aka "the widget") ([gist](https://gist.github.com/thedod/6028657)).
* [Bloggers for privacy](http://m.no2bio.org/bloggers.html) ([gist](https://gist.github.com/thedod/5912762)).
* [Contact](http://m.no2bio.org/contact.html) ([repo](https://github.com/thedod/whatmail)).

