#!/bin/sh
# Cache-busting for the static site. GitHub Pages lets browsers cache
# styles.css and the .js files for 10 minutes, so right after a deploy a
# visitor can get the NEW html with the OLD css/js (e.g. unstyled pages).
# Every page references them as `styles.css?v=<version>`; changing the
# version makes browsers fetch the new files immediately.
#
# Run before committing changes to styles.css or any .js file:
#   sh web/bump-version.sh
set -e
cd "$(dirname "$0")"
v=$(date +%Y%m%d%H%M)
for f in *.html; do
  sed -E -i.bak \
    -e "s/(href=\"styles\.css)(\?v=[0-9]+)?\"/\1?v=$v\"/g" \
    -e "s/(src=\"(auth|catalog|config)\.js)(\?v=[0-9]+)?\"/\1?v=$v\"/g" \
    "$f"
  rm -f "$f.bak"
done
echo "Asset version set to $v"
