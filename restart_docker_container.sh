REPOSITORY_DIRECTORY=$1

echo "\n\n-------------------------"
date

cd $REPOSITORY_DIRECTORY

echo "pull latest version of the SynthwaveAtomChallengeCreator repository"
git reset --hard
git checkout master
git pull

echo ""

OLD_IMAGE_ID=`docker image list | grep ghcr.io/laguna1989/synthwaveatomchallengecreator | grep latest | awk '{print $3}'`

echo "pull latest docker image"
docker pull ghcr.io/laguna1989/synthwaveatomchallengecreator:latest

echo ""

UPDATED_IMAGE_ID=`docker image list | grep ghcr.io/laguna1989/synthwaveatomchallengecreator | grep latest | awk '{print $3}'`


echo "old container image id: $OLD_IMAGE_ID"
echo "new container image id: $UPDATED_IMAGE_ID"

if [ "$OLD_IMAGE_ID" != "$UPDATED_IMAGE_ID" ]; then
  echo "image ids differ, restart docker"

  DOCKER_CONTAINER_ID=`docker ps | grep ghcr.io_laguna1989_synthwaveatomchallengecreator_latest | awk '{print $1}' | tail -1`
  echo ""
  echo "attempting to restart container"
  echo "stop container with id $DOCKER_CONTAINER_ID"
  docker stop $DOCKER_CONTAINER_ID

  echo ""
  echo "remove docker container"
  docker container remove $DOCKER_CONTAINER_ID

  echo ""
  echo "start new docker container"
  docker run --restart=always --env-file ~/.env -d --name "ghcr.io_laguna1989_synthwaveatomchallengecreator_latest" ghcr.io/laguna1989/synthwaveatomchallengecreator:latest
else
  echo "no new image, keep docker running"
fi
