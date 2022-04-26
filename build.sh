COMMIT_HASH=`git rev-parse --short HEAD`

docker build -t folder-view:$COMMIT_HASH .
docker tag folder-view:$COMMIT_HASH folder-view:latest
