#!/bin/bash

if [[ ${GITHUB_EVENT_NAME} == "push" ]]; then
    echo "Linting ${0}"
    ack "en-us" "${@}"
fi
