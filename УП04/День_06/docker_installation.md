# Установка и проверка Docker

Docker Engine установлен из официального APT-репозитория Docker для Ubuntu. Использовались команды:

```bash
sudo apt update
sudo apt install -y ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

**Результаты проверки:**
- Docker Engine: `29.1.0` (build `fdd4b8e`)
- Docker Compose: `v5.8.0`
- Служба `docker.service`: `active (running)`, включена (`enabled`)
- Установка завершилась; служба запущена

Команды проверки: `docker --version`, `docker compose version`, `sudo systemctl status docker --no-pager`
