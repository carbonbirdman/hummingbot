#! /bin/bash
docker build --file Dockerfile --memory-swap='4g' --memory='2g' --tag carbonbot:dev .
#docker build --file Dockerfile_half --tag carbonbot:dev .
