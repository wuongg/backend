"""
ĐÂY LÀ FILE CHÍNH CỦA BACKEND FASTAPI (KHUNG TRẮNG + GỢI Ý)
------------------------------------------------------------

Mục tiêu: giúp bạn TỰ TAY code backend cho 1 trang web.

Gợi ý lộ trình tự code trong file này:
1. Tạo instance FastAPI
2. Tạo vài endpoint đơn giản (GET, POST)
3. Tách router ra file riêng trong `app/api`
4. Kết nối DB, viết model, schema, CRUD

Lưu ý: mình chỉ để GỢI Ý, không viết sẵn code hoàn chỉnh để bạn khỏi bị “copy y chang”.
"""

from fastapi import FastAPI


# 1. KHỞI TẠO ỨNG DỤNG FASTAPI
# -----------------------------
# TODO (bạn tự làm):
# - Tạo biến app = FastAPI(...)
#   + tự đặt title
#   + tự đặt description
# Gợi ý cú pháp:
#   app = FastAPI(title="...", description="...")
app = FastAPI()


# 2. TẠO ENDPOINT ĐẦU TIÊN
# ------------------------
# TODO (bạn tự viết hoàn toàn):
# - Tạo 1 endpoint GET /health trả về JSON:
#   {"status": "ok"}
#
# Gợi ý:
#   @app.get("/health")
#   async def health_check():
#       ...


# 3. BÀI TẬP THÊM CHO BẠN
# -----------------------
# Sau khi có /health, hãy thử:
# - Tạo 1 endpoint GET /hello trả về {"message": "Hello, FastAPI"}
# - Tạo 1 endpoint GET /items/{item_id} nhận path param
# - Tạo 1 endpoint POST /echo nhận body JSON và trả lại y chang
#
# Khi đã quen, chuyển sang dùng router trong `app/api/v1/example.py`.


