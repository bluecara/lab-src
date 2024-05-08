# Docker

### for local development environment

* CentOS `6.10` `7` `8`
* Apache `2.2` `2.4`
* PHP `5.3` `5.6` `7.1` `7.4` `8.2` `8.3`
* Nginx `1.20.1`
* node.js `20.11.1`
* Rocky `9.2`
* NPM `10.5.0`
<br><br>

```
docker-compose up -d
```

```
docker run -it -d
    -p 8080:80
    -e VIRTUAL_HOST=http://my.project.co.kr
    -e HTTPS_METHOD=noredirect
    -e TZ=Asia/Seoul
    -v {project_root}:/var/www/approot
    --name container-name {container_name}
```