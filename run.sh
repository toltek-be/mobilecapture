#!/bin/bash
URL=${1:-"https://example.com"}
DELAY=${2:-3}

docker run --rm \
  -e TARGET_URL="$URL" \
  -e LOAD_DELAY="$DELAY" \
  -v $(pwd)/screenshots:/screenshots \
  screencapture
