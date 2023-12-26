REPOSITORY_DIRECTORY=$1

cd $REPOSITORY_DIRECTORY

echo "pull latest version of the SynthwaveAtomChallengeCreator repository"
git reset --hard
git checkout master
git pull

echo ""

echo "pull latest docker image"
docker pull ghcr.io/laguna1989/synthwaveatomchallengecreator:latest

DOCKER_CONTAINER_ID=`docker ps | grep ghcr.io/laguna1989/synthwaveatomchallengecreator:latest | awk '{print $1}' | tail -1`
echo ""
echo "attempting to restart container with id $DOCKER_CONTAINER_ID"

docker restart $DOCKER_CONTAINER_ID