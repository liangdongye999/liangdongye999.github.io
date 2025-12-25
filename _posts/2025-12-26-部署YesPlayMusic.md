用命令行：

```bash
docker run -d \
  --name yesplaymusic  \
  --restart always    \
  -p 7950:80   \
  fogforest/yesplaymusic
```

或Compose：

```yaml
versions: "3.8"

services:
  yesplaymusic:
    image: fogforest/yesplaymusic
    ports:
      - 7950:80
    restart: always
```
