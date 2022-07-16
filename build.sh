#!/bin/bash
docker buildx build --platform=linux/arm64,linux/amd64 -t  jxch/capital-baostock:$(date +%Y%m%d) -t jxch/capital-baostock:latest . --push