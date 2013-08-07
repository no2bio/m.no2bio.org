The menu is defined at [menu.csv](https://github.com/thedod/m.no2bio.org/blob/master/menu.csv) in the format and with the semantics documented here.

The format supports infinite levels of nesting, but the mustache templates would probably only support 2 levels (and there's no real need for more).

###Fields
The first line *has* to be `"id","name","type","parent","arg"` (or `make-m.py` would break).
These are, of course the field names of all columns.

####id
Should be unique (regardless of nesting level).
Depending on `type` (see below), this may be used to construct a filename (e.g. "`id`.html").

####name
Displayed as the menu item's text. Most probably Hebrew.

####type
One of the following options:
* *homepage* - Generate `id`.html (`id` would probably be "index") from the "homepage" template (hard-wired html, depends on events etc.).
* *iframe* - Generate `id`.html (`id` would probably be "index") from the "iframe" template. `arg` (see below) is iframe's src.
* *submenu* - Menu items defined *later* in the csv file can use this item's `id` as the `parent` (see below).
* *category* - Get a catageory from the blogs Api, generate an entire submenu, and the actual html pages. `arg` (see below) is slug of post to appear first on the menu.

####parent
Either empty (item will appear at root), or the `id` of a *previously defined* item with `type` *submenu*. Once again, note that although a *submenu* can have a *submenu* parent, this isn't supported by the mustach themes, and anyway - it isn't practical GUI-wise.

####arg
Depends on `type`

* For *iframe*, it's the iframe's src.
* For *category*, it's the slug of the post to be shown first in the category's sub menu (the rest are sorted alphabetically). This conforms to the logic of the "desktop site", where most categories have a "representing" or "read this first" post.

