# Tài liệu Yêu cầu Nghiệp vụ - Hệ thống FAM Upgrade Wave 4

## 1. Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Project Scope & Objectives](#2-project-scope-objectives)
3. [Stakeholders](#3-stakeholders)
4. [Business Requirements](#4-business-requirements)
   - 4.1. [Asset Dashboard Module](#41-asset-dashboard-module)
   - 4.2. [Warehouse Management Module](#42-warehouse-management-module)
     - 4.2.1. [Create Warehouse Intake Request](#421-create-warehouse-intake-request)
     - 4.2.2. [Approve Warehouse Entry Request](#422-approve-warehouse-entry-request)
     - 4.2.3. [Warehouse Receipt Confirmation](#423-warehouse-receipt-confirmation)
     - 4.2.4. [Manual Warehouse Intake Process](#424-manual-warehouse-intake-process)
     - 4.2.5. [Cancel Warehouse Request](#425-cancel-warehouse-request)
     - 4.2.6. [Asset Allocation from Warehouse](#426-asset-allocation-from-warehouse)
     - 4.2.7. [Cancel Warehouse Export Request](#427-cancel-warehouse-export-request)
     - 4.2.8. [Inter-warehouse Transfer](#428-inter-warehouse-transfer)
5. [Assumptions & Constraints](#5-assumptions-constraints)
6. [Dependencies](#6-dependencies)
7. [Acceptance Criteria](#7-acceptance-criteria)
8. [Glossary](#8-glossary)

## 1. Executive Summary

Dự án nâng cấp hệ thống FAM (Fixed Asset Management) đợt 4 bao gồm 11 yêu cầu chính được phân thành hai nhóm: Enhancement (cải tiến tính năng hiện có) và New launch (tính năng mới). Đây là dự án quan trọng nhằm nâng cao hiệu quả quản lý tài sản và tối ưu hóa quy trình nghiệp vụ.

Các sản phẩm chính bao gồm [module dashboard tài sản](#41-asset-dashboard-module) với khả năng trực quan hóa dữ liệu, [module quản lý kho toàn diện](#42-warehouse-management-module) hỗ trợ xuất-nhập kho tự động, và module sửa chữa tài sản tích hợp với hệ thống ITSM. Ngoài ra, dự án còn cải tiến các tính năng hiện có như quản lý hiển thị tài sản vô hiệu hóa, tối ưu hóa quy trình cấp tài sản và tự động đồng bộ dữ liệu với các hệ thống OMS và EMS.

Các tính năng Enhancement có mức độ ưu tiên 1-3, trong khi module kho mới có mức ưu tiên cao nhất (1) và module sửa chữa có mức ưu tiên 4. Dự án sẽ cải thiện đáng kể trải nghiệm người dùng và khả năng quản trị hệ thống.

## 2. Project Scope & Objectives

### Trong phạm vi dự án:
- Phát triển dashboard tài sản với khả năng trực quan hóa và tùy biến theo nhiều tiêu chí
- Xây dựng module quản lý kho hoàn chỉnh hỗ trợ các quy trình xuất-nhập kho
- Tích hợp tự động với các hệ thống OMS, EMS, ITSM
- Cải tiến giao diện và tối ưu hóa quy trình cấp tài sản hiện có
- Phát triển module sửa chữa tài sản với liên kết sang hệ thống bên ngoài

### Ngoài phạm vi dự án:
- Thay đổi cấu trúc cơ sở dữ liệu cốt lõi hiện có
- Tích hợp với các hệ thống khác ngoài OMS, EMS, ITSM
- Phát triển ứng dụng mobile

### Mục tiêu dự án:
- Nâng cao hiệu quả quản lý tài sản thông qua tự động hóa
- Cải thiện trải nghiệm người dùng với giao diện trực quan
- Tăng cường khả năng kiểm soát và theo dõi quy trình nghiệp vụ
- Đảm bảo tính nhất quán dữ liệu giữa các hệ thống

## 3. Stakeholders

### Vai trò trong hệ thống:
- **AMP (Asset Management Personnel)**: Nhân viên quản lý tài sản
- **AM (Asset Manager)**: Quản lý tài sản cấp cao
- **WM (Warehouse Manager)**: Quản lý kho
- **WK (Warehouse Keeper)**: Thủ kho
- **BU User (Business Unit User)**: Người dùng đơn vị kinh doanh
- **BU Manager**: Quản lý đơn vị kinh doanh
- **Checker**: Người kiểm soát
- **Approver**: Người phê duyệt

### Hệ thống liên quan:
- **OMS (Organization Management System)**: Hệ thống quản lý tổ chức
- **EMS (Equipment Management System)**: Hệ thống quản lý thiết bị
- **ITSM (IT Service Management)**: Hệ thống quản lý dịch vụ IT
- **Cổng hỗ trợ chi nhánh**: Trên intranet

## 4. Business Requirements

### 4.1. Asset Dashboard Module

Dashboard tài sản cung cấp giao diện tổng quan để trực quan hóa và quản lý thông tin tài sản của tổ chức. Hệ thống hiển thị thông tin tài sản theo nhiều khía cạnh khác nhau như phòng ban, trạng thái, thời gian sử dụng và biến động theo thời gian, hỗ trợ đưa ra quyết định nhanh chóng và hiệu quả.

Dashboard bao gồm các thành phần chính: dashboard tổng quan với 4 chỉ số KPI chính, các biểu đồ tương tác đa dạng, bộ lọc dữ liệu theo nhiều tiêu chí và tính năng xuất dữ liệu ra Excel. Đặc biệt, dashboard loại trừ các tài sản đã thanh lý và vô hiệu hóa khỏi các phép tính chính để đảm bảo tính chính xác của dữ liệu báo cáo.

#### Đặc tả kỹ thuật dashboard:

**Chỉ số KPI chính:**

| STT | Chỉ số | Công thức tính toán | Ghi chú |
|-----|--------|-------------------|---------|
| 1 | Total assets | Count số lượng (All tài sản - Đã thanh lý - Vô hiệu hóa) | |
| 2 | Total value | Sum nguyên giá (All tài sản - Đã thanh lý - Vô hiệu hóa) | |
| 3 | Warranty status | Tỷ lệ % theo số lượng tài sản còn hạn bảo hành/(All tài sản - Vô hiệu hóa - Đã thanh lý) | |
| 4 | Utilization rate | Tỷ lệ % theo số lượng tài sản có trạng thái đang sử dụng/(All tài sản - Vô hiệu hóa - Đã thanh lý) | |

**Bộ lọc dữ liệu:**

| STT | Tiêu chí lọc | Loại dữ liệu | Ghi chú |
|-----|-------------|-------------|---------|
| 1 | Vùng | LOV | |
| 2 | Đơn vị sử dụng | LOV đồng bộ từ OMS | |
| 3 | CAT 1 | LOV | |
| 4 | Group name | LOV | |
| 5 | Asset status | LOV asset status | Không bao gồm Đã thanh lý, Vô hiệu hóa |

**Specifications biểu đồ:**

| Biểu đồ | Dữ liệu hiển thị | Loại biểu đồ | Ghi chú |
|---------|------------------|-------------|---------|
| Asset Distribution - Cơ cấu nhóm tài sản theo trạng thái | Nguyên giá | Sunburst (Vòng trong: Nhóm IT/ADM/CMD, Vòng ngoài: Trạng thái) | Khi Hover hiển thị số lượng và giá trị |
| Asset Distribution - Cơ cấu nhóm tài sản theo Vùng/Đơn vị | Nguyên giá | Stacked Column | |
| Asset Value by Group Name | Nguyên giá | Column | |
| Asset Fluctuation Over Time (Month/Year) | Nguyên giá | Line | |
| Asset by Time in Use | Số lượng | Scatter | |

### 4.2. Warehouse Management Module

Module quản lý kho là tính năng mới quan trọng nhất với mức ưu tiên cao nhất trong dự án. Module này hỗ trợ toàn bộ quy trình xuất-nhập kho tài sản, tiếp nhận yêu cầu từ các quy trình cấp, thanh lý, và điều chuyển với mức độ tự động hóa cao.

Hệ thống được thiết kế với các quy trình chính bao gồm: [tạo yêu cầu nhập kho tự động](#421-create-warehouse-intake-request), [phê duyệt yêu cầu nhập kho](#422-approve-warehouse-entry-request), [xác nhận nhập kho](#423-warehouse-receipt-confirmation), [nhập kho thủ công](#424-manual-warehouse-intake-process), [hủy yêu cầu nhập/xuất kho](#425-cancel-warehouse-request), [cấp tài sản từ kho](#426-asset-allocation-from-warehouse), và [điều chuyển giữa các kho](#428-inter-warehouse-transfer).

Đặc điểm nổi bật của thiết kế là việc tự động hóa nhiều bước trong quy trình, đặc biệt là hệ thống tự động tạo yêu cầu nhập/xuất kho thay cho người dùng AMP. Các quy trình được thiết kế với luồng phê duyệt rõ ràng, có cơ chế từ chối và quay lại bước trước, đồng thời tích hợp chặt chẽ giữa các module.

#### 4.2.1. Create Warehouse Intake Request

![Giao diện tạo yêu cầu nhập kho](images/5_1_1a_B5_image1.png)

##### 4.2.1.1. Thông số kỹ thuật giao diện người dùng

Quy trình tạo yêu cầu nhập kho được khởi tạo tự động khi có yêu cầu chuyển kho được xác nhận. Hệ thống sẽ kế thừa toàn bộ thông tin từ yêu cầu chuyển kho bao gồm thông tin tài sản, chi tiết kho đích và các tệp đính kèm.

Người dùng AMP có thể tìm kiếm yêu cầu theo nhiều tiêu chí: mã yêu cầu, tiêu đề, người xử lý, loại điều chuyển, trạng thái, người tạo, người đề xuất, ngày tạo, đơn vị điều chuyển và đơn vị nhận điều chuyển. Giao diện hiển thị đầy đủ thông tin tài sản bao gồm thông tin bảo hành, người sử dụng, vị trí đặt tài sản và cho phép đính kèm hồ sơ với quản lý quyền truy cập file.

Khi AMP xác nhận yêu cầu, hệ thống sẽ tự động tạo yêu cầu nhập kho tương ứng với mã theo format "NK.YY.xxxx", cập nhật trạng thái các yêu cầu liên quan, và gửi thông báo email cho warehouse manager theo template định sẵn.

##### 4.2.1.2. Thông số kỹ thuật chi tiết

**Đặc tả trường thông tin chung:**

| Trường | Operator | Action | Tên trường | M/O | Kiểu | Editable | Max length | Format | Default | Quy tắc dữ liệu |
|--------|----------|--------|------------|-----|------|----------|------------|--------|---------|-----------------|
| Số yêu cầu | System | Display | Số yêu cầu | M | Text | N | 50 | NK.YY.xxxx | - | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| Ngày tạo | System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | - |
| Tiêu đề | System | Display | Tiêu đề | M | Text | N | 150 | - | - | = Tiêu đề RQ điều chuyển |

**Đặc tả thông tin kho nhập:**

| Trường | Operator | Action | Tên trường | M/O | Kiểu | Editable | Max length | Data source | Quy tắc dữ liệu |
|--------|----------|--------|------------|-----|------|----------|------------|-------------|-----------------|
| Tên kho | System | Display | Tên kho | M | List | N | 50 | - | = Kho trong RQ điều chuyển |
| Địa chỉ kho | System | Display | Địa chỉ kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| Quản lý kho | System | Display | Quản lý kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho (Tên \| Phòng ban \| Email) |

**Đặc tả thông tin đầu mối giao hàng:**

| Trường | Operator | Action | Tên trường | M/O | Kiểu | Editable | Max length | Quy tắc dữ liệu |
|--------|----------|--------|------------|-----|------|----------|------------|-----------------|
| Đầu mối | User | Input | Đầu mối | M | Text | N | 50 | = Đầu mối giao hàng trong RQ điều chuyển |
| Số điện thoại | User | Input | Số điện thoại | M | Number | N | 52 | - |
| Thời gian bàn giao | User | Input | Thời gian bàn giao | O | Date | N | 50 | - |
| Ghi chú | User | Input | Ghi chú | M | Text | N | 150 | = SỐ RQ điều chuyển |

**Cập nhật trạng thái và tasklist:**

| Đối tượng | Action | Trạng thái/Giá trị |
|-----------|--------|--------------------|
| Trạng thái RQ điều chuyển | Update | Đã xác nhận |
| Trạng thái RQ nhập kho | Update | Chờ phê duyệt |
| Tasklist AMP | Update | Đã xử lý |
| Tasklist WM | Update | Cần xử lý |
| Email notification | Send | Gửi cho Warehouse Manager |

#### 4.2.2. Approve Warehouse Entry Request

![Giao diện phê duyệt yêu cầu nhập kho](images/5_1_2a_B6_image2.png)

##### 4.2.2.1. Thông số kỹ thuật giao diện người dùng

Warehouse Manager có thể tìm kiếm và phê duyệt các yêu cầu nhập kho thông qua giao diện chuyên biệt. Hệ thống hiển thị đầy đủ thông tin về yêu cầu bao gồm thông tin tài sản, kho nhập, đầu mối giao hàng, hồ sơ đính kèm và lịch sử xử lý.

Quy trình phê duyệt bao gồm 13 bước chính từ tìm kiếm yêu cầu đến thông báo kết quả. Warehouse Manager có thể từ chối yêu cầu (cần nhập lý do) hoặc phê duyệt để chuyển sang giai đoạn chờ nhập kho. Khi từ chối, hệ thống sẽ unlock tài sản và thông báo cho AMP. Khi phê duyệt, hệ thống chuyển trạng thái thành "Chờ nhập kho" và cập nhật tasklist cho Warehouse Keeper.

##### 4.2.2.2. Thông số kỹ thuật chi tiết

**Thông tin tìm kiếm yêu cầu:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|--------|---------------|-----|------------|----------|------------|
| User | Input | Số yêu cầu | O | Text | Y | 20 |
| User | Input | Ngày tạo | O | Date | Y | 20 |
| User | Input | Tiêu đề | O | Text | Y | 150 |
| User | Select | Người tạo | O | List | Y | 20 |
| User | Select | Trạng thái yêu cầu | O | List | Y | 20 |
| User | Select | Người xử lý | O | List | Y | 20 |
| User | Input | Ngày xác nhận | O | Date | Y | 20 |

**Danh sách tài sản nhập kho:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Data rule |
|----------|--------|---------------|-----|------------|----------|-----------|
| System | Display | Mã tài sản | M |  | N | Hiển thị mặc định |
| System | Display | Tên Tài sản | M |  | N | Hiển thị mặc định |
| System | Display | Mô tả TS | M |  | N | Hiển thị mặc định |
| System | Display | Trạng thái TS | M |  | N | Hiển thị mặc định |
| System | Display | Phân nhóm TS (group name) | M |  | N | Hiển thị mặc định |
| System | Display | Nhóm TS (CAT1) | M |  | N | Hiển thị mặc định |
| System | Display | Số PO | M |  | N | Hiển thị mặc định |
| System | Display | Tên nhà cung cấp | O |  | N | Ẩn hiện tùy biến |
| System | Display | Nguyên giá TS (VAT incl) | M |  | N | Ẩn hiện tùy biến |
| System | Display | Mã TS liên quan | O |  | N | Ẩn hiện tùy biến |
| System | Display | Mô tả TS liên quan | O |  | N | Ẩn hiện tùy biến |
| System | Display | Tên người sử dụng | M |  | N | Hiển thị mặc định |
| System | Display | Tên đơn vị | M |  | N | Hiển thị mặc định |
| System | Display | Mã nhân viên | M |  | N | Ẩn hiện tùy biến |
| System | Display | Đơn vị sử dụng cha | M |  | N | Hiển thị mặc định |
| System | Display | Email nhân viên | M |  | N | Ẩn hiện tùy biến |

#### 4.2.3. Warehouse Receipt Confirmation

![Giao diện xác nhận nhập kho](images/5.1.3a_B5)

##### 4.2.3.1. Thông số kỹ thuật giao diện người dùng

Warehouse Keeper thực hiện xác nhận nhập kho thông qua giao diện chuyên biệt cho phép tìm kiếm yêu cầu, xem chi tiết và đưa ra quyết định cuối cùng về việc nhập kho tài sản. Giao diện hiển thị đầy đủ thông tin tài sản với 26 trường thông tin từ cơ bản đến chi tiết, bao gồm khả năng tùy biến hiển thị/ẩn một số trường.

Quy trình xác nhận bao gồm 14 bước chính từ tìm kiếm đến thông báo hoàn thành. Nếu từ chối, hệ thống sẽ unlock tài sản và cập nhật trạng thái thành "Từ chối". Nếu xác nhận, hệ thống sẽ cập nhật thông tin tài sản (đơn vị sử dụng = null, kho = kho chuyển về), thay đổi trạng thái thành "Đã nhập kho" và tự động cập nhật "Ngày bắt đầu sử dụng" nếu giá trị hiện tại là N/A.

##### 4.2.3.2. Thông số kỹ thuật chi tiết

**Tìm kiếm yêu cầu:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|--------|---------------|-----|------------|----------|------------|
| User | Input | Số yêu cầu | O | Text | Y | 20 |
| User | Input | Ngày tạo | O | Date | Y | 20 |
| User | Input | Tiêu đề | O | Text | Y | 150 |
| User | Select | Người tạo | O | List | Y | 20 |
| User | Select | Trạng thái yêu cầu | O | List | Y | 20 |
| User | Select | Người xử lý | O | List | Y | 20 |
| User | Input | Ngày xác nhận | O | Date | Y | 20 |

**Hiển thị danh sách tài sản:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Data rule |
|----------|--------|---------------|-----|------------|----------|------------|-----------|
| System | Display | Mã tài sản | M | - | N | - | Hiển thị mặc định |
| System | Display | Tên Tài sản | M | - | N | - | Hiển thị mặc định |
| System | Display | Mô tả TS | M | - | N | - | Hiển thị mặc định |
| System | Display | Trạng thái TS | M | - | N | - | Hiển thị mặc định |
| System | Display | Phân nhóm TS (group name) | M | - | N | - | Hiển thị mặc định |
| System | Display | Nhóm TS (CAT1) | M | - | N | - | Hiển thị mặc định |
| System | Display | Số PO | M | - | N | - | Hiển thị mặc định |
| System | Display | Tên nhà cung cấp | O | - | N | - | Ẩn hiện tùy biến |
| System | Display | Nguyên giá TS (VAT incl) | M | - | N | - | Ẩn hiện tùy biến |
| System | Display | Mã TS liên quan | O | - | N | - | Ẩn hiện tùy biến |
| System | Display | Mô tả TS liên quan | O | - | N | - | Ẩn hiện tùy biến |
| System | Display | Tên người sử dụng | M | - | N | - | Hiển thị mặc định |
| System | Display | Tên đơn vị | M | - | N | - | Hiển thị mặc định |
| System | Display | Mã nhân viên | M | - | N | - | Ẩn hiện tùy biến |
| System | Display | Đơn vị sử dụng cha | M | - | N | - | Hiển thị mặc định |
| System | Display | Email nhân viên | M | - | N | - | Ẩn hiện tùy biến |

**Thông tin kho và đầu mối:**

| Tab/section | Operator | Action | Field name VN | M/O | Field type | Max length | Data source | Data rule |
|-------------|----------|--------|---------------|-----|------------|------------|-------------|-----------|
| Thông tin kho nhập | System | Display | Tên kho | M | List | 50 | - | - |
| Thông tin kho nhập | System | Display | Địa chỉ kho | M | Text | 50 | OMS | Tự động nhận diện theo Tên kho |

#### 4.2.4. Manual Warehouse Intake Process

##### 4.2.4.1. Thông số kỹ thuật giao diện người dùng

![Giao diện tạo yêu cầu nhập kho thủ công](images/5_2_1a_B5_image4.png)

Chức năng nhập kho thủ công cho phép người dùng tạo yêu cầu nhập tài sản vào kho một cách thủ công thay vì thông qua quy trình tự động. Giao diện được chia thành các phần chính: thông tin chung của yêu cầu, phần tìm kiếm và chọn tài sản cần nhập kho, thông tin kho đích, thông tin đầu mối giao hàng, và phần đính kèm hồ sơ.

Hệ thống có cơ chế cảnh báo khi tài sản đã bị khóa trong một yêu cầu khác đang xử lý. Quy trình bao gồm 5 bước tự động: tạo yêu cầu, khóa tài sản để tránh xung đột, cập nhật trạng thái thành "Chờ phê duyệt", cập nhật tasklist cho Warehouse Manager, và gửi thông báo email.

##### 4.2.4.2. Thông số kỹ thuật chi tiết

**Thông tin trường dữ liệu trong phần tìm kiếm tài sản:**

| Tab/Section | Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Format | Default value | Data rule |
|------------|----------|---------|---------------|-----|------------|----------|------------|--------|---------------|-----------|
| Thông tin chung | System | Display | Số yêu cầu | M | Text | N | 50 | NK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| | System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| | User | Input | Tiêu đề | O | Text | Y | 150 | | | |
| | User | Select | Thêm tài sản | M | Button | N | | | | |
| Tìm kiếm tài sản | User | Input | Mã tài sản | O | Text | N | 20 | | | |
| | User | Input | Tên tài sản | O | Text | Y | 20 | | | |
| | User | Select | Phân loại tài sản | O | List | N | 20 | | | |
| | User | Select | Nhóm tài sản | O | List | N | 20 | | | |
| | User | Input | PO number | O | Text | Y | 20 | | | |
| | User | Select | Trạng thái TS | O | List | N | 50 | | | |
| | User | Select | Tên nhà cung cấp | O | List | N | 50 | | | |
| | User | Input | Tên kho | O | List | Y | 50 | | | |
| | User | Select | Vị trí đặt tài sản | O | Text | N | 100 | | | |

**Thông tin kho và đầu mối giao hàng:**

| Tab/Section | Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Data source | Data rule |
|------------|----------|---------|---------------|-----|------------|----------|------------|-------------|-----------|
| Thông tin kho nhập | System/User | Display/Search/Select | Tên kho | M | List | N | 50 | | |
| | System | Display | Địa chỉ kho | M | Text | Y | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| | System | Display | Quản lý kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho (Tên \| Phòng ban \| Email) |
| Thông tin đầu mối giao hàng | User | Input | Đầu mối | M | Text | Y | 50 | | |
| | User | Input | Số điện thoại | M | Number | Y | 52 | | |
| | User | Input | Thời gian bàn giao | O | Date | Y | 50 | | |
| Ghi chú | User | Input | Ghi chú | M | Text | Y | 150 | | |

Quy trình phê duyệt nhập kho thủ công tuân theo cùng nguyên tắc với [quy trình phê duyệt nhập kho tự động](#422-approve-warehouse-entry-request), nhưng với khả năng tùy chọn tài sản linh hoạt hơn. Sau khi được phê duyệt, quy trình chuyển sang [giai đoạn xác nhận nhập kho](#423-warehouse-receipt-confirmation).

#### 4.2.5. Cancel Warehouse Request

##### 4.2.5.1. Thông số kỹ thuật giao diện người dùng

![Giao diện hủy yêu cầu nhập kho](images/5_3_1a_B5_image7.png)

Chức năng hủy yêu cầu nhập kho cho phép hủy bỏ các yêu cầu đã được tạo trước đó với điều kiện yêu cầu chưa có trạng thái "Đã nhập kho". Giao diện tương tự như các chức năng khác với khả năng tìm kiếm, xem chi tiết và thực hiện hành động hủy.

Khi hủy yêu cầu xuất kho, hệ thống phải xem xét mối quan hệ với yêu cầu liên quan. Đối với yêu cầu liên kết với thanh lý, nút "Từ chối" sẽ bị ẩn và trạng thái tài sản sẽ được trả về trạng thái trước khi thanh lý. Hệ thống cũng tự động hủy các yêu cầu liên quan khác như yêu cầu cấp tài sản hoặc thanh lý khi hủy yêu cầu xuất kho.

##### 4.2.5.2. Thông số kỹ thuật chi tiết

**Thông tin tìm kiếm yêu cầu:**

| Trường | Loại tác vụ | Kiểu dữ liệu | Bắt buộc | Độ dài | Chỉnh sửa |
|--------|-------------|--------------|----------|---------|-----------|
| Số yêu cầu | Input | Text | O | 20 | Y |
| Ngày tạo | Input | Date | O | 20 | Y |
| Tiêu đề | Input | Text | O | 150 | Y |
| Người tạo | Select | List | O | 20 | Y |
| Trạng thái yêu cầu | Select | List | O | 20 | Y |
| Người xử lý | Select | List | O | 20 | Y |
| Ngày xác nhận | Input | Date | O | 20 | Y |

**Thông tin kho nhập:**

| Trường | Kiểu dữ liệu | Bắt buộc | Độ dài | Nguồn dữ liệu | Quy tắc |
|--------|--------------|----------|---------|---------------|---------|
| Tên kho | List | M | 50 | - | Y |
| Địa chỉ kho | Text | M | 50 | OMS | Tự động nhận diện theo Tên kho |
| Quản lý kho | Text | M | 50 | OMS | Hiển thị: Tên \| Phòng ban \| Email |

**Cập nhật trạng thái hệ thống:**

| Đối tượng | Hành động | Trạng thái mới | Ghi chú |
|-----------|-----------|----------------|---------|
| Trạng thái lock tài sản | Update | Unlock | Asset có thể được pickup cho request khác |
| RQ điều chuyển | Update | Đã hủy | - |
| RQ nhập kho | Update | Đã hủy | - |
| Tasklist WM | Update | Đã xử lý | - |
| Tasklist AMP/BU user | Update | Cần xử lý | - |

#### 4.2.6. Asset Allocation from Warehouse

##### 4.2.6.1. Thông số kỹ thuật giao diện người dùng

![Giao diện phê duyệt cấp tài sản](images/5.4.0a)

Quy trình cấp tài sản từ kho bắt đầu với việc Asset Manager phê duyệt yêu cầu cấp tài sản. Sau đó, hệ thống sẽ tự động tạo yêu cầu xuất kho tương ứng để thực hiện việc lấy tài sản từ kho. Quy trình này được thiết kế để đảm bảo tính minh bạch và kiểm soát trong việc cấp phát tài sản.

Giao diện phê duyệt cho phép Asset Manager tìm kiếm, xem chi tiết và đưa ra quyết định phê duyệt hoặc từ chối. Khi phê duyệt, hệ thống sẽ chuyển sang quy trình [tạo yêu cầu xuất kho](#4261-create-export-request), sau đó là [phê duyệt xuất kho](#4262-approve-export-request) và cuối cùng là [nhận tài sản](#4263-receive-assets).

##### 4.2.6.2. Thông số kỹ thuật chi tiết

**Tìm kiếm yêu cầu:**

| Trường | Loại thao tác | Kiểu dữ liệu | Bắt buộc | Có thể chỉnh sửa | Độ dài tối đa |
|--------|---------------|--------------|----------|------------------|---------------|
| Mã yêu cầu | Input | Text | M | Y | 20 |
| Tiêu đề | Input | Text | M | Y | 150 |
| Người tạo | Select | List | M | Y | 20 |
| Trạng thái | Select | List | M | Y | 20 |
| Ngày tạo | Input | Date | M | Y | 20 |
| Loại cấp tài sản | Select | List | M | Y | 100 |
| Người xử lý | Select | List | M | Y | 20 |
| Ngày xác nhận | Input | Date | M | Y | 20 |

**Thông tin tài sản cấp (hiển thị):**

| Trường | Bắt buộc | Quy tắc hiển thị |
|--------|----------|------------------|
| Mã tài sản | M | Hiển thị mặc định |
| Tên Tài sản | M | Hiển thị mặc định |
| Mô tả TS | M | Hiển thị mặc định |
| Trạng thái TS | M | Hiển thị mặc định |
| Phân nhóm TS (group name) | M | Hiển thị mặc định |
| Nhóm TS (CAT1) | M | Hiển thị mặc định |
| Số PO | M | Hiển thị mặc định |
| Tên nhà cung cấp | O | Ẩn hiện tùy biến |
| Nguyên giá TS (VAT incl) | M | Ẩn hiện tùy biến |
| Mã TS liên quan | O | Ẩn hiện tùy biến |
| Tên người sử dụng | M | Hiển thị mặc định |
| Tên đơn vị | M | Hiển thị mặc định |
| Mã nhân viên | M | Ẩn hiện tùy biến |
| Email nhân viên | M | Ẩn hiện tùy biến |
| Thông tin bảo hành | O | Ẩn hiện tùy biến |

###### 4.2.6.1. Create Export Request

![Giao diện tạo yêu cầu xuất kho](images/5_4_1a__B5_image9.png)

Hệ thống tự động tạo yêu cầu xuất kho dựa trên thông tin từ phiếu cấp/thanh lý đã được phê duyệt. Form yêu cầu xuất kho bao gồm thông tin chung, danh sách tài sản xuất kho, thông tin kho xuất, thông tin đầu mối nhận hàng, ghi chú và hồ sơ đính kèm.

**Đặc tả trường dữ liệu:**

| Section | Operator | Action | Field Name (VN) | M/O | Field Type | Editable | Max Length | Format | Default Value | Data Rule |
|---------|----------|---------|-----------------|-----|------------|----------|------------|--------|---------------|-----------|
| **Thông tin chung** ||||||||||| 
| | System | Display | Số yêu cầu | M | Text | N | 50 | XK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 |
| | System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| | System | Input | Tiêu đề | O | Text | Y | 150 | | | =Tiêu đề RQ Cấp/Thanh lý |
| **DS tài sản xuất kho** ||||||||||| 
| | System | Display | Mã tài sản | M | | N | | | | Hiển thị mặc định |
| | System | Display | Tên Tài sản | M | | N | | | | Hiển thị mặc định |
| | System | Display | Mô tả TS | M | | N | | | | Hiển thị mặc định |
| | System | Display | Trạng thái TS | M | | N | | | | Hiển thị mặc định |
| | System | Display | Tên người sử dụng | M | | N | | | | Hiển thị mặc định |
| | System | Display | Tên đơn vị | M | | N | | | | Hiển thị mặc định |
| | System | Display | Tên nhà cung cấp | O | | N | | | | Ẩn hiện tùy biến |
| | System | Display | Nguyên giá TS (VAT incl) | M | | N | | | | Ẩn hiện tùy biến |
| **Thông tin kho xuất** ||||||||||| 
| | System/User | Display/Search/Select | Tên kho | M | List | N | 50 | | | = Thông tin kho trên RQ cấp/Thanh lý |
| | System | Display | Địa chỉ kho | M | Text | Y | 50 | | | |
| | System | Display | Quản lý kho | M | Text | N | 50 | | | |
| **Thông tin đầu mối nhận hàng** ||||||||||| 
| | User | Input | Đầu mối | M | Text | Y | 50 | | | |
| | User | Input | Số điện thoại | M | Number | Y | 52 | | | |
| | User | Input | Thời gian bàn giao | O | Date | Y | 50 | | | |
| **Khác** ||||||||||| 
| Ghi chú | User | Input | Ghi chú | M | Text | Y | 150 | | | = Mã RQ cấp/thanh lý |
| Hồ sơ đính kèm | User | Select | Thêm | M | Button | N | | | | |

###### 4.2.6.2. Approve Export Request

![Giao diện phê duyệt xuất kho](images/5_4_3a__B5_image11.png)

Warehouse Manager xem xét và phê duyệt yêu cầu xuất kho với quy trình tương tự như [phê duyệt nhập kho](#422-approve-warehouse-entry-request). Hệ thống ẩn nút "Từ chối" nếu yêu cầu xuất kho xuất phát từ yêu cầu thanh lý để tránh xung đột logic nghiệp vụ.

**Thông tin tìm kiếm yêu cầu xuất kho:**

| Trường | Operator | Action | Bắt buộc | Loại | Có thể chỉnh sửa | Độ dài tối đa |
|--------|----------|--------|----------|------|------------------|---------------|
| Mã yêu cầu | User | Input | M | Text | Y | 20 |
| Tiêu đề | User | Input | M | Text | Y | 150 |
| Người tạo | User | Select | M | List | Y | 20 |
| Trạng thái | User | Select | M | List | Y | 20 |
| Ngày tạo | User | Input | M | Date | Y | 20 |
| Loại cấp tài sản | User | Select | M | List | Y | 100 |
| Người xử lý | User | Select | M | List | Y | 20 |
| Ngày xác nhận | User | Input | M | Date | Y | 20 |

**Thông tin tài sản xuất kho:**

| Trường | Operator | Action | Bắt buộc | Hiển thị |
|--------|----------|--------|----------|----------|
| Mã tài sản | System | Display | M | Hiển thị mặc định |
| Tên Tài sản | System | Display | M | Hiển thị mặc định |
| Mô tả TS | System | Display | M | Hiển thị mặc định |
| Trạng thái TS | System | Display | M | Hiển thị mặc định |
| Phân nhóm TS | System | Display | M | Hiển thị mặc định |
| Nhóm TS (CAT1) | System | Display | M | Hiển thị mặc định |
| Số PO | System | Display | M | Hiển thị mặc định |
| Tên nhà cung cấp | System | Display | O | Ẩn hiện tùy biến |
| Nguyên giá TS (VAT incl) | System | Display | M | Ẩn hiện tùy biến |
| Mã TS liên quan | System | Display | O | Ẩn hiện tùy biến |
| Mô tả TS liên quan | System | Display | O | Ẩn hiện tùy biến |
| Tên người sử dụng | System | Display | M | Hiển thị mặc định |
| Tên đơn vị | System | Display | M | Hiển thị mặc định |
| Mã nhân viên | System | Display | M | Ẩn hiện tùy biến |
| Đơn vị sử dụng cha | System | Display | M | Hiển thị mặc định |
| Email nhân viên | System | Display | M | Ẩn hiện tùy biến |

###### 4.2.6.3. Receive Assets

![Giao diện nhận tài sản](images/5.4.4a)

Business User thực hiện xác nhận nhận tài sản từ kho thông qua giao diện chuyên biệt. Quy trình bao gồm 11 bước từ tìm kiếm yêu cầu đến cập nhật trạng thái cuối cùng. Khi xác nhận nhận tài sản, hệ thống sẽ clear thông tin kho và cập nhật đơn vị sử dụng theo thông tin người nhận.

**Tìm kiếm yêu cầu:**

| Operator | Field name VN | M/O | Field type | Editable | Max length | Format |
|----------|---------------|-----|------------|----------|------------|---------|
| User | Mã yêu cầu | M | Text | Y | 20 | |
| User | Tiêu đề | M | Text | Y | 150 | |
| User | Người tạo | M | List | Y | 20 | |
| User | Trạng thái | M | List | Y | 20 | |
| User | Ngày tạo | M | Date | Y | 20 | |
| User | Nghiệp vụ kho | M | List | Y | 100 | |
| User | Người xử lý | M | List | Y | 20 | |
| User | Ngày xác nhận | M | Date | Y | 20 | |

**Cập nhật trạng thái hệ thống:**

| Action | Đối tượng | Status | Mô tả |
|---------|-----------|--------|-------|
| Update | RQ Cấp tài sản | Từ chối | Khi từ chối nhận tài sản |
| Update | RQ Xuất kho | Từ chối | Khi từ chối nhận tài sản |
| Update | RQ Cấp tài sản | Đã xác nhận | Khi xác nhận nhận tài sản |
| Update | RQ Xuất kho | Đã nhận tài sản | Khi xác nhận nhận tài sản |
| Update | Tasklist Warehouse Mgr. | Đã xử lý | Cập nhật sau xử lý |
| Update | Tasklist AMP | Cần xử lý | Chuyển công việc cho AMP |

#### 4.2.7. Cancel Warehouse Export Request

![Giao diện hủy yêu cầu xuất kho](images/5.5.1a)

Chức năng hủy yêu cầu xuất kho cho phép AMP hủy các yêu cầu xuất kho chưa được xác nhận. Điều kiện tiên quyết là yêu cầu phải có trạng thái khác "Đã xác nhận". Quy trình hủy tương tự như [hủy yêu cầu nhập kho](#425-cancel-warehouse-request) với các bước tự động unlock tài sản và thông báo cho các bên liên quan.

**Thông tin tìm kiếm yêu cầu:**

| STT | Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Format | Default value |
|-----|----------|---------|---------------|-----|------------|----------|-------------|---------|---------------|
| 1 | User | Input | Mã yêu cầu | M | Text | Y | 20 | - | - |
| 2 | User | Input | Tiêu đề | M | Text | Y | 150 | - | - |
| 3 | User | Select | Người tạo | M | List | Y | 20 | - | - |
| 4 | User | Select | Trạng thái | M | List | Y | 20 | - | - |
| 5 | User | Input | Ngày tạo | M | Date | Y | 20 | - | - |
| 6 | User | Select | Nghiệp vụ kho | M | List | Y | 100 | - | - |
| 7 | User | Select | Người xử lý | M | List | Y | 20 | - | - |
| 8 | User | Input | Ngày xác nhận | M | Date | Y | 20 | - | - |

**Cập nhật trạng thái:**

| STT | Operator | Action | Đối tượng | Status |
|-----|----------|---------|-----------|---------|
| 1 | System | Update | RQ Cấp/Thanh lý | Đã hủy |
| 2 | System | Update | RQ xuất kho | Đã hủy |
| 3 | System | Update | Tasklist AMP | Đã xử lý |

#### 4.2.8. Inter-warehouse Transfer

##### 4.2.8.1. Thông số kỹ thuật giao diện người dùng

![Giao diện tạo yêu cầu điều chuyển kho](images/5.6.1a)

Chức năng điều chuyển tài sản giữa các kho cho phép di chuyển tài sản từ kho này sang kho khác thông qua hệ thống yêu cầu có kiểm soát. Giao diện tạo yêu cầu bao gồm thông tin chung, tìm kiếm tài sản, thông tin kho đi/nhập, đầu mối giao hàng và hồ sơ đính kèm.

Quy trình bao gồm 6 bước tự động: tạo yêu cầu, khóa tài sản, cập nhật trạng thái thành "Chờ phê duyệt", tìm và gán người duyệt, cập nhật tasklist cho Asset Manager và Warehouse Manager, và gửi thông báo email cho các bên liên quan.

##### 4.2.8.2. Thông số kỹ thuật chi tiết

**Thông tin chung:**

| Trường | Operator | Action | Field Name | M/O | Type | Editable | Max Length | Format | Default | Data Rule |
|--------|----------|--------|------------|-----|------|----------|------------|--------|---------|-----------|
| Số yêu cầu | System | Display | Số yêu cầu | M | Text | N | 50 | CK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| Ngày tạo | System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| Tiêu đề | User | Input | Tiêu đề | O | Text | Y | 150 | | | |

**Tìm kiếm tài sản:**

| Trường | Operator | Action | Field Name | M/O | Type | Editable | Max Length |
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

**Thông tin kho:**

| Phần | Trường | Operator | Action | Field Name | M/O | Type | Editable | Max Length | Data Source | Data Rule |
|------|--------|----------|--------|------------|-----|------|----------|------------|-------------|-----------|
| Kho đi | Tên kho | System/User | Display/Search/Select | Tên kho | M | List | N | 50 | | |
| Kho đi | Địa chỉ kho | System | Display | Địa chỉ kho | M | Text | Y | 50 | OMS | Tự động nhận diện theo Tên kho |
| Kho đi | Quản lý kho | System | Display | Quản lý kho | M | Text | N | 50 | OMS | Hiển thị theo format: Tên \| Phòng ban \| Email |
| Kho nhập | Tên kho | User | Select | Tên kho | M | List | N | 50 | | |
| Kho nhập | Địa chỉ kho | System | Display | Địa chỉ kho | M | Text | Y | 50 | OMS | Tự động nhận diện theo Tên kho |
| Kho nhập | Quản lý kho | System | Display | Quản lý kho | M | Text | N | 50 | OMS | Hiển thị theo format: Tên \| Phòng ban \| Email |

**Thông tin giao hàng:**

| Trường | Operator | Action | Field Name | M/O | Type | Editable | Max Length |
|--------|----------|--------|------------|-----|------|----------|------------|
| Đầu mối | User | Input | Đầu mối | M | Text | Y | 50 |

Sau khi tạo yêu cầu, quy trình chuyển sang [phê duyệt điều chuyển kho](#4281-approve-transfer-request) với quy trình tương tự như các phê duyệt khác.

##### 4.2.8.1. Approve Transfer Request

![Giao diện phê duyệt điều chuyển kho](images/5_6_2a_B5_image15.png)

Approver xem xét và phê duyệt yêu cầu điều chuyển tài sản giữa các kho thông qua quy trình 14 bước từ tìm kiếm đến bàn giao thực tế. Khi phê duyệt, hệ thống tự động tạo biên bản điều chuyển và cập nhật thông tin kho của tài sản. Cuối cùng là quá trình bàn giao thực tế giữa warehouse keeper của kho đi và kho đến.

**Tìm kiếm yêu cầu:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|--------|---------------|-----|------------|----------|------------|
| User | Input | Số yêu cầu | O | Text | Y | 20 |
| User | Input | Ngày tạo | O | Date | Y | 20 |
| User | Input | Tiêu đề | O | Text | Y | 150 |
| User | Select | Người tạo | O | List | Y | 20 |
| User | Select | Trạng thái yêu cầu | O | List | Y | 20 |
| User | Select | Người xử lý | O | List | Y | 20 |
| User | Input | Ngày xác nhận | O | Date | Y | 20 |

**Thông tin chung yêu cầu:**

| Operator | Action | Field name VN | M/O | Field type | Max length | Format | Default value | Data rule |
|----------|--------|---------------|-----|------------|------------|--------|---------------|-----------|
| System | Display | Số yêu cầu | M | Text | 50 | CK.YY.xxxx |  | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| System | Display | Ngày tạo | M | Date | 50 | MM.DD.YYYY | Today |  |
| User | Input | Tiêu đề | O | Text | 150 |  |  |  |
| User | Select | Thêm tài sản | M | Button |  |  |  |  |

**Thông tin đầu mối giao hàng:**

| Operator | Action | Field name VN | M/O | Field type | Max length |
|----------|--------|---------------|-----|------------|------------|
| User | Input | Đầu mối | M | Text | 50 |
| User | Input | Số điện thoại | M | Number | 52 |
| User | Input | Thời gian bàn giao | O | Date | 50 |
| User | Input | Ghi chú | M | Text | 150 |

## 5. Assumptions & Constraints

### Giả định:
- Tất cả hệ thống liên quan (OMS, EMS, ITSM) đều hoạt động ổn định và có API tích hợp
- Người dùng có kiến thức cơ bản về quy trình quản lý tài sản
- Hạ tầng mạng và phần cứng đáp ứng yêu cầu hiệu năng
- Dữ liệu master (kho, nhân sự, phòng ban) được đồng bộ chính xác từ OMS

### Ràng buộc:
- Không được thay đổi cấu trúc database hiện có của hệ thống FAM
- Thời gian phát triển trong vòng 6 tháng
- Tuân thủ các chuẩn bảo mật thông tin của tổ chức
- Hỗ trợ các trình duyệt phổ biến (Chrome, Firefox, Edge, Safari)
- Tích hợp với hệ thống Single Sign-On hiện tại

## 6. Dependencies

### Phụ thuộc kỹ thuật:
- **OMS API**: Để đồng bộ thông tin đơn vị sử dụng, kho và nhân sự
- **EMS API**: Để đồng bộ tiêu đề PO và thông tin thời gian bảo hành
- **ITSM API**: Để tích hợp module sửa chữa tài sản
- **Email Service**: Để gửi thông báo tự động trong quy trình workflow

### Phụ thuộc nghiệp vụ:
- Hoàn thiện quy định về phân quyền và workflow phê duyệt
- Đào tạo người dùng về quy trình mới
- Kiểm tra và làm sạch dữ liệu tài sản hiện có
- Thiết lập quy trình backup và khôi phục dữ liệu

## 7. Acceptance Criteria

### Dashboard tài sản:
- Hiển thị 4 chỉ số KPI chính với độ chính xác 99%
- Các biểu đồ phải có tính năng tương tác (hover, click)
- Bộ lọc hoạt động với thời gian phản hồi dưới 3 giây
- Xuất Excel thành công với định dạng chuẩn
- Đồng bộ dữ liệu từ OMS trong vòng 24 giờ

### Module quản lý kho:
- Tự động tạo yêu cầu nhập/xuất kho với độ chính xác 100%
- Workflow phê duyệt hoạt động đúng logic nghiệp vụ
- Email notification được gửi trong vòng 5 phút
- Tasklist cập nhật real-time
- Tài sản được lock/unlock chính xác theo trạng thái yêu cầu

### Tích hợp hệ thống:
- API calls thành công với uptime 99.5%
- Đồng bộ dữ liệu không có lỗi
- Xử lý exception gracefully
- Log đầy đủ cho việc troubleshooting

## 8. Glossary

| Thuật ngữ | Định nghĩa |
|-----------|------------|
| **AMP** | Asset Management Personnel - Nhân viên quản lý tài sản |
| **AM** | Asset Manager - Quản lý tài sản cấp cao |
| **WM** | Warehouse Manager - Quản lý kho |
| **WK** | Warehouse Keeper - Thủ kho, người quản lý trực tiếp hàng hóa trong kho |
| **BU User** | Business Unit User - Người dùng đơn vị kinh doanh |
| **OMS** | Organization Management System - Hệ thống quản lý tổ chức |
| **EMS** | Equipment Management System - Hệ thống quản lý thiết bị |
| **ITSM** | IT Service Management - Hệ thống quản lý dịch vụ IT |
| **LOV** | List of Values - Danh sách giá trị được định trước |
| **Tasklist** | Danh sách công việc cần xử lý của từng vai trò |
| **Lock/Unlock** | Khóa/mở khóa tài sản để tránh xung đột trong quy trình |
| **RQ** | Request - Yêu cầu |
| **TS** | Tài sản |
| **NK** | Nhập kho (mã định danh yêu cầu nhập kho) |
| **XK** | Xuất kho (mã định danh yêu cầu xuất kho) |
| **CK** | Chuyển kho (mã định danh yêu cầu chuyển kho) |

---

*Generated by Claude Sonnet 4.5 from 37 sheet summaries*
*Headings: 32 | Internal Links: 35*

*⚠️ Validation warnings - some links may need manual review*
