# Dockerized Online Bookstore

## 1. Gioi thieu
Du an xay dung ung dung quan ly sach bang Flask, PostgreSQL,
Nginx va Docker Compose.

## 2. Cong nghe
- Docker va Docker Compose
- Python Flask
- PostgreSQL 16
- Nginx Alpine

## 3. Kien truc
- Web: xu ly cac chuc nang quan ly sach.
- Database: luu thong tin sach trong PostgreSQL.
- Nginx: tiep nhan HTTP va chuyen tiep den Web.
- Docker Network: ket noi cac container trong he thong.
- Named Volume: luu tru du lieu PostgreSQL.
- Bind Mount: chia se ma nguon Web va cau hinh Nginx.

## 4. Cau truc thu muc
- Dockerfile
- docker-compose.yml
- web/app.py
- web/requirements.txt
- db/init.sql
- nginx/default.conf
- README.md

## 5. Khoi dong du an
Mo terminal tai thu muc du an va chay:

    docker compose up -d --build

Kiem tra trang thai:

    docker compose ps

Truy cap website tren Ubuntu:

    http://localhost:8080

Kiem tra suc khoe ung dung:

    curl -s http://localhost:8080/health

Ket qua mong doi:

    {"status":"ok"}

## 6. Chuc nang
- Hien thi danh sach sach.
- Xem chi tiet sach.
- Them sach.
- Sua thong tin sach.
- Xoa sach.

## 7. Cac lenh quan ly Docker

Xem container:

    docker compose ps

Xem log:

    docker compose logs --tail=30

Xem log Web:

    docker logs --tail=20 bookstore-web

Dung cac dich vu:

    docker compose stop

Khoi dong cac dich vu:

    docker compose start

Khoi dong lai cac dich vu:

    docker compose restart

Truy cap shell trong container Web:

    docker exec -it bookstore-web sh

Thoat shell:

    exit

Xem chi tiet container:

    docker inspect bookstore-web

Xoa container DB da dung:

    docker compose rm -f db

Tao lai dich vu DB:

    docker compose up -d db

Luu y: Khong dung lenh xoa Named Volume khi can giu du lieu.

## 8. Docker Network
Compose tao mang mac dinh bookstore_default.

Kiem tra mang:

    docker network ls

Xem cac container ket noi vao mang:

    docker network inspect bookstore_default

## 9. Named Volume va Bind Mount
Kiem tra Named Volume:

    docker volume ls

Kiem tra mount cua Web:

    docker inspect bookstore-web

Named Volume luu du lieu PostgreSQL doc lap voi container.
Bind Mount dong bo ma nguon Web tu thu muc web vao /app
trong container va mount cau hinh Nginx.

## 10. Kiem tra tinh ben vung du lieu
1. Ghi nhan danh sach sach hien tai.
2. Xoa rieng container DB, khong xoa volume.
3. Tao lai container DB.
4. Kiem tra website va danh sach sach.
5. Xac nhan du lieu cu van con.

Lenh kiem tra:

    curl -s http://localhost:8080/

## 11. Cac tinh huong loi da kiem thu

### Tinh huong 1: Database bi dung
- Kiem tra trang thai va log DB.
- Khoi dong lai DB.
- Xac nhan DB healthy va website hoat dong.

### Tinh huong 2: Container Database bi xoa
- Xoa container DB.
- Tao lai DB tu Docker Compose.
- Kiem tra du lieu van con nhờ Named Volume.

### Tinh huong 3: Container Web bi dung
- Kiem tra trang thai va log Web.
- Khoi dong lai Web.
- Kiem tra endpoint /health.

## 12. Dung du an
Dung cac dich vu nhung giu Named Volume:

    docker compose down

Khong them tham so -v neu can giu du lieu database.
