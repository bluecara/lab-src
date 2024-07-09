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

### 개행 문자를 제거 - vi
```
# 변경 방법 1
:%s/^M//
# 변경 방법 2
:%s/\015//
# 변경 방법 3 - 파일 포멧 변경 > 저장 > 다시 파일 열기 > 변경됨(ff: File Format)
:set ff=unix
:wq
```
