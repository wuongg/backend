# Backend FastAPI Structure

## Cấu trúc thư mục

Trong thư mục dự án, backend FastAPI được tổ chức như sau:

- `app/` – thư mục chính của ứng dụng FastAPI
  - `app/api/` – chứa các router
  - `app/api/v1/` – router cho version 1
  - `app/core/` – cấu hình lõi, security, middleware
  - `app/db/` – kết nối database, session
  - `app/models/` – ORM models
  - `app/schemas/` – Pydantic schemas
  - `app/services/` – business logic
  - `app/utils/` – các hàm tiện ích dùng chung
  - `app/config/` – cấu hình, đọc biến môi trường (env)
  - `app/tests/` – test cho ứng dụng
