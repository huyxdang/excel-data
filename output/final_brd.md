# Tài Liệu Yêu Cầu Nghiệp Vụ (BRD) - FAM Upgrade Wave 4

## Mục lục

- [1. Executive Summary](#1-executive-summary)
- [2. Project Scope & Objectives](#2-project-scope-objectives)
- [3. Stakeholders](#3-stakeholders)
- [4. Business Requirements](#4-business-requirements)
  - [4.1. Asset Dashboard Module](#41-asset-dashboard-module)
  - [4.2. Warehouse Management Module](#42-warehouse-management-module)
    - [4.2.1. Create Warehouse Intake Request](#421-create-warehouse-intake-request)
    - [4.2.2. Approve Warehouse Entry Request](#422-approve-warehouse-entry-request)
    - [4.2.3. Warehouse Receipt Confirmation](#423-warehouse-receipt-confirmation)
    - [4.2.4. Manual Warehouse Entry](#424-manual-warehouse-entry)
    - [4.2.5. Cancel Warehouse Request](#425-cancel-warehouse-request)
    - [4.2.6. Asset Allocation and Warehouse Exit](#426-asset-allocation-and-warehouse-exit)
    - [4.2.7. Cancel Warehouse Exit Request](#427-cancel-warehouse-exit-request)
    - [4.2.8. Inter-Warehouse Transfer](#428-inter-warehouse-transfer)
  - [4.3. Asset Enhancement Features](#43-asset-enhancement-features)
- [5. Business Process Flows](#5-business-process-flows)
- [6. System Status Management](#6-system-status-management)
- [7. Task Assignment Matrix](#7-task-assignment-matrix)
- [8. Assumptions & Constraints](#8-assumptions-constraints)
- [9. Dependencies](#9-dependencies)
- [10. Acceptance Criteria](#10-acceptance-criteria)
- [11. Glossary](#11-glossary)

---

## 1. Executive Summary

Dự án nâng cấp hệ thống quản lý tài sản FAM (Fixed Asset Management) giai đoạn Wave 4 tập trung vào việc phát triển và cải tiến các tính năng cốt lõi nhằm tối ưu hóa quy trình quản lý tài sản doanh nghiệp.

Các sản phẩm chính bao gồm [4.1. module dashboard tài sản](#41-asset-dashboard-module) với khả năng visualization và customization, [4.2. module quản lý kho toàn diện](#42-warehouse-management-module) xử lý xuất-nhập kho tài sản, và [4.3. các tính năng cải tiến](#43-asset-enhancement-features) cho hệ thống hiện tại.

Dự án bao gồm 11 yêu cầu chính được phân loại thành ba nhóm: Enhancement (cải tiến), New Launch (module mới), và Integration (tích hợp hệ thống). Trong đó, [module kho](#42-warehouse-management-module) được đánh giá mức ưu tiên cao nhất với khả năng xử lý các quy trình xuất-nhập kho phức tạp và tích hợp với các module khác trong hệ thống.

---

## 2. Project Scope & Objectives

### Trong phạm vi dự án

- Phát triển dashboard tài sản với khả năng trực quan hóa dữ liệu và tùy chỉnh theo nhiều tiêu chí
- Xây dựng module quản lý kho hoàn chỉnh với các chức năng xuất-nhập kho tự động và thủ công
- Cải tiến các tính năng hiện có của hệ thống quản lý tài sản
- Tích hợp với các hệ thống OMS và EMS để đồng bộ dữ liệu
- Phát triển module sửa chữa tài sản tích hợp với ITSM

### Ngoài phạm vi dự án

- Thay đổi cấu trúc cơ sở dữ liệu hiện tại
- Phát triển các module không được liệt kê trong yêu cầu
- Tích hợp với các hệ thống bên ngoài khác OMS và EMS

### Mục tiêu dự án

- Nâng cao hiệu quả quản lý tài sản thông qua tự động hóa quy trình
- Cải thiện khả năng theo dõi và báo cáo tình trạng tài sản
- Tối ưu hóa quy trình xuất-nhập kho và điều chuyển tài sản
- Đảm bảo tính nhất quán dữ liệu giữa các hệ thống

---

## 3. Stakeholders

### Vai trò trong hệ thống

- **AMP (Asset Management Personnel)** - Nhân viên quản lý tài sản: Thực hiện các tác vụ quản lý tài sản hàng ngày
- **AM (Asset Manager)** - Quản lý tài sản: Phê duyệt các yêu cầu cấp phát và thanh lý tài sản
- **BU User (Business Unit User)** - Người dùng đơn vị kinh doanh: Tạo yêu cầu và nhận tài sản
- **BU Head (Business Unit Head)** - Trưởng đơn vị kinh doanh: Phê duyệt yêu cầu từ đơn vị
- **WK (Warehouse Keeper)** - Thủ kho: Thực hiện các tác vụ xuất-nhập kho
- **Warehouse Manager** - Quản lý kho: Phê duyệt các yêu cầu liên quan đến kho
- **Checker** - Người kiểm soát: Kiểm tra các yêu cầu trước khi phê duyệt
- **Approver** - Người phê duyệt: Phê duyệt cuối cùng các yêu cầu quan trọng

### Hệ thống liên quan

- **OMS (Organization Management System)** - Hệ thống quản lý tổ chức
- **EMS (Employee Management System)** - Hệ thống quản lý nhân sự  
- **ITSM (IT Service Management)** - Hệ thống quản lý dịch vụ IT
- **Cổng hỗ trợ chi nhánh** - Trên intranet

---

## 4. Business Requirements

### 4.1. Asset Dashboard Module

Module dashboard tài sản cung cấp giao diện tổng quan trực quan hóa dữ liệu tài sản của tổ chức, hỗ trợ việc đưa ra quyết định nhanh chóng về quản lý tài sản. Dashboard hiển thị các thông số tổng quan như tổng số tài sản, tổng giá trị, tỷ lệ tài sản còn bảo hành và tỷ lệ sử dụng tài sản.

![Dashboard tài sản](images/1.csv)

Hệ thống cung cấp nhiều dạng biểu đồ tương tác (Sunburst, Stacked Column, Line, Scatter) để hiển thị phân bổ tài sản, giá trị theo nhóm, biến động theo thời gian và phân tích theo thời gian sử dụng. Dashboard có khả năng lọc dữ liệu theo nhiều tiêu chí và hỗ trợ xuất báo cáo ra Excel.

**Yêu cầu chức năng:**
- Giao diện phải trực quan và hỗ trợ đưa ra quyết định nhanh chóng
- Biểu đồ có tính tương tác với khả năng click chuyển sang module liên quan
- Loại bỏ tài sản đã thanh lý và vô hiệu hóa khỏi các tính toán chính
- Đồng bộ dữ liệu đơn vị sử dụng từ [hệ thống OMS](#3-stakeholders)
- Phân nhóm tài sản theo categories IT/ADM/CMD

#### Thông số kỹ thuật Dashboard

| Content | Value | Type of Chart | Note |
|---------|-------|---------------|------|
| Total assets | Count số lượng (All tài sản - Đã thanh lý - Vô hiệu hóa) | - | - |
| Total value | Sum nguyên giá (All tài sản - Đã thanh lý - Vô hiệu hóa) | - | - |
| Warranty status | Tỷ lệ phần trăm theo số lượng tài sản còn hạn bảo hành/(All tài sản - Vô hiệu hóa - Đã thanh lý) | - | - |
| Utilization rate | Tỷ lệ phần trăm theo số lượng tài sản có trạng thái đang sử dụng/(All tài sản - Vô hiệu hóa - Đã thanh lý) | - | - |

#### Cấu hình bộ lọc

| Filter Name | Data Source | Type |
|-------------|-------------|------|
| Vùng | LOV | Dropdown |
| Đơn vị sử dụng | LOV đồng bộ từ OMS | Dropdown |
| CAT 1 | LOV | Dropdown |
| Group name | LOV | Dropdown |
| Asset status | LOV asset status (Không bao gồm Đã thanh lý, Vô hiệu hóa) | Dropdown |

#### Đặc tả biểu đồ

| Chart Name | Data Value | Chart Type | Notes |
|------------|------------|------------|-------|
| Asset Distribution - Cơ cấu nhóm tài sản theo trạng thái | Nguyên giá | Sunburst (Vòng trong: Nhóm IT/ADM/CMD, Vòng ngoài: Trạng thái) | Khi Hover chuột thể hiện số lượng và giá trị |
| Asset Distribution - Cơ cấu theo Vùng/Đơn vị | Nguyên giá | Stacked Column | - |
| Asset Value by Group Name | Nguyên giá | Column | - |
| Asset Fluctuation Over Time (Month/Year) | Nguyên giá | Line | - |
| Asset by Time in Use | Số lượng | Scatter | - |

---

### 4.2. Warehouse Management Module

Module quản lý kho xử lý toàn bộ quy trình xuất-nhập kho tài sản, hỗ trợ cả việc xử lý tự động và thủ công. Module này tích hợp chặt chẽ với các quy trình cấp tài sản, thanh lý và điều chuyển, đảm bảo tính nhất quán và truy xuất được của toàn bộ vòng đời tài sản.

Các quy trình chính bao gồm:
- [4.2.1. Tạo yêu cầu nhập kho](#421-create-warehouse-intake-request) (tự động từ điều chuyển)
- [4.2.2. Phê duyệt yêu cầu nhập kho](#422-approve-warehouse-entry-request)
- [4.2.3. Xác nhận nhập kho](#423-warehouse-receipt-confirmation)
- [4.2.4. Nhập kho thủ công](#424-manual-warehouse-entry)
- [4.2.5. Hủy yêu cầu nhập kho](#425-cancel-warehouse-request)
- [4.2.6. Cấp tài sản và xuất kho](#426-asset-allocation-and-warehouse-exit)
- [4.2.7. Hủy yêu cầu xuất kho](#427-cancel-warehouse-exit-request)
- [4.2.8. Điều chuyển giữa các kho](#428-inter-warehouse-transfer)

#### 4.2.1. Create Warehouse Intake Request

##### 4.2.1.1. Thông số kỹ thuật giao diện người dùng

![Giao diện tạo yêu cầu nhập kho](images/5_1_1a_B5_image1.png)

Quy trình tạo yêu cầu nhập kho được khởi tạo tự động khi có yêu cầu chuyển kho được xác nhận. Hệ thống sẽ kế thừa toàn bộ thông tin từ yêu cầu chuyển kho bao gồm thông tin tài sản, chi tiết kho đích và các tệp đính kèm.

**Cấu trúc màn hình:**
- Phần header hiển thị số yêu cầu và trạng thái
- Phần thông tin chung cho phép nhập tiêu đề và ghi chú
- Phần chi tiết tài sản hiển thị danh sách tài sản được chuyển
- Phần tệp đính kèm cho phép upload thêm tài liệu

Quy trình xử lý bao gồm 4 bước chính: tạo yêu cầu nhập kho, cập nhật trạng thái các yêu cầu liên quan, cập nhật tasklist cho [AMP và WM](#3-stakeholders), và gửi thông báo email cho Warehouse Manager.

**Các bên liên quan:** Hệ thống (tự động tạo), [Quản lý kho](#3-stakeholders) (phê duyệt), [AMP](#3-stakeholders) (theo dõi)

##### 4.2.1.2. Thông số kỹ thuật chi tiết

Hệ thống tự động sinh số yêu cầu theo format NK.YY.xxxx và kế thừa toàn bộ thông tin từ yêu cầu điều chuyển gốc. Tài sản sẽ được unlock khỏi RQ điều chuyển và lock bởi RQ nhập kho mới để đảm bảo tính nhất quán dữ liệu.

**Đặc tả trường dữ liệu:**

| Tab/Section | Operator | Action | Field Name VN | M/O | Field Type | Editable | Max Length | Format | Default Value | Data Rule |
|-------------|----------|--------|---------------|-----|------------|----------|------------|---------|---------------|-----------|
| Thông tin chung | System | Display | Số yêu cầu | M | Text | N | 50 | NK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| Thông tin chung | System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| Thông tin chung | System | Display | Tiêu đề | M | Text | N | 150 | | | =Tiêu đề RQ điều chuyển |
| DS tài sản nhập kho | System | Display | Mã tài sản | M | | N | | | | Hiển thị mặc định |
| DS tài sản nhập kho | System | Display | Tên Tài sản | M | | N | | | | Hiển thị mặc định |
| DS tài sản nhập kho | System | Display | Mô tả TS | M | | N | | | | Hiển thị mặc định |
| DS tài sản nhập kho | System | Display | Trạng thái TS | M | | N | | | | Hiển thị mặc định |
| DS tài sản nhập kho | System | Display | Phân nhóm TS (group name) | M | | N | | | | Hiển thị mặc định |
| DS tài sản nhập kho | System | Display | Nhóm TS (CAT1) | M | | N | | | | Hiển thị mặc định |
| DS tài sản nhập kho | System | Display | Số PO | M | | N | | | | Hiển thị mặc định |
| DS tài sản nhập kho | System | Display | Tên nhà cung cấp | O | | N | | | | Ẩn hiện tùy biến |
| DS tài sản nhập kho | System | Display | Nguyên giá TS (VAT incl) | M | | N | | | | Ẩn hiện tùy biến |
| Thông tin kho nhập | System | Display | Tên kho | M | List | N | 50 | | | = Kho trong RQ điều chuyển |
| Thông tin kho nhập | System | Display | Địa chỉ kho | M | Text | N | 50 | | | Tự động nhận diện, hiển thị theo Tên kho |
| Thông tin kho nhập | System | Display | Quản lý kho | M | Text | N | 50 | | | Tự động nhận diện (Tên \| Phòng ban \| Email) |
| Thông tin đầu mối giao hàng | User | Input | Đầu mối | M | Text | N | 50 | | | = Đầu mối giao hàng trong RQ điều chuyển |
| Thông tin đầu mối giao hàng | User | Input | Số điện thoại | M | Number | N | 52 | | | |
| Thông tin đầu mối giao hàng | User | Input | Thời gian bàn giao | O | Date | N | 50 | | | |

**Quy trình xử lý từ AMP:**

Khi yêu cầu điều chuyển được xử lý, [AMP](#3-stakeholders) có thể từ chối, xác nhận hoặc yêu cầu bổ sung thông tin. Hệ thống hiển thị đầy đủ thông tin tài sản bao gồm thông tin cơ bản, người sử dụng hiện tại, vị trí đặt và thông tin bảo hành.

**Bảng tìm kiếm yêu cầu:**

| Field name VN | M/O | Field type | Editable | Max length | Operator | Action |
|---------------|-----|------------|----------|------------|----------|---------|
| Mã yêu cầu | O | Text | Y | 20 | User | Input |
| Tiêu đề | O | Text | Y | 100 | User | Input |
| Người xử lý | O | List | Y | 20 | User | Select |
| Loại điều chuyển | O | List | Y | 20 | User | Select |
| Trạng thái | O | List | Y | 20 | User | Select |
| Người tạo | O | List | Y | 20 | User | Select |
| Người đề xuất | O | List | Y | 20 | User | Select |
| Ngày tạo | O | Date | Y | 50 | User | Input |
| Đơn vị điều chuyển | O | List | Y | 50 | User | Select |
| Đơn vị nhận điều chuyển | O | List | Y | 50 | User | Select |

Khi xác nhận, hệ thống tự động tạo yêu cầu nhập kho với số theo format NK.YY.xxxx và chuyển sang [quy trình phê duyệt](#422-approve-warehouse-entry-request).

#### 4.2.2. Approve Warehouse Entry Request

##### 4.2.2.1. Thông số kỹ thuật giao diện người dùng

![Giao diện phê duyệt yêu cầu nhập kho](images/5.1.2a_B6_image2.png)

Quy trình phê duyệt yêu cầu nhập kho được thiết kế cho [Warehouse Manager](#3-stakeholders) để xem xét và phê duyệt các yêu cầu nhập kho tài sản. Giao diện hiển thị toàn bộ thông tin chi tiết về yêu cầu và tài sản để hỗ trợ quyết định phê duyệt.

**Luồng xử lý:**
1. Warehouse Manager tìm kiếm yêu cầu cần xử lý
2. Xem chi tiết thông tin tài sản và yêu cầu
3. Đưa ra quyết định phê duyệt hoặc từ chối
4. Hệ thống cập nhật trạng thái và thông báo

##### 4.2.2.2. Thông số kỹ thuật chi tiết

Giao diện được thiết kế với nhiều phần thông tin chi tiết bao gồm danh sách tài sản cần nhập kho với 25+ thuộc tính có thể tùy biến hiển thị, thông tin kho đích, đầu mối giao hàng và lịch sử xử lý.

**Bảng tìm kiếm yêu cầu:**

| Trường | Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|--------|----------|---------|---------------|-----|------------|----------|------------|
| User | Input | Số yêu cầu | O | Text | Y | 20 |
| User | Input | Ngày tạo | O | Date | Y | 20 |
| User | Input | Tiêu đề | O | Text | Y | 150 |
| User | Select | Người tạo | O | List | Y | 20 |
| User | Select | Trạng thái yêu cầu | O | List | Y | 20 |
| User | Select | Người xử lý | O | List | Y | 20 |
| User | Input | Ngày xác nhận | O | Date | Y | 20 |

**Bảng hiển thị tài sản:**

| Operator | Action | Field name VN | M/O | Data rule |
|----------|---------|---------------|-----|-----------|
| System | Display | Mã tài sản | M | Hiển thị mặc định |
| System | Display | Tên Tài sản | M | Hiển thị mặc định |
| System | Display | Mô tả TS | M | Hiển thị mặc định |
| System | Display | Trạng thái TS | M | Hiển thị mặc định |
| System | Display | Phân nhóm TS (group name) | M | Hiển thị mặc định |
| System | Display | Nhóm TS (CAT1) | M | Hiển thị mặc định |
| System | Display | Số PO | M | Hiển thị mặc định |
| System | Display | Tên nhà cung cấp | O | Ẩn hiện tùy biến |
| System | Display | Nguyên giá TS (VAT incl) | M | Ẩn hiện tùy biến |
| System | Display | Tên người sử dụng | M | Hiển thị mặc định |
| System | Display | Tên đơn vị | M | Hiển thị mặc định |
| System | Display | Đơn vị sử dụng cha | M | Hiển thị mặc định |

Khi từ chối, hệ thống yêu cầu nhập lý do từ chối (bắt buộc, max 150 ký tự) và tự động unlock tài sản. Khi phê duyệt, chuyển sang [quy trình xác nhận nhập kho](#423-warehouse-receipt-confirmation).

#### 4.2.3. Warehouse Receipt Confirmation

##### 4.2.3.1. Thông số kỹ thuật giao diện người dùng

![Giao diện xác nhận nhập kho](images/5_1_3a_B5_image3.png)

Quy trình xác nhận nhập kho là bước cuối cùng trong chu trình nhập kho, được thực hiện bởi [Warehouse Keeper](#3-stakeholders) để xác nhận việc nhận tài sản vào kho.

##### 4.2.3.2. Thông số kỹ thuật chi tiết

Giao diện cho phép [WK](#3-stakeholders) tìm kiếm, xem chi tiết và xác nhận nhận tài sản vào kho. Khi xác nhận, hệ thống tự động cập nhật "Ngày bắt đầu sử dụng" nếu trường này đang là N/A.

**Bảng tìm kiếm yêu cầu:**

| Field name VN | M/O | Field type | Editable | Max length | Operator | Action |
|---------------|-----|------------|----------|------------|----------|---------|
| Số yêu cầu | O | Text | Y | 20 | User | Input |
| Ngày tạo | O | Date | Y | 20 | User | Input |
| Tiêu đề | O | Text | Y | 150 | User | Input |
| Người tạo | O | List | Y | 20 | User | Select |
| Trạng thái yêu cầu | O | List | Y | 20 | User | Select |
| Người xử lý | O | List | Y | 20 | User | Select |
| Ngày xác nhận | O | Date | Y | 20 | User | Input |

**Quy trình xử lý:**
- Khi xác nhận: cập nhật trạng thái "Đã nhập kho", unlock tài sản
- Khi từ chối: cập nhật trạng thái request điều chuyển liên quan, unlock tài sản
- Gửi thông báo email cho [AMP](#3-stakeholders) theo từng trường hợp

#### 4.2.4. Manual Warehouse Entry

##### 4.2.4.1. Thông số kỹ thuật giao diện người dùng

Chức năng nhập kho thủ công cho phép người dùng tạo yêu cầu nhập kho không thông qua các quy trình tự động. Giao diện hỗ trợ tìm kiếm tài sản theo nhiều tiêu chí và chọn tài sản cần nhập kho.

##### 4.2.4.2. Thông số kỹ thuật chi tiết

**Bảng thông tin chung yêu cầu:**

| Trường | Operator | Action | Tên trường | M/O | Kiểu | Editable | Max Length | Format | Default | Data Rule |
|--------|----------|--------|------------|-----|------|----------|------------|--------|---------|-----------|
| Số yêu cầu | System | Display | Số yêu cầu | M | Text | N | 50 | NK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| Ngày tạo | System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| Tiêu đề | User | Input | Tiêu đề | O | Text | Y | 150 | | | |

**Bảng tìm kiếm tài sản:**

| Trường | Operator | Action | Tên trường | M/O | Kiểu | Editable | Max Length |
|--------|----------|--------|------------|-----|------|----------|------------|
| Mã tài sản | User | Input | Mã tài sản | O | Text | N | 20 |
| Tên tài sản | User | Input | Tên tài sản | O | Text | Y | 20 |
| Phân loại tài sản | User | Select | Phân loại tài sản | O | List | N | 20 |
| Nhóm tài sản | User | Select | Nhóm tài sản | O | List | N | 20 |
| PO number | User | Input | PO number | O | Text | Y | 20 |
| Trạng thái TS | User | Select | Trạng thái TS | O | List | N | 50 |
| Tên nhà cung cấp | User | Select | Tên nhà cung cấp | O | List | N | 50 |
| Tên kho | User | Input | Tên kho | O | List | Y | 50 |
| Vị trí đặt tài sản | User | Select | Vị trí đặt tài sản | O | Text | N | 100 |

**Yêu cầu đặc biệt:**
- Hệ thống cảnh báo khi tài sản được chọn đang bị lock trong request khác
- Cho phép chọn nhiều tài sản trong một yêu cầu
- Tự động nhận diện thông tin kho từ [hệ thống OMS](#3-stakeholders)

Quy trình sau khi tạo yêu cầu sẽ chuyển sang [phê duyệt](#422-approve-warehouse-entry-request) và [xác nhận](#423-warehouse-receipt-confirmation) tương tự như quy trình tự động.

#### 4.2.5. Cancel Warehouse Request

##### 4.2.5.1. Thông số kỹ thuật giao diện người dùng

Chức năng hủy yêu cầu nhập kho cho phép [AMP](#3-stakeholders) hủy bỏ các yêu cầu nhập kho đã tạo với điều kiện yêu cầu chưa ở trạng thái "Đã nhập kho".

##### 4.2.5.2. Thông số kỹ thuật chi tiết

**Điều kiện tiên quyết:** Yêu cầu nhập kho phải có trạng thái khác "Đã nhập kho"

**Bảng tìm kiếm yêu cầu:**

| STT | Operator | Action | Field Name | M/O | Field Type | Editable | Max Length |
|-----|----------|--------|------------|-----|------------|----------|------------|
| 1 | User | Input | Số yêu cầu | O | Text | Y | 20 |
| 2 | User | Input | Ngày tạo | O | Date | Y | 20 |
| 3 | User | Input | Tiêu đề | O | Text | Y | 150 |
| 4 | User | Select | Người tạo | O | List | Y | 20 |
| 5 | User | Select | Trạng thái yêu cầu | O | List | Y | 20 |
| 6 | User | Select | Người xử lý | O | List | Y | 20 |
| 7 | User | Input | Ngày xác nhận | O | Date | Y | 20 |

**Quy trình hủy:**
1. [AMP](#3-stakeholders) tìm kiếm và chọn yêu cầu cần hủy
2. Nhập lý do hủy (bắt buộc)
3. Hệ thống unlock tài sản, cập nhật trạng thái "Đã hủy"
4. Gửi thông báo cho [BU/user](#3-stakeholders) và cập nhật tasklist

#### 4.2.6. Asset Allocation and Warehouse Exit

##### 4.2.6.1. Thông số kỹ thuật giao diện người dùng

![Giao diện phê duyệt yêu cầu cấp tài sản](images/5.4.0a_A4_image8.png)

Module cấp tài sản xử lý việc phê duyệt yêu cầu cấp phát tài sản và tự động tạo yêu cầu xuất kho tương ứng. Quy trình được chia thành các giai đoạn từ phê duyệt yêu cầu đến xuất kho và bàn giao tài sản.

##### 4.2.6.2. Thông số kỹ thuật chi tiết

**Quy trình phê duyệt yêu cầu cấp tài sản:**

Giao diện cho phép [Asset Manager](#3-stakeholders) tìm kiếm, xem chi tiết và phê duyệt yêu cầu cấp tài sản. Sau khi phê duyệt, hệ thống tự động tạo yêu cầu xuất kho với format số "XK.YY.xxxx".

**Bảng tìm kiếm yêu cầu:**

| Tên trường | Operator | Action | Loại trường | Bắt buộc | Có thể chỉnh sửa | Độ dài tối đa |
|------------|----------|--------|-------------|----------|------------------|---------------|
| Mã yêu cầu | User | Input | Text | M | Y | 20 |
| Tiêu đề | User | Input | Text | M | Y | 150 |
| Người tạo | User | Select | List | M | Y | 20 |
| Trạng thái | User | Select | List | M | Y | 20 |
| Ngày tạo | User | Input | Date | M | Y | 20 |
| Loại cấp tài sản | User | Select | List | M | Y | 100 |
| Người xử lý | User | Select | List | M | Y | 20 |
| Ngày xác nhận | User | Input | Date | M | Y | 20 |

**Tạo yêu cầu xuất kho:**

Khi yêu cầu cấp tài sản được phê duyệt, hệ thống tự động tạo yêu cầu xuất kho với các thông tin:

**Bảng đặc tả trường dữ liệu chính:**

| Phân nhóm | Tên trường | Operator | Action | M/O | Field Type | Editable | Max Length | Format | Default Value | Data Rule |
|-----------|------------|----------|---------|-----|------------|----------|------------|--------|---------------|-----------|
| **Thông tin chung** |
| | Số yêu cầu | System | Display | M | Text | N | 50 | XK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| | Ngày tạo | System | Display | M | Date | N | 50 | MM.DD.YYYY | Today | |
| | Tiêu đề | System | Input | O | Text | Y | 150 | | | =Tiêu đề RQ Cấp/Thanh lý |
| **DS tài sản xuất kho** |
| | Mã tài sản | System | Display | M | | N | | | | Hiển thị mặc định |
| | Tên Tài sản | System | Display | M | | N | | | | Hiển thị mặc định |
| | Mô tả TS | System | Display | M | | N | | | | Hiển thị mặc định |
| | Trạng thái TS | System | Display | M | | N | | | | Hiển thị mặc định |
| **Thông tin kho xuất** |
| | Tên kho | System/User | Display/Search/Select | M | List | N | 50 | | | = Thông tin kho trên RQ cấp/Thanh lý |
| | Địa chỉ kho | System | Display | M | Text | Y | 50 | | | |
| | Quản lý kho | System | Display | M | Text | N | 50 | | | |

**Quy trình tiếp nhận yêu cầu xuất kho:**

[Warehouse Keeper](#3-stakeholders) tiếp nhận và xử lý yêu cầu xuất kho thông qua giao diện chuyên dụng. Lưu ý rằng nút "Từ chối" sẽ bị ẩn nếu yêu cầu xuất kho xuất phát từ yêu cầu thanh lý.

**Quy trình phê duyệt xuất kho:**

[Warehouse Manager](#3-stakeholders) phê duyệt yêu cầu xuất kho sau khi [WK](#3-stakeholders) đồng ý. Quy trình này đảm bảo kiểm soát kép trước khi tài sản được xuất khỏi kho.

**Quy trình nhận tài sản:**

[BU User](#3-stakeholders) xác nhận nhận tài sản từ kho, hoàn tất quy trình cấp phát tài sản. Khi xác nhận, hệ thống cập nhật thông tin sở hữu tài sản và trạng thái sử dụng.

#### 4.2.7. Cancel Warehouse Exit Request

##### 4.2.7.1. Thông số kỹ thuật giao diện người dùng

Chức năng hủy yêu cầu xuất kho cho phép [AMP](#3-stakeholders) hủy bỏ các yêu cầu xuất kho với điều kiện chưa ở trạng thái "Đã xác nhận".

##### 4.2.7.2. Thông số kỹ thuật chi tiết

**Điều kiện tiên quyết:** Yêu cầu xuất kho phải có trạng thái khác "Đã xác nhận"

**Bảng tìm kiếm yêu cầu xuất kho:**

| Trường | Operator | Action | Tên trường | M/O | Kiểu | Chỉnh sửa | Độ dài | Định dạng |
|--------|----------|--------|------------|-----|------|-----------|--------|-----------|
| Tasklist | User | - | Mã yêu cầu | M | Text | N | 20 | - |
| Tasklist | User | - | Tiêu đề | M | Text | N | 150 | - |
| Tasklist | User | - | Người tạo | M | List | N | 20 | - |
| Tasklist | User | - | Trạng thái | M | List | N | 20 | - |
| Tasklist | User | - | Ngày tạo | M | Date | N | 20 | - |
| Tasklist | User | - | Nghiệp vụ kho | M | List | N | 100 | - |
| Tasklist | User | - | Người xử lý | O | List | N | 20 | - |
| Tasklist | User | - | Ngày xác nhận | O | Date | N | 20 | - |

**Quy trình hủy:**
- Bắt buộc nhập lý do hủy (max 150 ký tự)
- Hệ thống unlock tài sản và trả về trạng thái trước thanh lý
- Nút "Từ chối" được ẩn đối với yêu cầu xuất kho liên kết với thanh lý
- Gửi thông báo cho [Warehouse Manager](#3-stakeholders) khi hoàn tất

Khi hủy yêu cầu xuất kho, hệ thống sẽ tự động hủy các yêu cầu liên quan (thanh lý, cấp tài sản) để đảm bảo tính nhất quán dữ liệu.

#### 4.2.8. Inter-Warehouse Transfer

##### 4.2.8.1. Thông số kỹ thuật giao diện người dùng

![Giao diện tạo yêu cầu điều chuyển kho](images/5_6_1a_B6_image14.png)

Chức năng điều chuyển tài sản giữa các kho cho phép di chuyển tài sản từ kho này sang kho khác trong cùng hệ thống. Quy trình bao gồm tạo yêu cầu, phê duyệt và thực hiện điều chuyển.

##### 4.2.8.2. Thông số kỹ thuật chi tiết

**Tạo yêu cầu điều chuyển kho:**

Giao diện hỗ trợ tìm kiếm tài sản đa tiêu chí và tạo yêu cầu điều chuyển với đầy đủ thông tin kho đi, kho nhận và đầu mối giao nhận.

**Bảng thông tin chung:**

| Tab/Section | Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Format | Default value | Data rule |
|-------------|----------|---------|---------------|-----|------------|----------|------------|---------|---------------|-----------|
| Thông tin chung | System | Display | Số yêu cầu | M | Text | N | 50 | CK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| Thông tin chung | System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| Thông tin chung | User | Input | Tiêu đề | O | Text | Y | 150 | | | |
| Thông tin chung | User | Select | Thêm tài sản | M | Button | N | | | | |

**Bảng tìm kiếm tài sản:**

| Field name VN | M/O | Field type | Editable | Max length | Data rule |
|---------------|-----|------------|----------|------------|-----------|
| Mã tài sản | O | Text | N | 20 | |
| Tên tài sản | O | Text | Y | 20 | |
| Phân loại tài sản | O | List | N | 20 | |
| Nhóm tài sản | O | List | N | 20 | |
| PO number | O | Text | Y | 20 | |
| Trạng thái TS | O | List | N | 50 | |
| Tên nhà cung cấp | O | List | N | 50 | |
| Tên kho | O | List | Y | 50 | |
| Vị trí đặt tài sản | O | Text | N | 100 | |

**Phê duyệt yêu cầu điều chuyển kho:**

[Approver](#3-stakeholders) xem xét và phê duyệt yêu cầu điều chuyển. Khi phê duyệt, hệ thống tự động tạo biên bản điều chuyển và cập nhật thông tin kho của tài sản.

**Bảng tìm kiếm yêu cầu điều chuyển:**

| Field name VN | M/O | Field type | Editable | Max length | Operator |
|---------------|-----|------------|----------|------------|----------|
| Số yêu cầu | O | Text | Y | 20 | Input |
| Ngày tạo | O | Date | Y | 20 | Input |
| Tiêu đề | O | Text | Y | 150 | Input |
| Người tạo | O | List | Y | 20 | Select |
| Trạng thái yêu cầu | O | List | Y | 20 | Select |
| Người xử lý | O | List | Y | 20 | Select |
| Ngày xác nhận | O | Date | Y | 20 | Input |

**Yêu cầu xử lý:**
- Tài sản được khóa trong suốt quá trình xử lý để tránh xung đột
- Hệ thống tự động nhận diện thông tin kho từ [OMS](#3-stakeholders)
- Bắt buộc nhập lý do khi từ chối yêu cầu
- Tự động gửi thông báo và cập nhật tasklist cho các vai trò liên quan

Sau khi được phê duyệt, yêu cầu điều chuyển kho sẽ kích hoạt [quy trình nhập kho](#421-create-warehouse-intake-request) tại kho đích.

---

### 4.3. Asset Enhancement Features

Các tính năng cải tiến cho module tài sản hiện tại bao gồm:

**Cải tiến Dashboard và Hiển thị:**
- Dashboard tài sản với khả năng visualization và customization theo nhiều tiêu chí (được mô tả chi tiết trong [4.1. Asset Dashboard Module](#41-asset-dashboard-module))
- Quản lý hiển thị tài sản vô hiệu hóa với tùy chọn ẩn/hiện khỏi danh sách
- Đổi vị trí hiển thị một số cột trong danh sách tài sản để tối ưu trải nghiệm người dùng

**Cải tiến Quy trình Cấp phát:**
- Upload phiếu cấp tài sản hàng loạt theo danh sách để xử lý khối lượng lớn
- Tự động xác nhận phiếu cấp tài sản sau 20 ngày không có phản hồi từ người dùng
- Bổ sung luồng phê duyệt cho ATM trong module thanh lý

**Tích hợp Hệ thống:**
- Tự động đồng bộ [OMS](#3-stakeholders) khi orgchart thay đổi
- Đồng bộ tiêu đề PO từ [EMS](#3-stakeholders) sang FAM
- Cập nhật thông tin thời gian sử dụng và bảo hành từ [EMS](#3-stakeholders) dựa trên thời gian phê duyệt PO

**Module Sửa chữa Tài sản (Mới):**
- Tạo yêu cầu sửa chữa tài sản trên FAM
- Tích hợp với hệ thống [ITSM](#3-stakeholders) để xử lý yêu cầu kỹ thuật
- Kết nối với cổng hỗ trợ chi nhánh trên intranet

---

## 5. Business Process Flows

Hệ thống FAM Wave 4 hỗ trợ các quy trình nghiệp vụ chính sau:

**Quy trình Quản lý Kho:**
- [Nhập kho tự động](#421-create-warehouse-intake-request) từ điều chuyển về kho
- [Nhập kho thủ công](#424-manual-warehouse-entry) cho các trường hợp đặc biệt
- [Xuất kho từ cấp tài sản](#426-asset-allocation-and-warehouse-exit) với quy trình phê duyệt đa cấp
- [Điều chuyển giữa các kho](#428-inter-warehouse-transfer) nội bộ

**Tích hợp và Tự động hóa:**
- Hệ thống tự động tạo yêu cầu xuất/nhập kho khi các quy trình upstream được phê duyệt
- Cơ chế liên kết giữa các yêu cầu (hủy yêu cầu xuất kho sẽ tự động hủy yêu cầu cấp/thanh lý liên quan)
- Đồng bộ dữ liệu với [OMS](#3-stakeholders) và [EMS](#3-stakeholders) để đảm bảo tính nhất quán

**Kiểm soát và Phê duyệt:**
- Quy trình phê duyệt đa cấp với khả năng từ chối và yêu cầu bổ sung thông tin
- Cơ chế lock/unlock tài sản để tránh xung đột dữ liệu
- Ghi lại lịch sử xử lý đầy đủ cho mục đích audit

---

## 6. System Status Management

Hệ thống quản lý trạng thái được thiết kế để theo dõi và kiểm soát vòng đời của từng yêu cầu và tài sản thông qua các trạng thái được định nghĩa rõ ràng.

### Trạng thái Quy trình Cấp tài sản

**Cấp tài sản không ở kho (3 bước):**

| Sub-process | PIC | Action | Rq Status | Asset Status | Note |
|-------------|-----|---------|-----------|--------------|------|
| 1 Tạo yêu cầu | AMP | Lưu | Đang tạo | - | - |
| | AMP | Gửi | Chờ xác nhận | - | - |
| 2. Xác nhận | BU User | Từ chối | Từ chối | - | - |
| | BU User | Xác nhận | Đã xác nhận | Đang sử dụng | Đã xác nhận >>> Đã nhận tài sản |
| | BU User | Bổ sung thông tin | Bổ sung thông tin | - | - |
| 3. Bổ sung TT | AMP | Bổ sung thông tin | Chờ xác nhận | - | - |

**Cấp tài sản từ kho (6 bước):**

| Sub-process | PIC | Action | Rq Status | Asset Status | Note |
|-------------|-----|---------|-----------|--------------|------|
| 1. Tạo yêu cầu | AMP | Lưu | Đang tạo | - | - |
| | AMP | Gửi | Chờ xác nhận | - | - |
| 2. Phê duyệt | AM | Từ chối | Từ chối | - | - |
| | AM | Duyệt | Đã xác nhận | - | - |
| 3. Tạo yêu cầu | System | - | Đã xác nhận | Chờ xuất kho | - |
| 4. Xuất kho | WK | Từ chối | Từ chối | Từ chối | - |
| | WK | Đồng ý | Đã xác nhận | Chờ phê duyệt | - |
| 5. Phê duyệt | Warehouse Mgr. | Từ chối | Từ chối | Từ chối | - |
| | Warehouse Mgr. | Duyệt | Đã xác nhận | Chờ xác nhận | - |
| 6. Nhận hàng | BU User | Từ chối | Từ chối | Từ chối | - |
| | BU User | Xác nhận | Đã xác nhận | Đã nhận tài sản | Đang sử dụng |

### Trạng thái Quy trình Thanh lý

**Thanh lý bán trực tiếp (8 bước):**

| Sub-process | PIC | Action | Rq Status | Asset Status | Note |
|-------------|-----|---------|-----------|--------------|------|
| 1. Tạo yêu cầu | AMP | Lưu | Đang tạo | - | - |
| | AMP | Gửi | Chờ kiểm soát | - | - |
| 2. Kiểm soát | Checker | Từ chối | Từ chối | - | - |
| | Checker | Yêu cầu bổ sung thông tin | Bổ sung thông tin | - | - |
| | Checker | Duyệt | Chờ phê duyệt | - | - |

Các trạng thái được thiết kế để đảm bảo:
- Theo dõi được tiến trình xử lý của từng yêu cầu
- Phân quyền rõ ràng cho từng bước xử lý
- Đảm bảo tính nhất quán giữa trạng thái yêu cầu và trạng thái tài sản
- Hỗ trợ rollback và xử lý exception khi cần thiết

---

## 7. Task Assignment Matrix

Ma trận phân công task định nghĩa rõ ràng ai làm gì, khi nào và task xuất hiện ở tasklist nào trong hệ thống. Hệ thống có hai loại tasklist chính:

### Ma trận Phân công Task

| Sub-process | Action | Role | Tasklist Điều chuyển - Cần xử lý | Tasklist Điều chuyển - Đã xử lý | Tasklist Kho - Cần xử lý | Tasklist Kho - Đã xử lý | Ghi chú |
|------------|---------|------|:-------------------------------:|:------------------------------:|:------------------------:|:-----------------------:|---------|
| 2.3.1a Tạo yêu cầu điều chuyển | Lưu | Initiator | x | | | | |
| | Gửi | | | x | | | |
| 2.3.3a Phê duyệt yêu cầu điều chuyển | Từ chối | Initiator | x | | | | |
| | | BUH | | x | | | |
| | Duyệt | Initiator | | x | | | |
| | | BUH | | x | | | |
| | | AMP | x | | | | |
| | Bổ sung thông tin | Initiator | x | | | | |
| | | BUH | | x | | | |
| 5.2.2a Xác nhận yêu cầu điều chuyển | Từ chối | Initiator | x | | | | |
| | | BUH | | x | | | |
| | | AMP | | x | | | |
| | Bổ sung thông tin | Initiator | x | | | | |
| | | BUH | | x | | | |
| | | AMP | | x | | | |
| | Xác nhận & Yêu cầu nhập kho | Initiator | x | | | | |
| | | BUH | | x | | | |
| | | AMP | | x | x | | |
| | | WM | | | x | | |

### Quy tắc Tasklist

**Tasklist Điều chuyển:**
- Cần xử lý: Hiển thị các task đang chờ xử lý của user
- Đã xử lý: Lưu trữ lịch sử các task đã hoàn thành

**Tasklist Kho:**
- Cần xử lý: Các yêu cầu liên quan đến kho chờ xử lý
- Đã xử lý: Lịch sử xử lý các yêu cầu kho

**Lưu ý quan trọng:** Có vấn đề về quy trình xử lý tại bước phê duyệt yêu cầu nhập kho cần được giải quyết trong quá trình phát triển.

---

## 8. Assumptions & Constraints

### Giả định

- Người dùng đã được đào tạo về quy trình nghiệp vụ hiện tại
- Hệ thống [OMS](#3-stakeholders) và [EMS](#3-stakeholders) hoạt động ổn định và có API để tích hợp
- Cơ sở hạ tầng IT đủ để hỗ trợ các tính năng mới
- Dữ liệu hiện tại trong hệ thống FAM đã được làm sạch và chuẩn hóa

### Ràng buộc

- Không được thay đổi cấu trúc database hiện tại một cách đột ngột
- Phải đảm bảo tương thích với các module FAM hiện tại
- Thời gian phát triển bị giới hạn theo kế hoạch dự án
- Ngân sách dự án đã được phê duyệt và không thể vượt quá
- Phải tuân thủ các quy định về bảo mật và quyền riêng tư dữ liệu

### Rủi ro

- Tích hợp với hệ thống bên ngoài có thể gặp khó khăn về kỹ thuật
- Dữ liệu từ [OMS](#3-stakeholders)/[EMS](#3-stakeholders) có thể không nhất quán
- Người dùng có thể cần thời gian để làm quen với giao diện mới
- Hiệu năng hệ thống có thể bị ảnh hưởng với khối lượng dữ liệu lớn

---

## 9. Dependencies

### Phụ thuộc Hệ thống

**Hệ thống OMS (Organization Management System):**
- Cung cấp dữ liệu về cơ cấu tổ chức, thông tin kho
- Hỗ trợ tự động đồng bộ khi orgchart thay đổi
- API để lấy thông tin địa chỉ kho và quản lý kho

**Hệ thống EMS (Employee Management System):**
- Cung cấp thông tin nhân viên và chức danh PO
- Đồng bộ thông tin thời gian đưa vào sử dụng và bảo hành
- Cập nhật dữ liệu tự động khi có thay đổi trong EMS

**Hệ thống ITSM:**
- Hỗ trợ module sửa chữa tài sản
- Xử lý các yêu cầu kỹ thuật từ FAM
- Cung cấp trạng thái xử lý yêu cầu sửa chữa

### Phụ thuộc Quy trình

- [Module dashboard](#41-asset-dashboard-module) phụ thuộc vào việc hoàn thành làm sạch dữ liệu
- [Module kho](#42-warehouse-management-module) cần hoàn thành trước các tính năng cấp tài sản
- Tích hợp OMS/EMS phải hoàn thành trước khi triển khai các tính năng tự động đồng bộ
- Module sửa chữa phụ thuộc vào việc tích hợp thành công với ITSM

### Phụ thuộc Dữ liệu

- Dữ liệu master về kho và tài sản phải được chuẩn hóa
- Thông tin phân quyền người dùng cần được cập nhật đầy đủ
- Cấu hình workflow phải được thiết lập trước khi go-live

---

## 10. Acceptance Criteria

### Tiêu chí Chức năng

**Dashboard Tài sản:**
- [ ] Hiển thị đúng 4 thông số tổng quan như đã định nghĩa
- [ ] Tất cả 5 loại biểu đồ hoạt động bình thường với dữ liệu thực
- [ ] Bộ lọc hoạt động chính xác và hiển thị kết quả real-time
- [ ] Tính năng export Excel hoạt động với dữ liệu được format đúng
- [ ] Tương thác click-through đến các module liên quan hoạt động

**Module Kho:**
- [ ] Tất cả quy trình nhập/xuất kho hoạt động end-to-end
- [ ] Cơ chế lock/unlock tài sản hoạt động chính xác
- [ ] Tự động tạo số yêu cầu theo đúng format đã định nghĩa
- [ ] Email notification gửi đúng người đúng thời điểm
- [ ] Tasklist cập nhật chính xác theo ma trận đã định nghĩa

**Tích hợp Hệ thống:**
- [ ] Đồng bộ dữ liệu từ [OMS](#3-stakeholders) và [EMS](#3-stakeholders) thành công
- [ ] Tự động cập nhật khi có thay đổi từ hệ thống bên ngoài
- [ ] Xử lý lỗi gracefully khi hệ thống bên ngoài không khả dụng

### Tiêu chí Phi chức năng

**Hiệu năng:**
- [ ] Thời gian response của dashboard < 3 giây với 1000 tài sản
- [ ] Quy trình nhập/xuất kho hoàn thành trong < 30 giây
- [ ] Hệ thống hỗ trợ đồng thời 50 người dùng

**Bảo mật:**
- [ ] Tất cả API calls được authenticate và authorize
- [ ] Dữ liệu nhạy cảm được mã hóa trong database
- [ ] Audit log ghi lại đầy đủ các thao tác quan trọng

**Khả năng sử dụng:**
- [ ] Giao diện trực quan, không cần training cho người dùng hiện tại
- [ ] Hỗ trợ các trình duyệt phổ biến (Chrome, Edge, Firefox)
- [ ] Responsive design hoạt động trên tablet

**Độ tin cậy:**
- [ ] Hệ thống có uptime > 99%
- [ ] Có cơ chế backup và recovery cho dữ liệu quan trọng
- [ ] Xử lý exception không làm crash toàn hệ thống

### Tiêu chí User Acceptance

- [ ] Người dùng có thể hoàn thành các tác vụ nghiệp vụ chính trong thời gian ngắn hơn so với hệ thống cũ
- [ ] Báo cáo từ dashboard cung cấp insight hữu ích cho việc ra quyết định
- [ ] Quy trình phê duyệt mới không tạo ra bottleneck so với quy trình cũ
- [ ] Người dùng hài lòng với trải nghiệm sử dụng tổng thể (>80% positive feedback)

---

## 11. Glossary

| Thuật ngữ | Định nghĩa |
|-----------|------------|
| **FAM** | Fixed Asset Management - Hệ thống quản lý tài sản cố định |
| **AMP** | Asset Management Personnel - Nhân viên quản lý tài sản |
| **AM** | Asset Manager - Quản lý tài sản |
| **BU User** | Business Unit User - Người dùng đơn vị kinh doanh |
| **BU Head** | Business Unit Head - Trưởng đơn vị kinh doanh |
| **WK** | Warehouse Keeper - Thủ kho |
| **WM** | Warehouse Manager - Quản lý kho |
| **OMS** | Organization Management System - Hệ thống quản lý tổ chức |
| **EMS** | Employee Management System - Hệ thống quản lý nhân sự |
| **ITSM** | IT Service Management - Hệ thống quản lý dịch vụ IT |
| **RQ** | Request - Yêu cầu |
| **TS** | Tài sản |
| **PO** | Purchase Order - Đơn hàng mua |
| **CAT1** | Category 1 - Phân loại tài sản cấp 1 |
| **NK.YY.xxxx** | Format số yêu cầu nhập kho (NK = Nhập Kho, YY = năm, xxxx = số thứ tự) |
| **XK.YY.xxxx** | Format số yêu cầu xuất kho (XK = Xuất Kho, YY = năm, xxxx = số thứ tự) |
| **CK.YY.xxxx** | Format số yêu cầu chuyển kho (CK = Chuyển Kho, YY = năm, xxxx = số thứ tự) |
| **Lock Asset** | Khóa tài sản để tránh xung đột trong quá trình xử lý yêu cầu |
| **Unlock Asset** | Mở khóa tài sản sau khi hoàn thành hoặc hủy yêu cầu |
| **Tasklist** | Danh sách công việc cần xử lý của từng vai trò người dùng |
| **Dashboard** | Bảng điều khiển hiển thị thông tin tổng quan |
| **Visualization** | Trực quan hóa dữ liệu thông qua biểu đồ |
| **Sunburst Chart** | Biểu đồ hình tròn phân cấp |
| **Workflow** | Luồng công việc |
| **Approver** | Người phê duyệt |
| **Checker** | Người kiểm soát |
| **Enhancement** | Cải tiến, nâng cấp tính năng hiện có |
| **Integration** | Tích hợp hệ thống |
| **API** | Application Programming Interface - Giao diện lập trình ứng dụng |

