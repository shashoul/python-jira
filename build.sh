#!/bin/bash

MODULE_NAME="jira_issue"
VERSION=0.0.1.${BUILD_NUMBER}

docker build --network host -t ${MODULE_NAME}:${VERSION} .

aws ecr get-login --no-include-email --region us-east-1
aws ecr describe-repositories --repository-names clewmed/${MODULE_NAME} || aws ecr create-repository --repository-name clewmed/${MODULE_NAME}
docker tag ${MODULE_NAME}:${VERSION} 194091609479.dkr.ecr.us-east-1.amazonaws.com/clewmed/${MODULE_NAME}:${VERSION}
docker push 194091609479.dkr.ecr.us-east-1.amazonaws.com/clewmed/${MODULE_NAME}:${VERSION}
docker tag ${MODULE_NAME}:${VERSION} 194091609479.dkr.ecr.us-east-1.amazonaws.com/clewmed/${MODULE_NAME}:latest
docker push 194091609479.dkr.ecr.us-east-1.amazonaws.com/clewmed/${MODULE_NAME}:latest