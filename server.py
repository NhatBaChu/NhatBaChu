import http.server
import socketserver

# Thiết lập cổng (port) mà server sẽ chạy.
PORT = 8080

# Sử dụng SimpleHTTPRequestHandler để phục vụ các tệp từ thư mục hiện tại
Handler = http.server.SimpleHTTPRequestHandler

# Khởi tạo và chạy máy chủ TCP
try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("---------------------------------------------------------")
        print(f"Server đã khởi động thành công.")
        print(f"Truy cập trang web của bạn tại: http://localhost:{PORT}")
        print("Nhấn Ctrl+C để dừng server.")
        print("---------------------------------------------------------")
        
        # Giữ server chạy vĩnh viễn
        httpd.serve_forever()

except KeyboardInterrupt:
    print("\nServer đã dừng.")
except Exception as e:
    print(f"\nLỗi khi khởi động server: {e}")