import time
import os


def get_latest_remote_tag():
    latest_remote_tag_command = "git -c 'versionsort.suffix=-' " \
                                "ls-remote --exit-code --refs --sort='version:refname' " \
                                "--tags https://github.com/Laguna1989/SynthwaveAtomChallengeCreator " \
                                "'*.*.*' | tail --lines=1 | cut --delimiter='/' --fields=3"
    latest_tag = os.popen(latest_remote_tag_command).read()
    print("latest remote tag '" + latest_tag + "'")
    return latest_tag


def get_latest_local_tag():
    latest_local_tag_command = "git describe --tags --abbrev=0"
    latest_tag = os.popen(latest_local_tag_command).read()
    print("latest local tag '" + latest_tag + "'")
    return latest_tag


def _pull_latest_docker_image():
    pull_command = "docker pull ghcr.io/laguna1989/synthwaveatomchallengecreator:latest"
    os.system(pull_command)


def _restart_docker():
    get_container_id_command = "docker ps | awk '{print $1}' | tail -1"
    container_id = os.popen(get_container_id_command).read()
    print("container id '" + container_id + "'")

    restart_docker_command = "docker restart " + container_id
    os.system(restart_docker_command)


def restart_docker_with_latest_image():
    _pull_latest_docker_image()
    _restart_docker()


while True:
    time.sleep(60)

    latest_remote_tag = get_latest_remote_tag()
    latest_local_tag = get_latest_local_tag()

    if not latest_local_tag == latest_remote_tag:
        restart_docker_with_latest_image()
