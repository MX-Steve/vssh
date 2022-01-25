# V_SSH
## 1. 搭建
```bash
docker pull mxsteve2021/vssh:v1.0
docker run -itd -p 8080:8080 -p 8000:8000 --restart always --name vir_ssh mxsteve2021/vssh:v1.0
docker exec vir_ssh bash -c "sh /data/vssh/deploy/init.sh"
```
## 2. 本地启动
```bash

```