FROM alpine:3.10

LABEL "com.github.actions.name"="forbiddenstrings"
LABEL "com.github.actions.description"="Checks markdown files for magic strings that are probably mistakes"
LABEL "com.github.actions.icon"="settings"
LABEL "com.github.actions.color"="yellow"

LABEL "repository"="http://github.com/lobrien/AzureDocsActions"
LABEL "homepage"="http://github.com/lobrien/AzureDocsActions"
LABEL "maintainer"="Larry O'Brien <lobrien@knowing.net>"

RUN apk --no-cache add \
  bash~=4 \
  git~=2 \
  binutils~=2.30 \

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]