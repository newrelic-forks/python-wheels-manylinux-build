import sys
import subprocess


def main():
    version = sys.argv[1]
    branch = "rel_" + version
    containers = [
        "manylinux2010_x86_64",
        "manylinux2010_x86_64:2021-02-06-3d322a5",
        "manylinux1_x86_64",
        "manylinux1_i686",
        "manylinux2010_i686",
        "manylinux2014_x86_64",
        "manylinux2014_i686",
        "manylinux2014_aarch64",
        "manylinux2014_ppc64le",
        "manylinux2014_s390x",
    ]
    files_to_edit = ["./Dockerfile"]

    # Setup Git
    subprocess.call(["git", "config", "--global", "user.email", '"opensource@newrelic.com"'])
    subprocess.call(["git", "config", "--global", "user.name", '"newrelic"'])

    # Checkout new branch
    subprocess.call(["git", "checkout", "-b", branch])

    # Replace, add, commit, tag
    for i, container in enumerate(containers):
        # Create scrubbed tag for git, which doesn't accept colons.
        tag = version + "-" + container.replace(":", "-")

        # Split container and tag to use separately.
        container_tuple = container.split(":")
        container = container_tuple[0]
        if len(container_tuple) > 1:
            container_version = container_tuple[1]
        else:
            container_version = "latest"

        if i > 0:
            for file_ in files_to_edit:
                # Edit manylinux platform
                subprocess.call(
                    [
                        "sed",
                        "-i",
                        "-e",
                        f"s/PLAT=.\+/PLAT={container}/g",
                        file_,
                    ]
                )
                # Edit manylinux container version tag
                subprocess.call(
                    [
                        "sed",
                        "-i",
                        "-e",
                        f"s/CONTAINER_VERSION=.\+/CONTAINER_VERSION={container_version}/g",
                        file_,
                    ]
                )
        subprocess.call(["git", "add"] + files_to_edit)
        subprocess.call(["git", "commit", "-m", f'Change container to {container}'])
        subprocess.call(["git", "tag", tag])

    # Push
    subprocess.call(["git", "push", "--set-upstream", "origin", branch])
    subprocess.call(["git", "push", "--tags"])


if __name__ == "__main__":
    main()
