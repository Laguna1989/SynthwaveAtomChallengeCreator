REPOSITORY_DIRECTORY=$1

echo "\n\n-------------------------"
date

cd $REPOSITORY_DIRECTORY

echo "pull latest version of the SynthwaveAtomChallengeCreator repository"
git reset --hard
git checkout master
git pull

echo ""

echo "pull latest docker image"
docker pull ghcr.io/laguna1989/synthwaveatomchallengecreator:latest

DOCKER_CONTAINER_ID=`docker ps | grep ghcr.io_laguna1989_synthwaveatomchallengecreator_latest | awk '{print $1}' | tail -1`
echo ""
echo "attempting to restart container"
echo "stop container with id $DOCKER_CONTAINER_ID"
docker stop $DOCKER_CONTAINER_ID

echo ""
echo "start new docker container"
docker run --restart=always --env-file .env -d --name "ghcr.io_laguna1989_synthwaveatomchallengecreator_latest" ghcr.io/laguna1989/synthwaveatomchallengecreator:latest
