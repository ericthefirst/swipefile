# swipefile
Inspired by *Steal Like an Artist*, a web-based swipe file app to stash away stuff that inspires you.

![screenshot](img/sf_ss_50pct.png)

## Warning!
If you put this on your website, you should absolutely learn how [htaccess](https://www.seas.upenn.edu/cets/answers/auth-htpasswd.html) works and use it in the upload/ directory.  Otherwise, who knows what people might throw onto your site?  Another option is to put it in the root logbook directory, to keep the whole thing private.

## TODO
* On upload, use ImageMagick to create a smaller version to reduce load times.  Image links to copy of the original file.
* Only load so many at a time
* Allow editing filenames
* Add search
