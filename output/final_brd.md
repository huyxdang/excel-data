# Business Requirements Document (BRD)
# Fixed Asset Management (FAM) Wave 4 Enhancement

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Project Scope & Objectives](#2-project-scope--objectives)
3. [Stakeholders](#3-stakeholders)
4. [Business Requirements](#4-business-requirements)
   - 4.1. [Dashboard Tài Sản](#41-dashboard-tài-sản)
   - 4.2. [Module Quản lý Kho](#42-module-quản-lý-kho)
     - 4.2.1. [Điều chuyển về kho - Tạo yêu cầu nhập kho](#421-điều-chuyển-về-kho---tạo-yêu-cầu-nhập-kho)
     - 4.2.2. [Điều chuyển về kho - Phê duyệt yêu cầu](#422-điều-chuyển-về-kho---phê-duyệt-yêu-cầu)
     - 4.2.3. [Điều chuyển về kho - Xác nhận nhập kho](#423-điều-chuyển-về-kho---xác-nhận-nhập-kho)
     - 4.2.4. [Nhập kho thủ công - Tạo yêu cầu](#424-nhập-kho-thủ-công---tạo-yêu-cầu)
     - 4.2.5. [Nhập kho thủ công - Phê duyệt yêu cầu](#425-nhập-kho-thủ-công---phê-duyệt-yêu-cầu)
     - 4.2.6. [Nhập kho thủ công - Xác nhận nhập kho](#426-nhập-kho-thủ-công---xác-nhận-nhập-kho)
     - 4.2.7. [Hủy yêu cầu nhập kho](#427-hủy-yêu-cầu-nhập-kho)
     - 4.2.8. [Cấp tài sản - Phê duyệt yêu cầu](#428-cấp-tài-sản---phê-duyệt-yêu-cầu)
     - 4.2.9. [Cấp tài sản - Tạo yêu cầu xuất kho](#429-cấp-tài-sản---tạo-yêu-cầu-xuất-kho)
     - 4.2.10. [Xuất kho từ cấp tài sản - Tiếp nhận yêu cầu](#4210-xuất-kho-từ-cấp-tài-sản---tiếp-nhận-yêu-cầu)
     - 4.2.11. [Xuất kho từ cấp tài sản - Phê duyệt xuất kho](#4211-xuất-kho-từ-cấp-tài-sản---phê-duyệt-xuất-kho)
     - 4.2.12. [Xuất kho từ cấp tài sản - Nhận tài sản](#4212-xuất-kho-từ-cấp-tài-sản---nhận-tài-sản)
     - 4.2.13. [Hủy yêu cầu xuất kho](#4213-hủy-yêu-cầu-xuất-kho)
     - 4.2.14. [Điều chuyển giữa các kho - Tạo yêu cầu](#4214-điều-chuyển-giữa-các-kho---tạo-yêu-cầu)
     - 4.2.15. [Điều chuyển giữa các kho - Phê duyệt yêu cầu](#4215-điều-chuyển-giữa-các-kho---phê-duyệt-yêu-cầu)
   - 4.3. [Status Management](#43-status-management)
   - 4.4. [Tasklist Management](#44-tasklist-management)
5. [Assumptions & Constraints](#5-assumptions--constraints)
6. [Dependencies](#6-dependencies)
7. [Acceptance Criteria](#7-acceptance-criteria)
8. [Glossary](#8-glossary)

---

## 1. Executive Summary

FAM Wave 4 Enhancement project aims to upgrade the Fixed Asset Management system with comprehensive dashboard visualization and warehouse management capabilities. The project delivers enhanced user experience through customizable asset dashboards, automated warehouse operations for asset transfers, and integrated workflow management systems.

The primary products include:
- [Dashboard Tài Sản](#41-dashboard-tài-sản) with advanced visualization and filtering capabilities  
- [Module Quản lý Kho](#42-module-quản-lý-kho) supporting complete warehouse lifecycle management
- Integration with external systems including OMS, EMS, and ITSM

Key enhancements encompass 11 priority items ranging from high-priority dashboard visualization and new warehouse modules to medium-priority workflow automation and system integrations. The solution provides end-to-end asset lifecycle management from procurement through disposal, with robust approval workflows and real-time status tracking.

---

## 2. Project Scope & Objectives

### In Scope
- Dashboard tài sản with comprehensive visualization and customization features
- Complete warehouse management module including intake, manual entry, and asset allocation processes  
- Automated request creation and approval workflows
- Integration with OMS for organizational data synchronization
- Integration with EMS for purchase order and warranty information
- Enhanced user interface with hide/show customizable fields
- Email notification system and tasklist management
- Asset locking mechanisms to prevent conflicts
- Comprehensive status tracking and workflow management

### Out of Scope
- Asset repair module implementation (identified as Priority 4 requiring process clarification)
- ITSM integration for repair workflows
- Branch support portal integration

### Project Objectives
- Implement Priority 1 items: Dashboard visualization and warehouse module
- Automate asset allocation confirmation after 20-day no-response period
- Establish seamless integration between asset management and warehouse operations
- Provide comprehensive audit trail and workflow visibility
- Enable customizable user interfaces based on role requirements

---

## 3. Stakeholders

### Primary Stakeholders
- **Asset Management Personnel (AMP)**: Core users managing asset lifecycle and processing requests
- **Warehouse Manager (WM)**: Responsible for warehouse operations approval and oversight
- **Warehouse Keeper (WK)**: Handles day-to-day warehouse transactions and confirmations
- **Asset Manager (AM)**: Strategic oversight and high-level approvals for asset requests
- **Business Unit (BU) Users**: End users receiving and using assets
- **Business Unit Managers**: Approval authorities for business unit asset requests

### Supporting Systems
- **OMS (Organization Management System)**: Provides organizational structure and warehouse information
- **EMS**: Source system for purchase order details and warranty information  
- **System**: Automated processing engine for workflow management

### Secondary Stakeholders
- **Checkers**: Quality control personnel for asset disposal processes
- **Approvers**: Various approval authorities throughout workflows
- **Initiators**: Users who create transfer and warehouse requests

---

## 4. Business Requirements

### 4.1. Dashboard Tài Sản

#### 4.1.1. Thông số kỹ thuật giao diện người dùng

Dashboard Tài Sản provides comprehensive asset visualization and reporting capabilities to support rapid decision-making. The system displays asset information across multiple dimensions including organizational distribution, asset status, temporal variations, and utilization rates.

**Chức năng chính:**
- 4 key performance indicators (KPIs) showing total assets, total value, warranty status, and utilization rate
- Interactive visualizations with hover and click functionality for drill-down analysis
- Multi-criteria filtering system supporting 5 filter types: region, organizational unit, CAT 1, group name, and asset status
- Export functionality to Excel format for offline analysis
- Real-time data synchronization with OMS for organizational structure updates

**Quy tắc nghiệp vụ:**
- Exclude "Đã thanh lý" and "Vô hiệu hóa" assets from main calculations to ensure accurate operational metrics
- Display assets with usage time > 3 years and > 5 years for depreciation analysis
- All visualizations must support interactive elements for enhanced user experience

#### 4.1.2. Thông số kỹ thuật chi tiết

**Dashboard KPI Specifications:**

| STT | Chỉ số | Mô tả tính toán | Loại giá trị |
|-----|---------|-----------------|--------------|
| 1 | Total assets | Count số lượng (All tài sản - Đã thanh lý - Vô hiệu hóa) | Số lượng |
| 2 | Total value | Sum nguyên giá (All tài sản - Đã thanh lý - Vô hiệu hóa) | Giá trị |
| 3 | Warranty status | Tỷ lệ % số lượng tài sản còn hạn bảo hành/(All tài sản - Vô hiệu hóa - Đã thanh lý) | Phần trăm |
| 4 | Utilization rate | Tỷ lệ % số lượng tài sản đang sử dụng/(All tài sản - Vô hiệu hóa - Đã thanh lý) | Phần trăm |

**Common Filter Configuration:**

| STT | Tên bộ lọc | Kiểu dữ liệu | Nguồn dữ liệu |
|-----|------------|--------------|---------------|
| 1 | Vùng | LOV | - |
| 2 | Đơn vị sử dụng | LOV | Đồng bộ từ OMS |
| 3 | CAT 1 | LOV | - |
| 4 | Group name | LOV | - |
| 5 | Asset status | LOV | Không bao gồm "Đã thanh lý", "Vô hiệu hóa" |

**Chart Specifications:**

| Tên biểu đồ | Dữ liệu hiển thị | Loại biểu đồ | Ghi chú |
|-------------|------------------|--------------|---------|
| Asset Distribution | Cơ cấu nhóm tài sản theo trạng thái | Sunburst | Vòng trong: IT/ADM/CMD, Vòng ngoài: Trạng thái. Hover hiển thị số lượng và giá trị |
| Asset Distribution | Cơ cấu theo Vùng/Đơn vị sử dụng | Stacked Column | Nguyên giá |
| Asset Value by Group Name | Giá trị theo Group Name | Column | Nguyên giá |
| Asset Fluctuation Over Time | Biến động theo tháng/năm | Line | Nguyên giá |
| Asset by Time in Use | Tài sản theo thời gian sử dụng | Scatter | Số lượng |

---

### 4.2. Module Quản lý Kho

Module Quản lý Kho provides comprehensive warehouse operations supporting the complete asset lifecycle from intake through distribution. The system handles 7 main workflows: internal transfers (cross-transfer and warehouse return), warehouse intake, manual warehouse entry, intake cancellation, asset allocation, asset disposal, warehouse distribution, distribution cancellation, and inter-warehouse transfers.

**Các quy trình chính:**
- [Warehouse intake operations](#421-điều-chuyển-về-kho---tạo-yêu-cầu-nhập-kho) for assets returned to warehouse storage
- [Manual warehouse entry](#424-nhập-kho-thủ-công---tạo-yêu-cầu) for direct asset registration
- [Asset allocation workflows](#428-cấp-tài-sản---phê-duyệt-yêu-cầu) from warehouse to end users
- [Inter-warehouse transfer processes](#4214-điều-chuyển-giữa-các-kho---tạo-yêu-cầu) for inventory optimization
- [Request cancellation capabilities](#427-hủy-yêu-cầu-nhập-kho) with proper asset unlock mechanisms

**Tích hợp hệ thống:**
The warehouse module automatically integrates with asset allocation and disposal processes. Upon completion of asset allocation or disposal processes, the system automatically creates corresponding distribution requests, ensuring seamless workflow continuity and minimizing manual intervention.

**Quy tắc nghiệp vụ quan trọng:**
- Automatic request generation when completing transfers to warehouse
- Automatic distribution request creation upon allocation or disposal completion  
- Asset locking mechanisms during processing to prevent concurrent modifications
- Automatic status updates and notification systems for all stakeholders
- Comprehensive audit trail for all warehouse operations

---

#### 4.2.1. Điều chuyển về kho - Tạo yêu cầu nhập kho

#### 4.2.1.1. Thông số kỹ thuật giao diện người dùng

![5.1.1a B5](images/5_1_1a_B5_image1.png)

**Các bước thực hiện:**
1. Tạo yêu cầu nhập kho: Bước khởi tạo yêu cầu trong hệ thống
2. Cập nhật trạng thái yêu cầu: Hệ thống cập nhật status của yêu cầu
3. Cập nhật tasklist: Yêu cầu được thêm vào danh sách công việc cần xử lý
4. Thông báo cho Warehouse Mgr.: Gửi notification đến người quản lý kho
5. Chuyển sang bước phê duyệt: Liên kết đến [quy trình phê duyệt](#422-điều-chuyển-về-kho---phê-duyệt-yêu-cầu)

**Các thành phần giao diện:**
- Biểu tượng bắt đầu workflow với luồng xử lý tuyến tính
- 4 bước xử lý tuần tự với biểu tượng bánh răng thể hiện hoạt động hệ thống
- Điểm chuyển tiếp tới quy trình phê duyệt yêu cầu
- Actor chính là "TẠO YÊU CẦU NHẬP KHO" được thực hiện trong hệ thống (System)

Quy trình này được khởi tạo tự động khi có yêu cầu chuyển kho được xác nhận. Hệ thống sẽ kế thừa toàn bộ thông tin từ yêu cầu chuyển kho bao gồm thông tin tài sản, chi tiết kho đích và các tệp đính kèm.

#### 4.2.1.2. Thông số kỹ thuật chi tiết

Hệ thống tự động tạo yêu cầu nhập kho khi xử lý điều chuyển tài sản về kho. Quy trình bao gồm 4 bước chính: tạo yêu cầu với số tự động theo format NK.YY.xxxx, cập nhật trạng thái các yêu cầu liên quan, cập nhật tasklist cho Asset Manager và Warehouse Manager, và gửi thông báo email.

**Đặc tả thông tin chung yêu cầu nhập kho:**

| STT | Tab/Section | Operator | Action | Field Name VN | M/O | Field Type | Editable | Max Length | Format | Default Value | Data Rule |
|-----|-------------|----------|---------|---------------|-----|------------|----------|------------|---------|---------------|-----------|
| 1 | Thông tin chung | System | Display | Số yêu cầu | M | Text | N | 50 | NK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| 2 | Thông tin chung | System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| 3 | Thông tin chung | System | Display | Tiêu đề | M | Text | N | 150 | | | =Tiêu đề RQ điều chuyển |

**Đặc tả danh sách tài sản nhập kho:**

| Field Name VN | M/O | Field Type | Editable | Data Rule |
|---------------|-----|------------|----------|-----------|
| Mã tài sản | M | | N | Hiển thị mặc định |
| Tên Tài sản | M | | N | Hiển thị mặc định |
| Mô tả TS | M | | N | Hiển thị mặc định |
| Trạng thái TS | M | | N | Hiển thị mặc định |
| Phân nhóm TS (group name) | M | | N | Hiển thị mặc định |
| Nhóm TS (CAT1) | M | | N | Hiển thị mặc định |
| Số PO | M | | N | Hiển thị mặc định |
| Tên nhà cung cấp | O | | N | Ẩn hiện tùy biến |
| Nguyên giá TS (VAT incl) | M | | N | Ẩn hiện tùy biến |
| Mã TS liên quan | O | | N | Ẩn hiện tùy biến |
| Mô tả TS liên quan | O | | N | Ẩn hiện tùy biến |
| Tên người sử dụng | M | | N | Hiển thị mặc định |
| Tên đơn vị | M | | N | Hiển thị mặc định |
| Mã nhân viên | M | | N | Ẩn hiện tùy biến |
| Đơn vị sử dụng cha | M | | N | Hiển thị mặc định |
| Email nhân viên | M | | N | Ẩn hiện tùy biến |
| Địa chỉ đặt TS | O | | N | Ẩn hiện tùy biến |
| Tầng đặt TS | O | | N | Ẩn hiện tùy biến |
| Phòng đặt TS | O | | N | Ẩn hiện tùy biến |

**Thông tin kho và đầu mối giao hàng:**

| Tab/Section | Operator | Action | Field Name VN | M/O | Field Type | Editable | Max Length | Data Source | Data Rule |
|-------------|----------|---------|---------------|-----|------------|----------|------------|-------------|-----------|
| Thông tin kho nhập | System | Display | Tên kho | M | List | N | 50 | | = Kho trong RQ điều chuyển |
| Thông tin kho nhập | System | Display | Địa chỉ kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| Thông tin kho nhập | System | Display | Quản lý kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho (Tên \| Phòng ban \| Email) |
| Thông tin đầu mối giao hàng | User | Input | Đầu mối | M | Text | N | 50 | | = Đầu mối giao hàng trong RQ điều chuyển |
| Thông tin đầu mối giao hàng | User | Input | Số điện thoại | M | Number | N | 52 | | |
| Thông tin đầu mối giao hàng | User | Input | Thời gian bàn giao | O | Date | N | 50 | | |

**Quy trình cập nhật trạng thái và tasklist:**

| Bước | Operator | Action | Đối tượng | Giá trị |
|------|----------|---------|-----------|---------|
| 2 | System | Update | Trạng thái RQ điều chuyển | Đã xác nhận |
| 2 | System | Update | Trạng thái RQ nhập kho | Chờ phê duyệt |
| 3 | System | Update | Tasklist AMP | "Đã xử lý" |
| 3 | System | Update | Tasklist WM | "Cần xử lý" |
| 4 | System | Send | Email notification | Notification |

**Quy tắc quan trọng:**
Tài sản sẽ được unlock khỏi yêu cầu điều chuyển khi hoàn thành, nhưng sẽ bị lock bởi yêu cầu nhập kho và chưa được cập nhật thông tin cho đến khi yêu cầu nhập kho hoàn tất trong [quy trình xác nhận](#423-điều-chuyển-về-kho---xác-nhận-nhập-kho).

---

#### 4.2.2. Điều chuyển về kho - Phê duyệt yêu cầu

#### 4.2.2.1. Thông số kỹ thuật giao diện người dùng

![5.1.2a B6](images/5_1_2a_B6_image2.png)

**Các bước thực hiện quy trình:**
1. **Bước 1-3:** Nhập thông tin tìm kiếm → Hiển thị kết quả → Chọn xem yêu cầu
2. **Điểm quyết định:** Gateway phê duyệt với hai nhánh xử lý

**Nhánh phê duyệt (trên):**
- Phê duyệt → Cập nhật trạng thái → Cập nhật tasklist → Gửi email → Chuyển đến [màn hình xác nhận nhập kho](#423-điều-chuyển-về-kho---xác-nhận-nhập-kho)

**Nhánh từ chối (dưới):**
- Nhập lý do từ chối → Xác nhận đồng ý → Unlock tài sản → Cập nhật trạng thái → Cập nhật tasklist → Gửi email thông báo

**Luồng công việc:**
Quy trình được thiết kế với luồng tuyến tính rõ ràng, có điểm phân nhánh duy nhất tại bước phê duyệt. Cả hai nhánh đều kết thúc bằng việc gửi email thông báo, đảm bảo người yêu cầu được cập nhật kết quả. Đặc biệt, nhánh từ chối có thêm bước unlock tài sản để giải phóng tài nguyên đã được lock trong quá trình xử lý.

#### 4.2.2.2. Thông số kỹ thuật chi tiết

Giao diện phê duyệt yêu cầu nhập kho cho Warehouse Manager với đầy đủ thông tin tài sản và khả năng ra quyết định phê duyệt hoặc từ chối. Hệ thống tự động cập nhật trạng thái, unlock tài sản (nếu từ chối), và gửi thông báo cho các bên liên quan.

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

**Thông tin tài sản hiển thị:**
Hệ thống hiển thị đầy đủ thông tin tài sản bao gồm cả thông tin có thể ẩn/hiện tùy biến như nguyên giá, thông tin nhà cung cấp, địa chỉ đặt tài sản, thông tin bảo hành và ngày bắt đầu sử dụng.

**Thông tin kho nhập:**

| Field name VN | M/O | Field type | Max length | Data source | Data rule |
|---------------|-----|------------|------------|-------------|-----------|
| Tên kho | M | List | 50 | | |
| Địa chỉ kho | M | Text | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| Quản lý kho | M | Text | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho (Tên \| Phòng ban \| Email) |

**Cập nhật trạng thái sau xử lý:**

| Action | Object | Status/Rule |
|--------|--------|-------------|
| System Update | Trạng thái RQ nhập kho | Từ chối (khi từ chối) / Chờ nhập kho (khi phê duyệt) |
| System Update | Trạng thái RQ Điều chuyển | Từ chối (khi từ chối) / Không update (khi phê duyệt) |
| System Update | Tasklist WM | Đã xử lý |
| System Update | Tasklist WK | Cần xử lý (khi phê duyệt) |
| System Update | Tasklist BU | Cần xử lý (khi từ chối) / Không update (khi phê duyệt) |
| System Update | Tasklist AMP | Cần xử lý (khi từ chối) / Không update (khi phê duyệt) |

**Quy tắc nghiệp vụ:**
- Bắt buộc nhập lý do khi từ chối yêu cầu (max 150 ký tự)
- Cho phép nhập ghi chú khi phê duyệt (max 150 ký tự)
- Hệ thống tự động unlock tài sản khi yêu cầu bị từ chối để cho phép sử dụng trong request khác

---

#### 4.2.3. Điều chuyển về kho - Xác nhận nhập kho

#### 4.2.3.1. Thông số kỹ thuật giao diện người dùng

![5.1.3a B5](images/5_1_3a_B5_image3.png)

**Các bước thực hiện quy trình:**
1. **Nhập thông tin tìm kiếm yêu cầu** - Nhập tiêu chí tìm kiếm
2. **Hiển thị kết quả tìm kiếm** - Hiển thị danh sách yêu cầu phù hợp
3. **Chọn, xem yêu cầu** - Lựa chọn yêu cầu cụ thể để xem chi tiết
4. **Gateway Xác nhận** - Điểm quyết định đồng ý hay từ chối

**Nhánh Đồng ý:**
- Nhập thông tin nhận hàng → Gateway kiểm tra → Unlock và cập nhật thông tin tài sản → Cập nhật trạng thái yêu cầu → Cập nhật tasklist → Gửi email thông báo

**Nhánh Từ chối:**
- Nhập lý do từ chối → Gateway kiểm tra → Unlock tài sản → Cập nhật trạng thái yêu cầu → Cập nhật tasklist → Gửi email thông báo

**Luồng công việc:**
Cả hai nhánh đều có điểm "Về bước 3" cho phép quay lại bước chọn/xem yêu cầu nếu cần thiết. Quy trình đảm bảo tính linh hoạt trong việc xử lý và có cơ chế rollback khi cần.

#### 4.2.3.2. Thông số kỹ thuật chi tiết

Quy trình hoàn chỉnh cho việc xác nhận nhập kho tài sản từ Warehouse Keeper với 8 bước từ tìm kiếm đến thông báo kết quả. Hệ thống tự động cập nhật "Ngày bắt đầu sử dụng" khi xác nhận nhập kho nếu trường này có giá trị N/A.

**Form tìm kiếm yêu cầu:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|--------|---------------|-----|------------|----------|------------|
| User | Input | Số yêu cầu | O | Text | Y | 20 |
| User | Input | Ngày tạo | O | Date | Y | 20 |
| User | Input | Tiêu đề | O | Text | Y | 150 |
| User | Select | Người tạo | O | List | Y | 20 |
| User | Select | Trạng thái yêu cầu | O | List | Y | 20 |
| User | Select | Người xử lý | O | List | Y | 20 |
| User | Input | Ngày xác nhận | O | Date | Y | 20 |

**Hiển thị kết quả tìm kiếm:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|--------|---------------|-----|------------|----------|------------|
| System | Display | Số yêu cầu | M | Text | N | 20 |
| System | Display | Ngày tạo | M | Date | N | 20 |
| System | Display | Tiêu đề | M | Text | N | 150 |
| System | Display | Người tạo | M | Text | N | 20 |
| System | Display | Trạng thái yêu cầu | M | Text | N | 20 |
| System | Display | Người xử lý | O | Text | N | 20 |
| System | Display | Ngày xác nhận | O | Date | N | 20 |

**Thông tin kho nhập:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Data source | Data rule |
|----------|--------|---------------|-----|------------|----------|------------|-------------|-----------|
| System | Display | Tên kho | M | List | N | 50 | | |
| System | Display | Địa chỉ kho | M | Text | Y | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| System | Display | Quản lý kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho (Tên \| Phòng ban \| Email) |

**Thông tin đầu mối giao hàng:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|--------|---------------|-----|------------|----------|------------|
| System | Display | Đầu mối | M | Text | Y | 50 |
| System | Display | Số điện thoại | M | Number | Y | 52 |
| System | Display | Thời gian bàn giao | O | Date | Y | 50 |
| System | Display | Ghi chú | M | Text | Y | 150 |

**Quy tắc nghiệp vụ quan trọng:**
- Hệ thống tự động unlock tài sản khi từ chối để asset có thể được pickup cho request khác
- Cập nhật tasklist cho các role khác nhau và gửi email notification
- Tích hợp với hệ thống OMS để lấy thông tin kho và quản lý kho tự động

Sau khi hoàn thành xác nhận nhập kho, quy trình kết thúc và tài sản chính thức được nhập vào kho để sẵn sàng cho các [quy trình cấp phát](#428-cấp-tài-sản---phê-duyệt-yêu-cầu) tiếp theo.

---

#### 4.2.4. Nhập kho thủ công - Tạo yêu cầu

#### 4.2.4.1. Thông số kỹ thuật giao diện người dùng

![5.2.1a B5](images/5_2_1a_B5_image4.png)

**Các bước thực hiện quy trình:**
1. **Tạo yêu cầu nhập kho, định nghĩa danh sách yêu cầu**: Bước đầu tiên để khởi tạo yêu cầu
2. **Lock tài sản**: Khóa tài sản để đảm bảo tính nhất quán dữ liệu
3. **Cập nhật trạng thái yêu cầu**: Cập nhật status của yêu cầu trong hệ thống  
4. **Cập nhật tasklist người nhận**: Thêm task vào danh sách công việc của người được giao
5. **Gửi email thông báo cho WM**: Gửi thông báo email đến Warehouse Manager

**Luồng công việc:**
Quy trình tuyến tính từ tạo yêu cầu → lock tài sản với điểm quyết định cho phép "Gửi" (tiếp tục quy trình) hoặc "Thoát" (kết thúc sớm). Nhánh "Gửi" dẫn đến chuỗi các bước cập nhật và thông báo, kết thúc bằng việc chuyển sang [quy trình phê duyệt](#425-nhập-kho-thủ-công---phê-duyệt-yêu-cầu).

#### 4.2.4.2. Thông số kỹ thuật chi tiết

Chức năng nhập kho thủ công cho phép người dùng tạo yêu cầu nhập tài sản trực tiếp vào kho mà không thông qua quy trình điều chuyển. Hệ thống hỗ trợ tìm kiếm tài sản linh hoạt và tự động hóa các bước xử lý sau khi gửi yêu cầu.

**Thông tin chung yêu cầu:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Format | Default value | Data rule |
|----------|--------|---------------|-----|------------|----------|------------|--------|---------------|-----------|
| User | Select | Tạo | M | Button | N | | | | |
| System | Display | Số yêu cầu | M | Text | N | 50 | NK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| User | Input | Tiêu đề | O | Text | Y | 150 | | | |
| User | Select | Thêm tài sản | M | Button | N | | | | |

**Form tìm kiếm tài sản:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|--------|---------------|-----|------------|----------|------------|
| User | Input | Mã tài sản | O | Text | N | 20 |
| User | Input | Tên tài sản | O | Text | Y | 20 |
| User | Select | Phân loại tài sản | O | List | N | 20 |
| User | Select | Nhóm tài sản | O | List | N | 20 |
| User | Input | PO number | O | Text | Y | 20 |
| User | Select | Trạng thái TS | O | List | N | 50 |
| User | Select | Tên nhà cung cấp | O | List | N | 50 |
| User | Input | Tên kho | O | List | Y | 50 |
| User | Select | Vị trí đặt tài sản | O | Text | N | 100 |

**Thông tin kho nhập:**

| Field name VN | M/O | Field type | Editable | Max length | Data source | Data rule |
|---------------|-----|------------|----------|------------|-------------|-----------|
| Tên kho | M | List | N | 50 | | System/User Display/Search/Select |
| Địa chỉ kho | M | Text | Y | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| Quản lý kho | M | Text | N | 50 | OMS | Tự động nhận diện (Tên \| Phòng ban \| Email) |

**Thông tin đầu mối giao hàng:**

| Field name VN | M/O | Field type | Editable | Max length |
|---------------|-----|------------|----------|------------|
| Đầu mối | M | Text | Y | 50 |
| Số điện thoại | M | Number | Y | 52 |
| Thời gian bàn giao | O | Date | Y | 50 |
| Ghi chú | M | Text | Y | 150 |

**Quy tắc nghiệp vụ quan trọng:**
- Có thể chọn nhiều tài sản cho một yêu cầu
- Cảnh báo khi tài sản đã bị lock trong request khác đang xử lý
- Tài sản bị lock không thể sử dụng cho request khác cho đến khi request hiện tại hoàn thành
- Sau khi gửi yêu cầu, hệ thống chuyển sang [quy trình phê duyệt](#425-nhập-kho-thủ-công---phê-duyệt-yêu-cầu)

---

#### 4.2.5. Nhập kho thủ công - Phê duyệt yêu cầu

#### 4.2.5.1. Thông số kỹ thuật giao diện người dùng

![5.2.2a B5](images/5_2_2a_B5_image5.png)

**Các bước thực hiện quy trình:**

*Luồng chính (Phê duyệt):*
1. Nhập thông tin tìm kiếm yêu cầu
2. Hiển thị kết quả tìm kiếm  
3. Chọn, xem yêu cầu
4. Điểm quyết định "Phê duyệt"
5. Cập nhật trạng thái yêu cầu
6. Cập nhật tasklist
7. Gửi email thông báo
8. Chuyển đến [quy trình xác nhận nhập kho](#426-nhập-kho-thủ-công---xác-nhận-nhập-kho)

*Luồng phụ (Từ chối):*
1. Nhập lý do từ chối
2. Điểm quyết định "Đồng ý"
3. Unlock tài sản
4. Cập nhật trạng thái yêu cầu
5. Cập nhật tasklist  
6. Gửi email thông báo
7. Kết thúc quy trình

**Luồng công việc:** Quy trình có cấu trúc rõ ràng với hai nhánh xử lý song song, đảm bảo mọi quyết định đều có hậu quả và thông báo tương ứng. Việc có điểm xác nhận "Đồng ý" trong luồng từ chối cho thấy hệ thống yêu cầu xác nhận cuối cùng trước khi thực hiện hành động từ chối.

#### 4.2.5.2. Thông số kỹ thuật chi tiết

Giao diện phê duyệt yêu cầu nhập kho thủ công cho Warehouse Manager với 13 bước xử lý từ tìm kiếm đến thông báo kết quả. Màn hình hiển thị đầy đủ thông tin tài sản, kho nhập, đầu mối giao hàng và lịch sử xử lý.

**Form tìm kiếm yêu cầu:**

| Trường | Operator | Action | Tên trường | M/O | Kiểu | Editable | Độ dài |
|--------|----------|--------|------------|-----|------|----------|--------|
| Warehouse Mgr. | User | Input | Số yêu cầu | O | Text | Y | 20 |
| Warehouse Mgr. | User | Input | Ngày tạo | O | Date | Y | 20 |
| Warehouse Mgr. | User | Input | Tiêu đề | O | Text | Y | 150 |
| Warehouse Mgr. | User | Select | Người tạo | O | List | Y | 20 |
| Warehouse Mgr. | User | Select | Trạng thái yêu cầu | O | List | Y | 20 |
| Warehouse Mgr. | User | Select | Người xử lý | O | List | Y | 20 |
| Warehouse Mgr. | User | Input | Ngày xác nhận | O | Date | Y | 20 |

**Thông tin tài sản chính:**

| Trường | M/O | Hiển thị | Mô tả |
|--------|-----|----------|-------|
| Mã tài sản | M | Hiển thị mặc định | |
| Tên Tài sản | M | Hiển thị mặc định | |
| Mô tả TS | M | Hiển thị mặc định | |
| Trạng thái TS | M | Hiển thị mặc định | |
| Phân nhóm TS (group name) | M | Hiển thị mặc định | |
| Nhóm TS (CAT1) | M | Hiển thị mặc định | |
| Số PO | M | Hiển thị mặc định | |
| Nguyên giá TS (VAT incl) | M | Ẩn hiện tùy biến | |
| Tên người sử dụng | M | Hiển thị mặc định | |
| Tên đơn vị | M | Hiển thị mặc định | |
| Đơn vị sử dụng cha | M | Hiển thị mặc định | |

**Thông tin kho:**

| Trường | M/O | Kiểu | Editable | Độ dài | Nguồn dữ liệu | Quy tắc |
|--------|-----|------|----------|--------|---------------|---------|
| Tên kho | M | List | N | 50 | | |
| Địa chỉ kho | M | Text | Y | 50 | OMS | Tự động nhận diện theo Tên kho |
| Quản lý kho | M | Text | N | 50 | OMS | Hiển thị: Tên \| Phòng ban \| Email |

**Quy tắc nghiệp vụ:**
- Bắt buộc nhập lý do khi từ chối yêu cầu (max 150 ký tự)
- Hệ thống tự động unlock tài sản khi yêu cầu bị từ chối
- Cập nhật tasklist và gửi email thông báo cho các bên liên quan
- Khi phê duyệt, chuyển sang [quy trình xác nhận nhập kho](#426-nhập-kho-thủ-công---xác-nhận-nhập-kho)

---

#### 4.2.6. Nhập kho thủ công - Xác nhận nhập kho

#### 4.2.6.1. Thông số kỹ thuật giao diện người dùng

![5.2.3a B6](images/5_2_3a_B6_image6.png)

**Các bước thực hiện quy trình:**
1. **Nhập thông tin tìm kiếm yêu cầu** - Nhập tiêu chí tìm kiếm
2. **Hiển thị kết quả tìm kiếm** - Hiển thị danh sách yêu cầu phù hợp
3. **Chọn, xem yêu cầu** - Lựa chọn yêu cầu cụ thể để xem chi tiết
4. **Gateway Xác nhận** - Điểm quyết định đồng ý hay từ chối

**Nhánh Đồng ý:** 
- Nhập thông tin nhận hàng → Gateway kiểm tra → Unlock và cập nhật thông tin tài sản → Cập nhật trạng thái yêu cầu → Cập nhật tasklist → Gửi email thông báo → Kết thúc

**Nhánh Từ chối:** 
- Nhập lý do từ chối → Gateway kiểm tra → Unlock tài sản → Cập nhật trạng thái yêu cầu → Cập nhật tasklist → Gửi email thông báo → Kết thúc

Cả hai nhánh đều có điểm "Về bước 3" cho phép quay lại bước chọn/xem yêu cầu nếu cần thiết, đảm bảo tính linh hoạt trong xử lý.

#### 4.2.6.2. Thông số kỹ thuật chi tiết

Quy trình xác nhận nhập kho thủ công hoàn chỉnh với 11 bước xử lý từ tìm kiếm đến hoàn tất. Hệ thống tự động cập nhật "Ngày bắt đầu sử dụng" khi xác nhận nếu trường này = N/A và unlock tài sản khi từ chối.

**Form tìm kiếm yêu cầu:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|--------|---------------|-----|------------|----------|------------|
| User | Input | Số yêu cầu | O | Text | Y | 20 |
| User | Input | Ngày tạo | O | Date | Y | 20 |
| User | Input | Tiêu đề | O | Text | Y | 150 |
| User | Select | Người tạo | O | List | Y | 20 |
| User | Select | Trạng thái yêu cầu | O | List | Y | 20 |
| User | Select | Người xử lý | O | List | Y | 20 |
| User | Input | Ngày xác nhận | O | Date | Y | 20 |

**Hiển thị kết quả tìm kiếm:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|--------|---------------|-----|------------|----------|------------|
| System | Display | Số yêu cầu | M | Text | N | 20 |
| System | Display | Ngày tạo | M | Date | N | 20 |
| System | Display | Tiêu đề | M | Text | N | 150 |
| System | Display | Người tạo | M | Text | N | 20 |
| System | Display | Trạng thái yêu cầu | M | Text | N | 20 |
| System | Display | Người xử lý | O | Text | N | 20 |
| System | Display | Ngày xác nhận | O | Date | N | 20 |

**Thông tin kho nhập:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Data source | Data rule |
|----------|--------|---------------|-----|------------|----------|------------|-------------|-----------|
| System | Display | Tên kho | M | List | N | 50 | | |
| System | Display | Địa chỉ kho | M | Text | Y | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| System | Display | Quản lý kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho (Tên \| Phòng ban \| Email) |

**Thông tin đầu mối giao hàng:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|--------|---------------|-----|------------|----------|------------|
| System | Display | Đầu mối | M | Text | Y | 50 |
| System | Display | Số điện thoại | M | Number | Y | 52 |
| System | Display | Thời gian bàn giao | O | Date | Y | 50 |
| System | Display | Ghi chú | M | Text | Y | 150 |

**Quy tắc nghiệp vụ quan trọng:**
- Hỗ trợ đính kèm hồ sơ tài liệu với thông tin chi tiết về file
- Tích hợp với hệ thống OMS để lấy thông tin kho và quản lý kho tự động
- Cập nhật tasklist cho các role khác nhau (WK, AMP, WM) và gửi email notification
- Unlock tài sản khi từ chối để asset có thể được pickup cho request khác

Sau khi hoàn thành xác nhận nhập kho thủ công, tài sản chính thức được lưu trữ trong kho và sẵn sàng cho các [quy trình cấp phát tài sản](#428-cấp-tài-sản---phê-duyệt-yêu-cầu).

---

#### 4.2.7. Hủy yêu cầu nhập kho

#### 4.2.7.1. Thông số kỹ thuật giao diện người dùng

![5.3.1a B5](images/5_3_1a_B5_image7.png)

**Các bước thực hiện quy trình:**
1. **Nhập thông tin tìm kiếm yêu cầu**: Bước khởi tạo để tìm yêu cầu cần hủy
2. **Tìm kiếm qua tìm kiếm**: Hệ thống thực hiện tìm kiếm theo tiêu chí
3. **Chọn yêu cầu cần xử lý**: Lựa chọn yêu cầu cụ thể từ danh sách
4. **Điểm quyết định**: Gateway với hai lựa chọn "Hủy" và "Thoát"
5. **Luồng hủy**: Nhập lý do hủy → Cập nhật trạng thái yêu cầu → Unlock tài sản → Cập nhật tasklist → Thông báo cho BU user
6. **Luồng thoát**: Quay về bước 3 với ghi chú "Về bước 3"

**Luồng công việc**: 
Quy trình tuyến tính với một điểm quyết định duy nhất, cho phép người dùng tiếp tục hủy yêu cầu hoặc thoát về bước trước đó. Khi chọn hủy, các bước xử lý được thực hiện tuần tự để đảm bảo tính toàn vẹn dữ liệu và thông báo đầy đủ.

#### 4.2.7.2. Thông số kỹ thuật chi tiết

Chức năng hủy yêu cầu nhập kho cho AMP với điều kiện yêu cầu phải được gửi thành công và có trạng thái khác "Đã nhập kho". Quy trình bao gồm 8 bước từ tìm kiếm đến thông báo kết quả.

**Điều kiện hủy yêu cầu:**
- Yêu cầu nhập kho gửi đi thành công
- Trạng thái yêu cầu khác "Đã nhập kho"

**Form tìm kiếm yêu cầu:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|--------|---------------|-----|------------|----------|------------|
| User | Input | Số yêu cầu | O | Text | Y | 20 |
| User | Input | Ngày tạo | O | Date | Y | 20 |
| User | Input | Tiêu đề | O | Text | Y | 150 |
| User | Select | Người tạo | O | List | Y | 20 |
| User | Select | Trạng thái yêu cầu | O | List | Y | 20 |
| User | Select | Người xử lý | O | List | Y | 20 |
| User | Input | Ngày xác nhận | O | Date | Y | 20 |

**Hiển thị danh sách yêu cầu:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|--------|---------------|-----|------------|----------|------------|
| System | Display | Số yêu cầu | M | Text | N | 20 |
| System | Display | Ngày tạo | M | Date | N | 20 |
| System | Display | Tiêu đề | M | Text | N | 150 |
| System | Display | Người tạo | M | Text | N | 20 |
| System | Display | Trạng thái yêu cầu | M | Text | N | 20 |
| System | Display | Người xử lý | O | Text | N | 20 |
| System | Display | Ngày xác nhận | O | Date | N | 20 |

**Thông tin chung yêu cầu:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Format | Default | Data Rule |
|----------|--------|---------------|-----|------------|----------|------------|--------|---------|-----------|
| System | Display | Số yêu cầu | M | Text | N | 50 | NK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 |
| System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| System | Input | Tiêu đề | O | Text | Y | 150 | | | |

**Quy tắc nghiệp vụ khi hủy:**
- Bắt buộc nhập lý do hủy khi thực hiện hủy yêu cầu
- Tự động unlock tài sản khi yêu cầu bị hủy để asset có thể được pickup cho request khác
- Cập nhật trạng thái yêu cầu thành "Đã hủy"
- Cập nhật tasklist: WM thành "Đã xử lý", AMP/BU user thành "Cần xử lý"
- Gửi thông báo email cho các bên liên quan

Giao diện hiển thị đầy đủ thông tin tài sản với 25+ trường dữ liệu bao gồm thông tin cơ bản, phân nhóm, giá trị, người sử dụng, địa chỉ đặt tài sản, và thông tin bảo hành. Một số trường có thể ẩn/hiện tùy biến theo cấu hình hệ thống.

---

#### 4.2.8. Cấp tài sản - Phê duyệt yêu cầu

#### 4.2.8.1. Thông số kỹ thuật giao diện người dùng

![5.4.0a A4](images/5_4_0a_A4_image8.png)

**Các bước thực hiện quy trình:**
1. **Nhập thông tin tìm kiếm yêu cầu**: Bước đầu tiên để tìm kiếm yêu cầu cần xử lý
2. **Hiển thị kết quả tìm kiếm**: Hiển thị danh sách yêu cầu phù hợp
3. **Chọn yêu cầu cần xử lý**: Người dùng chọn yêu cầu cụ thể để xử lý
4. **Exclusive Gateway**: Điểm quyết định với hai luồng "Từ chối" và "Phê duyệt"

**Luồng từ chối:**
- Dẫn đến End Event và chuyển sang "Và bước 3"

**Luồng phê duyệt:**
- Nhập lý do từ chối → Cập nhật trạng thái yêu cầu → Unlock tài sản → Cập nhật tasklist → Thông báo cho AMP
- Sub-process reference: [Tạo yêu cầu xuất kho](#429-cấp-tài-sản---tạo-yêu-cầu-xuất-kho) được tham chiếu trong luồng phê duyệt

**Luồng công việc:**
Quy trình được thiết kế với hai nhánh xử lý rõ ràng. Luồng phê duyệt bao gồm chuỗi các hoạt động tự động và kết nối với quy trình con để tạo yêu cầu xuất kho, đảm bảo tính liên tục trong toàn bộ quy trình cấp phát tài sản.

#### 4.2.8.2. Thông số kỹ thuật chi tiết

Giao diện phê duyệt yêu cầu cấp tài sản dành cho Asset Manager với 8 bước xử lý từ tìm kiếm đến thông báo. Màn hình hiển thị thông tin chi tiết tài sản và hỗ trợ quyết định phê duyệt/từ chối.

**Form tìm kiếm yêu cầu:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|--------|---------------|-----|------------|----------|------------|
| User | Input | Mã yêu cầu | M | Text | Y | 20 |
| User | Input | Tiêu đề | M | Text | Y | 150 |
| User | Select | Người tạo | M | List | Y | 20 |
| User | Select | Trạng thái | M | List | Y | 20 |
| User | Input | Ngày tạo | M | Date | Y | 20 |
| User | Select | Loại cấp tài sản | M | List | Y | 100 |
| User | Select | Người xử lý | M | List | Y | 20 |
| User | Input | Ngày xác nhận | M | Date | Y | 20 |

**Thông tin tài sản được cấp:**

| Operator | Action | Field name VN | M/O | Data rule |
|----------|--------|---------------|-----|-----------|
| System | Display | Mã tài sản | M | Hiển thị mặc định |
| System | Display | Tên Tài sản | M | Hiển thị mặc định |
| System | Display | Mô tả TS | M | Hiển thị mặc định |
| System | Display | Trạng thái TS | M | Hiển thị mặc định |
| System | Display | Phân nhóm TS (group name) | M | Hiển thị mặc định |
| System | Display | Nhóm TS (CAT1) | M | Hiển thị mặc định |
| System | Display | Số PO | M | Hiển thị mặc định |
| System | Display | Tên nhà cung cấp | O | Ẩn hiện tùy biến |
| System | Display | Nguyên giá TS (VAT incl) | M | Ẩn hiện tùy biến |
| System | Display | Mã TS liên quan | O | Ẩn hiện tùy biến |
| System | Display | Mô tả TS liên quan | O | Ẩn hiện tùy biến |
| System | Display | Tên người sử dụng | M | Hiển thị mặc định |
| System | Display | Tên đơn vị | M | Hiển thị mặc định |
| System | Display | Mã nhân viên | M | Ẩn hiện tùy biến |
| System | Display | Đơn vị sử dụng cha | M | Hiển thị mặc định |
| System | Display | Email nhân viên | M | Ẩn hiện tùy biến |
| System | Display | Địa chỉ đặt TS | O | Ẩn hiện tùy biến |
| System | Display | Tầng đặt TS | O | Ẩn hiện tùy biến |
| System | Display | Phòng đặt TS | O | Ẩn hiện tùy biến |
| System | Display | Ngày bắt đầu bảo hành | O | Ẩn hiện tùy biến |
| System | Display | Thời hạn bảo hành | O | Ẩn hiện tùy biến |
| System | Display | Ngày kết thúc bảo hành | O | Ẩn hiện tùy biến |
| System | Display | Công ty bảo hành | O | Ẩn hiện tùy biến |
| System | Display | Tên người liên hệ bảo hành | O | Ẩn hiện tùy biến |
| System | Display | Điện thoại người liên hệ | O | Ẩn hiện tùy biến |
| System | Display | Ngày bắt đầu sử dụng | O | Ẩn hiện tùy biến |

**Thông tin đơn vị nhận:**

| Operator | Action | Field name VN | M/O | Max length | Default value | Data source | Data rule |
|----------|--------|---------------|-----|------------|---------------|-------------|-----------|
| System/User | Display/Search/Select | Tên Người nhận | M | 50 | = Người khởi tạo | OMS | |
| System | Display | Tên ĐVKD/ Phòng ban HO | M | 50 | | OMS | Tự động nhận diện, hiển thị tên đơn vị Người khởi tạo |
| System | Display | Địa chỉ nhận | M | 150 | | OMS | Tự động nhận diện, hiển thị Khối theo Người khởi tạo |
| System/User | Display/Input | Điện thoại di động | M | 50 | | OMS | Tự động nhận diện, hiển thị số điện thoại của Người khởi tạo |

**Quy tắc nghiệp vụ:**
- Bắt buộc nhập lý do khi từ chối yêu cầu (trường text, độ dài tối đa 150 ký tự)
- Hệ thống tự động unlock tài sản khi yêu cầu bị từ chối
- AM có thể thêm/xóa file đính kèm nhưng không được xóa file do người khởi tạo đính kèm
- Sau khi phê duyệt, hệ thống tự động chuyển sang [quy trình tạo yêu cầu xuất kho](#429-cấp-tài-sản---tạo-yêu-cầu-xuất-kho)

---

#### 4.2.9. Cấp tài sản - Tạo yêu cầu xuất kho

#### 4.2.9.1. Thông số kỹ thuật giao diện người dùng

![5.4.1a. B5](images/5_4_1a__B5_image9.png)

**Các bước thực hiện quy trình:**
1. **Tạo yêu cầu xuất kho**: Khởi tạo yêu cầu xuất kho mới
2. **Cập nhật trạng thái yêu cầu**: Cập nhật status của yêu cầu
3. **Cập nhật tasklist**: Cập nhật danh sách công việc
4. **Thông báo cho WK**: Gửi thông báo đến người quản lý kho

**Luồng công việc:**
Quy trình tuần tự từ trái qua phải, sau khi hoàn thành 4 bước chính sẽ chuyển sang [quy trình tiếp nhận yêu cầu xuất kho](#4210-xuất-kho-từ-cấp-tài-sản---tiếp-nhận-yêu-cầu). Đây là một sub-process trong quy trình cấp tài sản tổng thể, thể hiện tính liên kết giữa các giai đoạn xử lý yêu cầu.

#### 4.2.9.2. Thông số kỹ thuật chi tiết

Quy trình tự động tạo yêu cầu xuất kho khi có phiếu cấp tài sản được phê duyệt. Hệ thống kế thừa toàn bộ thông tin từ phiếu cấp gốc và tự động xử lý các bước workflow.

**Thông tin chung yêu cầu:**

| Trường | Operator | Action | Tên trường | M/O | Kiểu | Editable | Max Length | Format | Default | Data Rule |
|--------|----------|---------|------------|-----|------|----------|------------|---------|---------|-----------|
| Số yêu cầu | System | Display | Số yêu cầu | M | Text | N | 50 | XK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| Ngày tạo | System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| Tiêu đề | System | Input | Tiêu đề | O | Text | Y | 150 | | | =Tiêu đề RQ Cấp/Thanh lý |

**Thông tin kho xuất:**

| Trường | Operator | Action | Tên trường | M/O | Kiểu | Editable | Max Length | Data Source | Data Rule |
|--------|----------|---------|------------|-----|------|----------|------------|-------------|-----------|
| Tên kho | System/User | Display/Search/Select | Tên kho | M | List | N | 50 | | = Thông tin kho trên RQ cấp/Thanh lý |
| Địa chỉ kho | System | Display | Địa chỉ kho | M | Text | Y | 50 | OMS | |
| Quản lý kho | System | Display | Quản lý kho | M | Text | N | 50 | OMS | |

**Thông tin đầu mối nhận hàng:**

| Trường | Operator | Action | Tên trường | M/O | Kiểu | Editable | Max Length |
|--------|----------|---------|------------|-----|------|----------|------------|
| Đầu mối | User | Input | Đầu mối | M | Text | Y | 50 |
| Số điện thoại | User | Input | Số điện thoại | M | Number | Y | 52 |
| Thời gian bàn giao | User | Input | Thời gian bàn giao | O | Date | Y | 50 |

**Cập nhật trạng thái và tasklist:**

| Đối tượng | Action | Trạng thái mới |
|-----------|---------|----------------|
| RQ Cấp tài sản/RQ Thanh lý | Update | Đã xác nhận/Đã cập nhật kết quả thanh lý/Đã phê duyệt kết quả thanh lý |
| RQ Xuất kho | Update | Chờ xuất kho |
| Tasklist AM | Update | Đã xử lý |
| Tasklist WK | Update | Cần xử lý |
| Tasklist AMP | Update | Đã xử lý |

**Quy tắc nghiệp vụ:**
- Danh sách tài sản phải kế thừa hoàn toàn từ phiếu cấp/thanh lý gốc
- Thông tin kho xuất phải khớp với thông tin kho trên RQ cấp/thanh lý
- Ghi chú mặc định phải chứa mã RQ cấp/thanh lý gốc
- Sau khi tạo thành công, chuyển sang [quy trình tiếp nhận yêu cầu](#4210-xuất-kho-từ-cấp-tài-sản---tiếp-nhận-yêu-cầu)

---

#### 4.2.10. Xuất kho từ cấp tài sản - Tiếp nhận yêu cầu

#### 4.2.10.1. Thông số kỹ thuật giao diện người dùng

![5.4.2a. B5](images/5_4_2a__B5_image10.png)

**Luồng chung (bước đầu):**
1. **Nhập thông tin tìm kiếm yêu cầu** - Điểm bắt đầu của quy trình
2. **Hiển thị kết quả tìm kiếm** - Hệ thống trả về danh sách yêu cầu
3. **Chọn yêu cầu cần xử lý** - Người dùng lựa chọn yêu cầu cụ thể

**Điểm quyết định:** Sau khi chọn yêu cầu, có hai hướng xử lý:

**Luồng từ chối (nhánh trên):**
- Cập nhật trạng thái yêu cầu (từ chối) → Unlock tài sản → Cập nhật tasklist → Thông báo cho AMP → Kết thúc quy trình

**Luồng đồng ý (nhánh dưới):**
- Cập nhật trạng thái yêu cầu (đồng ý) → Cập nhật tasklist → Thông báo cho Warehouse Manager → Chuyển sang [bước phê duyệt xuất kho](#4211-xuất-kho-từ-cấp-tài-sản---phê-duyệt-xuất-kho)

**Đặc điểm kỹ thuật:**
- Sử dụng ký hiệu diamond (hình thoi) cho điểm quyết định
- Có hai điểm kết thúc: một cho luồng từ chối, một cho luồng chuyển tiếp
- Mỗi bước được thể hiện bằng hộp chữ nhật màu xanh với icon minh họa
- Sơ đồ được vẽ theo chuẩn BPMN với hướng luồng từ trái sang phải

#### 4.2.10.2. Thông số kỹ thuật chi tiết

Giao diện tiếp nhận yêu cầu xuất kho từ warehouse keeper với khả năng tìm kiếm, xem chi tiết và quyết định phê duyệt/từ chối. Đặc biệt, quy trình ẩn nút "Từ chối" nếu yêu cầu xuất kho xuất phát từ yêu cầu thanh lý.

**Form tìm kiếm yêu cầu:**

| Operator | Field name VN | M/O | Field type | Editable | Max length |
|----------|---------------|-----|------------|----------|------------|
| User Input | Mã yêu cầu | M | Text | Y | 20 |
| User Input | Tiêu đề | M | Text | Y | 150 |
| User Select | Người tạo | M | List | Y | 20 |
| User Select | Trạng thái | M | List | Y | 20 |
| User Input | Ngày tạo | M | Date | Y | 20 |
| User Select | Nghiệp vụ kho | M | List | Y | 100 |
| User Select | Người xử lý | M | List | Y | 20 |
| User Input | Ngày xác nhận | M | Date | Y | 20 |

**Thông tin tài sản chi tiết:**

| Field name VN | M/O | Editable | Hiển thị |
|---------------|-----|----------|----------|
| Mã tài sản | M | N | Hiển thị mặc định |
| Tên Tài sản | M | N | Hiển thị mặc định |
| Mô tả TS | M | N | Hiển thị mặc định |
| Trạng thái TS | M | N | Hiển thị mặc định |
| Phân nhóm TS (group name) | M | N | Hiển thị mặc định |
| Nhóm TS (CAT1) | M | N | Hiển thị mặc định |
| Số PO | M | N | Hiển thị mặc định |
| Tên nhà cung cấp | O | N | Ẩn hiện tùy biến |
| Nguyên giá TS (VAT incl) | M | N | Ẩn hiện tùy biến |
| Mã TS liên quan | O | N | Ẩn hiện tùy biến |
| Mô tả TS liên quan | O | N | Ẩn hiện tùy biến |
| Tên người sử dụng | M | N | Hiển thị mặc định |
| Tên đơn vị | M | N | Hiển thị mặc định |
| Mã nhân viên | M | N | Ẩn hiện tùy biến |
| Đơn vị sử dụng cha | M | N | Hiển thị mặc định |
| Email nhân viên | M | N | Ẩn hiện tùy biến |

**Thông tin đầu mối nhận hàng:**

| Field name VN | M/O | Field type | Editable | Max length |
|---------------|-----|------------|----------|------------|
| Đầu mối | M | Text | Y | 50 |
| Số điện thoại | M | Number | Y | 52 |
| Thời gian bàn giao | O | Date | Y | 50 |
| Ghi chú | M | Text | Y | 150 |

**Quy tắc nghiệp vụ đặc biệt:**
- Ẩn nút "Từ chối" đối với RQ xuất kho liên kết với RQ thanh lý
- Hệ thống tự động lock/unlock tài sản khi từ chối yêu cầu
- Cập nhật multiple tasklist và gửi email notification theo workflow
- Khi đồng ý, chuyển sang [quy trình phê duyệt xuất kho](#4211-xuất-kho-từ-cấp-tài-sản---phê-duyệt-xuất-kho)

---

#### 4.2.11. Xuất kho từ cấp tài sản - Phê duyệt xuất kho

#### 4.2.11.1. Thông số kỹ thuật giao diện người dùng

![5.4.3a. B5](images/5_4_3a__B5_image11.png)

**Các bước thực hiện quy trình:**
1. **Luồng chính:** Bắt đầu → Nhập thông tin → Tìm kiếm → Chọn yêu cầu → Gateway quyết định
2. **Nhánh từ chối:** Cập nhật trạng thái yêu cầu → Thông báo BU user, WK → Kết thúc
3. **Nhánh duyệt:** Thực hiện song song 4 task (Cập nhật trạng thái, Mở khóa tài sản, Cập nhật tasklist, Thông báo AMP/WK) → Xuất báo cáo → Chuyển đến [màn hình nhận tài sản](#4212-xuất-kho-từ-cấp-tài-sản---nhận-tài-sản) → Kết thúc

**Các thành phần UI và quy trình:**
- **Start Event:** Điểm bắt đầu quy trình (hình tròn xanh)
- **Các Task boxes:** Các hộp màu xanh thể hiện các bước xử lý
- **Gateway quyết định:** Hình thoi vàng với hai nhánh "Từ chối" và "Duyệt"
- **Parallel Gateway:** Hình thoi với dấu "+" để xử lý đồng thời nhiều task
- **End Events:** Hai điểm kết thúc (hình tròn đỏ) cho hai luồng khác nhau

Sơ đồ thể hiện rõ ràng luồng xử lý có điều kiện và xử lý song song, đảm bảo tính nhất quán trong quy trình phê duyệt xuất kho.

#### 4.2.11.2. Thông số kỹ thuật chi tiết

Giao diện phê duyệt yêu cầu xuất kho từ cấp tài sản cho Warehouse Manager với 12 bước xử lý. Hệ thống có cơ chế lock/unlock tài sản và tùy biến hiển thị thông tin.

**Tiêu chí tìm kiếm yêu cầu:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|--------|---------------|-----|------------|----------|------------|
| User | Input | Mã yêu cầu | M | Text | Y | 20 |
| User | Input | Tiêu đề | M | Text | Y | 150 |
| User | Select | Người tạo | M | List | Y | 20 |
| User | Select | Trạng thái | M | List | Y | 20 |
| User | Input | Ngày tạo | M | Date | Y | 20 |
| User | Select | Loại cấp tài sản | M | List | Y | 100 |
| User | Select | Người xử lý | M | List | Y | 20 |
| User | Input | Ngày xác nhận | M | Date | Y | 20 |

**Thông tin tài sản xuất kho (26 trường):**

| Operator | Action | Field name VN | M/O | Hiển thị | Data rule |
|----------|--------|---------------|-----|----------|-----------|
| System | Display | Mã tài sản | M | Hiển thị mặc định | Từ danh mục tài sản trong phiếu cấp |
| System | Display | Tên Tài sản | M | Hiển thị mặc định | Từ danh mục tài sản trong phiếu cấp |
| System | Display | Mô tả TS | M | Hiển thị mặc định | Từ danh mục tài sản trong phiếu cấp |
| System | Display | Trạng thái TS | M | Hiển thị mặc định | Từ danh mục tài sản trong phiếu cấp |
| System | Display | Phân nhóm TS (group name) | M | Hiển thị mặc định | Từ danh mục tài sản trong phiếu cấp |
| System | Display | Nhóm TS (CAT1) | M | Hiển thị mặc định | Từ danh mục tài sản trong phiếu cấp |
| System | Display | Số PO | M | Hiển thị mặc định | Từ danh mục tài sản trong phiếu cấp |
| System | Display | Tên nhà cung cấp | O | Ẩn hiện tùy biến | Từ danh mục tài sản trong phiếu cấp |
| System | Display | Nguyên giá TS (VAT incl) | M | Ẩn hiện tùy biến | Từ danh mục tài sản trong phiếu cấp |
| System | Display | Mã TS liên quan | O | Ẩn hiện tùy biến | Từ danh mục tài sản trong phiếu cấp |
| System | Display | Mô tả TS liên quan | O | Ẩn hiện tùy biến | Từ danh mục tài sản trong phiếu cấp |
| System | Display | Tên người sử dụng | M | Hiển thị mặc định | Từ danh mục tài sản trong phiếu cấp |
| System | Display | Tên đơn vị | M | Hiển thị mặc định | Từ danh mục tài sản trong phiếu cấp |
| System | Display | Mã nhân viên | M | Ẩn hiện tùy biến | Từ danh mục tài sản trong phiếu cấp |
| System | Display | Đơn vị sử dụng cha | M | Hiển thị mặc định | Từ danh mục tài sản trong phiếu cấp |

**Quy trình cập nhật trạng thái:**

| Bước | Thực hiện | Hành động | Đối tượng | Trạng thái mới |
|------|-----------|-----------|-----------|---------------|
| 5 | Hệ thống | Update | RQ Cấp tài sản | Từ chối |
| 5 | Hệ thống | Update | RQ Xuất kho | Từ chối |
| 9 | Hệ thống | Update | RQ Cấp tài sản | Đã xác nhận |
| 9 | Hệ thống | Update | RQ Xuất kho | Chờ xác nhận |

**Quy tắc nghiệp vụ:**
- Tìm kiếm yêu cầu xuất kho với 8 tiêu chí lọc
- Hiển thị chi tiết 26 trường thông tin tài sản với tùy chọn ẩn/hiện
- Xử lý phê duyệt/từ chối với cập nhật trạng thái tự động
- Quản lý lock/unlock tài sản trong quá trình xử lý
- Khi phê duyệt, chuyển sang [quy trình nhận tài sản](#4212-xuất-kho-từ-cấp-tài-sản---nhận-tài-sản)

---

#### 4.2.12. Xuất kho từ cấp tài sản - Nhận tài sản

#### 4.2.12.1. Thông số kỹ thuật giao diện người dùng

![5.4.4a B6](images/5_4_4a_B6_image12.png)

**Các bước thực hiện quy trình:**
1. Bắt đầu quy trình
2. Nhập thông tin tìm kiếm yêu cầu
3. Hiển thị kết quả tìm kiếm
4. Chọn yêu cầu cần xử lý
5. Xác nhận yêu cầu (điểm phân nhánh)

**Nhánh từ chối:**
- Cập nhật trạng thái yêu cầu → Unlock tài sản → Cập nhật tasklist → Thông báo cho WK và AMP

**Nhánh xác nhận:**
- Cập nhật trạng thái yêu cầu → Unlock tài sản → Cập nhật tasklist → Thông báo cho WK và AMP

**Luồng công việc:**
Sơ đồ được tạo bằng công cụ Visual Paradigm Modeler, thể hiện một quy trình nghiệp vụ có tính tích hợp cao với các hệ thống bên ngoài. Cả hai nhánh đều kết thúc bằng việc thông báo cho các bên liên quan, đảm bảo tính nhất quán trong xử lý.

#### 4.2.12.2. Thông số kỹ thuật chi tiết

Giao diện nhận tài sản cho Business User trong quy trình xuất kho với 11 bước xử lý từ tìm kiếm đến hoàn tất xác nhận. Hệ thống tự động cập nhật đơn vị sử dụng và clear thông tin kho khi xác nhận nhận tài sản.

**Form tìm kiếm yêu cầu:**

| Operator | Field name VN | M/O | Field type | Editable | Max length |
|----------|---------------|-----|------------|----------|------------|
| User/Input | Mã yêu cầu | M | Text | Y | 20 |
| User/Input | Tiêu đề | M | Text | Y | 150 |
| User/Select | Người tạo | M | List | Y | 20 |
| User/Select | Trạng thái | M | List | Y | 20 |
| User/Input | Ngày tạo | M | Date | Y | 20 |
| User/Select | Nghiệp vụ kho | M | List | Y | 100 |
| User/Select | Người xử lý | M | List | Y | 20 |
| User/Input | Ngày xác nhận | M | Date | Y | 20 |

**Thông tin chung yêu cầu:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Format | Default value | Data rule |
|----------|--------|---------------|-----|------------|----------|------------|--------|---------------|-----------|
| System | Display | Số yêu cầu | M | Text | N | 50 | XK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| System | Input | Tiêu đề | O | Text | Y | 150 | | | |

**Thông tin kho xuất:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Data source | Data rule |
|----------|--------|---------------|-----|------------|----------|------------|-------------|-----------|
| System/User | Display/Search/Select | Tên kho | M | List | N | 50 | | = Thông tin kho trên RQ cấp tài sản |
| System | Display | Địa chỉ kho | M | Text | Y | 50 | OMS | |
| System | Display | Quản lý kho | M | Text | N | 50 | OMS | |

**Thông tin đầu mối nhận hàng:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|--------|---------------|-----|------------|----------|------------|
| User | Input | Đầu mối | M | Text | Y | 50 |
| User | Input | Số điện thoại | M | Number | Y | 52 |
| User | Input | Thời gian bàn giao | O | Date | Y | 50 |
| User | Input | Ghi chú | M | Text | Y | 150 |

**Quy tắc nghiệp vụ:**
- Format số yêu cầu: XK.YY.xxxx (YY=năm, xxxx=số chạy 1-9999 không dùng lại)
- Danh sách tài sản xuất kho phải bằng danh mục tài sản trong phiếu cấp/thanh lý
- Hỗ trợ hiển thị tùy biến cho một số trường thông tin (ẩn/hiện theo cấu hình)
- Bắt buộc nhập lý do khi từ chối yêu cầu
- Tự động unlock tài sản khi từ chối để cho phép request khác sử dụng
- Cập nhật đơn vị sử dụng và clear thông tin kho khi xác nhận nhận tài sản

Sau khi hoàn thành quy trình nhận tài sản, toàn bộ workflow cấp phát tài sản từ kho kết thúc và tài sản được chuyển giao chính thức cho người sử dụng cuối.

---

#### 4.2.13. Hủy yêu cầu xuất kho

#### 4.2.13.1. Thông số kỹ thuật giao diện người dùng

![5.5.1a B5](images/5_5_1a_B5_image13.png)

**Các bước thực hiện quy trình:**
1. **Nhập thông tin tìm kiếm yêu cầu**: Bước khởi tạo để tìm yêu cầu cần hủy
2. **Liên thi kết quả tìm kiếm**: Hiển thị danh sách kết quả
3. **Chọn yêu cầu cần xử lý**: Lựa chọn yêu cầu cụ thể từ danh sách
4. **Điểm quyết định "Hủy"**: Hình thoi màu vàng với hai lựa chọn
5. **Nhánh "Thoát"**: Dẫn đến điểm kết thúc với đường viền
6. **Nhánh "Hủy"**: Tiếp tục quy trình với các bước:
   - Nhận lý do hủy → Cập nhật trạng thái yêu cầu → Unlock tài sản → Cập nhật tasklist → Thông báo cho WK

**Luồng công việc**: 
Quy trình tuần tự với điểm phân nhánh quan trọng, cho phép người dùng quyết định tiếp tục hủy hoặc thoát, đảm bảo tính linh hoạt trong xử lý nghiệp vụ. Có các điểm "Về Bước 3" cho phép quay lại bước trước.

#### 4.2.13.2. Thông số kỹ thuật chi tiết

Chức năng "Hủy Yêu Cầu Xuất Kho" cho AMP với điều kiện yêu cầu phải có trạng thái khác "Đã xác nhận". Quy trình bao gồm 8 bước từ tìm kiếm đến thông báo kết quả.

**Điều kiện hủy:**
- Chỉ được hủy yêu cầu có trạng thái khác "Đã xác nhận"
- Ẩn nút "Từ chối" đối với RQ xuất kho liên kết với RQ thanh lý

**Form tìm kiếm yêu cầu:**

| Trường | Loại | Bắt buộc | Max Length | Editable | Kiểu |
|--------|------|----------|------------|----------|------|
| Mã yêu cầu | User Input | M | 20 | Y | Text |
| Tiêu đề | User Input | M | 150 | Y | Text |
| Người tạo | User Select | M | 20 | Y | List |
| Trạng thái | User Select | M | 20 | Y | List |
| Ngày tạo | User Input | M | 20 | Y | Date |
| Nghiệp vụ kho | User Select | M | 100 | Y | List |
| Người xử lý | User Select | M | 20 | Y | List |
| Ngày xác nhận | User Input | M | 20 | Y | Date |

**Thông tin yêu cầu - Thông tin chung:**

| Trường | Operator | Action | Bắt buộc | Max Length | Format | Default | Data Rule |
|--------|----------|--------|----------|------------|--------|---------|-----------|
| Số yêu cầu | System | Display | M | 50 | XK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 |
| Ngày tạo | System | Display | M | 50 | MM.DD.YYYY | Today | |
| Tiêu đề | System | Input | O | 150 | | | |

**Thông tin kho xuất:**

| Trường | Operator | Action | Bắt buộc | Max Length | Data Source | Data Rule |
|--------|----------|--------|----------|------------|-------------|-----------|
| Tên kho | System/User | Display/Search/Select | M | 50 | | Thông tin kho trên RQ cấp tài sản |
| Địa chỉ kho | System | Display | M | 50 | OMS | |
| Quản lý kho | System | Display | M | 50 | OMS | |

**Thông tin đầu mối nhận hàng:**

| Trường | Operator | Action | Bắt buộc | Max Length | Kiểu |
|--------|----------|--------|----------|------------|------|
| Đầu mối | User | Input | M | 50 | Text |
| Số điện thoại | User | Input | M | 52 | Number |
| Thời gian bàn giao | User | Input | O | 50 | Date |

**Quy tắc nghiệp vụ khi hủy:**
- Bắt buộc nhập lý do hủy (tối đa 150 ký tự)
- Hệ thống phải tự động unlock tài sản khi hủy yêu cầu
- Cập nhật trạng thái tài sản về trạng thái trước khi thanh lý
- Gửi email thông báo cho WK sau khi hủy
- Hiển thị đầy đủ 25+ trường thông tin tài sản với khả năng ẩn/hiện tùy biến

---

#### 4.2.14. Điều chuyển giữa các kho - Tạo yêu cầu

#### 4.2.14.1. Thông số kỹ thuật giao diện người dùng

![5.6.1a B6](images/5_6_1a_B6_image14.png)

**Các bước thực hiện quy trình:**
- **Start node**: Điểm bắt đầu quy trình "Tạo yêu cầu điều chuyển"
- **Decision diamond**: Gateway quyết định với 2 luồng - "Gửi" (tiếp tục) hoặc "Thoát" (kết thúc)
- **5 bước xử lý tuần tự**:
  1. "Lock tài sản" - Khóa tài sản để chuẩn bị điều chuyển
  2. "Cập nhật trạng thái yêu cầu" - Cập nhật status trong hệ thống  
  3. "Tìm và gán người phê duyệt" - Xác định approver cho yêu cầu
  4. "Cập nhật tasklist" - Cập nhật danh sách công việc
  5. "Thông báo Warehouse Mgr." - Gửi notification tới quản lý kho

**Luồng công việc:**
Quy trình theo mô hình tuần tự với điểm quyết định đầu tiên. Sau khi người dùng tạo yêu cầu, hệ thống sẽ thực hiện 5 bước xử lý tự động liên tiếp trước khi chuyển sang [bước phê duyệt yêu cầu](#4215-điều-chuyển-giữa-các-kho---phê-duyệt-yêu-cầu). Có exit point cho phép hủy bỏ quy trình nếu cần thiết.

#### 4.2.14.2. Thông số kỹ thuật chi tiết

Màn hình tạo yêu cầu điều chuyển tài sản giữa các kho với tích hợp OMS và workflow tự động. Hệ thống hỗ trợ tìm kiếm tài sản linh hoạt và tự động hóa 6 bước xử lý.

**Thông tin chung yêu cầu:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Format | Default value | Data rule |
|----------|--------|---------------|-----|------------|----------|------------|--------|---------------|-----------|
| User | Select | Tạo | M | Button | N | | | | |
| System | Display | Số yêu cầu | M | Text | N | 50 | CK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| User | Input | Tiêu đề | O | Text | Y | 150 | | | |
| User | Select | Thêm tài sản | M | Button | N | | | | |

**Form tìm kiếm tài sản:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|--------|---------------|-----|------------|----------|------------|
| User | Input | Mã tài sản | O | Text | N | 20 |
| User | Input | Tên tài sản | O | Text | Y | 20 |
| User | Select | Phân loại tài sản | O | List | N | 20 |
| User | Select | Nhóm tài sản | O | List | N | 20 |
| User | Input | PO number | O | Text | Y | 20 |
| User | Select | Trạng thái TS | O | List | N | 50 |
| User | Select | Tên nhà cung cấp | O | List | N | 50 |
| User | Input | Tên kho | O | List | Y | 50 |
| User | Select | Vị trí đặt tài sản | O | Text | N | 100 |

**Thông tin kho:**

| Section | Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Data source | Data rule |
|---------|----------|--------|---------------|-----|------------|----------|------------|-------------|-----------|
| Kho đi | System/User | Display/Search/Select | Tên kho | M | List | N | 50 | | |
| Kho đi | System | Display | Địa chỉ kho | M | Text | Y | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| Kho đi | System | Display | Quản lý kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho (Tên \| Phòng ban \| Email) |
| Kho nhập | User | Select | Tên kho | M | List | N | 50 | | |
| Kho nhập | System | Display | Địa chỉ kho | M | Text | Y | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| Kho nhập | System | Display | Quản lý kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho (Tên \| Phòng ban \| Email) |

**Thông tin đầu mối và quy trình:**

| Section | Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|---------|----------|--------|---------------|-----|------------|----------|------------|
| Đầu mối giao hàng | User | Input | Đầu mối | M | Text | Y | 50 |
| Đầu mối giao hàng | User | Input | Số điện thoại | M | Number | Y | 52 |
| Đầu mối giao hàng | User | Input | Thời gian bàn giao | O | Date | Y | 50 |
| Ghi chú | User | Input | Ghi chú | M | Text | Y | 150 |
| Quyết định | User | Select | Gửi | M | Button | N | |
| Quyết định | User | Select | Hủy | M | Button | N | |

**Quy tắc nghiệp vụ:**
- Tự động tạo số yêu cầu theo format CK.YY.xxxx
- Lock tài sản khi có yêu cầu để tránh xung đột với các request khác
- Tích hợp với OMS để lấy thông tin kho và quản lý kho
- Hỗ trợ tùy biến hiển thị các trường thông tin (ẩn/hiện theo nhu cầu)
- Sau khi gửi, chuyển sang [quy trình phê duyệt](#4215-điều-chuyển-giữa-các-kho---phê-duyệt-yêu-cầu)

---

#### 4.2.15. Điều chuyển giữa các kho - Phê duyệt yêu cầu

#### 4.2.15.1. Thông số kỹ thuật giao diện người dùng

![5.6.2a B5](images/5_6_2a_B5_image15.png)

**Các bước thực hiện quy trình:**
1. **Bắt đầu**: Nhập thông tin tìm kiếm yêu cầu
2. **Xử lý**: Hiển thị kết quả tìm kiếm → Chọn yêu cầu cần xử lý
3. **Quyết định**: Điểm phê duyệt với hai lựa chọn (Phê duyệt/Từ chối)

**Luồng công việc phê duyệt:**
- Cập nhật trạng thái yêu cầu → Unlock tài sản → Cập nhật tasklist → Thông báo cho WK → Bàn giao tài sản → Kết thúc

**Luồng công việc từ chối:**
- Cập nhật trạng thái → Thông báo cho WK khối đi và kho đến → Tạo biên bản xuất kho, nhập kho → Cập nhật thông tin kho cho tài sản → Bàn giao tại sân → Kết thúc

Sơ đồ này cung cấp cái nhìn tổng quan về toàn bộ quy trình phê duyệt điều chuyển kho, từ khâu tìm kiếm yêu cầu đến hoàn thành việc điều chuyển tài sản.

#### 4.2.15.2. Thông số kỹ thuật chi tiết

Giao diện phê duyệt yêu cầu điều chuyển tài sản giữa các kho cho Approver với 14 bước xử lý. Sau khi phê duyệt, hệ thống tự động tạo biên bản điều chuyển và cập nhật thông tin tài sản.

**Form tìm kiếm yêu cầu:**

| Field name VN | M/O | Field type | Editable | Max length | Operator | Action |
|---------------|-----|------------|----------|------------|----------|---------|
| Số yêu cầu | O | Text | Y | 20 | User | Input |
| Ngày tạo | O | Date | Y | 20 | User | Input |
| Tiêu đề | O | Text | Y | 150 | User | Input |
| Người tạo | O | List | Y | 20 | User | Select |
| Trạng thái yêu cầu | O | List | Y | 20 | User | Select |
| Người xử lý | O | List | Y | 20 | User | Select |
| Ngày xác nhận | O | Date | Y | 20 | User | Input |

**Thông tin chung yêu cầu:**

| Field name VN | M/O | Field type | Editable | Max length | Format | Default value | Data rule |
|---------------|-----|------------|----------|------------|---------|---------------|-----------|
| Số yêu cầu | M | Text | N | 50 | CK.YY.xxxx | - | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | - |
| Tiêu đề | O | Text | Y | 150 | - | - | - |

**Form tìm kiếm tài sản:**

| Field name VN | M/O | Field type | Editable | Max length |
|---------------|-----|------------|----------|------------|
| Mã tài sản | O | Text | N | 20 |
| Tên tài sản | O | Text | Y | 20 |
| Phân loại tài sản | O | List | N | 20 |
| Nhóm tài sản | O | List | N | 20 |
| PO number | O | Text | Y | 20 |
| Trạng thái TS | O | List | N | 50 |
| Tên nhà cung cấp | O | List | N | 50 |
| Vị trí đặt tài sản | O | Text | N | 100 |

**Thông tin kho:**

| Loại kho | Field name VN | M/O | Field type | Editable | Max length | Data source | Data rule |
|----------|---------------|-----|------------|----------|------------|-------------|-----------|
| Kho đi | Tên kho | M | List | N | 50 | - | - |
| Kho đi | Địa chỉ kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| Kho đi | Quản lý kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho (Tên \| Phòng ban \| Email) |
| Kho nhập | Tên kho | M | List | N | 50 | - | - |
| Kho nhập | Địa chỉ kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| Kho nhập | Quản lý kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho (Tên \| Phòng ban \| Email) |

**Thông tin đầu mối giao hàng:**

| Field name VN | M/O | Field type | Editable | Max length |
|---------------|-----|------------|----------|------------|
| Đầu mối | M | Text | N | 50 |
| Số điện thoại | M | Number | N | 52 |
| Thời gian bàn giao | O | Date | N | 50 |
| Ghi chú | M | Text | N | 150 |

**Quy tắc nghiệp vụ:**
- Tìm kiếm yêu cầu điều chuyển theo nhiều tiêu chí
- Hiển thị chi tiết thông tin tài sản với khả năng cấu hình ẩn/hiện các trường
- Cho phép Approver từ chối (yêu cầu nhập lý do) hoặc phê duyệt yêu cầu
- Tự động tạo phiếu xuất kho và nhập kho khi phê duyệt
- Cập nhật trạng thái lock/unlock tài sản theo từng bước xử lý
- Quản lý tasklist và thông báo email tự động
- Lưu trữ lịch sử xử lý và quá trình phê duyệt

Sau khi hoàn thành phê duyệt điều chuyển kho, toàn bộ module quản lý kho hoạt động đồng bộ để đảm bảo tài sản được theo dõi chính xác trong toàn hệ thống.

---

### 4.3. Status Management

Module Status Management định nghĩa một hệ thống trạng thái phức tạp cho việc quản lý tài sản với ba quy trình chính: cấp tài sản, thanh lý tài sản và điều chuyển tài sản. Mỗi quy trình được chia thành các sub-process với các trạng thái yêu cầu và trạng thái tài sản tương ứng.

**Cấu trúc hệ thống trạng thái:**
Hệ thống theo dõi cả Request Status (trạng thái yêu cầu) và Asset Status (trạng thái tài sản), cho phép kiểm soát chặt chẽ toàn bộ vòng đời của tài sản. Quy trình cấp tài sản được chia thành hai luồng: cấp tài sản không ở kho (luồng đơn giản) và cấp tài sản từ kho (luồng phức tạp với nhiều bước phê duyệt).

**Ma trận trạng thái - Cấp tài sản không ở kho:**

| Sub-process | PIC | Action | Request Status | Asset Status | Note |
|-------------|-----|--------|----------------|--------------|------|
| 1 Tạo yêu cầu | AMP | Lưu | Đang tạo | - | - |
| 1 Tạo yêu cầu | AMP | Gửi | Chờ xác nhận | - | - |
| 2. Xác nhận | BU User | Từ chối | Từ chối | - | - |
| 2. Xác nhận | BU User | Xác nhận | Đã xác nhận | Đang sử dụng | Đã xác nhận >>> Đã nhận tài sản |
| 2. Xác nhận | BU User | Bổ sung thông tin | Bổ sung thông tin | - | - |
| 3. Bổ sung TT | AMP | Bổ sung thông tin | Chờ xác nhận | - | - |

**Ma trận trạng thái - Cấp tài sản từ kho:**

| Sub-process | PIC | Action | Request Status | Warehouse Status | Asset Status |
|-------------|-----|--------|----------------|------------------|--------------|
| 1. Tạo yêu cầu | AMP | Lưu | Đang tạo | - | - |
| 1. Tạo yêu cầu | AMP | Gửi | Chờ xác nhận | - | - |
| 2. Phê duyệt | AM | Từ chối | Từ chối | - | - |
| 2. Phê duyệt | AM | Duyệt | Đã xác nhận | - | - |
| 3. Tạo yêu cầu | System | - | Đã xác nhận | Chờ xuất kho | - |
| 4. Xuất kho | WK | Từ chối | Từ chối | Từ chối | - |
| 4. Xuất kho | WK | Đồng ý | Đã xác nhận | Chờ phê duyệt | - |
| 5. Phê duyệt | Warehouse Mgr. | Từ chối | Từ chối | Từ chối | - |
| 5. Phê duyệt | Warehouse Mgr. | Duyệt | Đã xác nhận | Chờ xác nhận | - |
| 6. Nhận hàng | BU User | Từ chối | Từ chối | Từ chối | - |
| 6. Nhận hàng | BU User | Xác nhận | Đã xác nhận | Đã nhận tài sản | Đang sử dụng |

**Ma trận trạng thái - Thanh lý tài sản (Bán trực tiếp):**

| Sub-process | PIC | Action | Request Status | Warehouse Status | Asset Status | Note |
|-------------|-----|--------|----------------|------------------|--------------|------|
| 1. Tạo yêu cầu | AMP | Lưu | Đang tạo | - | - | - |
| 1. Tạo yêu cầu | AMP | Gửi | Chờ kiểm soát | - | - | - |
| 2. Kiểm soát | Checker | Từ chối | Từ chối | - | - | - |
| 2. Kiểm soát | Checker | Yêu cầu bổ sung thông tin | Bổ sung thông tin | - | - | - |
| 2. Kiểm soát | Checker | Đồng ý | Chờ phê duyệt | - | - | - |
| 3. Phê duyệt | Approver | Từ chối | Đang tạo | - | - | - |
| 3. Phê duyệt | Approver | Yêu cầu bổ sung thông tin | Bổ sung thông tin | - | - | - |
| 3. Phê duyệt | Approver | Phê duyệt | Chờ cập nhật kết quả | - | - | - |
| 4. Cập nhật kết quả thanh lý | AMP | Hủy | Đã hủy | - | - | - |
| 4. Cập nhật kết quả thanh lý | AMP | Cập nhật kết quả | Đã cập nhật kết quả thanh lý | - | Đã thanh lý | - |
| 5. Tạo yêu cầu xuất kho | System | Send | Đã cập nhật kết quả thanh lý | Chờ xuất kho | Đã thanh lý | - |
| 5.1 View yêu cầu xuất kho | AMP | Hủy | Đã hủy | Đã hủy | Trả lại trạng thái ban đầu trước khi thanh lý | - |

**Quy tắc nghiệp vụ quan trọng:**
- Hệ thống phải hỗ trợ các trạng thái yêu cầu: Đang tạo, Chờ xác nhận, Đã xác nhận, Từ chối, Bổ sung thông tin
- Hệ thống phải theo dõi trạng thái tài sản: Đang sử dụng, Đã nhập kho, Đã thanh lý
- Cần có cơ chế rollback trạng thái tài sản về "trạng thái ban đầu trước khi thanh lý" khi hủy yêu cầu
- Hệ thống phải tự động tạo yêu cầu xuất kho/nhập kho sau khi hoàn thành các bước phê duyệt

Quy trình thanh lý cũng có hai hình thức: bán trực tiếp và bán đấu giá,

---

## Phụ lục: Hình ảnh bổ sung

Các hình ảnh sau được trích xuất từ tài liệu gốc nhưng chưa được đặt vào nội dung chính:

![filename](images/filename)



---

*Generated by Claude Sonnet 4.5 from 37 sheet summaries*
*Headings: 61 | Internal Links: 53 | Images: 16*

*⚠️ Link validation warnings - some links may need manual review*
*✅ All image tokens converted successfully*
