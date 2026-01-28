# Phân tích Sheet: Status

## 1. Loại sheet
**Quy trình** - Mô tả các quy trình nghiệp vụ và luồng trạng thái của hệ thống quản lý tài sản.

## 2. Mức độ chi tiết
**Chi tiết cao** - Sheet chứa thông tin kỹ thuật về trạng thái, action, và vai trò cụ thể trong từng bước quy trình → CẦN GIỮ NGUYÊN DẠNG BẢNG.

## 3. Chủ đề/tiêu đề chính
Định nghĩa trạng thái và luồng xử lý cho các quy trình quản lý tài sản bao gồm: Cấp tài sản, Thanh lý tài sản, và Điều chuyển tài sản.

## 4. Tóm tắt thông tin chính

Sheet Status định nghĩa chi tiết các luồng nghiệp vụ trong hệ thống quản lý tài sản với 3 quy trình chính. Quy trình cấp tài sản bao gồm hai luồng con: cấp tài sản không ở kho (workflow đơn giản với 3 bước) và cấp tài sản từ kho (workflow phức tạp với 6 bước và nhiều cấp phê duyệt).

Quy trình thanh lý tài sản được chia thành hai phương thức: bán trực tiếp và bán đấu giá. Cả hai đều có luồng kiểm soát - phê duyệt - cập nhật kết quả - xuất kho, nhưng bán đấu giá có thêm bước kiểm soát và phê duyệt kết quả thanh lý riêng biệt. Quy trình điều chuyển tài sản hỗ trợ hai hình thức: điều chuyển về kho và điều chuyển giữa các kho, mỗi loại có workflow và vai trò phê duyệt khác nhau.

Mỗi quy trình được thiết kế với các checkpoint kiểm soát, cho phép từ chối, yêu cầu bổ sung thông tin, và có cơ chế rollback khi cần thiết. Hệ thống trạng thái được thiết kế để theo dõi cả trạng thái yêu cầu (Request Status) và trạng thái tài sản (Asset Status) một cách độc lập.

## 5. Các bên liên quan/vai trò được đề cập
- **AMP** (Asset Management Personnel)
- **BU User** (Business Unit User) 
- **AM** (Asset Manager)
- **WK** (Warehouse Keeper)
- **Warehouse Mgr.** (Warehouse Manager)
- **Checker** (Kiểm soát viên)
- **Approver** (Người phê duyệt)
- **BU Head** (Trưởng đơn vị kinh doanh)
- **System** (Hệ thống tự động)

## 6. Các yêu cầu tìm thấy
- Hệ thống phải hỗ trợ workflow approval nhiều cấp cho các quy trình khác nhau
- Cần có cơ chế từ chối, yêu cầu bổ sung thông tin và rollback
- Trạng thái yêu cầu và trạng thái tài sản phải được quản lý độc lập
- Hệ thống phải tự động tạo yêu cầu xuất/nhập kho sau khi được phê duyệt
- Cần phân quyền rõ ràng cho từng vai trò trong từng bước quy trình

## 7. Các sheet liên quan
Không có tham chiếu rõ ràng đến sheet khác trong nội dung hiện tại.

## 8. Bảng cần giữ nguyên

### Bảng trạng thái quy trình Cấp tài sản

| Process | Sub-process | PIC | Action | Rq Status | Asset status | Note |
|---------|-------------|-----|--------|-----------|-------------|------|
| Cấp tài sản | - | | - | Cấp tài sản | - | |
| Cấp tài sản không ở kho | 1 Tạo yêu cầu | AMP | Lưu | Đang tạo | | |
| | | | Gửi | Chờ xác nhận | | |
| | 2. Xác nhận | BU User | Từ chối | Từ chối | | |
| | | | Xác nhận | Đã xác nhận | Đang sử dụng | Đã xác nhận >>> Đã nhận tài sản |
| | | | Bổ sung thông tin | Bổ sung thông tin | | |
| | 3. Bổ sung TT | AMP | Bổ sung thông tin | Chờ xác nhận | | |
| Cấp tài sản từ kho | 1. Tạo yêu cầu | AMP | Lưu | Đang tạo | | |
| | | | Gửi | Chờ xác nhận | | |
| | 2. Phê duyệt | AM | Từ chối | Từ chối | | |
| | | | Duyệt | Đã xác nhận | | |
| | 3. Tạo yêu cầu | System | | Đã xác nhận | Chờ xuất kho | |
| | 4. Xuất kho | WK | Từ chối | Từ chối | Từ chối | |
| | | | Đồng ý | Đã xác nhận | Chờ phê duyệt | |
| | 5. Phê duyệt | Warehouse Mgr. | Từ chối | Từ chối | Từ chối | |
| | | | Duyệt | Đã xác nhận | Chờ xác nhận | |
| | 6. Nhận hàng | BU User | Từ chối | Từ chối | Từ chối | |
| | | | Xác nhận | Đã xác nhận | Đã nhận tài sản | Đang sử dụng |

### Bảng trạng thái quy trình Thanh lý tài sản

| Process | Sub-process | PIC | Action | Rq Status | Asset status | Note |
|---------|-------------|-----|--------|-----------|-------------|------|
| Thanh lý tài sản | - | | - | Thanh lý | Xuất kho | |
| Bán trực tiếp | 1. Tạo yêu cầu | AMP | Lưu | Đang tạo | | |
| | | | Gửi | Chờ kiểm soát | | |
| | 2. Kiểm soát | Checker | Từ chối | Từ chối | | |
| | | | Yêu cầu bổ sung thông tin | Bổ sung thông tin | | |
| | | | Đồng ý | Chờ phê duyệt | | |
| | 3. Phê duyệt | Approver | Từ chối | Đang tạo | | |
| | | | Yêu cầu bổ sung thông tin | Bổ sung thông tin | | |
| | | | Phê duyệt | Chờ cập nhật kết quả | | |
| | 4. Cập nhật kết quả thanh lý | AMP | Hủy | Đã hủy | | |
| | | | Cập nhật kết quả | Đã cập nhật kết quả thanh lý | | Đã thanh lý |

### Bảng trạng thái quy trình Điều chuyển tài sản

| Process | Sub-process | PIC | Action | Rq Status | Asset status | Note |
|---------|-------------|-----|--------|-----------|-------------|------|
| Điều chuyển tài sản | - | | - | Điều chuyển | Nhập kho | |
| Điều chuyển về kho | 1. Tạo yêu cầu | BU user | Lưu | Đang tạo | | |
| | | | Gửi | Chờ phê duyệt | | |
| | 2. Phê duyệt yêu cầu | BU Head | Từ chối | Từ chối | | |
| | | | Yêu cầu bổ sung thông tin | Bổ sung thông tin | | |
| | | | Phê duyệt | Chờ xác nhận | | |
| | 3. Xác nhận điều chuyển | AMP | Từ chối | Từ chối | | |
| | | | Đồng ý | Đã xác nhận | | |
| | 4. Tạo yêu cầu nhập kho | System | Send | Đã xác nhận | Chờ phê duyệt | |
| | 5. Phê duyệt nhập kho | Warehouse Mgr. | Từ chối | Từ chối | Từ chối | |
| | | | Phê duyệt | Đã xác nhận | Chờ nhập kho | |
| | 6. Nhập kho tài sản | WK | Từ chối | Từ chối | Từ chối | |
| | | | Xác nhận | Đã xác nhận | Đã xác nhận | Đã nhập kho |

## 9. Hình ảnh trong sheet
Không có hình ảnh.

---
*Source: Status.csv | Rows: 87 | Images: 0 | Images analyzed: 0 | Generated by Claude Sonnet 4.5*
