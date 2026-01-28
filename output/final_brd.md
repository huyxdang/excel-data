# Tài liệu Yêu cầu Nghiệp vụ (BRD)
## FAM UPGRADE - WAVE 4

---

## Mục lục

1. [Executive Summary](#1-executive-summary)
2. [Project Scope & Objectives](#2-project-scope-objectives)
3. [Stakeholders](#3-stakeholders)
4. [Assumptions & Constraints](#4-assumptions-constraints)
5. [Business Requirements](#5-business-requirements)
   - [5.1. Dashboard Tài sản](#51-dashboard-tài-sản)
   - [5.2. Module Quản lý Kho](#52-module-quản-lý-kho)
   - [5.3. Điều chuyển về kho - Tạo yêu cầu nhập kho](#53-điều-chuyển-về-kho-tạo-yêu-cầu-nhập-kho)
   - [5.4. Điều chuyển về kho - Phê duyệt yêu cầu nhập kho](#54-điều-chuyển-về-kho-phê-duyệt-yêu-cầu-nhập-kho)
   - [5.5. Nhập kho từ quy trình điều chuyển về kho](#55-nhập-kho-từ-quy-trình-điều-chuyển-về-kho)
   - [5.6. NHẬP KHO THỦ CÔNG](#56-nhập-kho-thủ-công)
   - [5.7. Hủy yêu cầu nhập kho](#57-hủy-yêu-cầu-nhập-kho)
   - [5.8. Cấp Tài Sản](#58-cấp-tài-sản)
   - [5.9. Create Warehouse Intake Request](#59-create-warehouse-intake-request)
   - [5.10. Xuất kho từ cấp tài sản - Tiếp nhận yêu cầu](#510-xuất-kho-từ-cấp-tài-sản-tiếp-nhận-yêu-cầu)
   - [5.11. Xuất kho từ cấp tài sản - Phê duyệt yêu cầu](#511-xuất-kho-từ-cấp-tài-sản-phê-duyệt-yêu-cầu)
   - [5.12. Xuất kho từ cấp tài sản - Nhận tài sản](#512-xuất-kho-từ-cấp-tài-sản-nhận-tài-sản)
   - [5.13. Hủy yêu cầu xuất kho](#513-hủy-yêu-cầu-xuất-kho)
   - [5.14. Điều chuyển tài sản giữa các kho - Tạo yêu cầu điều chuyển kho](#514-điều-chuyển-tài-sản-giữa-các-kho-tạo-yêu-cầu-điều-chuyển-kho)
   - [5.15. Điều chuyển tài sản giữa các kho - Phê duyệt yêu cầu](#515-điều-chuyển-tài-sản-giữa-các-kho-phê-duyệt-yêu-cầu)
   - [5.16. Status](#516-status)
   - [5.17. Tasklist](#517-tasklist)
6. [Dependencies](#6-dependencies)
7. [Acceptance Criteria](#7-acceptance-criteria)
8. [Glossary](#8-glossary)

---

## 1. Executive Summary

Dự án FAM UPGRADE - WAVE 4 là giai đoạn nâng cấp quan trọng nhằm mở rộng và cải tiến hệ thống quản lý tài sản (Fixed Asset Management) của tổ chức. Dự án tập trung vào việc phát triển các tính năng mới và cải thiện các module hiện có để nâng cao hiệu quả quản lý tài sản.

### Các sản phẩm chính

Dự án bao gồm 11 yêu cầu chính được phân chia thành hai nhóm: Enhancement và New launch. Nhóm Enhancement tập trung vào việc cải tiến [5.1. Dashboard Tài sản](#51-dashboard-tài-sản) với khả năng visualization và customization, tối ưu hóa quy trình cấp phát và thanh lý tài sản, và tích hợp với các hệ thống khác như OMS và EMS.

Nhóm New launch bao gồm hai module mới quan trọng: [5.2. Module Quản lý Kho](#52-module-quản-lý-kho) cho phép quản lý xuất-nhập kho tài sản và Module sửa chữa tài sản tích hợp với ITSM. Đặc biệt, hệ thống sẽ có khả năng tự động hóa nhiều quy trình như xác nhận phiếu cấp tài sản và đồng bộ dữ liệu với các hệ thống liên kết.

---

## 2. Project Scope & Objectives

### Trong phạm vi dự án
- Phát triển dashboard tài sản với khả năng visualization và customization theo nhiều tiêu chí
- Cải thiện tính năng quản lý danh sách tài sản với khả năng ẩn/hiện và điều chỉnh layout
- Triển khai quy trình upload phiếu cấp tài sản theo batch và tự động xác nhận
- Tích hợp đồng bộ tự động với OMS và EMS
- Phát triển module quản lý kho toàn diện cho xuất-nhập kho tài sản
- Xây dựng module sửa chữa tài sản tích hợp với ITSM
- Bổ sung luồng phê duyệt thanh lý cho ATM

### Ngoài phạm vi dự án
- Thay đổi cấu trúc dữ liệu core của hệ thống FAM hiện tại
- Tích hợp với các hệ thống bên ngoài khác ngoài OMS, EMS và ITSM
- Phát triển mobile application

### Mục tiêu dự án
- Nâng cao hiệu quả quản lý tài sản thông qua tự động hóa quy trình
- Cải thiện khả năng báo cáo và phân tích dữ liệu tài sản
- Tăng cường kiểm soát và theo dõi tài sản trong kho
- Đơn giản hóa quy trình cấp phát và thanh lý tài sản

---

## 3. Stakeholders

### Vai trò quản lý
- **Asset Manager (AM)**: Quản lý tài sản, thực hiện phê duyệt yêu cầu
- **Asset Management Personnel (AMP)**: Nhân viên quản lý tài sản, xử lý yêu cầu hàng ngày
- **Warehouse Manager (WM)**: Quản lý kho, phê duyệt yêu cầu nhập/xuất kho
- **Warehouse Keeper (WK)**: Thủ kho, thực hiện các tác vụ xuất/nhập kho
- **Business Unit Head (BUH)**: Trưởng đơn vị kinh doanh

### Vai trò người dùng
- **User/BU User**: Người dùng cuối của hệ thống
- **Checker**: Người kiểm soát trong quy trình phê duyệt
- **Approver**: Người phê duyệt các yêu cầu
- **Initiator**: Người khởi tạo yêu cầu

### Hệ thống liên kết
- **OMS (Organization Management System)**: Hệ thống quản lý tổ chức
- **EMS**: Hệ thống quản lý doanh nghiệp
- **ITSM (IT Service Management)**: Hệ thống quản lý dịch vụ IT
- **Cổng hỗ trợ chi nhánh trên intranet**

---

## 4. Assumptions & Constraints

### Giả định
- Các hệ thống OMS, EMS và ITSM đã sẵn sàng để tích hợp
- Người dùng có kỹ năng cơ bản về công nghệ thông tin
- Dữ liệu hiện tại trong hệ thống FAM đã được làm sạch và chuẩn hóa
- Khung thời gian triển khai không bị ảnh hưởng bởi các yếu tố bên ngoài

### Ràng buộc
- Phải đảm bảo tương thích ngược với hệ thống FAM hiện tại
- Tuân thủ các quy định về bảo mật dữ liệu của tổ chức
- Sử dụng infrastructure và công nghệ hiện có
- Ngân sách và thời gian triển khai theo kế hoạch được phê duyệt

---

## 5. Business Requirements

### 5.1. Dashboard Tài sản

Dashboard Tài sản được thiết kế để cung cấp giao diện tổng quan và trực quan hóa dữ liệu tài sản nhằm hỗ trợ đưa ra quyết định nhanh chóng. Hệ thống cho phép người dùng theo dõi dữ liệu tài sản theo orgchart và trạng thái, giám sát biến động tài sản theo thời gian và cảnh báo về tài sản hết bảo hành hoặc có thời gian sử dụng quá 3-5 năm.

**Các thành phần chính:**
- Dashboard tổng quan với 4 chỉ số KPI quan trọng
- Bộ lọc dữ liệu theo 5 tiêu chí chính
- 4 loại biểu đồ tương tác khác nhau
- Tích hợp với hệ thống OMS và khả năng xuất dữ liệu Excel

#### 5.1.1. Thông số kỹ thuật dashboard

**Dashboard Tổng Quan - KPI:**

| Content | Value | Type of chart | Note |
|---------|--------|---------------|------|
| 1. Total assets | Count số lượng (All tài sản - Đã thanh lý - Vô hiệu hóa) | | |
| 2. Total value | Sum nguyên giá (All tài sản - Đã thanh lý - Vô hiệu hóa) | | |
| 3. Warranty status | Tỷ lệ phần trăm theo số lượng tài sản còn hạn bảo hành/(All tài sản - Vô hiệu hóa - Đã thanh lý) | | |
| 4. Utilization rate | Tỷ lệ phần trăm theo số lượng tài sản có trạng thái đang sử dụng/(All tài sản - Vô hiệu hóa - Đã thanh lý) | | |

**Bộ Lọc Dùng Chung:**

| Content | Value | Type of chart | Note |
|---------|--------|---------------|------|
| 1. Vùng | LOV | | |
| 2. Đơn vị sử dụng | LOV đồng bộ từ OMS | | |
| 3. CAT 1 | LOV | | |
| 4. Group name | LOV | | |
| 5. Asset status | LOV asset status (Không bao gồm Đã thanh lý, Vô hiệu hóa) | | |

**Biểu Đồ (Chart):**

| Content | Value | Type of chart | Note |
|---------|--------|---------------|------|
| 1. Asset Distribution - Cơ cấu nhóm tài sản theo trạng thái tài sản | Nguyên giá | Sunburst - Vòng trong: Nhóm IT/ADM/CMD - Vòng ngoài: Trạng thái | Khi Hover chuột thể hiện số lượng, và giá trị |
| - Cơ cấu nhóm tài sản theo Vùng, theo Đơn vị sử dụng | Nguyên giá | Stacked Column | |
| 2. Asset Value by Group Name | Nguyên giá | Column | |
| 3. Asset Fluctuation Over Time (Month/Year) | Nguyên giá | Line | |
| 4. Asset by Time in Use | Số lượng | Scatter | |

### 5.2. Module Quản lý Kho

Module Quản lý Kho là một hệ thống toàn diện để quản lý việc xuất nhập kho tài sản, bao gồm 8 quy trình chính từ điều chuyển nội bộ đến điều chuyển kho. Module này được thiết kế theo mô hình so sánh As-is và To-be với mức độ tự động hóa cao.

**Điểm nổi bật của thiết kế:**
- Khả năng tự động hóa cao - hệ thống tự động tạo các yêu cầu liên quan
- Xử lý ngoại lệ tốt với khả năng từ chối và quay lại bước trước
- Hỗ trợ hủy bỏ yêu cầu khi cần thiết
- Tự động cập nhật kết quả cho các yêu cầu liên quan

**Quy trình chính:**
1. [5.3. Điều chuyển về kho - Tạo yêu cầu nhập kho](#53-điều-chuyển-về-kho-tạo-yêu-cầu-nhập-kho)
2. [5.4. Điều chuyển về kho - Phê duyệt yêu cầu nhập kho](#54-điều-chuyển-về-kho-phê-duyệt-yêu-cầu-nhập-kho)
3. [5.5. Nhập kho từ quy trình điều chuyển về kho](#55-nhập-kho-từ-quy-trình-điều-chuyển-về-kho)
4. [5.6. NHẬP KHO THỦ CÔNG](#56-nhập-kho-thủ-công)
5. [5.7. Hủy yêu cầu nhập kho](#57-hủy-yêu-cầu-nhập-kho)
6. [5.8. Cấp Tài Sản](#58-cấp-tài-sản) và quy trình xuất kho liên quan
7. [5.13. Hủy yêu cầu xuất kho](#513-hủy-yêu-cầu-xuất-kho)
8. [5.14. Điều chuyển tài sản giữa các kho](#514-điều-chuyển-tài-sản-giữa-các-kho-tạo-yêu-cầu-điều-chuyển-kho)

### 5.3. Điều chuyển về kho - Tạo yêu cầu nhập kho

#### 5.3.1. Thông số kỹ thuật giao diện người dùng

![Giao diện tạo yêu cầu nhập kho](images/5_1_1a_B5_image1.png)

Quy trình này xử lý việc tạo yêu cầu nhập kho tự động khi có yêu cầu điều chuyển tài sản về kho. Hệ thống sẽ kế thừa toàn bộ thông tin từ yêu cầu điều chuyển gốc bao gồm thông tin tài sản, chi tiết kho đích và các tệp đính kèm.

**Cấu trúc màn hình:**
- Phần header hiển thị số yêu cầu và trạng thái
- Phần thông tin chung cho phép nhập tiêu đề và ghi chú
- Phần chi tiết tài sản hiển thị danh sách tài sản được chuyển
- Phần tệp đính kèm cho phép upload thêm tài liệu

**Các bên liên quan:** Hệ thống (tự động tạo), Quản lý kho (phê duyệt), AMP (theo dõi)

#### 5.3.2. Thông số kỹ thuật chi tiết

Hệ thống tự động tạo yêu cầu nhập kho với đầy đủ thông tin từ yêu cầu điều chuyển gốc. Sau khi tạo yêu cầu, hệ thống tự động cập nhật trạng thái các yêu cầu liên quan, cập nhật tasklist cho Asset Manager và Warehouse Manager, đồng thời gửi thông báo email cho Warehouse Manager để xử lý tiếp.

**Thông tin chung yêu cầu nhập kho:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Format | Default value | Data rule |
|----------|--------|---------------|-----|------------|----------|------------|---------|---------------|-----------|
| System | Display | Số yêu cầu | M | Text | N | 50 | NK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| System | Display | Tiêu đề | M | Text | N | 150 | | | =Tiêu đề RQ điều chuyển |

**Thông tin tài sản nhập kho:**

| Operator | Action | Field name VN | M/O | Editable | Data rule |
|----------|--------|---------------|-----|----------|-----------|
| System | Display | Mã tài sản | M | N | Hiển thị mặc định |
| System | Display | Tên Tài sản | M | N | Hiển thị mặc định |
| System | Display | Mô tả TS | M | N | Hiển thị mặc định |
| System | Display | Trạng thái TS | M | N | Hiển thị mặc định |
| System | Display | Phân nhóm TS (group name) | M | N | Hiển thị mặc định |
| System | Display | Nhóm TS (CAT1) | M | N | Hiển thị mặc định |
| System | Display | Số PO | M | N | Hiển thị mặc định |
| System | Display | Tên nhà cung cấp | O | N | Ẩn hiện tùy biến |
| System | Display | Nguyên giá TS (VAT incl) | M | N | Ẩn hiện tùy biến |

**Thông tin kho và giao hàng:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Data source | Data rule |
|----------|--------|---------------|-----|------------|----------|------------|-------------|-----------|
| System | Display | Tên kho | M | List | N | 50 | | = Kho trong RQ điều chuyển |
| System | Display | Địa chỉ kho | M | Text | N | 50 | OMS | Tự động nhận diện |
| System | Display | Quản lý kho | M | Text | N | 50 | OMS | Tên \| Phòng ban \| Email |

### 5.4. Điều chuyển về kho - Phê duyệt yêu cầu nhập kho

#### 5.4.1. Thông số kỹ thuật giao diện người dùng

![Giao diện phê duyệt yêu cầu nhập kho](images/5_1_2a_B6_image2.png)

Warehouse Manager có thể tìm kiếm, xem chi tiết và quyết định phê duyệt hoặc từ chối các yêu cầu nhập kho từ các đơn vị khác. Giao diện được thiết kế với nhiều section khác nhau hiển thị thông tin tài sản chi tiết, thông tin kho, đầu mối giao hàng và hồ sơ đính kèm.

#### 5.4.2. Thông số kỹ thuật chi tiết

Quy trình phê duyệt bao gồm các bước: tìm kiếm yêu cầu, hiển thị kết quả danh sách, xem chi tiết yêu cầu và đưa ra quyết định. Warehouse Manager có thể từ chối (kèm lý do) hoặc phê duyệt yêu cầu, hệ thống sẽ tự động cập nhật trạng thái và gửi thông báo cho các bên liên quan.

**Bảng tìm kiếm yêu cầu:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|--------|---------------|-----|------------|----------|------------|
| User | Input | Số yêu cầu | O | Text | Y | 20 |
| User | Input | Ngày tạo | O | Date | Y | 20 |
| User | Input | Tiêu đề | O | Text | Y | 150 |
| User | Select | Người tạo | O | List | Y | 20 |
| User | Select | Trạng thái yêu cầu | O | List | Y | 20 |
| User | Select | Người xử lý | O | List | Y | 20 |
| User | Input | Ngày xác nhận | O | Date | Y | 20 |

**Yêu cầu kỹ thuật:**
- Bắt buộc nhập lý do khi từ chối yêu cầu
- Tự động unlock tài sản khi từ chối yêu cầu
- Cập nhật trạng thái yêu cầu và tasklist tự động
- Gửi email notification cho các bên liên quan

### 5.5. Nhập kho từ quy trình điều chuyển về kho

#### 5.5.1. Thông số kỹ thuật giao diện người dùng

![Giao diện xác nhận nhập kho](images/5_1_3a_B5_image3.png)

Warehouse Keeper thực hiện quy trình xác nhận nhập kho thực tế. Giao diện bao gồm tìm kiếm yêu cầu theo nhiều tiêu chí, hiển thị kết quả danh sách, và màn hình chi tiết để xem thông tin đầy đủ của yêu cầu.

#### 5.5.2. Thông số kỹ thuật chi tiết

Quy trình gồm các bước: tìm kiếm yêu cầu → xem chi tiết → quyết định từ chối hoặc xác nhận → cập nhật trạng thái và thông báo. Khi từ chối, hệ thống sẽ unlock tài sản và cập nhật trạng thái là "Từ chối". Khi xác nhận, hệ thống sẽ cập nhật thông tin tài sản, chuyển tài sản về kho đích và cập nhật trạng thái là "Đã nhập kho".

**Yêu cầu đặc biệt:**
- Hệ thống tự động cập nhật "Ngày bắt đầu sử dụng" khi xác nhận nếu trường này = N/A
- Hệ thống phải unlock tài sản khi từ chối để asset có thể được sử dụng cho request khác
- Cập nhật ngược trạng thái request điều chuyển khi từ chối nhập kho

### 5.6. NHẬP KHO THỦ CÔNG

#### 5.6.1. Tạo yêu cầu

![Giao diện nhập kho thủ công](images/5_2_1a_B5_image4.png)

Chức năng nhập kho thủ công cho phép người dùng tạo các yêu cầu nhập kho một cách thủ công thay vì tự động. Quy trình bao gồm 5 bước chính: tạo yêu cầu, lock tài sản, cập nhật trạng thái yêu cầu, cập nhật tasklist và thông báo cho WM.

**Đặc tả chi tiết:**

**Thông tin chung:**

| Tab/section | Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Format | Default value | Data rule |
|-------------|----------|--------|---------------|-----|------------|----------|------------|--------|---------------|-----------|
| Thông tin chung | System | Display | Số yêu cầu | M | Text | N | 50 | NK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| | System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| | User | Input | Tiêu đề | O | Text | Y | 150 | | | |
| | User | Select | Thêm tài sản | M | Button | N | | | | |

**Tìm kiếm tài sản:**

| Field name VN | M/O | Field type | Editable | Max length | Operator | Action |
|---------------|-----|------------|----------|------------|----------|--------|
| Mã tài sản | O | Text | N | 20 | User | Input |
| Tên tài sản | O | Text | Y | 20 | User | Input |
| Phân loại tài sản | O | List | N | 20 | User | Select |
| Nhóm tài sản | O | List | N | 20 | User | Select |
| PO number | O | Text | Y | 20 | User | Input |
| Trạng thái TS | O | List | N | 50 | User | Select |
| Tên nhà cung cấp | O | List | N | 50 | User | Select |
| Tên kho | O | List | Y | 50 | User | Input |
| Vị trí đặt tài sản | O | Text | N | 100 | User | Select |

#### 5.6.2. Phê duyệt yêu cầu nhập kho thủ công

![Giao diện phê duyệt nhập kho thủ công](images/5_2_2a_B5_image5.png)

Warehouse Manager thực hiện phê duyệt yêu cầu nhập kho thủ công với giao diện tương tự như phê duyệt nhập kho từ điều chuyển. Sau khi phê duyệt, hệ thống chuyển trạng thái thành "Chờ nhập kho" và thông báo cho Warehouse Keeper (WK).

#### 5.6.3. Xác nhận nhập kho thủ công

![Giao diện xác nhận nhập kho thủ công](images/5_2_3a_B6_image6.png)

Warehouse Keeper thực hiện xác nhận nhập kho thủ công với quy trình tương tự như xác nhận nhập kho từ điều chuyển. Khi xác nhận, hệ thống tự động cập nhật ngày bắt đầu sử dụng và chuyển trạng thái thành "Đã nhập kho".

### 5.7. Hủy yêu cầu nhập kho

![Giao diện hủy yêu cầu nhập kho](images/5_3_1a_B5_image7.png)

Chức năng hủy yêu cầu nhập kho cho phép hủy bỏ các yêu cầu nhập kho đã tạo nhưng chưa được xử lý hoặc cần điều chỉnh. Quy trình bao gồm 8 bước từ tìm kiếm yêu cầu đến thông báo kết quả.

**Điều kiện hủy:** Yêu cầu nhập kho phải có trạng thái khác "Đã nhập kho"

**Quy trình chính:**
1. Tìm kiếm yêu cầu cần hủy
2. Hiển thị kết quả và cho phép chọn yêu cầu
3. Nhập lý do hủy (bắt buộc)
4. Hệ thống tự động unlock tài sản
5. Cập nhật trạng thái thành "Đã hủy"
6. Cập nhật tasklist cho các role liên quan
7. Gửi email notification đến BU/user

### 5.8. Cấp Tài Sản

#### 5.8.1. Phê duyệt yêu cầu cấp tài sản

![Giao diện phê duyệt cấp tài sản](images/5_4_0a_A4_image8.png)

Asset Manager thực hiện phê duyệt yêu cầu cấp tài sản với giao diện tìm kiếm, xem chi tiết và ra quyết định phê duyệt/từ chối. Giao diện hiển thị đầy đủ thông tin tài sản, người sử dụng và thông tin bảo hành.

Khi từ chối, hệ thống sẽ unlock tài sản để có thể sử dụng cho yêu cầu khác, cập nhật tasklist và gửi thông báo cho Asset Management Planner (AMP).

### 5.9. Create Warehouse Intake Request

![Giao diện tạo yêu cầu xuất kho](images/5_4_1a__B5_image9.png)

Hệ thống tự động tạo yêu cầu xuất kho dựa trên thông tin từ phiếu cấp/thanh lý đã được phê duyệt. Giao diện hiển thị đầy đủ thông tin tài sản và cho phép người dùng nhập thông tin đầu mối nhận hàng.

**Yêu cầu kỹ thuật:**
- Số yêu cầu xuất kho theo format XK.YY.xxxx
- Hiển thị đầy đủ thông tin tài sản từ yêu cầu gốc
- Bắt buộc nhập thông tin đầu mối nhận hàng
- Tự động cập nhật trạng thái và gửi email cho WK

### 5.10. Xuất kho từ cấp tài sản - Tiếp nhận yêu cầu

![Giao diện tiếp nhận yêu cầu xuất kho](images/5_4_2a__B5_image10.png)

Quy trình tiếp nhận và xử lý yêu cầu xuất kho từ cấp tài sản bao gồm 11 bước chính. Người dùng có thể từ chối hoặc đồng ý yêu cầu. Đặc biệt, nút "Từ chối" sẽ bị ẩn nếu yêu cầu xuất kho xuất phát từ yêu cầu thanh lý.

**Yêu cầu đặc biệt:**
- Ẩn nút "Từ chối" nếu yêu cầu xuất kho xuất phát từ yêu cầu thanh lý
- Hệ thống tự động unlock asset khi từ chối
- Danh sách tài sản xuất kho phải bằng danh mục tài sản trong phiếu cấp/thanh lý

### 5.11. Xuất kho từ cấp tài sản - Phê duyệt yêu cầu

![Giao diện phê duyệt xuất kho](images/5_4_3a__B5_image11.png)

Warehouse Manager thực hiện phê duyệt yêu cầu xuất kho tài sản từ kho với quy trình 12 bước. Sau khi phê duyệt, hệ thống sẽ thông báo cho Warehouse Keeper để thực hiện xuất hàng.

### 5.12. Xuất kho từ cấp tài sản - Nhận tài sản

![Giao diện nhận tài sản](images/5_4_4a_B6_image12.png)

Business Unit User thực hiện quy trình nhận tài sản từ kho. Khi xác nhận, hệ thống phải clear thông tin kho và cập nhật đơn vị sử dụng cho tài sản. Quy trình đảm bảo tính nhất quán và truy vết đầy đủ trong việc quản lý tài sản.

### 5.13. Hủy yêu cầu xuất kho

![Giao diện hủy yêu cầu xuất kho](images/5_5_1a_B5_image13.png)

Chức năng hủy yêu cầu xuất kho cho phép hủy bỏ các yêu cầu xuất kho đã tạo. Điều kiện hủy là yêu cầu xuất kho phải có trạng thái khác "Đã xác nhận". Quy trình bao gồm 8 bước từ tìm kiếm đến thông báo kết quả.

**Yêu cầu đặc biệt:**
- Điều kiện hủy: Yêu cầu xuất kho phải có trạng thái khác "Đã xác nhận"
- Lý do hủy là trường bắt buộc
- Hệ thống phải unlock tài sản sau khi hủy
- Ẩn nút "Từ chối" đối với RQ xuất kho liên kết với RQ thanh lý

### 5.14. Điều chuyển tài sản giữa các kho - Tạo yêu cầu điều chuyển kho

![Giao diện tạo yêu cầu điều chuyển kho](images/5_6_1a_B6_image14.png)

Chức năng điều chuyển tài sản giữa các kho cho phép tạo yêu cầu chuyển tài sản từ kho này sang kho khác. Giao diện được chia thành nhiều phần: thông tin chung, tìm kiếm tài sản, thông tin kho đi/kho nhận và đầu mối giao hàng.

**Quy trình tự động sau khi tạo yêu cầu:**
1. Khóa tài sản để tránh xung đột
2. Cập nhật trạng thái yêu cầu thành "Chờ phê duyệt"
3. Tìm và gán người duyệt phù hợp
4. Cập nhật tasklist cho Asset Manager và Warehouse Manager
5. Gửi thông báo email cho các bên liên quan

**Thông tin chung yêu cầu:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Format | Default value | Data rule |
|----------|--------|---------------|-----|------------|----------|------------|--------|---------------|-----------|
| User | Select | Tạo | M | Button | N | | | | |
| System | Display | Số yêu cầu | M | Text | N | 50 | CK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 |
| System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| User | Input | Tiêu đề | O | Text | Y | 150 | | | |

### 5.15. Điều chuyển tài sản giữa các kho - Phê duyệt yêu cầu

![Giao diện phê duyệt điều chuyển kho](images/5_6_2a_B5_image15.png)

Approver thực hiện phê duyệt yêu cầu điều chuyển tài sản giữa các kho với quy trình 14 bước. Sau khi phê duyệt, hệ thống tự động tạo biên bản điều chuyển và cập nhật thông tin kho của tài sản.

**Quy trình kết thúc:**
- Bàn giao thực tế tài sản giữa warehouse keeper của kho đi và kho nhận
- Cập nhật thông tin kho trong hệ thống để phản ánh vị trí mới của tài sản
- Tự động tạo biên bản điều chuyển

### 5.16. Status

Module Status định nghĩa chi tiết các quy trình nghiệp vụ chính trong hệ thống quản lý tài sản bao gồm: Cấp tài sản, Thanh lý tài sản và Điều chuyển tài sản. Hệ thống theo dõi song song cả trạng thái yêu cầu (Request Status) và trạng thái tài sản (Asset Status).

**Ma trận trạng thái quy trình quản lý tài sản:**

| Process | Sub-process | PIC | Action | Rq Status | Asset Status | Note |
|---------|-------------|-----|--------|-----------|--------------|------|
| **Cấp tài sản** | - | - | - | Cấp tài sản | Xuất kho | - |
| Cấp tài sản không ở kho | 1. Tạo yêu cầu | AMP | Lưu | Đang tạo | | |
| | | | Gửi | Chờ xác nhận | | |
| | 2. Xác nhận | BU User | Từ chối | Từ chối | | |
| | | | Xác nhận | Đã xác nhận | Đang sử dụng | Đã xác nhận >>> Đã nhận tài sản |
| | | | Bổ sung thông tin | Bổ sung thông tin | | |
| | 3. Bổ sung TT | AMP | Bổ sung thông tin | Chờ xác nhận | | |
| **Cấp tài sản từ kho** | 1. Tạo yêu cầu | AMP | Lưu | Đang tạo | | |
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

**Yêu cầu hệ thống:**
- Hỗ trợ workflow approval cho từng loại yêu cầu
- Theo dõi trạng thái song song cho Request và Asset
- Hỗ trợ chức năng từ chối và yêu cầu bổ sung thông tin tại mọi bước phê duyệt
- Tự động tạo yêu cầu xuất/nhập kho sau khi hoàn thành phê duyệt
- Khả năng hủy yêu cầu và trả về trạng thái ban đầu

### 5.17. Tasklist

Module Tasklist quản lý các task trong quy trình từ tạo yêu cầu điều chuyển đến xác nhận nhập kho. Quy trình được chia thành hai nhóm: "Tasklist Điều chuyển" và "Tasklist Kho" với trạng thái "Cần xử lý" và "Đã xử lý".

**Danh sách công việc (Tasklist):**

| Sub-process | Action | Role | Tasklist Điều chuyển |  | Tasklist Kho |  | Ghi chú |
|-------------|--------|------|---------------------|--|--------------|--|---------|
|             |        |      | Cần xử lý | Đã xử lý | Cần xử lý | Đã xử lý |  |
| **2.3.1a Tạo yêu cầu điều chuyển** | Lưu | Initiator | x |  |  |  |  |
|  | Gửi |  |  | x |  |  |  |
| **2.3.3a Phê duyệt yêu cầu điều chuyển** | Từ chối | Initiator | x |  |  |  |  |
|  |  | BUH |  | x |  |  |  |
|  | Duyệt | Initiator |  | x |  |  |  |
|  |  | BUH |  | x |  |  |  |
|  |  | AMP | x |  |  |  |  |
|  | Bổ sung thông tin | Initiator | x |  |  |  |  |
|  |  | BUH |  | x |  |  |  |
| **5.2.2a Xác nhận yêu cầu điều chuyển** | Từ chối | Initiator | x |  |  |  |  |
|  |  | BUH |  | x |  |  |  |
|  |  | AMP |  | x |  |  |  |
|  | Bổ sung thông tin | Initiator | x |  |  |  |  |
|  |  | BUH |  | x |  |  |  |
|  |  | AMP |  | x |  |  |  |
|  | Xác nhận & Yêu cầu nhập kho | Gửi | Initiator | x |  |  |  |
|  |  |  | BUH |  | x |  |  |
|  |  |  | AMP |  | x | x |  |
|  |  |  | WM |  |  | x |  |

**Yêu cầu hệ thống:**
- Quy trình phải trải qua các bước: Tạo yêu cầu → Phê duyệt → Xác nhận → Nhập kho
- Mỗi bước đều có cơ chế từ chối và yêu cầu bổ sung thông tin
- Task phải được phân loại theo trạng thái "Cần xử lý" và "Đã xử lý"
- Cần giải quyết vấn đề về quy trình xử lý tại bước phê duyệt nhập kho

---

## 6. Dependencies

### Hệ thống phụ thuộc
- **OMS (Organization Management System)**: Cung cấp thông tin kho, địa chỉ và quản lý kho
- **EMS**: Đồng bộ tiêu đề PO và thông tin tài sản
- **ITSM (IT Service Management)**: Tích hợp cho module sửa chữa tài sản
- **Cổng hỗ trợ chi nhánh trên intranet**: Kết nối cho quy trình sửa chữa

### Phụ thuộc kỹ thuật
- Infrastructure hiện tại phải đủ khả năng xử lý tải tăng thêm từ các module mới
- Database schema hiện tại cần được mở rộng để hỗ trợ thêm các trường dữ liệu mới
- Hệ thống notification/email hiện tại cần được nâng cấp

---

## 7. Acceptance Criteria

### Criteria cho Dashboard Tài sản
- Dashboard hiển thị chính xác 4 chỉ số KPI như đã định nghĩa
- Bộ lọc hoạt động đúng với dữ liệu từ OMS
- Các biểu đồ tương tác hiển thị đúng dữ liệu khi hover và click
- Khả năng xuất dữ liệu ra Excel hoạt động chính xác

### Criteria cho Module Quản lý Kho
- Tất cả 8 quy trình hoạt động đúng với thiết kế As-is và To-be
- Hệ thống tự động tạo yêu cầu liên quan đúng như mô tả
- Chức năng lock/unlock tài sản hoạt động chính xác
- Email notification được gửi đến đúng người nhận

### Criteria cho tích hợp hệ thống
- Đồng bộ dữ liệu với OMS, EMS hoạt động real-time
- Không gây gián đoạn đến các chức năng hiện tại của FAM
- Performance không bị giảm quá 20% so với hiện tại

---

## 8. Glossary

| Thuật ngữ | Định nghĩa |
|-----------|------------|
| **FAM** | Fixed Asset Management - Hệ thống quản lý tài sản cố định |
| **AMP** | Asset Management Personnel - Nhân viên quản lý tài sản |
| **WM** | Warehouse Manager - Quản lý kho |
| **WK** | Warehouse Keeper - Thủ kho |
| **BU** | Business Unit - Đơn vị kinh doanh |
| **OMS** | Organization Management System - Hệ thống quản lý tổ chức |
| **EMS** | Enterprise Management System - Hệ thống quản lý doanh nghiệp |
| **ITSM** | IT Service Management - Hệ thống quản lý dịch vụ IT |
| **LOV** | List of Values - Danh sách giá trị |
| **CAT1** | Category 1 - Phân loại tài sản cấp 1 |
| **RQ** | Request - Yêu cầu |
| **TS** | Tài sản |
| **ATM** | Automated Teller Machine - Máy ATM |

---

*Tài liệu này được tạo từ 37 sheet specifications và bao gồm tất cả các yêu cầu nghiệp vụ chi tiết cho dự án FAM UPGRADE - WAVE 4.*

---

*Generated by Claude Sonnet 4.5 from 37 sheet summaries*
*Headings: 52 | Internal Links: 35 | Images: 15*

*✅ All internal links validated successfully*
*✅ All image paths validated successfully*
