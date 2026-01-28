# Tài Liệu Yêu Cầu Nghiệp vụ (BRD) - FAM UPGRADE WAVE 4

---

## 1. Table of Contents

1. [Table of Contents](#1-table-of-contents)
2. [Executive Summary](#2-executive-summary)
3. [Project Scope & Objectives](#3-project-scope-objectives)
4. [Stakeholders](#4-stakeholders)
5. [Business Requirements](#5-business-requirements)
   - [5.1. FAM UPGRADE - WAVE 4](#51-fam-upgrade-wave-4)
   - [5.2. Dashboard Tài sản](#52-dashboard-tài-sản)
   - [5.3. Module Quản lý Kho](#53-module-quản-lý-kho)
   - [5.4. Tạo yêu cầu nhập kho (Điều chuyển về kho)](#54-tạo-yêu-cầu-nhập-kho-điều-chuyển-về-kho)
   - [5.5. Tạo yêu cầu nhập kho](#55-tạo-yêu-cầu-nhập-kho)
   - [5.6. Phê duyệt yêu cầu xuất kho](#56-phê-duyệt-yêu-cầu-xuất-kho)
   - [5.7. Nhập kho thủ công](#57-nhập-kho-thủ-công)
   - [5.8. Hủy yêu cầu nhập kho](#58-hủy-yêu-cầu-nhập-kho)
   - [5.9. Cấp tài sản](#59-cấp-tài-sản)
   - [5.10. Hủy yêu cầu xuất kho](#510-hủy-yêu-cầu-xuất-kho)
   - [5.11. Tạo yêu cầu điều chuyển kho](#511-tạo-yêu-cầu-điều-chuyển-kho)
   - [5.12. Phê duyệt yêu cầu điều chuyển kho](#512-phê-duyệt-yêu-cầu-điều-chuyển-kho)
   - [5.13. Status](#513-status)
   - [5.14. Tasklist](#514-tasklist)
6. [Assumptions & Constraints](#6-assumptions-constraints)
7. [Dependencies](#7-dependencies)
8. [Acceptance Criteria](#8-acceptance-criteria)
9. [Glossary](#9-glossary)

---

## 2. Executive Summary

Dự án FAM UPGRADE - WAVE 4 nhằm nâng cấp hệ thống quản lý tài sản FAM (Fixed Asset Management) với các tính năng enhancement và phát triển mới. Các sản phẩm chính bao gồm [Dashboard tài sản](#52-dashboard-tài-sản) với khả năng trực quan hóa dữ liệu tùy chỉnh, [Module quản lý kho](#53-module-quản-lý-kho) hoàn toàn mới để quản lý xuất nhập kho tài sản, và các cải tiến giao diện và quy trình cấp phát/thanh lý tài sản.

Dự án tập trung vào ba nhóm chính: cải tiến giao diện và hiển thị tài sản, tối ưu hóa quy trình cấp phát và thanh lý tài sản, và phát triển hai module mới là [module kho (ưu tiên 1)](#53-module-quản-lý-kho) và module sửa chữa tài sản (ưu tiên 4). Hệ thống sẽ tích hợp với các hệ thống khác như OMS và EMS để đảm bảo đồng bộ dữ liệu và tự động hóa quy trình.

---

## 3. Project Scope & Objectives

### In Scope
- Dashboard tài sản với visualization tùy chỉnh theo nhiều tiêu chí
- Module quản lý kho hoàn toàn mới bao gồm xuất/nhập kho và điều chuyển tài sản
- Cải tiến giao diện danh sách tài sản và tùy chọn ẩn/hiện tài sản vô hiệu hóa
- Upload phiếu cấp tài sản theo danh sách hàng loạt
- Tự động xác nhận sau 20 ngày không phản hồi từ user
- Tích hợp OMS và đồng bộ EMS
- Luồng phê duyệt ATM cho quy trình thanh lý

### Out of Scope
- Module sửa chữa tài sản (dành cho phase tiếp theo)
- Tích hợp với ITSM và cổng hỗ trợ chi nhánh (phase sau)

### Objectives
- Tăng cường khả năng quản lý và theo dõi tài sản thông qua dashboard
- Tự động hóa quy trình xuất nhập kho và điều chuyển tài sản
- Cải thiện trải nghiệm người dùng và hiệu quả xử lý
- Đảm bảo tính minh bạch và kiểm soát trong quản lý tài sản

---

## 4. Stakeholders

| Vai trò | Mô tả | Trách nhiệm |
|---------|-------|-------------|
| **AMP (Asset Management Personnel)** | Nhân viên quản lý tài sản | Tạo và xử lý các yêu cầu liên quan đến tài sản |
| **BU User** | Người dùng đơn vị kinh doanh | Sử dụng tài sản và xác nhận các yêu cầu |
| **BU Manager** | Quản lý đơn vị kinh doanh | Phê duyệt các yêu cầu từ đơn vị |
| **Asset Manager (AM)** | Quản lý tài sản | Phê duyệt các yêu cầu cấp phát và thanh lý tài sản |
| **Warehouse Keeper (WK)** | Thủ kho | Thực hiện xuất nhập kho tài sản |
| **Warehouse Manager** | Quản lý kho | Phê duyệt các yêu cầu xuất nhập kho |
| **Checker** | Người kiểm soát | Kiểm soát các yêu cầu trước khi phê duyệt |
| **Approver** | Người phê duyệt | Phê duyệt các yêu cầu theo thẩm quyền |
| **System** | Hệ thống tự động | Xử lý các tác vụ tự động và tích hợp |

---

## 5. Business Requirements

### 5.1. FAM UPGRADE - WAVE 4

Nâng cấp hệ thống quản lý tài sản FAM trong đợt Wave 4 bao gồm 11 yêu cầu chính được phân loại theo mức độ ưu tiên từ 1-4. Các yêu cầu enhancement tập trung vào cải tiến giao diện người dùng, tối ưu hóa quy trình nghiệp vụ và phát triển các module mới.

**Các yêu cầu ưu tiên cao:**
1. **Dashboard tài sản** (Ưu tiên 1): Phát triển [Dashboard với khả năng visualization](#52-dashboard-tài-sản) tùy chỉnh theo nhiều tiêu chí
2. **Module kho mới** (Ưu tiên 1): Xây dựng [hệ thống quản lý xuất-nhập kho](#53-module-quản-lý-kho) tài sản hoàn toàn mới

**Các cải tiến quy trình:**
- Ẩn/hiện tài sản vô hiệu hóa trong danh sách (Ưu tiên 2)
- Cải tiến vị trí hiển thị các cột trong giao diện (Ưu tiên 2)
- Upload phiếu cấp tài sản theo danh sách hàng loạt (Ưu tiên 3)
- Tự động xác nhận sau 20 ngày không phản hồi (Ưu tiên 2)

**Tích hợp hệ thống:**
- [Tích hợp OMS](#7-dependencies) để đồng bộ tự động khi orgchart thay đổi (Ưu tiên 2)
- [Đồng bộ EMS](#7-dependencies) cho tiêu đề PO và thông tin bảo hành (Ưu tiên 2)
- Luồng phê duyệt ATM cho quy trình thanh lý (Ưu tiên 3)

Module sửa chữa tài sản (Ưu tiên 4) sẽ được triển khai trong phase tiếp theo với tích hợp ITSM và cổng hỗ trợ chi nhánh.

---

### 5.2. Dashboard Tài sản

Dashboard Tài sản cung cấp góc nhìn tổng quan và trực quan hóa dữ liệu tài sản của tổ chức, hỗ trợ việc đưa ra quyết định nhanh chóng thông qua các biểu đồ tương tác và chỉ số thống kê.

#### 5.2.1. Phạm vi dữ liệu và thống kê tổng quan

Dashboard hiển thị thông tin tài sản được phân bổ theo cơ cấu tổ chức, trạng thái tài sản, biến động theo thời gian, tỷ lệ sử dụng và các chỉ số bảo hành. Hệ thống loại trừ tài sản đã thanh lý và vô hiệu hóa khỏi các tính toán chính để đảm bảo độ chính xác.

**Thống kê tổng quan:**

| Content | Value | Type of chart | Note |
|---------|-------|---------------|------|
| 1. Total assets | Count số lượng (All tài sản - Đã thanh lý - Vô hiệu hóa) | | |
| 2. Total value | Sum nguyên giá (All tài sản - Đã thanh lý - Vô hiệu hóa) | | |
| 3. Warranty status | Tỷ lệ phần trăm theo số lượng tài sản còn hạn bảo hành/(All tài sản - Vô hiệu hóa - Đã thanh lý) | | |
| 4. Utilization rate | Tỷ lệ phần trăm theo số lượng tài sản có trạng thái đang sử dụng/(All tài sản - Vô hiệu hóa - Đã thanh lý) | | |

#### 5.2.2. Biểu đồ tương tác và bộ lọc

Hệ thống cung cấp các biểu đồ tương tác đa dạng (biểu đồ tròn, cột, đường, scatter) với khả năng hover và click để xem chi tiết. Bộ lọc dữ liệu linh hoạt cho phép người dùng phân tích theo nhiều tiêu chí khác nhau.

**Thông số biểu đồ:**

| Chart Name | Data | Chart Type | Note |
|------------|------|------------|------|
| Asset Distribution - Cơ cấu nhóm tài sản theo trạng thái | Nguyên giá | Sunburst (Vòng trong: Nhóm IT/ADM/CMD, Vòng ngoài: Trạng thái) | Khi Hover chuột thể hiện số lượng, và giá trị |
| Asset Distribution - Cơ cấu nhóm tài sản theo Vùng, theo Đơn vị sử dụng | Nguyên giá | Stacked Column | |
| Asset Value by Group Name | Nguyên giá | Column | |
| Asset Fluctuation Over Time (Month/Year) | Nguyên giá | Line | |
| Asset by Time in Use | Số lượng | Scatter | |

**Bộ lọc dùng chung:**

| Filter | Type | Description |
|--------|------|-------------|
| 1. Vùng | LOV | |
| 2. Đơn vị sử dụng | LOV đồng bộ từ OMS | |
| 3. CAT 1 | LOV | |
| 4. Group name | LOV | |
| 5. Asset status | LOV asset status (Không bao gồm Đã thanh lý, Vô hiệu hóa) | |

Dashboard tích hợp với [hệ thống OMS](#7-dependencies) để đồng bộ dữ liệu đơn vị sử dụng và hỗ trợ chức năng xuất dữ liệu ra Excel để phục vụ nhu cầu báo cáo.

---

### 5.3. Module Quản lý Kho

Module quản lý kho là một hệ thống hoàn toàn mới trong FAM UPGRADE WAVE 4, cung cấp khả năng quản lý xuất nhập kho và điều chuyển tài sản một cách tự động và có kiểm soát. Module này bao gồm các quy trình nghiệp vụ chính để đáp ứng nhu cầu quản lý tài sản trong kho.

#### 5.3.1. Các quy trình nghiệp vụ chính

Module hỗ trợ các quy trình sau:
- [Điều chuyển nội bộ và về kho](#54-tạo-yêu-cầu-nhập-kho-điều-chuyển-về-kho)
- [Nhập kho tự động và thủ công](#55-tạo-yêu-cầu-nhập-kho) và [#57-nhập-kho-thủ-công](#57-nhập-kho-thủ-công)
- [Xuất kho từ cấp tài sản](#56-phê-duyệt-yêu-cầu-xuất-kho) và [#59-cấp-tài-sản](#59-cấp-tài-sản)
- [Thanh lý tài sản](#513-status)
- [Điều chuyển giữa các kho](#511-tạo-yêu-cầu-điều-chuyển-kho) và [#512-phê-duyệt-yêu-cầu-điều-chuyển-kho](#512-phê-duyệt-yêu-cầu-điều-chuyển-kho)

#### 5.3.2. Tự động hóa quy trình

Hệ thống được thiết kế với khả năng tự động hóa cao:
- Tự động tạo yêu cầu xuất/nhập kho sau khi các quy trình cấp phát hoặc thanh lý được phê duyệt
- Tự động tạo biên bản và bút toán khi xuất/nhập kho trong điều chuyển kho  
- Khả năng rollback khi có từ chối ở các bước sau, yêu cầu sẽ quay về bước đầu

#### 5.3.3. Quản lý và theo dõi

Module cung cấp các tính năng quản lý:
- Tìm kiếm và [hủy yêu cầu](#58-hủy-yêu-cầu-nhập-kho) cho cả nhập kho và [xuất kho](#510-hủy-yêu-cầu-xuất-kho)
- Quản lý [trạng thái và workflow](#513-status) chi tiết cho từng quy trình
- Hệ thống [tasklist](#514-tasklist) để theo dõi công việc của từng vai trò
- Tích hợp với các hệ thống khác như OMS và EMS

Module này đóng vai trò trung tâm trong việc quản lý tài sản, đảm bảo tính minh bạch, kiểm soát và tự động hóa trong toàn bộ quy trình từ nhập kho đến cấp phát cho người sử dụng cuối.

---

### 5.4. Tạo yêu cầu nhập kho (Điều chuyển về kho)

#### 5.4.1. Thông số kỹ thuật giao diện người dùng

![Quy trình tạo yêu cầu nhập kho](images/5_1_1a_B5_image1.png)

**Các bước thực hiện quy trình:**
1. **Tạo yêu cầu nhập kho** - Bước khởi tạo yêu cầu trong hệ thống
2. **Cập nhật trạng thái yêu cầu** - Cập nhật status theo tiến độ xử lý
3. **Cập nhật tasklist** - Cập nhật danh sách công việc liên quan
4. **Thông báo cho Warehouse Mgr** - Gửi notification đến người quản lý kho
5. **Phê duyệt yêu cầu** - Bước phê duyệt cuối cùng chuyển sang [phê duyệt yêu cầu xuất kho](#56-phê-duyệt-yêu-cầu-xuất-kho)

**Luồng công việc:** Quy trình tuyến tính từ trái sang phải, mỗi bước được thực hiện tuần tự và có sự liên kết chặt chẽ với nhau. Quy trình kết thúc sau khi hoàn thành phê duyệt yêu cầu và chuyển tiếp đến [xác nhận nhập kho](#56-phê-duyệt-yêu-cầu-xuất-kho).

#### 5.4.2. Thông số kỹ thuật chi tiết

Quy trình này xử lý việc tạo yêu cầu nhập kho tự động khi có yêu cầu điều chuyển tài sản về kho. Hệ thống sẽ kế thừa toàn bộ thông tin từ yêu cầu điều chuyển ban đầu và tự động phân công cho Warehouse Manager xử lý tiếp.

**Thông tin chung yêu cầu nhập kho:**

| Field name VN | Operator | Action | M/O | Field type | Editable | Max length | Format | Default value | Data rule |
|---------------|----------|--------|-----|------------|----------|------------|---------|---------------|-----------|
| Số yêu cầu | System | Display | M | Text | N | 50 | NK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| Ngày tạo | System | Display | M | Date | N | 50 | MM.DD.YYYY | Today | |
| Tiêu đề | System | Display | M | Text | N | 150 | | | =Tiêu đề RQ điều chuyển |

**Danh sách tài sản nhập kho:**

| Field name VN | Operator | Action | M/O | Editable | Data rule |
|---------------|----------|--------|-----|----------|-----------|
| Mã tài sản | System | Display | M | N | Hiển thị mặc định |
| Tên Tài sản | System | Display | M | N | Hiển thị mặc định |
| Mô tả TS | System | Display | M | N | Hiển thị mặc định |
| Trạng thái TS | System | Display | M | N | Hiển thị mặc định |
| Phân nhóm TS (group name) | System | Display | M | N | Hiển thị mặc định |
| Nhóm TS (CAT1) | System | Display | M | N | Hiển thị mặc định |
| Số PO | System | Display | M | N | Hiển thị mặc định |
| Tên nhà cung cấp | System | Display | O | N | Ẩn hiện tùy biến |
| Nguyên giá TS (VAT incl) | System | Display | M | N | Ẩn hiện tùy biến |

**Thông tin kho nhập:**

| Field name VN | Operator | Action | M/O | Field type | Max length | Data source | Data rule |
|---------------|----------|--------|-----|------------|------------|-------------|-----------|
| Tên kho | System | Display | M | List | 50 | | = Kho trong RQ điều chuyển |
| Địa chỉ kho | System | Display | M | Text | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| Quản lý kho | System | Display | M | Text | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho (Tên \| Phòng ban \| Email) |

Trong quy trình này, tài sản sẽ được unlock khỏi yêu cầu điều chuyển nhưng được lock bởi yêu cầu nhập kho. Thông tin tài sản chưa được cập nhật cho đến khi [yêu cầu nhập kho hoàn thành](#56-phê-duyệt-yêu-cầu-xuất-kho).

---

### 5.5. Tạo yêu cầu nhập kho

#### 5.5.1. Thông số kỹ thuật giao diện người dùng

![Quy trình nhập kho thủ công](images/5_2_1a_B5_image4.png)

**Các bước thực hiện quy trình:**
1. Tạo yêu cầu nhập kho, định hình kèm lý do yêu cầu
2. Khóa tài sản  
3. Cập nhật trạng thái yêu cầu
4. Cập nhật danh sách người nhận
5. Gửi email thông báo cho WM
6. Phê duyệt yêu cầu

**Luồng công việc:** Workflow có cấu trúc tuyến tính với một điểm quyết định. Sau bước đầu tiên, quy trình có thể kết thúc sớm (Thoát) hoặc tiếp tục qua chuỗi các bước xử lý. Luồng chính đi qua tất cả các bước từ khóa tài sản đến gửi email, cuối cùng đến bước phê duyệt.

#### 5.5.2. Thông số kỹ thuật chi tiết

Giao diện "Nhập kho thủ công" cho phép người dùng tạo yêu cầu nhập kho tài sản với đầy đủ thông tin chi tiết và quy trình xử lý tự động.

**Đặc tả trường thông tin chung:**

| Trường | Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Format | Default value | Data source | Data rule |
|--------|----------|---------|---------------|-----|------------|----------|------------|--------|---------------|-------------|-----------|
| Số yêu cầu | System | Display | Số yêu cầu | M | Text | N | 50 | NK.YY.xxxx | | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| Ngày tạo | System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | | |
| Tiêu đề | User | Input | Tiêu đề | O | Text | Y | 150 | | | | |
| Thêm tài sản | User | Select | Thêm tài sản | M | Button | N | | | | | |

**Đặc tả trường tìm kiếm tài sản:**

| Trường | Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|--------|----------|---------|---------------|-----|------------|----------|------------|
| Mã tài sản | User | Input | Mã tài sản | O | Text | N | 20 |
| Tên tài sản | User | Input | Tên tài sản | O | Text | Y | 20 |
| Phân loại tài sản | User | Select | Phân loại tài sản | O | List | N | 20 |
| Nhóm tài sản | User | Select | Nhóm tài sản | O | List | N | 20 |
| PO number | User | Input | PO number | O | Text | Y | 20 |
| Trạng thái TS | User | Select | Trạng thái TS | O | List | N | 50 |
| Tên nhà cung cấp | User | Select | Tên nhà cung cấp | O | List | N | 50 |
| Tên kho | User | Input | Tên kho | O | List | Y | 50 |
| Vị trí đặt tài sản | User | Select | Vị trí đặt tài sản | O | Text | N | 100 |

Quy trình bao gồm 5 bước tự động: tạo yêu cầu với đính kèm và xem lại, khóa tài sản để tránh xung đột, cập nhật trạng thái yêu cầu thành "Chờ phê duyệt", cập nhật tasklist cho Warehouse Manager (WM), và gửi thông báo email cho WM. Sau khi tạo thành công, quy trình chuyển sang [phê duyệt yêu cầu xuất kho](#56-phê-duyệt-yêu-cầu-xuất-kho).

---

### 5.6. Phê duyệt yêu cầu xuất kho

#### 5.6.1. Thông số kỹ thuật giao diện người dùng

![Quy trình phê duyệt yêu cầu](images/5_2_2a_B5_image5.png)

**Các bước thực hiện quy trình:**
- **Bước 1-3**: Chuỗi các hộp xanh dương thực hiện tuần tự (Nhập thông tin tìm kiếm yêu cầu → Hiển thị kết quả tìm kiếm → Chọn, xem yêu cầu)
- **Gateway phê duyệt**: Hình thoi vàng với dấu "+" để ra quyết định phê duyệt
- **Luồng từ chối**: Hộp xanh dương "Nhập lý do từ chối" với gateway quyết định "Đồng ý" dẫn đến chuỗi cập nhật (Unlock tài sản → Cập nhật trạng thái yêu cầu → Cập nhật tasklist → Gửi email thông báo)

**Luồng công việc:**
- Quy trình có hai nhánh chính từ gateway phê duyệt
- Nhánh phê duyệt (trên): Thực hiện chuỗi cập nhật và chuyển tiếp đến [xác nhận nhập kho](#58-hủy-yêu-cầu-nhập-kho)
- Nhánh từ chối (dưới): Yêu cầu nhập lý do từ chối, sau đó thực hiện chuỗi cập nhật tương tự

#### 5.6.2. Thông số kỹ thuật chi tiết

Giao diện phê duyệt yêu cầu nhập kho thủ công cho Warehouse Manager với khả năng tìm kiếm, xem xét và đưa ra quyết định phê duyệt hoặc từ chối.

**Bảng thông tin tìm kiếm yêu cầu:**

| Field name VN | M/O | Field type | Editable | Max length | Operator | Action |
|---------------|-----|------------|----------|------------|----------|---------|
| Số yêu cầu | O | Text | Y | 20 | User | Input |
| Ngày tạo | O | Date | Y | 20 | User | Input |
| Tiêu đề | O | Text | Y | 150 | User | Input |
| Người tạo | O | List | Y | 20 | User | Select |
| Trạng thái yêu cầu | O | List | Y | 20 | User | Select |
| Người xử lý | O | List | Y | 20 | User | Select |
| Ngày xác nhận | O | Date | Y | 20 | User | Input |

**Bảng thông tin tài sản nhập kho:**

| Field name VN | M/O | Field type | Editable | Data rule |
|---------------|-----|------------|----------|-----------|
| Mã tài sản | M | - | N | Hiển thị mặc định |
| Tên Tài sản | M | - | N | Hiển thị mặc định |
| Mô tả TS | M | - | N | Hiển thị mặc định |
| Trạng thái TS | M | - | N | Hiển thị mặc định |
| Phân nhóm TS (group name) | M | - | N | Hiển thị mặc định |
| Nhóm TS (CAT1) | M | - | N | Hiển thị mặc định |
| Số PO | M | - | N | Hiển thị mặc định |
| Tên nhà cung cấp | O | - | N | Ẩn hiện tùy biến |
| Nguyên giá TS (VAT incl) | M | - | N | Ẩn hiện tùy biến |

Warehouse Manager có thể thực hiện hai hành động chính: từ chối (với lý do bắt buộc, tối đa 150 ký tự) hoặc phê duyệt. Hệ thống sẽ tự động unlock tài sản nếu từ chối, cập nhật tasklist cho các bên liên quan và gửi thông báo email tương ứng. Sau khi phê duyệt, quy trình chuyển sang [xác nhận nhập kho](#58-hủy-yêu-cầu-nhập-kho).

---

### 5.7. Nhập kho thủ công

#### 5.7.1. Thông số kỹ thuật giao diện người dùng  

![Quy trình xác nhận nhập kho](images/5_2_3a_B6_image6.png)

**Luồng công việc chi tiết:**
1. **Bước 1**: Nhập thông tin tìm kiếm yêu cầu
2. **Bước 2**: Hiển thị kết quả tìm kiếm  
3. **Bước 3**: Chọn, xem chi tiết yêu cầu
4. **Điểm quyết định 1**: Xác nhận - phân nhánh thành "Đồng ý" và "Từ chối"

**Nhánh Đồng ý:**
- **Bước 5**: Nhập thông tin nhận hàng
- **Bước 10**: Unlock, update thông tin tài sản
- **Bước 11**: Cập nhật trạng thái yêu cầu
- **Bước 12**: Cập nhật tasklist
- **Bước 13**: Gửi email thông báo

**Nhánh Từ chối:**
- **Bước 4**: Nhập lý do từ chối
- **Bước tương ứng**: Unlock tài sản, cập nhật trạng thái yêu cầu, cập nhật tasklist, gửi email thông báo

#### 5.7.2. Thông số kỹ thuật chi tiết

Giao diện xác nhận nhập kho thủ công cho Warehouse Keeper (WK) với 13 bước từ tìm kiếm yêu cầu đến thông báo hoàn tất.

**Bảng thông tin tìm kiếm yêu cầu:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|--------|---------------|-----|------------|----------|------------|
| User | Input | Số yêu cầu | O | Text | Y | 20 |
| User | Input | Ngày tạo | O | Date | Y | 20 |
| User | Input | Tiêu đề | O | Text | Y | 150 |
| User | Select | Người tạo | O | List | Y | 20 |
| User | Select | Trạng thái yêu cầu | O | List | Y | 20 |
| User | Select | Người xử lý | O | List | Y | 20 |
| User | Input | Ngày xác nhận | O | Date | Y | 20 |

**Bảng thông tin tài sản chi tiết:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Data rule |
|----------|--------|---------------|-----|------------|----------|-----------|
| System | Display | Mã tài sản | M | | N | Hiển thị mặc định |
| System | Display | Tên Tài sản | M | | N | Hiển thị mặc định |
| System | Display | Mô tả TS | M | | N | Hiển thị mặc định |
| System | Display | Trạng thái TS | M | | N | Hiển thị mặc định |
| System | Display | Phân nhóm TS (group name) | M | | N | Hiển thị mặc định |
| System | Display | Nhóm TS (CAT1) | M | | N | Hiển thị mặc định |
| System | Display | Số PO | M | | N | Hiển thị mặc định |
| System | Display | Tên nhà cung cấp | O | | N | Ẩn hiện tùy biến |
| System | Display | Nguyên giá TS (VAT incl) | M | | N | Ẩn hiện tùy biến |

WK có thể từ chối (yêu cầu nhập lý do, hệ thống unlock tài sản và chuyển tasklist về AMP) hoặc xác nhận nhập kho (cập nhật trạng thái "Đã nhập kho"). Đặc biệt, khi xác nhận nhập kho, hệ thống tự động cập nhật "Ngày bắt đầu sử dụng" nếu trường này đang để trống, đồng thời cập nhật thông tin đơn vị sử dụng và tên kho cho tài sản.

---

### 5.8. Hủy yêu cầu nhập kho

#### 5.8.1. Thông số kỹ thuật giao diện người dùng

![Quy trình hủy yêu cầu nhập kho](images/5_3_1a_B5_image7.png)

**Các bước thực hiện quy trình:**
1. **Nhập thông tin tìm kiếm yêu cầu** - Bước đầu để tìm kiếm yêu cầu nhập kho
2. **Chọn thị kết quả tìm kiếm** - Hiển thị danh sách các yêu cầu phù hợp  
3. **Chọn yêu cầu cần xử lý** - Lựa chọn yêu cầu cụ thể để xử lý
4. **Decision Point**: Quyết định từ chối hoặc đồng ý xử lý yêu cầu

**Luồng công việc:**
- **Luồng chính**: Từ nhập thông tin → hiển thị kết quả → chọn yêu cầu → quyết định xử lý
- **Nếu chọn "Hủy"**: Nhập lý do hủy → Cập nhật trạng thái yêu cầu → Unlock tài sản → Cập nhật tasklist → Thông báo cho BU user → Kết thúc
- **Nếu chọn "Thoát"**: Quy trình kết thúc sớm với ghi chú "Về bước 3"

#### 5.8.2. Thông số kỹ thuật chi tiết

Giao diện "HỦY YÊU CẦU NHẬP KHO" cho phép hủy các yêu cầu nhập kho tài sản chưa được thực hiện. Điều kiện áp dụng là yêu cầu phải được gửi thành công và có trạng thái khác "Đã nhập kho".

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

**Bảng thông tin tài sản nhập kho:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Data rule |
|----------|--------|---------------|-----|------------|----------|-----------|
| System | Display | Mã tài sản | M | | N | Hiển thị mặc định |
| System | Display | Tên Tài sản | M | | N | Hiển thị mặc định |
| System | Display | Mô tả TS | M | | N | Hiển thị mặc định |
| System | Display | Trạng thái TS | M | | N | Hiển thị mặc định |
| System | Display | Phân nhóm TS (group name) | M | | N | Hiển thị mặc định |
| System | Display | Nhóm TS (CAT1) | M | | N | Hiển thị mặc định |
| System | Display | Số PO | M | | N | Hiển thị mặc định |
| System | Display | Tên nhà cung cấp | O | | N | Ẩn hiện tùy biến |
| System | Display | Nguyên giá TS (VAT incl) | M | | N | Ẩn hiện tùy biến |

Quy trình hủy bao gồm 8 bước: tìm kiếm yêu cầu, hiển thị kết quả, xem chi tiết yêu cầu, nhập lý do hủy (bắt buộc), unlock tài sản để có thể được sử dụng cho request khác, cập nhật trạng thái thành "Đã hủy", cập nhật tasklist cho các bên liên quan và gửi thông báo email cho BU/user. Sau khi hủy thành công, tài sản sẽ được giải phóng và có thể sử dụng cho [các yêu cầu khác](#53-module-quản-lý-kho).

---

### 5.9. Cấp tài sản

#### 5.9.1. Thông số kỹ thuật giao diện người dùng

![Quy trình phê duyệt yêu cầu cấp tài sản](images/5_4_0a_A4_image8.png)

**Các bước thực hiện quy trình:**
- **Bước 1**: "Nhận thông tin tìm kiếm yêu cầu" - Nhận input từ hệ thống
- **Bước 2**: "Hiển thị kết quả tìm kiếm" - Hiển thị danh sách yêu cầu để lựa chọn
- **Bước 3**: "Chọn yêu cầu cần xử lý" - AM thực hiện lựa chọn yêu cầu cụ thể

**Điểm quyết định**: Phê duyệt hoặc từ chối yêu cầu

**Nhánh phê duyệt:**
- "Nhập dữ liệu tự chọn" 
- "Cập nhật trạng thái yêu cầu"
- "Unlock tài sản" 
- "Cập nhật tasklist"
- "Thông báo cho AMP"
- Kết thúc

**Nhánh từ chối:** Chuyển đến [quy trình tạo yêu cầu xuất kho](#510-hủy-yêu-cầu-xuất-kho) và kết thúc tại điểm dừng riêng.

#### 5.9.2. Thông số kỹ thuật chi tiết

Quy trình phê duyệt yêu cầu cấp tài sản được thực hiện bởi Asset Manager (AM) với 8 bước xử lý từ tìm kiếm đến phê duyệt cuối cùng.

**Bảng tìm kiếm yêu cầu - Input fields:**

| STT | Tab/Section | Operator | Action | Field Name VN | M/O | Field Type | Editable | Max Length |
|-----|-------------|----------|--------|---------------|-----|------------|----------|------------|
| 1 | Tìm kiếm yêu cầu | User | Input | Mã yêu cầu | M | Text | Y | 20 |
| 2 | Tìm kiếm yêu cầu | User | Input | Tiêu đề | M | Text | Y | 150 |
| 3 | Tìm kiếm yêu cầu | User | Select | Người tạo | M | List | Y | 20 |
| 4 | Tìm kiếm yêu cầu | User | Select | Trạng thái | M | List | Y | 20 |
| 5 | Tìm kiếm yêu cầu | User | Input | Ngày tạo | M | Date | Y | 20 |
| 6 | Tìm kiếm yêu cầu | User | Select | Loại cấp tài sản | M | List | Y | 100 |
| 7 | Tìm kiếm yêu cầu | User | Select | Người xử lý | M | List | Y | 20 |
| 8 | Tìm kiếm yêu cầu | User | Input | Ngày xác nhận | M | Date | Y | 20 |

**Bảng thông tin tài sản cần cấp (một phần):**

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

AM có thể xem chi tiết đầy đủ thông tin tài sản (20+ thuộc tính) với tùy chọn hiển thị mặc định/ẩn hiện tùy biến. Khi từ chối, bắt buộc nhập lý do và hệ thống tự động unlock tài sản để cho phép cấp cho request khác. Sau khi phê duyệt, quy trình tự động [tạo yêu cầu xuất kho](#510-hủy-yêu-cầu-xuất-kho) và cập nhật tasklist cho AMP.

#### 5.9.3. Tạo yêu cầu xuất kho

![Quy trình tạo yêu cầu xuất kho](images/5_4_1a__B5_image9.png)

**Các bước thực hiện quy trình:**
1. **Tạo yêu cầu xuất kho**: Bước khởi tạo yêu cầu trong hệ thống
2. **Cập nhật trạng thái yêu cầu**: Cập nhật status của yêu cầu vừa tạo
3. **Cập nhật tasklist**: Cập nhật danh sách công việc cần thực hiện
4. **Thông báo cho WK**: Gửi notification đến người phụ trách warehouse

**Luồng công việc:**
- Quy trình bắt đầu từ system trigger
- Thực hiện tuần tự 4 bước xử lý chính
- Sau đó chuyển sang [quy trình tiếp nhận yêu cầu xuất kho](#510-hủy-yêu-cầu-xuất-kho)
- Kết thúc quy trình tại điểm cuối

Hệ thống sẽ tự động tạo yêu cầu xuất kho dựa trên thông tin từ phiếu cấp/thanh lý, bao gồm đầy đủ thông tin tài sản, thông tin kho xuất, và thông tin người nhận. Số yêu cầu theo format XK.YY.xxxx (YY = năm, xxxx = số chạy 1-9999) và hệ thống tự động cập nhật tasklist cho các vai trò AM, WK, AMP.

#### 5.9.4. Tiếp nhận yêu cầu xuất kho  

![Quy trình tiếp nhận yêu cầu xuất kho](images/5_4_2a__B5_image10.png)

**Luồng công việc:**
- **Luồng chính**: Từ nhập thông tin → hiển thị kết quả → chọn yêu cầu → quyết định xử lý
- **Luồng từ chối** (nhánh trên): Cập nhật trạng thái từ chối → Unlock tài sản → Cập nhật tasklist → Thông báo cho AXP → Kết thúc
- **Luồng đồng ý** (nhánh dưới): Cập nhật trạng thái yêu cầu → Cập nhật tasklist → Thông báo cho Warehouse Mgr → Chuyển sang [phê duyệt xuất kho](#510-hủy-yêu-cầu-xuất-kho)

Quy trình tiếp nhận yêu cầu xuất kho cho phép người xử lý từ chối hoặc đồng ý xử lý yêu cầu. Nếu từ chối, hệ thống unlock tài sản và thông báo cho AXP. Nếu đồng ý, quy trình tiếp tục với việc thông báo cho Warehouse Manager và chuyển sang bước phê duyệt xuất kho.

#### 5.9.5. Phê duyệt xuất kho

![Quy trình phê duyệt yêu cầu xuất kho](images/5_4_3a__B5_image11.png)

**Luồng công việc được thể hiện:**

1. **Bước khởi tạo**: Bắt đầu từ "Nhập thông tin tìm kiếm yêu cầu"
2. **Bước tìm kiếm**: "Hiển thị kết quả tìm kiếm" và "Chọn yêu cầu cần xử lý"
3. **Điểm quyết định**: Phân nhánh thành hai luồng song song
4. **Nhánh từ chối** (luồng trên):
   - Nhập lý do từ chối → Cập nhật trạng thái yêu cầu → Unlock tài sản → Cập nhật tasklist → Thông báo cho AMP/WK
5. **Nhánh duyệt** (luồng dưới):
   - Cập nhật trạng thái yêu cầu → Cập nhật tasklist → Thông báo cho BU user, WK → Xuất hàng → Chuyển đến [nhận tài sản](#510-hủy-yêu-cầu-xuất-kho)

Warehouse Manager có thể phê duyệt hoặc từ chối yêu cầu xuất kho. Nếu yêu cầu xuất kho xuất phát từ yêu cầu thanh lý, nút "Từ chối" sẽ bị ẩn. Hệ thống tự động unlock tài sản khi yêu cầu bị từ chối để cho phép pickup cho request khác.

#### 5.9.6. Nhận tài sản

![Quy trình nhận tài sản](images/5_4_4a_B6_image12.png)

**Các bước thực hiện quy trình:**
1. **Nhập thông tin tìm kiếm yêu cầu** (bước khởi đầu)
2. **Hiển thị kết quả tìm kiếm**
3. **Chọn yêu cầu cần xử lý**
4. **Điểm quyết định** với hai lựa chọn: "Từ chối" và "Xác nhận"

**Luồng công việc:**
- **Luồng từ chối** (trên): Cập nhật trạng thái từ chối → Unlock tài sản → Cập nhật tasklist → Thông báo cho WK và AMP → Kết thúc
- **Luồng xác nhận** (dưới): Cập nhật trạng thái xác nhận → Unlock tài sản → Cập nhật tasklist → Thông báo cho WK và AMP → Kết thúc

Quy trình nhận tài sản cho phép BU user xác nhận hoặc từ chối việc nhận tài sản từ kho. Cả hai trường hợp đều có các bước xử lý tương tự sau khi đưa ra quyết định, bao gồm unlock tài sản, cập nhật tasklist và thông báo cho các bên liên quan.

---

### 5.10. Hủy yêu cầu xuất kho

#### 5.10.1. Thông số kỹ thuật giao diện người dùng

![Quy trình hủy yêu cầu xuất kho](images/5_5_1a_B5_image13.png)

**Các bước thực hiện quy trình:**
- **Start node** (hình tròn xanh): Điểm bắt đầu quy trình
- **Hộp xanh "Nhập thông tin tìm kiếm yêu cầu"**: Bước đầu tiên cho phép nhập thông tin
- **Hộp xanh "Hiển thị kết quả tìm kiếm"**: Hiển thị danh sách yêu cầu phù hợp
- **Hộp xanh "Chọn yêu cầu cần xử lý"**: Cho phép chọn yêu cầu cụ thể
- **Diamond decision "Hủy"**: Điểm quyết định với 2 lựa chọn
- **Các hộp xanh xử lý hủy**: "Nhập lý do hủy", "Cập nhật trạng thái yêu cầu", "Unlock tài sản", "Cập nhật tasklist", "Thông báo cho WK"

**Luồng công việc:**
Quy trình có luồng chính từ trái sang phải, với một nhánh rẽ tại điểm quyết định "Hủy". Nếu chọn "Hủy", quy trình tiếp tục với 5 bước xử lý tuần tự. Nếu chọn "Thoát", quy trình kết thúc ngay và có ghi chú "Về bước 3" cho thấy có thể quay lại bước trước đó trong quy trình tổng thể.

#### 5.10.2. Thông số kỹ thuật chi tiết

Giao diện "HỦY YÊU CẦU XUẤT KHO" cho phép Asset Manager (AMP) hủy các yêu cầu xuất kho tài sản với điều kiện yêu cầu chưa được xác nhận.

**Bảng tìm kiếm yêu cầu xuất kho:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Format |
|----------|--------|---------------|-----|------------|----------|------------|---------|
| User | Input | Mã yêu cầu | M | Text | Y | 20 | |
| User | Input | Tiêu đề | M | Text | Y | 150 | |
| User | Select | Người tạo | M | List | Y | 20 | |
| User | Select | Trạng thái | M | List | Y | 20 | |
| User | Input | Ngày tạo | M | Date | Y | 20 | |
| User | Select | Nghiệp vụ kho | M | List | Y | 100 | |
| User | Select | Người xử lý | M | List | Y | 20 | |
| User | Input | Ngày xác nhận | M | Date | Y | 20 | |

**Bảng thông tin chung yêu cầu:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Format | Default value | Data rule |
|----------|--------|---------------|-----|------------|----------|------------|---------|---------------|-----------|
| System | Display | Số yêu cầu | M | Text | N | 50 | XK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| System | Input | Tiêu đề | O | Text | Y | 150 | | | |

Điều kiện hủy: Yêu cầu xuất kho đã tạo thành công và có trạng thái ≠ "Đã xác nhận". Khi hủy, bắt buộc nhập lý do (trường text, độ dài tối đa 150 ký tự). Hệ thống tự động unlock tài sản khi hủy để cho phép sử dụng trong request khác và cập nhật trạng thái về "Đã hủy" cho cả RQ cấp/thanh lý và RQ xuất kho. Đặc biệt, nút "Từ chối" bị ẩn đối với RQ xuất kho liên kết với RQ thanh lý, đảm bảo quy trình thanh lý không bị gián đoạn.

---

### 5.11. Tạo yêu cầu điều chuyển kho

#### 5.11.1. Thông số kỹ thuật giao diện người dùng

![Quy trình tạo yêu cầu điều chuyển kho](images/5_6_1a_B6_image14.png)

**Các bước thực hiện quy trình:**
1. **Tạo yêu cầu điều chuyển kho, đính kèm, xem lại yêu cầu** - Bước khởi tạo
2. **Lock tài sản** - Khóa tài sản để tránh xung đột
3. **Cập nhật trạng thái cầu** - Cập nhật status trong hệ thống  
4. **Tìm và gán người phê duyệt** - Xác định approver phù hợp
5. **Cập nhật tasklist** - Cập nhật danh sách công việc
6. **Thông báo Warehouse Mgr** - Gửi notification cho quản lý kho

**Luồng công việc:**
Quy trình có luồng tuyến tính chính từ tạo yêu cầu đến thông báo, với một điểm gateway cho phép thoát sớm. Sau khi hoàn thành các bước xử lý, quy trình chuyển sang [phê duyệt yêu cầu điều chuyển kho](#512-phê-duyệt-yêu-cầu-điều-chuyển-kho). Thiết kế này đảm bảo tính nhất quán và kiểm soát trong quá trình điều chuyển tài sản giữa các kho.

#### 5.11.2. Thông số kỹ thuật chi tiết

Giao diện tạo yêu cầu điều chuyển kho tài sản bao gồm các phần: thông tin chung, tìm kiếm và chọn tài sản cần điều chuyển, thông tin kho đi và kho nhập, thông tin đầu mối giao hàng, ghi chú và hồ sơ đính kèm.

**Bảng thông tin chung và tìm kiếm:**

| Tab/Section | Operator | Action | Field Name VN | M/O | Field Type | Editable | Max Length | Format | Default Value | Data Rule |
|-------------|----------|---------|---------------|-----|------------|----------|------------|---------|---------------|-----------|
| AMP | User | Select | Tạo | M | Button | N | | | | |
| Thông tin chung | System | Display | Số yêu cầu | M | Text | N | 50 | CK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| | System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| | User | Input | Tiêu đề | O | Text | Y | 150 | | | |
| | User | Select | Thêm tài sản | M | Button | N | | | | |

**Bảng thông tin kho:**

| Tab/Section | Field Name VN | M/O | Field Type | Editable | Max Length | Data Source | Data Rule |
|-------------|---------------|-----|------------|----------|------------|-------------|-----------|
| Thông tin kho đi | Tên kho | M | List | N | 50 | | |
| | Địa chỉ kho | M | Text | Y | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| | Quản lý kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho (Tên \| Phòng ban \| Email) |
| Thông tin kho nhập | Tên kho | M | List | N | 50 | | |
| | Địa chỉ kho | M | Text | Y | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| | Quản lý kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho (Tên \| Phòng ban \| Email) |

Quy trình xử lý tự động bao gồm: khóa tài sản khi tạo yêu cầu, cập nhật trạng thái "Chờ phê duyệt", tìm và gán người duyệt (AM/Warehouse Manager), cập nhật tasklist và gửi thông báo email cho các bên liên quan. Số yêu cầu theo format "CK.YY.xxxx" với YY là năm và xxxx là số chạy từ 1-9999. Hệ thống hiển thị thông tin kho và quản lý kho từ [hệ thống OMS](#7-dependencies).

---

### 5.12. Phê duyệt yêu cầu điều chuyển kho

#### 5.12.1. Thông số kỹ thuật giao diện người dùng

![Quy trình phê duyệt yêu cầu điều chuyển kho](images/5_6_2a_B5_image15.png)

**Luồng chính (từ trái sang phải):**
1. **Bắt đầu** → **Nhập thông tin tìm kiếm yêu cầu**
2. **Hiển thị kết quả tìm kiếm** 
3. **Chọn yêu cầu cần xử lý**
4. **Gateway phê duyệt** - điểm quyết định quan trọng

**Luồng phê duyệt (nhánh trên):**
- Từ chối → **Nhập lý do từ chối** → **Cập nhật trạng thái yêu cầu** → **Cập nhật tasklet** → **Unlock tài sản** → **Cập nhật thông tin kho** → **Thông báo cho WK** → **Kết thúc**

**Luồng từ chối (nhánh dưới):**
- Phê duyệt → **Cập nhật trạng thái yêu cầu** → **Cập nhật tasklet** → **Thông báo cho WK kho đi và kho đến** → **Tạo biên bản xuất kho, nhập kho** → **Cập nhật thông tin kho cho tài sản** → **Báo giao tài sản** → **Kết thúc**

#### 5.12.2. Thông số kỹ thuật chi tiết

Giao diện phê duyệt yêu cầu điều chuyển tài sản giữa các kho cho Approver với quy trình 14 bước từ tìm kiếm yêu cầu đến hoàn tất việc bàn giao tài sản.

**Bảng trường tìm kiếm yêu cầu:**

| Field name VN | Operator | Action | Field type | M/O | Editable | Max length |
|---------------|----------|--------|------------|-----|----------|------------|
| Số yêu cầu | User | Input | Text | O | Y | 20 |
| Ngày tạo | User | Input | Date | O | Y | 20 |
| Tiêu đề | User | Input | Text | O | Y | 150 |
| Người tạo | User | Select | List | O | Y | 20 |
| Trạng thái yêu cầu | User | Select | List | O | Y | 20 |
| Người xử lý | User | Select | List | O | Y | 20 |
| Ngày xác nhận | User | Input | Date | O | Y | 20 |

**Bảng thông tin chung yêu cầu:**

| Field name VN | Operator | Action | Field type | M/O | Editable | Max length | Format | Default value | Data rule |
|---------------|----------|--------|------------|-----|----------|------------|---------|---------------|-----------|
| Số yêu cầu | System | Display | Text | M | N | 50 | CK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| Ngày tạo | System | Display | Date | M | N | 50 | MM.DD.YYYY | Today | |
| Tiêu đề | User | Input | Text | O | Y | 150 | | | |
| Thêm tài sản | User | Select | Button | M | N | | | | |

**Bảng thông tin kho:**

| Field name VN | Operator | Action | Field type | M/O | Editable | Max length | Data source | Data rule |
|---------------|----------|--------|------------|-----|----------|------------|-------------|-----------|
| Tên kho | User/System | Select/Display | List | M | N/Y | 50 | | |
| Địa chỉ kho | System | Display | Text | M | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| Quản lý kho | System | Display | Text | M | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho (Tên \| Phòng ban \| Email) |

Quy trình được thiết kế tự động hóa cao với các bước cập nhật trạng thái, gửi thông báo, tạo biên bản và cập nhật thông tin kho tài sản sau khi được phê duyệt. Khi từ chối: hệ thống unlock tài sản, cập nhật tasklist và thông báo cho AMP. Khi phê duyệt: hệ thống tự động tạo phiếu xuất/nhập kho, thông báo cho WK và AM, đồng thời tạo biên bản điều chuyển và cập nhật thông tin kho cho tài sản.

---

### 5.13. Status

Hệ thống trạng thái định nghĩa các luồng nghiệp vụ trong quản lý tài sản với 3 quy trình chính, mỗi quy trình có workflow và vai trò phê duyệt riêng biệt. Mỗi quy trình được thiết kế với các checkpoint kiểm soát, cho phép từ chối, yêu cầu bổ sung thông tin, và có cơ chế rollback khi cần thiết.

#### 5.13.1. Quy trình cấp tài sản

Quy trình cấp tài sản bao gồm hai luồng con: cấp tài sản không ở kho (workflow đơn giản với 3 bước) và cấp tài sản từ kho (workflow phức tạp với 6 bước và nhiều cấp phê duyệt). Để biết chi tiết về quy trình cấp tài sản, xem [5.9. Cấp tài sản](#59-cấp-tài-sản).

**Trạng thái quy trình Cấp tài sản:**

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

#### 5.13.2. Quy trình thanh lý tài sản

Quy trình thanh lý tài sản được chia thành hai phương thức: bán trực tiếp và bán đấu giá. Cả hai đều có luồng kiểm soát - phê duyệt - cập nhật kết quả - xuất kho, nhưng bán đấu giá có thêm bước kiểm soát và phê duyệt kết quả thanh lý riêng biệt.

**Trạng thái quy trình Thanh lý tài sản:**

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

#### 5.13.3. Quy trình điều chuyển tài sản

Quy trình điều chuyển tài sản hỗ trợ hai hình thức: [điều chuyển về kho](#54-tạo-yêu-cầu-nhập-kho-điều-chuyển-về-kho) và [điều chuyển giữa các kho](#511-tạo-yêu-cầu-điều-chuyển-kho). Để biết chi tiết các quy trình này, xem các section tương ứng.

**Trạng thái quy trình Điều chuyển tài sản:**

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

Hệ thống trạng thái được thiết kế để theo dõi cả trạng thái yêu cầu (Request Status) và trạng thái tài sản (Asset Status) một cách độc lập, đảm bảo tính nhất quán và khả năng truy xuất trong toàn bộ [Module quản lý kho](#53-module-quản-lý-kho).

---

### 5.14. Tasklist

Hệ thống tasklist quản lý và phân bổ các công việc trong quy trình điều chuyển và nhập kho cho các vai trò khác nhau, đảm bảo workflow tuần tự và theo dõi trạng thái xử lý chi tiết.

#### 5.14.1. Phân chia task list

Tasklist được phân chia rõ ràng giữa "Tasklist Điều chuyển" và "Tasklist Kho", mỗi loại có trạng thái "Cần xử lý" và "Đã xử lý" riêng biệt cho từng vai trò.

#### 5.14.2. Mapping task và workflow

Quy trình bao gồm 3 sub-process chính: [tạo yêu cầu điều chuyển](#511-tạo-yêu-cầu-điều-chuyển-kho) (2.3.1a), [phê duyệt yêu cầu điều chuyển](#512-phê-duyệt-yêu-cầu-điều-chuyển-kho) (2.3.3a), và xác nhận yêu cầu điều chuyển (5.2.2a). Các action bao gồm Lưu, Gửi, Từ chối, Duyệt, Bổ sung thông tin, và các action liên quan đến nhập kho.

**Task mapping chi tiết:**

| Sub-process | Action | Role | Tasklist Điều chuyển - Cần xử lý | Tasklist Điều chuyển - Đã xử lý | Tasklist Kho - Cần xử lý | Tasklist Kho - Đã xử lý | Ghi chú |
|-------------|--------|------|----------------------------------|--------------------------------|--------------------------|------------------------|---------|
| 2.3.1a Tạo yêu cầu điều chuyển | Lưu | Initator | x | | | | |
| | Gửi | | | x | | | |
| 2.3.3a Phê duyệt yêu cầu điều chuyển | Từ chối | Initator | x | | | | |
| | | BUH | | x | | | |
| | Duyệt | Initator | | x | | | |
| | | BUH | | x | | | |
| | | AMP | x | | | | |
| | Bổ sung thông tin | Initator | x | | | | |
| | | BUH | | x | | | |
| 5.2.2a Xác nhận yêu cầu điều chuyển | Từ chối | Initator | x | | | | |
| | | BUH | | x | | | |
| | | AMP | | x | | | |
| | Bổ sung thông tin | Initator | x | | | | |
| | | BUH | | x | | | |
| | | AMP | | x | | | |
| | Xác nhận & Yêu cầu nhập kho | Gửi | Initator | x | | | |
| | | BUH | | x | | | |
| | | AMP | | x | | x | |
| | | WM | | | x | | |
| | Phê duyệt yêu cầu nhập kho | Từ chối | Initator | x | | x | | Vấn đề về quy trình xử lý |
| | Duyệt | | | | | | |
| Xác nhận nhập kho | Từ chối | | | | | | |
| | Xác nhận | | | | | | |

#### 5.14.3. Vấn đề cần giải quyết

Có một vấn đề được ghi nhận trong quy trình xử lý ở task phê duyệt yêu cầu nhập kho, cho thấy cần được xem xét và điều chỉnh để đảm bảo tính nhất quán trong workflow. Việc này liên quan đến [hệ thống trạng thái](#513-status) và cần được đồng bộ với các quy trình trong [Module quản lý kho](#53-module-quản-lý-kho).

---

## 6. Assumptions & Constraints

### Assumptions
- Hệ thống OMS và EMS đã sẵn sàng để tích hợp và đồng bộ dữ liệu
- Người dùng đã được đào tạo cơ bản về hệ thống FAM hiện tại
- Dữ liệu tài sản hiện tại đã được làm sạch và chuẩn hóa
- Hạ tầng hệ thống đủ khả năng hỗ trợ module kho mới và dashboard visualization
- ITSM và cổng hỗ trợ chi nhánh sẽ sẵn sàng cho tích hợp trong phase sau

### Constraints
- Timeline phát triển module sửa chữa tài sản phụ thuộc vào hoàn thành Wave 4
- Tích hợp với hệ thống legacy có thể có giới hạn về định dạng dữ liệu
- Số lượng concurrent users cho dashboard có thể bị giới hạn bởi hiệu năng server
- Module kho cần tuân thủ quy trình kiểm toán và compliance hiện tại
- Workflow approval cần tuân theo cấu trúc tổ chức và thẩm quyền được định nghĩa

---

## 7. Dependencies

### Technical Dependencies
- **OMS Integration**: Dashboard và module kho phụ thuộc vào dữ liệu từ OMS cho thông tin đơn vị sử dụng, kho và quản lý kho
- **EMS Synchronization**: Đồng bộ dữ liệu tiêu đề PO và thông tin bảo hành từ EMS
- **Database Infrastructure**: Module kho yêu cầu cấu trúc database mới để lưu trữ transaction history và workflow status
- **Email System**: Tất cả quy trình workflow phụ thuộc vào hệ thống email notification

### Business Dependencies  
- **User Training**: Thành công của dashboard và module kho phụ thuộc vào việc đào tạo user
- **Data Migration**: Module kho cần migrate dữ liệu tài sản hiện tại với trạng thái kho
- **Process Alignment**: Quy trình mới cần được align với policy và procedure hiện tại của tổ chức
- **Change Management**: Sự chấp nhận của user với workflow mới và giao diện dashboard

### External Dependencies
- **ITSM System**: Module sửa chữa tài sản (phase sau) sẽ phụ thuộc vào tích hợp ITSM
- **Branch Support Portal**: Tích hợp với cổng hỗ trợ chi nhánh cho module sửa chữa
- **Audit Requirements**: Quy trình workflow cần tuân thủ requirements của bộ phận audit
- **Compliance Standards**: Module kho cần đáp ứng các chuẩn quản lý tài sản của công ty

---

## 8. Acceptance Criteria

### Dashboard Tài sản
- [ ] Hiển thị đầy đủ 4 thống kê tổng quan với tính toán chính xác (loại trừ tài sản đã thanh lý và vô hiệu hóa)
- [ ] 5 biểu đồ tương tác hoạt động đúng với hover và click functionality
- [ ] Bộ lọc dữ liệu hoạt động với tất cả 5 tiêu chí và đồng bộ từ OMS
- [ ] Chức năng xuất dữ liệu ra Excel hoạt động chính xác
- [ ] Performance: Load dashboard dưới 5 giây cho dữ liệu < 10,000 assets

### Module Quản lý Kho
- [ ] Tất cả 11 quy trình workflow hoạt động end-to-end không lỗi
- [ ] Tự động tạo yêu cầu xuất/nhập kho sau khi phê duyệt cấp phát/thanh lý
- [ ] Lock/unlock tài sản hoạt động đúng để tránh xung đột
- [ ] Rollback mechanism hoạt động khi có từ chối ở các bước sau
- [ ] Email notification gửi đúng cho các bên liên quan theo từng workflow
- [ ] Tasklist cập nhật chính xác theo trạng thái của từng role

### Workflow và Trạng thái
- [ ] Tất cả status transition được implement đúng theo bảng Status
- [ ] Tasklist mapping hoạt động chính xác cho tất cả role và action
- [ ] Quy trình từ chối/bổ sung thông tin hoạt động đúng logic
- [ ] Audit trail đầy đủ cho mọi thay đổi trạng thái và action

### Tích hợp Hệ thống
- [ ] Đồng bộ dữ liệu OMS cho đơn vị sử dụng và thông tin kho
- [ ] Đồng bộ EMS cho tiêu đề PO và thông tin bảo hành
- [ ] API endpoints response time < 2 giây
- [ ] Data consistency 99.9% giữa FAM và các hệ thống tích hợp

### User Experience
- [ ] Giao diện responsive hoạt động trên desktop và tablet
- [ ] Tất cả form validation hoạt động với error message rõ ràng
- [ ] File upload/download hoạt động với hỗ trợ multiple formats
- [ ] Search functionality với performance < 3 giây cho large dataset

---

## 9. Glossary

| Thuật ngữ | Định nghĩa |
|-----------|------------|
| **AMP** | Asset Management Personnel - Nhân viên quản lý tài sản |
| **AM** | Asset Manager - Quản lý tài sản cấp cao |
| **BU** | Business Unit - Đơn vị kinh doanh |
| **BUH** | Business Unit Head - Trưởng đơn vị kinh doanh |
| **WK** | Warehouse Keeper - Thủ kho |
| **WM** | Warehouse Manager - Quản lý kho |
| **Dashboard** | Giao diện tổng quan hiển thị thống kê và biểu đồ tài sản |
| **FAM** | Fixed Asset Management - Hệ thống quản lý tài sản cố định |
| **Lock/Unlock** | Khóa/mở khóa tài sản để tránh xung đột trong quy trình |
| **OMS** | Organization Management System - Hệ thống quản lý tổ chức |
| **EMS** | Employee Management System - Hệ thống quản lý nhân viên |
| **ITSM** | IT Service Management - Quản lý dịch vụ CNTT |
| **Rollback** | Quay về trạng thái trước đó khi có lỗi hoặc từ chối |
| **Tasklist** | Danh sách công việc được phân bổ cho từng vai trò |
| **Workflow** | Luồng công việc với các bước tuần tự và điểm quyết định |
| **Visualization** | Trực quan hóa dữ liệu thông qua biểu đồ và chart |
| **Asset Status** | Trạng thái tài sản (Đang sử dụng, Trong kho, Đã thanh lý, v.v.) |
| **Request Status** | Trạng thái yêu cầu (Đang tạo, Chờ phê duyệt, Đã xác nhận, v.v.) |

---

*Tài liệu này được tạo cho FAM UPGRADE - WAVE 4. Phiên bản: 1.0*

---

*Generated by Claude Sonnet 4.5 from 37 sheet summaries*
*Headings: 69 | Internal Links: 65 | Images: 13*

*✅ All internal links validated successfully*
*⚠️ 2 images from summaries not included in BRD*
