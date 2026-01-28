# Tài liệu Yêu cầu Nghiệp vụ (BRD)
## Hệ thống Quản lý Tài sản - FAM Upgrade Wave 4

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Project Scope & Objectives](#2-project-scope-objectives)
3. [Stakeholders](#3-stakeholders)
4. [Ma trận trạng thái và Tasklist](#4-ma-trận-trạng-thái-và-tasklist)
5. [Business Requirements](#5-business-requirements)
   - [5.1. FAM UPGRADE WAVE 4](#51-fam-upgrade-wave-4)
   - [5.2. Dashboard Tài Sản](#52-dashboard-tài-sản)
   - [5.3. Module Quản lý Kho](#53-module-quản-lý-kho)
     - [5.3.1. Tạo yêu cầu nhập kho](#531-tạo-yêu-cầu-nhập-kho)
     - [5.3.2. Phê duyệt yêu cầu nhập kho](#532-phê-duyệt-yêu-cầu-nhập-kho)
     - [5.3.3. Xác nhận nhập kho](#533-xác-nhận-nhập-kho)
     - [5.3.4. Nhập kho thủ công - Tạo yêu cầu](#534-nhập-kho-thủ-công-tạo-yêu-cầu)
     - [5.3.5. Nhập kho thủ công - Phê duyệt](#535-nhập-kho-thủ-công-phê-duyệt)
     - [5.3.6. Nhập kho thủ công - Xác nhận](#536-nhập-kho-thủ-công-xác-nhận)
     - [5.3.7. Hủy yêu cầu nhập kho](#537-hủy-yêu-cầu-nhập-kho)
   - [5.4. Module Cấp tài sản](#54-module-cấp-tài-sản)
     - [5.4.1. Phê duyệt yêu cầu cấp tài sản](#541-phê-duyệt-yêu-cầu-cấp-tài-sản)
     - [5.4.2. Tạo yêu cầu xuất kho](#542-tạo-yêu-cầu-xuất-kho)
     - [5.4.3. Tiếp nhận yêu cầu xuất kho](#543-tiếp-nhận-yêu-cầu-xuất-kho)
     - [5.4.4. Phê duyệt yêu cầu xuất kho](#544-phê-duyệt-yêu-cầu-xuất-kho)
     - [5.4.5. Nhận tài sản](#545-nhận-tài-sản)
     - [5.4.6. Hủy yêu cầu xuất kho](#546-hủy-yêu-cầu-xuất-kho)
   - [5.5. Module Điều chuyển kho](#55-module-điều-chuyển-kho)
     - [5.5.1. Tạo yêu cầu điều chuyển kho](#551-tạo-yêu-cầu-điều-chuyển-kho)
     - [5.5.2. Phê duyệt yêu cầu điều chuyển kho](#552-phê-duyệt-yêu-cầu-điều-chuyển-kho)
6. [Assumptions & Constraints](#6-assumptions-constraints)
7. [Dependencies](#7-dependencies)
8. [Acceptance Criteria](#8-acceptance-criteria)
9. [Glossary](#9-glossary)

---

## 1. Executive Summary

Dự án FAM (Fixed Asset Management) Upgrade Wave 4 là giai đoạn nâng cấp quan trọng nhằm cải thiện toàn diện hệ thống quản lý tài sản của tổ chức. Với 11 yêu cầu chính được phân loại từ mức độ ưu tiên 1 đến 4, dự án tập trung vào hai nhóm chính: Enhancement (nâng cấp chức năng hiện có) và New Launch (các module hoàn toàn mới).

Các sản phẩm chính bao gồm [Dashboard Tài Sản](#52-dashboard-tài-sản) với khả năng visualization và customization, [Module Quản lý Kho](#53-module-quản-lý-kho) toàn diện cho xuất-nhập kho tài sản, và [Module Cấp tài sản](#54-module-cấp-tài-sản) được tối ưu hóa. Đặc biệt, dự án bao gồm [Module Điều chuyển kho](#55-module-điều-chuyển-kho) cho phép di chuyển tài sản giữa các kho một cách hiệu quả.

Hệ thống mới sẽ tích hợp chặt chẽ với các hệ thống hiện có như EMS, OMS, và ITSM, đồng thời cung cấp khả năng tự động hóa cao như auto xác nhận phiếu cấp tài sản sau 20 ngày và đồng bộ dữ liệu thời gian thực.

---

## 2. Project Scope & Objectives

### Trong phạm vi dự án
- Phát triển Dashboard tài sản với visualization và customization
- Xây dựng Module quản lý kho hoàn chỉnh (xuất-nhập-điều chuyển)
- Tạo Module sửa chữa tài sản tích hợp ITSM
- Nâng cấp quy trình cấp phát và thanh lý tài sản
- Tích hợp tự động với EMS, OMS, ITSM
- Implement luồng phê duyệt cho ATM trong thanh lý

### Ngoài phạm vi dự án
- Thay đổi kiến trúc cơ sở dữ liệu cốt lõi
- Tích hợp với các hệ thống ngoài EMS, OMS, ITSM
- Phát triển mobile application
- Thay đổi quy trình nghiệp vụ không được liệt kê

### Mục tiêu chính
- Tăng cường khả năng báo cáo và phân tích thông qua dashboard
- Tự động hóa quy trình quản lý kho và giảm thiểu thao tác thủ công
- Cải thiện trải nghiệm người dùng với giao diện thân thiện
- Đảm bảo tính nhất quán dữ liệu qua tích hợp hệ thống

---

## 3. Stakeholders

### Vai trò chính trong hệ thống
- **AMP (Asset Management Personnel)**: Nhân viên quản lý tài sản
- **AM (Asset Manager)**: Quản lý tài sản cấp cao
- **BU User**: Người dùng đơn vị kinh doanh
- **BU Head**: Trưởng đơn vị kinh doanh
- **WK (Warehouse Keeper)**: Thủ kho
- **Warehouse Manager**: Quản lý kho
- **Checker**: Người kiểm soát
- **Approver**: Người phê duyệt

### Hệ thống tích hợp
- **EMS (Enterprise Management System)**: Đồng bộ tiêu đề PO và thời gian bảo hành
- **OMS (Organization Management System)**: Đồng bộ orgchart và thông tin đơn vị
- **ITSM (IT Service Management)**: Tích hợp yêu cầu sửa chữa tài sản
- **Cổng hỗ trợ chi nhánh trên intranet**: Nhận yêu cầu sửa chữa

---

## 4. Ma trận trạng thái và Tasklist

### Ma trận trạng thái nghiệp vụ

Hệ thống quản lý tài sản được thiết kế với ma trận trạng thái phức tạp cho phép theo dõi chi tiết từng bước trong quy trình. Chi tiết về [trạng thái yêu cầu và tài sản](#541-phê-duyệt-yêu-cầu-cấp-tài-sản) sẽ được mô tả trong từng module cụ thể.

| Process | Sub-process | PIC | Action | Rq Status | Asset Status | Note |
|---------|-------------|-----|---------|-----------|--------------|------|
| **Cấp tài sản không ở kho** | | | | Cấp tài sản | - | |
| | 1 Tạo yêu cầu | AMP | Lưu | Đang tạo | | |
| | | | Gửi | Chờ xác nhận | | |
| | 2. Xác nhận | BU User | Từ chối | Từ chối | | |
| | | | Xác nhận | Đã xác nhận | Đang sử dụng | Đã xác nhận >>> Đã nhận tài sản |
| | | | Bổ sung thông tin | Bổ sung thông tin | | |
| | 3. Bổ sung TT | AMP | Bổ sung thông tin | Chờ xác nhận | | |

### Ma trận phân công nhiệm vụ

Quy trình điều chuyển kho sử dụng ma trận Tasklist để quản lý phân công nhiệm vụ. Chi tiết về [quy trình điều chuyển](#55-module-điều-chuyển-kho) được mô tả trong module tương ứng.

| Sub-process | Action | Role | Tasklist Điều chuyển - Cần xử lý | Tasklist Điều chuyển - Đã xử lý | Tasklist Kho - Cần xử lý | Tasklist Kho - Đã xử lý |
|-------------|--------|------|--------------------------------|-------------------------------|-------------------------|------------------------|
| Tạo yêu cầu điều chuyển | Gửi | Initiator | | x | | |
| Phê duyệt yêu cầu | Duyệt | AMP | x | | | |
| Xác nhận điều chuyển | Xác nhận | AMP | | x | x | |

---

## 5. Business Requirements

### 5.1. FAM UPGRADE WAVE 4

Danh sách chi tiết các yêu cầu nâng cấp cho hệ thống FAM trong Wave 4, bao gồm cả Enhancement và New Launch với phân loại mức độ ưu tiên từ 1-4.

| STT | Phân loại | Module | Mô tả chi tiết | Priority | Ghi chú |
|-----|-----------|---------|----------------|----------|---------|
| 1 | Enhancement | Tài sản | Dashboard tài sản hiển thị theo hướng visualize; có thể customize theo nhiều tiêu chí | 1 | Login vào là nhìn thấy luôn. Cần liệt kê rõ ràng role |
| 2 | Enhancement | Tài sản | Ẩn hiện tùy chọn tài sản vô hiệu hóa khỏi danh sách tài sản | 2 | |
| 3 | Enhancement | Tài sản | Đổi vị trí hiển thị một số cột trong danh sách tài sản | 2 | |
| 4 | Enhancement | Cấp tài sản | Upload phiếu cấp tài sản theo danh sách | 3 | |
| 5 | Enhancement | Cấp tài sản | Auto xác nhận phiếu cấp tài sản sau 20 ngày kể từ khi request bàn giao tài sản được tạo, user không có phản hồi, Hệ thống tự động xác nhận | 2 | |
| 6 | Enhancement | Integration | Auto đồng bộ OMS khi orgchart thay đổi | 2 | |
| 7 | Enhancement | Integration | Đồng bộ tiêu đề PO từ EMS sang FAM | 2 | |
| 8 | Enhancement | Integration | Tài sản từ EMS, cột "Thông tin thời gian đưa vào sử dụng, Thời gian bắt đầu bảo hành" = thời gian PO được phê duyệt | 2 | |
| 9 | Enhancement | Thanh lý | Bổ sung luồng phê duyệt cho ATM | 3 | Thêm thông tin as is và to be |
| 10 | New launch | Modul kho | Xuất - nhập kho tài sản. Tiếp nhận yêu cầu xuất - nhập kho từ yêu cầu cấp ts, thanh lý tài sản, điều chuyển ts về kho | 1 | |
| 11 | New launch | Modul sửa chữa | Tạo yêu cầu sửa chữa tài sản thực hiện trên FAM => Hệ thống tạo yêu cầu (gửi link) sang Hệ thống ITSM và Cổng hỗ trợ chi nhánh trên intranet. Hoàn tất, yêu cầu được feed back qua FAM | 4 | Cần Clear qui trình |

### 5.2. Dashboard Tài Sản

Dashboard tài sản cung cấp giao diện tổng quan trực quan hóa dữ liệu tài sản với khả năng customization và các biểu đồ tương tác đa dạng. Dashboard hiển thị thông tin theo nhiều chiều: phòng ban theo orgchart, trạng thái tài sản, biến động theo thời gian, tỷ lệ sử dụng và thông tin bảo hành.

**Các KPI chính:**

| STT | Nội dung | Công thức tính | Loại dữ liệu | Ghi chú |
|-----|----------|----------------|--------------|---------|
| 1 | Total assets | Count số lượng (All tài sản - Đã thanh lý - Vô hiệu hóa) | Số lượng | |
| 2 | Total value | Sum nguyên giá (All tài sản - Đã thanh lý - Vô hiệu hóa) | Giá trị | |
| 3 | Warranty status | Tỷ lệ % theo số lượng tài sản còn hạn bảo hành/(All tài sản - Vô hiệu hóa - Đã thanh lý) | Phần trăm | |
| 4 | Utilization rate | Tỷ lệ % theo số lượng tài sản đang sử dụng/(All tài sản - Vô hiệu hóa - Đã thanh lý) | Phần trăm | |

**Cấu hình bộ lọc:**

| STT | Tên bộ lọc | Nguồn dữ liệu | Loại | Ghi chú |
|-----|------------|---------------|------|---------|
| 1 | Vùng | LOV | Danh sách | |
| 2 | Đơn vị sử dụng | LOV đồng bộ từ OMS | Danh sách | Tích hợp với hệ thống OMS |
| 3 | CAT 1 | LOV | Danh sách | |
| 4 | Group name | LOV | Danh sách | |
| 5 | Asset status | LOV | Danh sách | Không bao gồm "Đã thanh lý", "Vô hiệu hóa" |

**Đặc tả biểu đồ:**

| STT | Tên biểu đồ | Dữ liệu hiển thị | Loại biểu đồ | Tính năng đặc biệt |
|-----|-------------|------------------|--------------|-------------------|
| 1 | Asset Distribution - Status | Nguyên giá | Sunburst (Vòng trong: IT/ADM/CMD, Vòng ngoài: Trạng thái) | Hover hiển thị số lượng và giá trị |
| 2 | Asset Distribution - Location | Nguyên giá | Stacked Column | |
| 3 | Asset Value by Group Name | Nguyên giá | Column | |
| 4 | Asset Fluctuation Over Time | Nguyên giá | Line | Theo tháng/năm |
| 5 | Asset by Time in Use | Số lượng | Scatter | |

### 5.3. Module Quản lý Kho

Module quản lý kho bao gồm 7 quy trình chính từ [điều chuyển về kho](#531-tạo-yêu-cầu-nhập-kho) đến [điều chuyển giữa các kho](#55-module-điều-chuyển-kho). Hệ thống tự động tạo yêu cầu liên quan và có luồng phê duyệt rõ ràng với tính tích hợp cao.

Các quy trình chính:
- [Tạo yêu cầu nhập kho](#531-tạo-yêu-cầu-nhập-kho) (tự động từ điều chuyển về kho)
- [Phê duyệt yêu cầu nhập kho](#532-phê-duyệt-yêu-cầu-nhập-kho) 
- [Xác nhận nhập kho](#533-xác-nhận-nhập-kho)
- [Nhập kho thủ công](#534-nhập-kho-thủ-công-tạo-yêu-cầu)
- [Hủy yêu cầu nhập kho](#537-hủy-yêu-cầu-nhập-kho)

#### 5.3.1. Tạo yêu cầu nhập kho

![Giao diện tạo yêu cầu nhập kho](images/5.1.1a_B5)

**Chức năng tự động tạo yêu cầu nhập kho khi có yêu cầu điều chuyển về kho được xác nhận.**

Quy trình này xử lý việc tạo yêu cầu nhập kho tự động với đầy đủ thông tin được kế thừa từ yêu cầu điều chuyển ban đầu. Hệ thống sẽ tự động cập nhật trạng thái và gửi thông báo cho Warehouse Manager.

**Đặc tả trường thông tin chung:**

| Tab/Section | Operator | Action | Field Name VN | M/O | Field Type | Editable | Max Length | Format | Default Value | Data Rule |
|-------------|----------|---------|---------------|-----|------------|----------|------------|---------|---------------|-----------|
| Hệ thống | System | Display | Số yêu cầu | M | Text | N | 50 | NK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| Hệ thống | System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| Hệ thống | System | Display | Tiêu đề | M | Text | N | 150 | | | =Tiêu đề RQ điều chuyển |

**Đặc tả thông tin tài sản:**

| Field Name VN | M/O | Editable | Data Rule |
|---------------|-----|----------|-----------|
| Mã tài sản | M | N | Hiển thị mặc định |
| Tên Tài sản | M | N | Hiển thị mặc định |
| Mô tả TS | M | N | Hiển thị mặc định |
| Trạng thái TS | M | N | Hiển thị mặc định |
| Phân nhóm TS (group name) | M | N | Hiển thị mặc định |
| Nhóm TS (CAT1) | M | N | Hiển thị mặc định |
| Số PO | M | N | Hiển thị mặc định |
| Tên nhà cung cấp | O | N | Ẩn hiện tùy biến |
| Nguyên giá TS (VAT incl) | M | N | Ẩn hiện tùy biến |

**Quy trình xử lý:** Sau khi tạo yêu cầu, hệ thống tự động cập nhật trạng thái yêu cầu điều chuyển thành "Đã xác nhận", yêu cầu nhập kho thành "Chờ phê duyệt", và gửi thông báo email cho Warehouse Manager. Xem chi tiết quy trình phê duyệt tại [5.3.2](#532-phê-duyệt-yêu-cầu-nhập-kho).

#### 5.3.2. Phê duyệt yêu cầu nhập kho

![Giao diện phê duyệt yêu cầu nhập kho](images/5.1.2a_B5)

**Warehouse Manager xem xét và phê duyệt các yêu cầu nhập kho từ quy trình điều chuyển về kho.**

Giao diện cho phép tìm kiếm yêu cầu theo nhiều tiêu chí và hiển thị đầy đủ thông tin tài sản, kho nhập, đầu mối giao hàng. WM có thể từ chối (cần nhập lý do) hoặc phê duyệt yêu cầu.

**Bảng tìm kiếm yêu cầu:**

| Trường | Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|---------|----------|---------|---------------|-----|------------|----------|------------|
| User | Input | Số yêu cầu | O | Text | Y | 20 |
| User | Input | Ngày tạo | O | Date | Y | 20 |
| User | Input | Tiêu đề | O | Text | Y | 150 |
| User | Select | Người tạo | O | List | Y | 20 |
| User | Select | Trạng thái yêu cầu | O | List | Y | 20 |
| User | Select | Người xử lý | O | List | Y | 20 |
| User | Input | Ngày xác nhận | O | Date | Y | 20 |

**Luồng xử lý:** Khi phê duyệt, yêu cầu chuyển sang trạng thái "Chờ nhập kho" và tạo task cho WK. Khi từ chối, hệ thống unlock tài sản và thông báo cho các bên liên quan. Sau phê duyệt, quy trình chuyển sang [xác nhận nhập kho](#533-xác-nhận-nhập-kho).

#### 5.3.3. Xác nhận nhập kho

![Giao diện xác nhận nhập kho](images/5_1_3a_B5_images2.png)

**Nhân viên kho (WK) thực hiện xác nhận nhập kho thực tế sau khi WM phê duyệt.**

Giao diện hiển thị thông tin chi tiết yêu cầu và cho phép WK từ chối hoặc xác nhận việc nhập kho. Khi xác nhận, hệ thống tự động cập nhật thông tin tài sản và kho.

**Bảng thông tin tài sản chi tiết:**

| Trường | Field name VN | M/O | Editable | Data rule |
|--------|---------------|-----|----------|-----------|
| System Display | Mã tài sản | M | N | Hiển thị mặc định |
| System Display | Tên Tài sản | M | N | Hiển thị mặc định |
| System Display | Mô tả TS | M | N | Hiển thị mặc định |
| System Display | Trạng thái TS | M | N | Hiển thị mặc định |
| System Display | Tên người sử dụng | M | N | Hiển thị mặc định |
| System Display | Tên đơn vị | M | N | Hiển thị mặc định |

**Quy trình:** Sau xác nhận, hệ thống unlock tài sản, cập nhật thông tin kho và "Ngày bắt đầu sử dụng" nếu = N/A, đồng thời gửi thông báo cho các bên liên quan.

#### 5.3.4. Nhập kho thủ công - Tạo yêu cầu

![Giao diện nhập kho thủ công](images/image4.png)

**Cho phép người dùng tạo yêu cầu nhập kho thủ công không thông qua quy trình điều chuyển tự động.**

Giao diện cung cấp chức năng tìm kiếm và chọn tài sản, cập nhật thông tin kho nhập và đầu mối giao hàng. Sau khi tạo, hệ thống lock tài sản và gửi cho WM phê duyệt.

**Bảng thông tin tìm kiếm tài sản:**

| Tab/Section | Operator | Action | Field Name VN | M/O | Field Type | Editable | Max Length | Format | Default Value | Data Rule |
|-------------|----------|---------|---------------|-----|------------|----------|------------|--------|---------------|-----------|
| Tìm kiếm tài sản | User | Input | Mã tài sản | O | Text | N | 20 | | | |
| Tìm kiếm tài sản | User | Input | Tên tài sản | O | Text | Y | 20 | | | |
| Tìm kiếm tài sản | User | Select | Phân loại tài sản | O | List | N | 20 | | | |
| Tìm kiếm tài sản | User | Select | Nhóm tài sản | O | List | N | 20 | | | |
| Tìm kiếm tài sản | User | Input | PO number | O | Text | Y | 20 | | | |

**Quy trình:** Sau khi gửi yêu cầu, chuyển đến [phê duyệt nhập kho thủ công](#535-nhập-kho-thủ-công-phê-duyệt).

#### 5.3.5. Nhập kho thủ công - Phê duyệt

![Giao diện phê duyệt nhập kho thủ công](images/5_4_2a__B5_image10.png)

**Warehouse Manager phê duyệt các yêu cầu nhập kho thủ công do người dùng tạo.**

Quy trình tương tự [phê duyệt yêu cầu nhập kho tự động](#532-phê-duyệt-yêu-cầu-nhập-kho) nhưng dành cho yêu cầu thủ công. WM có thể xem chi tiết tài sản, thông tin kho và đưa ra quyết định phê duyệt.

**Bảng thông tin tài sản nhập kho:**

| Operator | Action | Field name VN | M/O | Data rule |
|----------|--------|---------------|-----|-----------|
| System | Display | Mã tài sản | M | Hiển thị mặc định |
| System | Display | Tên Tài sản | M | Hiển thị mặc định |
| System | Display | Mô tả TS | M | Hiển thị mặc định |
| System | Display | Trạng thái TS | M | Hiển thị mặc định |
| System | Display | Tên nhà cung cấp | O | Ẩn hiện tùy biến |

**Luồng xử lý:** Sau phê duyệt, chuyển đến [xác nhận nhập kho thủ công](#536-nhập-kho-thủ-công-xác-nhận).

#### 5.3.6. Nhập kho thủ công - Xác nhận

![Giao diện xác nhận nhập kho thủ công](images/image6.png)

**WK thực hiện xác nhận nhập kho thực tế cho các yêu cầu nhập kho thủ công đã được WM phê duyệt.**

Giao diện hiển thị thông tin chi tiết yêu cầu với đầy đủ thông tin tài sản, kho nhập, đầu mối giao hàng. WK có thể từ chối (nhập lý do) hoặc xác nhận nhập kho.

**Quy trình xử lý:** Tương tự [xác nhận nhập kho tự động](#533-xác-nhận-nhập-kho), hệ thống cập nhật thông tin tài sản, unlock asset và gửi thông báo cho các bên liên quan.

#### 5.3.7. Hủy yêu cầu nhập kho

![Giao diện hủy yêu cầu nhập kho](images/5_3_1a_B5_image7.png)

**Cho phép hủy các yêu cầu nhập kho đã được tạo nhưng chưa hoàn thành (trạng thái khác "Đã nhập kho").**

Chức năng này áp dụng cho cả yêu cầu nhập kho tự động và thủ công. Khi hủy, hệ thống unlock tài sản và cập nhật trạng thái thành "Đã hủy".

**Bảng thông tin tìm kiếm yêu cầu:**

| STT | Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|-----|----------|--------|---------------|-----|------------|----------|------------|
| 1 | User | Input | Số yêu cầu | O | Text | Y | 20 |
| 2 | User | Input | Ngày tạo | O | Date | Y | 20 |
| 3 | User | Input | Tiêu đề | O | Text | Y | 150 |
| 4 | User | Select | Người tạo | O | List | Y | 20 |
| 5 | User | Select | Trạng thái yêu cầu | O | List | Y | 20 |

**Yêu cầu:** Bắt buộc nhập lý do hủy (tối đa 150 ký tự). Hệ thống tự động unlock tài sản, cập nhật tasklist và gửi thông báo email cho các bên liên quan.

### 5.4. Module Cấp tài sản

Module cấp tài sản được nâng cấp với quy trình tự động tạo yêu cầu xuất kho và luồng phê duyệt đa cấp. Bao gồm các chức năng chính:
- [Phê duyệt yêu cầu cấp tài sản](#541-phê-duyệt-yêu-cầu-cấp-tài-sản)
- [Tạo yêu cầu xuất kho](#542-tạo-yêu-cầu-xuất-kho) (tự động)
- [Xử lý xuất kho](#543-tiếp-nhận-yêu-cầu-xuất-kho)
- [Nhận tài sản](#545-nhận-tài-sản)

#### 5.4.1. Phê duyệt yêu cầu cấp tài sản

![Giao diện phê duyệt cấp tài sản](images/5_4_0a_A4_image8.png)

**Asset Manager xem xét và phê duyệt các yêu cầu cấp tài sản từ người dùng.**

Giao diện hiển thị đầy đủ thông tin tài sản, người nhận, đầu mối phụ trách và cho phép AM đưa ra quyết định phê duyệt hoặc từ chối với lý do cụ thể.

**Bảng thông tin tìm kiếm yêu cầu:**

| Trường | Người thao tác | Thao tác | Kiểu | Bắt buộc | Chỉnh sửa | Độ dài |
|--------|----------------|----------|------|----------|-----------|---------|
| Mã yêu cầu | User | Input | Text | M | Y | 20 |
| Tiêu đề | User | Input | Text | M | Y | 150 |
| Người tạo | User | Select | List | M | Y | 20 |
| Trạng thái | User | Select | List | M | Y | 20 |
| Ngày tạo | User | Input | Date | M | Y | 20 |
| Loại cấp tài sản | User | Select | List | M | Y | 100 |
| Người xử lý | User | Select | List | M | Y | 20 |
| Ngày xác nhận | User | Input | Date | M | Y | 20 |

**Bảng thông tin tài sản cấp:**

| Trường | Người thao tác | Thao tác | Bắt buộc | Chỉnh sửa | Hiển thị |
|--------|----------------|----------|----------|-----------|----------|
| Mã tài sản | System | Display | M | N | Hiển thị mặc định |
| Tên Tài sản | System | Display | M | N | Hiển thị mặc định |
| Mô tả TS | System | Display | M | N | Hiển thị mặc định |
| Trạng thái TS | System | Display | M | N | Hiển thị mặc định |
| Phân nhóm TS (group name) | System | Display | M | N | Hiển thị mặc định |
| Nhóm TS (CAT1) | System | Display | M | N | Hiển thị mặc định |
| Số PO | System | Display | M | N | Hiển thị mặc định |
| Tên nhà cung cấp | System | Display | O | N | Ẩn hiện tùy biến |
| Nguyên giá TS (VAT incl) | System | Display | M | N | Ẩn hiện tùy biến |

**Luồng xử lý:** Khi phê duyệt, hệ thống tự động chuyển đến [tạo yêu cầu xuất kho](#542-tạo-yêu-cầu-xuất-kho). Khi từ chối, unlock tài sản và thông báo cho AMP.

#### 5.4.2. Tạo yêu cầu xuất kho

![Giao diện tạo yêu cầu xuất kho](images/5_4_1a__B5_image9.png)

**Hệ thống tự động tạo yêu cầu xuất kho từ thông tin phiếu cấp/thanh lý tài sản đã được phê duyệt.**

Quy trình tự động kế thừa 100% thông tin từ phiếu gốc và tạo yêu cầu xuất kho với đầy đủ thông tin tài sản, kho xuất, và đầu mối nhận hàng.

**Thông tin chung và cấu hình trường:**

| STT | Tab/Section | Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Format | Default value | Data rule |
|-----|-------------|----------|--------|---------------|-----|------------|----------|------------|--------|---------------|-----------|
| 1 | Thông tin chung | System | Display | Số yêu cầu | M | Text | N | 50 | XK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| 2 | Thông tin chung | System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| 3 | Thông tin chung | System | Input | Tiêu đề | O | Text | Y | 150 | | | =Tiêu đề RQ Cấp/Thanh lý |

**Thông tin kho xuất:**

| STT | Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Data source | Data rule |
|-----|----------|--------|---------------|-----|------------|----------|------------|-------------|-----------|
| 1 | System/User | Display/Search/Select | Tên kho | M | List | N | 50 | | = Thông tin kho trên RQ cấp/Thanh lý |
| 2 | System | Display | Địa chỉ kho | M | Text | Y | 50 | OMS | |
| 3 | System | Display | Quản lý kho | M | Text | N | 50 | OMS | |

**Quy trình:** Sau khi tạo, chuyển đến [tiếp nhận yêu cầu xuất kho](#543-tiếp-nhận-yêu-cầu-xuất-kho).

#### 5.4.3. Tiếp nhận yêu cầu xuất kho

![Giao diện tiếp nhận xuất kho](images/5_4_2a__B5_image10.png)

**WK tiếp nhận và xử lý yêu cầu xuất kho từ cấp tài sản.**

Giao diện cho phép tìm kiếm yêu cầu, xem thông tin chi tiết tài sản và đưa ra quyết định đồng ý hoặc từ chối. Đặc biệt, nút "Từ chối" bị ẩn nếu yêu cầu xuất phát từ thanh lý.

**Bảng thông tin tìm kiếm yêu cầu:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Default value |
|----------|---------|---------------|-----|------------|----------|------------|---------------|
| User | Input | Mã yêu cầu | M | Text | Y | 20 | |
| User | Input | Tiêu đề | M | Text | Y | 150 | |
| User | Select | Người tạo | M | List | Y | 20 | |
| User | Select | Trạng thái | M | List | Y | 20 | |
| User | Input | Ngày tạo | M | Date | Y | 20 | |
| User | Select | Nghiệp vụ kho | M | List | Y | 100 | |
| User | Select | Người xử lý | M | List | Y | 20 | |
| User | Input | Ngày xác nhận | M | Date | Y | 20 | |

**Luồng xử lý:** Khi đồng ý, chuyển đến [phê duyệt yêu cầu xuất kho](#544-phê-duyệt-yêu-cầu-xuất-kho). Khi từ chối, unlock tài sản và thông báo cho AMP.

#### 5.4.4. Phê duyệt yêu cầu xuất kho

![Giao diện phê duyệt xuất kho](images/5.4.3a_B5_image11.png)

**Warehouse Manager phê duyệt các yêu cầu xuất kho đã được WK đồng ý.**

Giao diện hiển thị thông tin yêu cầu, danh sách tài sản xuất kho, thông tin kho và đầu mối nhận hàng. WM có thể phê duyệt hoặc từ chối (ẩn nút từ chối với yêu cầu từ thanh lý).

**Bảng tìm kiếm yêu cầu:**

| STT | Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|-----|----------|--------|---------------|-----|------------|----------|------------|
| 1 | User | Input | Mã yêu cầu | M | Text | Y | 20 |
| 2 | User | Input | Tiêu đề | M | Text | Y | 150 |
| 3 | User | Select | Người tạo | M | List | Y | 20 |
| 4 | User | Select | Trạng thái | M | List | Y | 20 |
| 5 | User | Input | Ngày tạo | M | Date | Y | 20 |
| 6 | User | Select | Loại cấp tài sản | M | List | Y | 100 |
| 7 | User | Select | Người xử lý | M | List | Y | 20 |
| 8 | User | Input | Ngày xác nhận | M | Date | Y | 20 |

**Quy trình:** Sau phê duyệt, chuyển đến [nhận tài sản](#545-nhận-tài-sản).

#### 5.4.5. Nhận tài sản

![Giao diện nhận tài sản](images/5_4_4a_B6_image12.png)

**BU user xác nhận nhận tài sản từ kho sau khi toàn bộ quy trình xuất kho hoàn thành.**

Đây là bước cuối trong quy trình xuất kho, cho phép người nhận xác nhận đã nhận được tài sản thực tế hoặc từ chối nếu có vấn đề.

**Bảng thông tin chung yêu cầu:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Format | Default value | Data rule |
|----------|--------|---------------|-----|------------|----------|------------|--------|---------------|-----------|
| System | Display | Số yêu cầu | M | Text | N | 50 | XK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| System | Input | Tiêu đề | O | Text | Y | 150 | | | |

**Bảng thông tin tài sản xuất kho:**

| Operator | Action | Field name VN | M/O | Editable | Data rule |
|----------|--------|---------------|-----|----------|-----------|
| System | Display | Mã tài sản | M | N | Hiển thị mặc định |
| System | Display | Tên Tài sản | M | N | Hiển thị mặc định |
| System | Display | Mô tả TS | M | N | Hiển thị mặc định |
| System | Display | Trạng thái TS | M | N | Hiển thị mặc định |
| System | Display | Tên người sử dụng | M | N | Hiển thị mặc định |
| System | Display | Tên đơn vị | M | N | Hiển thị mặc định |

**Quy trình:** Khi xác nhận, hệ thống unlock tài sản, cập nhật trạng thái thành "Đã nhận tài sản" và gửi thông báo hoàn thành cho các bên liên quan.

#### 5.4.6. Hủy yêu cầu xuất kho

![Giao diện hủy yêu cầu xuất kho](images/5.5.1a_B6)

**AMP có thể hủy yêu cầu xuất kho chưa được xác nhận để rollback quy trình.**

Chức năng này cho phép hủy yêu cầu xuất kho có trạng thái khác "Đã xác nhận", unlock tài sản và cập nhật trạng thái các yêu cầu liên quan.

**Bảng tìm kiếm yêu cầu xuất kho:**

| STT | Field name VN | Operator | Field type | Editable | Max length | M/O | Mô tả |
|-----|---------------|----------|------------|----------|------------|-----|-------|
| 1 | Mã yêu cầu | User Input | Text | Y | 20 | M | Trường tìm kiếm |
| 2 | Tiêu đề | User Input | Text | Y | 150 | M | Trường tìm kiếm |
| 3 | Người tạo | User Select | List | Y | 20 | M | Danh sách người tạo |
| 4 | Trạng thái | User Select | List | Y | 20 | M | Danh sách trạng thái |
| 5 | Ngày tạo | User Input | Date | Y | 20 | M | Trường ngày tạo |

**Yêu cầu:** Bắt buộc nhập lý do hủy (tối đa 150 ký tự). Hệ thống cập nhật trạng thái thành "Đã hủy", unlock tài sản và gửi thông báo cho WK.

### 5.5. Module Điều chuyển kho

Module điều chuyển kho cho phép di chuyển tài sản giữa các kho trong hệ thống với quy trình phê duyệt đầy đủ. Bao gồm:
- [Tạo yêu cầu điều chuyển](#551-tạo-yêu-cầu-điều-chuyển-kho)
- [Phê duyệt yêu cầu điều chuyển](#552-phê-duyệt-yêu-cầu-điều-chuyển-kho)

#### 5.5.1. Tạo yêu cầu điều chuyển kho

![Giao diện tạo yêu cầu điều chuyển kho](images/5_6_1a_B6_image14.png)

**Cho phép người dùng tạo yêu cầu điều chuyển tài sản giữa các kho với thông tin đầy đủ về kho đi, kho đến và đầu mối giao nhận.**

Giao diện hỗ trợ tìm kiếm và lựa chọn tài sản theo nhiều tiêu chí, hiển thị thông tin chi tiết tài sản và cho phép cấu hình thông tin điều chuyển.

**Bảng thông tin chung và tìm kiếm tài sản:**

| Tab/Section | Operator | Action | Field Name VN | M/O | Field Type | Editable | Max Length | Format | Default Value | Data Rule |
|-------------|----------|---------|---------------|-----|------------|----------|------------|--------|---------------|-----------|
| Thông tin chung | System | Display | Số yêu cầu | M | Text | N | 50 | CK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| | System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| | User | Input | Tiêu đề | O | Text | Y | 150 | | | |
| | User | Select | Thêm tài sản | M | Button | N | | | | |
| Tìm kiếm tài sản | User | Input | Mã tài sản | O | Text | N | 20 | | | |
| | User | Input | Tên tài sản | O | Text | Y | 20 | | | |
| | User | Select | Phân loại tài sản | O | List | N | 20 | | | |
| | User | Select | Nhóm tài sản | O | List | N | 20 | | | |
| | User | Input | PO number | O | Text | Y | 20 | | | |

**Bảng thông tin kho và giao hàng:**

| Tab/Section | Operator | Action | Field Name VN | M/O | Field Type | Editable | Max Length | Data Source | Data Rule |
|-------------|----------|---------|---------------|-----|------------|----------|------------|-------------|-----------|
| Thông tin kho đi | System/User | Display/Search/Select | Tên kho | M | List | N | 50 | | |
| | System | Display | Địa chỉ kho | M | Text | Y | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| | System | Display | Quản lý kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho (Tên \| Phòng ban \| Email) |
| Thông tin kho nhập | User | Select | Tên kho | M | List | N | 50 | | |
| | System | Display | Địa chỉ kho | M | Text | Y | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| | System | Display | Quản lý kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho (Tên \| Phòng ban \| Email) |

**Quy trình:** Sau khi tạo yêu cầu, hệ thống lock tài sản, tìm và gán người phê duyệt phù hợp, gửi thông báo cho AM và Warehouse Manager, sau đó chuyển đến [phê duyệt yêu cầu điều chuyển](#552-phê-duyệt-yêu-cầu-điều-chuyển-kho).

#### 5.5.2. Phê duyệt yêu cầu điều chuyển kho

![Giao diện phê duyệt điều chuyển kho](images/5.6.2a_B5_image15.png)

**Approver xem xét và phê duyệt các yêu cầu điều chuyển tài sản giữa các kho.**

Giao diện hiển thị đầy đủ thông tin yêu cầu, danh sách tài sản cần điều chuyển, thông tin kho đi/đến, đầu mối giao nhận và cho phép Approver đưa ra quyết định.

**Bảng tìm kiếm yêu cầu điều chuyển kho:**

| Trường | Operator | Action | Loại | Bắt buộc | Editable | Max Length |
|--------|----------|--------|------|-----------|----------|------------|
| Số yêu cầu | User | Input | Text | O | Y | 20 |
| Ngày tạo | User | Input | Date | O | Y | 20 |
| Tiêu đề | User | Input | Text | O | Y | 150 |
| Người tạo | User | Select | List | O | Y | 20 |
| Trạng thái yêu cầu | User | Select | List | O | Y | 20 |
| Người xử lý | User | Select | List | O | Y | 20 |
| Ngày xác nhận | User | Input | Date | O | Y | 20 |

**Bảng thông tin yêu cầu điều chuyển:**

| Trường | Operator | Action | Loại | Bắt buộc | Editable | Max Length | Format/Default | Ghi chú |
|--------|----------|--------|------|-----------|----------|------------|----------------|---------|
| Số yêu cầu | System | Display | Text | M | N | 50 | CK.YY.xxxx | YY = Year, xxxx = số chạy từ 1-9999 |
| Ngày tạo | System | Display | Date | M | N | 50 | MM.DD.YYYY | Today |
| Tiêu đề | User | Input | Text | O | Y | 150 | | |
| Tên kho đi | System | Display | List | M | N | 50 | | Từ OMS |
| Tên kho nhập | User | Select | List | M | N | 50 | | |
| Đầu mối | User | Input | Text | M | N | 50 | | |
| Số điện thoại | User | Input | Number | M | N | 52 | | |
| Thời gian bàn giao | User | Input | Date | O | N | 50 | | |
| Ghi chú | User | Input | Text | M | N | 150 | | |

**Luồng xử lý:** Khi phê duyệt, hệ thống tự động tạo biên bản điều chuyển, cập nhật thông tin kho của tài sản và thông báo cho WK thực hiện bàn giao. Khi từ chối, unlock tài sản và thông báo cho AMP.

---

## 6. Assumptions & Constraints

### Giả định
- Các hệ thống EMS, OMS, ITSM hoạt động ổn định và cung cấp API/interface cần thiết
- Người dùng đã được đào tạo về quy trình nghiệp vụ quản lý tài sản
- Hạ tầng mạng và server đảm bảo hiệu năng cho các tính năng real-time
- Dữ liệu master về kho, nhân sự, tài sản đã được chuẩn hóa

### Ràng buộc
- Tuân thủ các quy định pháp lý về quản lý tài sản của tổ chức
- Đảm bảo tính bảo mật thông tin tài sản và quản lý quyền truy cập
- Hệ thống phải backward compatible với dữ liệu FAM hiện tại
- Thời gian downtime tối đa 4 giờ cho việc deployment

---

## 7. Dependencies

### Hệ thống ngoại vi
- **EMS**: Cung cấp dữ liệu PO, thời gian phê duyệt, thông tin nhà cung cấp
- **OMS**: Đồng bộ orgchart, thông tin nhân sự, thông tin kho
- **ITSM**: Tích hợp yêu cầu sửa chữa, cập nhật trạng thái sửa chữa
- **Cổng hỗ trợ chi nhánh**: Nhận và xử lý yêu cầu sửa chữa

### Yêu cầu kỹ thuật
- Database server hỗ trợ transaction và concurrent access
- Web server hỗ trợ real-time notification
- Email server cho gửi thông báo tự động
- File storage cho quản lý hồ sơ đính kèm

### Tài nguyên con người
- Business Analyst để định nghĩa chi tiết requirements
- Solution Architect để thiết kế hệ thống
- Development team có kinh nghiệm về workflow engine
- QA team để test các scenario nghiệp vụ phức tạp

---

## 8. Acceptance Criteria

### Dashboard Tài Sản
- Hiển thị đúng 4 KPI chính với thời gian load < 3 giây
- Bộ lọc hoạt động chính xác với tối đa 5 tiêu chí đồng thời
- Biểu đồ interactive với hover và click functionality
- Export Excel thành công với dữ liệu đầy đủ

### Module Quản lý Kho
- Tự động tạo yêu cầu nhập/xuất kho từ quy trình điều chuyển/cấp phát
- Email notification gửi đúng người và đúng thời điểm
- Lock/unlock tài sản hoạt động chính xác
- Tasklist cập nhật real-time theo trạng thái xử lý

### Tích hợp Hệ thống
- Đồng bộ dữ liệu OMS thành công trong vòng 1 giờ
- Đồng bộ thông tin EMS không có data loss
- ITSM integration với response time < 5 giây
- Auto xác nhận sau 20 ngày hoạt động đúng schedule

### Performance
- Hệ thống xử lý đồng thời 100 concurrent users
- Database query response time < 2 giây
- File upload tối đa 10MB, thời gian upload < 30 giây
- System availability 99.5% trong business hours

---

## 9. Glossary

| Thuật ngữ | Định nghĩa |
|-----------|------------|
| **AMP** | Asset Management Personnel - Nhân viên quản lý tài sản |
| **AM** | Asset Manager - Quản lý tài sản cấp cao |
| **BU** | Business Unit - Đơn vị kinh doanh |
| **WK** | Warehouse Keeper - Thủ kho |
| **WM** | Warehouse Manager - Quản lý kho |
| **EMS** | Enterprise Management System - Hệ thống quản lý doanh nghiệp |
| **OMS** | Organization Management System - Hệ thống quản lý tổ chức |
| **ITSM** | IT Service Management - Quản lý dịch vụ CNTT |
| **FAM** | Fixed Asset Management - Quản lý tài sản cố định |
| **Dashboard** | Bảng điều khiển hiển thị thông tin tổng quan |
| **Tasklist** | Danh sách công việc cần xử lý |
| **Lock/Unlock** | Khóa/mở khóa tài sản trong quy trình |
| **Auto Confirmation** | Tự động xác nhận sau thời gian qui định |
| **Workflow** | Luồng công việc có các bước xử lý tuần tự |

---

*Tài liệu này được tạo dựa trên 37 sheet đầu vào và bao gồm đầy đủ các yêu cầu nghiệp vụ cho dự án FAM Upgrade Wave 4.*

---

*Generated by Claude Sonnet 4.5 from 37 sheet summaries*
*Headings: 47 | Internal Links: 59*

*✅ All internal links validated successfully*
