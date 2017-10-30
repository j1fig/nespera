#!/bin/bash

VERSION="0.1.0"
TAG="j1fig/nespera:$VERSION"

docker pull $TAG:$VERSION

docker run -it --volume `pwd`/db:/app/db --rm $TAG
