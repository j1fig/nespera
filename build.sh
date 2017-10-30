#!/bin/bash

VERSION="0.1.0"
TAG="j1fig/nespera:$VERSION"

echo Building nespera v$VERSION ...

docker build -t $TAG .
docker push $TAG

echo Done!
