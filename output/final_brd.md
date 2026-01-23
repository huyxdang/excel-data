# Tài liệu Yêu cầu Nghiệp vụ (BRD) - FAM UPGRADE WAVE 4

## Mục lục

1. [Executive Summary](#1-executive-summary)
2. [Project Scope & Objectives](#2-project-scope-objectives)
3. [Stakeholders](#3-stakeholders)
4. [Business Requirements](#4-business-requirements)
   - 4.1. [Asset Dashboard Module](#41-asset-dashboard-module)
   - 4.2. [Warehouse Management Module](#42-warehouse-management-module)
     - 4.2.1. [Create Warehouse Intake Request](#421-create-warehouse-intake-request)
     - 4.2.2. [Approve Warehouse Entry Request](#422-approve-warehouse-entry-request)
     - 4.2.3. [Warehouse Receipt Confirmation](#423-warehouse-receipt-confirmation)
     - 4.2.4. [Manual Warehouse Entry](#424-manual-warehouse-entry)
     - 4.2.5. [Cancel Warehouse Entry Request](#425-cancel-warehouse-entry-request)
     - 4.2.6. [Warehouse Exit Process](#426-warehouse-exit-process)
     - 4.2.7. [Inter-Warehouse Transfer](#427-inter-warehouse-transfer)
   - 4.3. [Asset Maintenance Module](#43-asset-maintenance-module)
5. [Assumptions & Constraints](#5-assumptions-constraints)
6. [Dependencies](#6-dependencies)
7. [Acceptance Criteria](#7-acceptance-criteria)
8. [Glossary](#8-glossary)

---

## 1. Executive Summary

Dự án FAM (Fixed Asset Management) Upgrade Wave 4 tập trung vào việc nâng cấp và mở rộng hệ thống quản lý tài sản cố định với 11 yêu cầu chính được phân loại theo mức độ ưu tiên từ 1-4. Các cải tiến chủ yếu xoay quanh việc tăng cường khả năng hiển thị và quản lý tài sản thông qua [4.1. dashboard có thể tùy chỉnh](#41-asset-dashboard-module), cải thiện quy trình cấp phát và thanh lý tài sản.

Dự án bao gồm các tính năng nâng cao như tự động xác nhận phiếu cấp tài sản sau 20 ngày, tích hợp đồng bộ dữ liệu với các hệ thống EMS và OMS, và đặc biệt là việc ra mắt hai module mới: [4.2. module kho](#42-warehouse-management-module) để quản lý xuất-nhập kho tài sản và [4.3. module sửa chữa](#43-asset-maintenance-module) tích hợp với hệ thống ITSM.

Các yêu cầu được sắp xếp theo mức độ ưu tiên với những tính năng cốt lõi như dashboard và module kho có mức ưu tiên cao nhất (mức 1), trong khi các tính năng hỗ trợ và tích hợp có mức ưu tiên thấp hơn.

## 2. Project Scope & Objectives

### Trong phạm vi dự án:
- Phát triển [dashboard tài sản tương tác](#41-asset-dashboard-module) với khả năng visualize và customize
- Xây dựng [hệ thống quản lý kho toàn diện](#42-warehouse-management-module) bao gồm xuất-nhập kho tự động và thủ công
- Tích hợp [module sửa chữa tài sản](#43-asset-maintenance-module) với ITSM và cổng hỗ trợ chi nhánh
- Cải thiện quy trình phê duyệt với tự động xác nhận sau 20 ngày
- Đồng bộ dữ liệu với OMS và EMS
- Bổ sung luồng phê duyệt ATM trong quy trình thanh lý

### Ngoài phạm vi dự án:
- Thay đổi cấu trúc cơ sở dữ liệu chính
- Tích hợp với các hệ thống ngoài OMS, EMS, ITSM
- Migration dữ liệu từ hệ thống cũ

### Mục tiêu dự án:
- Tăng cường khả năng hiển thị và báo cáo tài sản
- Tự động hóa quy trình quản lý kho
- Cải thiện trải nghiệm người dùng
- Tích hợp chặt chẽ với các hệ thống hiện có

## 3. Stakeholders

Các bên liên quan chính trong dự án bao gồm:

### Vai trò quản lý tài sản:
- **AMP (Asset Management Personnel)**: Nhân viên quản lý tài sản, xử lý yêu cầu và phê duyệt
- **AM (Asset Manager)**: Quản lý tài sản cấp cao, phê duyệt các yêu cầu cấp tài sản
- **Checker**: Nhân viên kiểm soát trong quy trình thanh lý
- **Approver**: Người phê duyệt các yêu cầu quan trọng

### Vai trò quản lý kho:
- **WM (Warehouse Manager)**: Quản lý kho, phê duyệt yêu cầu nhập/xuất kho
- **WK (Warehouse Keeper)**: Thủ kho, thực hiện các thao tác nhập/xuất kho thực tế
- **Quản lý kho**: Người quản lý từng kho cụ thể

### Vai trò nghiệp vụ:
- **BU User**: Người dùng đơn vị kinh doanh, tạo yêu cầu và nhận tài sản
- **BU Head**: Trưởng đơn vị kinh doanh, phê duyệt yêu cầu cấp cao
- **Người sử dụng tài sản**: Người cuối cùng sử dụng tài sản được cấp

### Hệ thống liên quan:
- **OMS (Organization Management System)**: Quản lý thông tin tổ chức và kho
- **EMS**: Hệ thống quản lý doanh nghiệp, cung cấp thông tin PO
- **ITSM**: Hệ thống quản lý dịch vụ IT cho module sửa chữa

## 4. Business Requirements

### 4.1. Asset Dashboard Module

Module này cung cấp bảng điều khiển tổng quan để trực quan hóa dữ liệu tài sản và hỗ trợ đưa ra quyết định nhanh chóng. Dashboard hiển thị dữ liệu tài sản theo nhiều góc độ khác nhau bao gồm phân bổ theo phòng ban/orgchart, trạng thái tài sản, biến động theo thời gian, tỷ lệ sử dụng và thông tin về tài sản hết bảo hành hoặc có thời gian sử dụng trên 3-5 năm.

#### Thông số kỹ thuật hiển thị:

Dashboard được thiết kế với phần tổng quan hiển thị các chỉ số quan trọng như số lượng tài sản, giá trị tài sản, tỷ lệ tài sản còn bảo hành và tỷ lệ sử dụng. Hệ thống cung cấp các biểu đồ tương tác đa dạng:

- **Biểu đồ Sunburst**: Hiển thị cơ cấu tài sản với vòng trong thể hiện nhóm IT/ADM/CMD và vòng ngoài thể hiện trạng thái
- **Biểu đồ cột xếp chồng**: Phân bổ theo vùng/đơn vị sử dụng
- **Biểu đồ cột**: Giá trị theo nhóm tài sản
- **Biểu đồ đường**: Biến động theo thời gian
- **Biểu đồ scatter**: Phân tích theo thời gian sử dụng

#### Yêu cầu chức năng:

- Bộ lọc dữ liệu linh hoạt theo vùng, đơn vị sử dụng, CAT 1, Group name, trạng thái tài sản, thời gian sử dụng, khoảng thời gian phát sinh
- Tương tác hover để xem chi tiết số lượng và giá trị tài sản
- Khả năng xuất dữ liệu ra file Excel để phục vụ báo cáo và phân tích chi tiết
- Tự động loại trừ tài sản đã thanh lý và vô hiệu hóa trong các tính toán chỉ số
- Tích hợp với OMS để đồng bộ dữ liệu đơn vị sử dụng khi orgchart thay đổi

### 4.2. Warehouse Management Module

Module quản lý kho toàn diện bao gồm các quy trình: điều chuyển nội bộ, nhập/xuất kho, cấp tài sản, thanh lý tài sản và điều chuyển kho. Hệ thống được thiết kế với tính năng tự động hóa cao và tích hợp chặt chẽ giữa các quy trình liên quan.

Các quy trình chính trong module:
- [4.2.1. Tạo yêu cầu nhập kho tự động](#421-create-warehouse-intake-request)
- [4.2.2. Phê duyệt yêu cầu nhập kho](#422-approve-warehouse-entry-request)  
- [4.2.3. Xác nhận nhập kho](#423-warehouse-receipt-confirmation)
- [4.2.4. Nhập kho thủ công](#424-manual-warehouse-entry)
- [4.2.5. Hủy yêu cầu nhập kho](#425-cancel-warehouse-entry-request)
- [4.2.6. Quy trình xuất kho](#426-warehouse-exit-process)
- [4.2.7. Điều chuyển giữa các kho](#427-inter-warehouse-transfer)

#### 4.2.1. Create Warehouse Intake Request

Quy trình này xử lý việc tạo yêu cầu nhập kho tự động khi tài sản được chuyển đến kho. Hệ thống tự động tạo yêu cầu nhập kho dựa trên các yêu cầu chuyển kho hiện có, kế thừa dữ liệu bao gồm thông tin tài sản, chi tiết kho và tài liệu đính kèm.

##### Thông số kỹ thuật giao diện người dùng

![Giao diện tạo yêu cầu nhập kho](images/5_1_1a_B5_image1.png)

Giao diện yêu cầu nhập kho được chia thành nhiều section: thông tin chung (số yêu cầu, ngày tạo, tiêu đề), danh sách tài sản nhập kho với các thuộc tính chi tiết, thông tin kho đích, thông tin đầu mối giao hàng và phần đính kèm hồ sơ. 

**Cấu trúc biểu mẫu:**
- Thông tin chung (số yêu cầu, ngày tạo, tiêu đề)
- Chi tiết kiểm kê tài sản (mã, tên, mô tả, danh mục, số PO)
- Thông tin kho (tên, địa chỉ, người quản lý)
- Chi tiết phối hợp giao hàng
- Tệp đính kèm

**Các bên liên quan:** Hệ thống, Quản lý kho (WM), AMP, Nhà cung cấp, Người dùng tài sản

##### Thông số kỹ thuật chi tiết

**Yêu cầu trường dữ liệu:**
- Số yêu cầu phải tuân theo định dạng "NK.YY.xxxx" (YY=năm, xxxx=số thứ tự 1-9999)
- Độ dài trường tối đa: 50, 150, 52 ký tự cho các trường khác nhau
- Định dạng ngày: MM.DD.YYYY

**Quy trình làm việc:**
1. Hệ thống tạo yêu cầu nhập kho với dữ liệu kế thừa từ yêu cầu điều chuyển
2. Cập nhật trạng thái: Yêu cầu chuyển kho → "Đã xác nhận", Yêu cầu nhập kho → "Chờ phê duyệt"
3. Cập nhật danh sách công việc: AMP → "Đã xử lý", WM → "Cần xử lý"
4. Gửi email thông báo đến quản lý kho
5. Chuyển sang [quy trình phê duyệt](#422-approve-warehouse-entry-request)

**Tích hợp hệ thống:** OMS, Danh sách công việc AMP/WM, Hệ thống thông báo email, Cơ chế khóa tài sản

#### 4.2.2. Approve Warehouse Entry Request

Chức năng này cho phép Warehouse Manager phê duyệt hoặc từ chối các yêu cầu nhập kho tài sản từ quá trình điều chuyển về kho.

##### Thông số kỹ thuật giao diện người dùng

![Giao diện phê duyệt yêu cầu nhập kho](images/5_1_2a_B6_image2.png)

Quy trình xử lý yêu cầu nhập kho bao gồm 13 bước chính từ tìm kiếm đến phê duyệt. Giao diện được thiết kế cho Warehouse Manager với các chức năng tìm kiếm yêu cầu theo nhiều tiêu chí (số yêu cầu, ngày tạo, tiêu đề, người tạo, trạng thái, người xử lý), hiển thị danh sách kết quả và xem chi tiết từng yêu cầu.

**Tìm kiếm và lựa chọn:**
- Tìm kiếm theo 7 tiêu chí khác nhau với các trường tùy chọn
- Hiển thị danh sách kết quả với đầy đủ thông tin yêu cầu và người xử lý
- Chọn yêu cầu cụ thể để xem chi tiết

##### Thông số kỹ thuật chi tiết

**Thông tin chi tiết yêu cầu:**
Phần thông tin chi tiết yêu cầu được chia thành các section: thông tin chung, danh sách tài sản nhập kho (với đầy đủ thông tin từ mã tài sản, tên, mô tả, trạng thái đến thông tin người sử dụng, địa chỉ đặt tài sản và bảo hành), thông tin kho nhập, đầu mối giao hàng, hồ sơ đính kèm, quá trình xử lý và lịch sử. Nhiều trường thông tin được thiết kế linh hoạt với tùy chọn "hiển thị mặc định" hoặc "ẩn hiện tùy biến".

**Quy trình xử lý:**
1. Tìm kiếm và chọn yêu cầu nhập kho cần xử lý
2. Xem chi tiết đầy đủ thông tin tài sản và yêu cầu
3. Đưa ra quyết định: từ chối hoặc phê duyệt
4. **Nếu từ chối**: unlock tài sản, cập nhật trạng thái về "Từ chối", thông báo cho AMP và BU
5. **Nếu phê duyệt**: cập nhật trạng thái thành "Chờ nhập kho", tạo task cho [Warehouse Keeper để xác nhận nhập kho](#423-warehouse-receipt-confirmation)
6. Hệ thống tự động cập nhật tasklist và gửi thông báo email cho các bên liên quan

**Yêu cầu nghiệp vụ:**
- Tự động unlock tài sản khi từ chối yêu cầu
- Cập nhật trạng thái yêu cầu và tasklist theo quyết định phê duyệt
- Gửi thông báo email tự động cho các bên liên quan
- Liên kết và cập nhật trạng thái giữa yêu cầu nhập kho và yêu cầu điều chuyển

#### 4.2.3. Warehouse Receipt Confirmation

Chức năng xác nhận nhập kho từ quy trình điều chuyển về kho, cho phép Warehouse Keeper xử lý các yêu cầu nhập kho đã được phê duyệt.

##### Thông số kỹ thuật giao diện người dùng

![Giao diện xác nhận nhập kho](images/5_1_3a_B5_image3.png)

Quy trình xác nhận nhập kho bao gồm 14 bước chính từ tìm kiếm yêu cầu đến thông báo hoàn tất. Giao diện hiển thị thông tin tài sản rất chi tiết với nhiều trường có thể tùy chỉnh hiển thị, bao gồm thông tin cơ bản, thông tin bảo hành, vị trí đặt tài sản, và các thông tin liên quan khác.

**Tính năng chính:**
- Tìm kiếm yêu cầu theo số yêu cầu, ngày tạo, tiêu đề, người tạo, trạng thái, người xử lý, ngày xác nhận
- Hiển thị đầy đủ thông tin tài sản với khả năng tùy chỉnh các trường "Ẩn hiện tùy biến" và "Hiển thị mặc định"
- Xử lý hai lựa chọn chính: từ chối hoặc xác nhận nhập kho

##### Thông số kỹ thuật chi tiết

**Quy trình xử lý:**
1. WK tìm kiếm và chọn yêu cầu nhập kho cần xử lý
2. Xem chi tiết thông tin tài sản, kho, đầu mối giao hàng và hồ sơ đính kèm
3. **Nếu từ chối**: yêu cầu nhập lý do, hệ thống unlock tài sản, cập nhật trạng thái "Từ chối" và thông báo cho AMP, BU
4. **Nếu xác nhận**: unlock tài sản, cập nhật thông tin tài sản (đưa về kho, xóa đơn vị sử dụng), cập nhật trạng thái "Đã nhập kho"
5. Hệ thống tự động cập nhật "Ngày bắt đầu sử dụng" nếu trước đó là N/A
6. Gửi email thông báo cho AMP và BU về kết quả xử lý

**Yêu cầu xử lý đặc biệt:**
- Bắt buộc nhập lý do khi từ chối yêu cầu nhập kho
- Tự động cập nhật ngày bắt đầu sử dụng khi xác nhận nếu chưa có
- Quản lý trạng thái tài sản: tự động unlock và cập nhật vị trí lưu trữ
- Tích hợp với OMS để cung cấp thông tin kho (địa chỉ kho, quản lý kho)

Sau khi hoàn tất, nếu cần thực hiện nhập kho thủ công, có thể chuyển sang [4.2.4. quy trình nhập kho thủ công](#424-manual-warehouse-entry).

#### 4.2.4. Manual Warehouse Entry

Module nhập kho thủ công cho phép người dùng tạo yêu cầu nhập tài sản vào kho một cách thủ công thay vì tự động từ quy trình điều chuyển.

##### 4.2.4.1. Create Manual Entry Request

![Giao diện tạo yêu cầu nhập kho thủ công](images/5_2_1a_B5_image4.png)

Chức năng cho phép người dùng tạo yêu cầu nhập kho bằng cách tìm kiếm và chọn tài sản từ danh sách có sẵn, sau đó nhập thông tin kho đích, đầu mối giao hàng và đính kèm hồ sơ liên quan.

**Quy trình tạo yêu cầu (5 bước chính):**
1. Nhập thông tin chung (số yêu cầu tự động NK.YY.xxxx, ngày tạo, tiêu đề)
2. Tìm kiếm và chọn tài sản với bộ lọc đa dạng (mã, tên, phân loại, nhóm, PO number, trạng thái, nhà cung cấp, kho, vị trí)
3. Nhập thông tin kho nhập và đầu mối giao hàng
4. Đính kèm hồ sơ và ghi chú liên quan
5. Gửi yêu cầu

**Tác vụ tự động sau khi gửi:**
- Khóa tài sản để tránh xung đột với yêu cầu khác
- Cập nhật trạng thái yêu cầu thành "Chờ phê duyệt"
- Cập nhật tasklist WM với trạng thái "Cần xử lý"
- Gửi email notification cho Warehouse Manager

##### 4.2.4.2. Approve Manual Entry Request

![Giao diện phê duyệt yêu cầu nhập kho thủ công](images/5_2_2a_B5_image5.png)

Warehouse Manager xem xét và phê duyệt các yêu cầu nhập kho tài sản được tạo thủ công thông qua giao diện gồm 3 phần chính: tìm kiếm yêu cầu, xem chi tiết và ra quyết định.

**Thông tin chi tiết hiển thị:**
- Danh sách tài sản cần nhập kho với các thông tin chi tiết (mã tài sản, tên, mô tả, trạng thái, phân nhóm, thông tin người sử dụng)
- Thông tin kho nhập, thông tin đầu mối giao hàng
- Hồ sơ đính kèm, quá trình xử lý và lịch sử
- Một số trường thông tin có thể được cấu hình hiển thị mặc định hoặc ẩn hiện tùy biến

**Quy trình phê duyệt:**
1. Tìm kiếm yêu cầu theo các tiêu chí: Số yêu cầu, Ngày tạo, Tiêu đề, Người tạo, Trạng thái yêu cầu, Người xử lý, Ngày xác nhận
2. Xem chi tiết yêu cầu với đầy đủ thông tin
3. **Nếu từ chối**: nhập lý do (bắt buộc), hệ thống unlock tài sản, cập nhật trạng thái thành "Từ chối" và thông báo cho AMP
4. **Nếu phê duyệt**: có thể nhập ghi chú, hệ thống cập nhật trạng thái thành "Chờ nhập kho", thông báo cho nhân viên kho (WK) để tiến hành [xác nhận nhập kho](#424-manual-warehouse-entry)

##### 4.2.4.3. Confirm Manual Warehouse Entry  

![Giao diện xác nhận nhập kho thủ công](images/5_2_3a_B6_image6.png)

Warehouse Keeper tìm kiếm, xem và xác nhận các yêu cầu nhập kho tài sản đã được phê duyệt thông qua quy trình gồm 13 bước chính từ tìm kiếm yêu cầu đến thông báo hoàn thành.

**Quy trình xác nhận:**
1. Tìm kiếm yêu cầu theo các tiêu chí: số yêu cầu, ngày tạo, tiêu đề, người tạo, trạng thái và người xử lý
2. Hiển thị danh sách kết quả và chọn yêu cầu cần xử lý
3. Xem thông tin chi tiết bao gồm danh sách tài sản với các thuộc tính chi tiết, thông tin kho nhập, đầu mối giao hàng, hồ sơ đính kèm và lịch sử xử lý
4. **Thực hiện quyết định:**
   - **Từ chối**: yêu cầu nhập lý do, hệ thống unlock tài sản và cập nhật trạng thái "Từ chối"
   - **Xác nhận**: nhập ghi chú, hệ thống cập nhật trạng thái "Đã nhập kho" và tự động cập nhật ngày bắt đầu sử dụng nếu chưa có
5. Gửi thông báo email cho AMP về kết quả xử lý

Sau khi hoàn tất, nếu cần hủy yêu cầu, có thể sử dụng [4.2.5. chức năng hủy yêu cầu nhập kho](#425-cancel-warehouse-entry-request).

#### 4.2.5. Cancel Warehouse Entry Request  

Chức năng cho phép hủy các yêu cầu nhập kho đã được tạo nhưng chưa hoàn thành việc nhập kho, với điều kiện yêu cầu phải đã được gửi thành công và có trạng thái khác "Đã nhập kho".

##### Thông số kỹ thuật giao diện người dùng

![Giao diện hủy yêu cầu nhập kho](images/5_3_1a_B5_image7.png)

Giao diện hủy yêu cầu nhập kho được thiết kế đơn giản với quy trình 8 bước chính từ tìm kiếm yêu cầu đến thông báo cho người dùng cuối.

**Điều kiện tiên quyết:**
- Yêu cầu nhập kho đã được gửi thành công
- Trạng thái yêu cầu khác "Đã nhập kho"

##### Thông số kỹ thuật chi tiết

**Giao diện và thông tin hiển thị:**
- Form tìm kiếm yêu cầu với các tiêu chí như số yêu cầu, ngày tạo, tiêu đề, người tạo và xử lý
- Hiển thị chi tiết yêu cầu bao gồm thông tin chung, danh sách tài sản nhập kho với đầy đủ thông tin từ mã tài sản, tên, mô tả, trạng thái đến thông tin người sử dụng và vị trí đặt tài sản
- Một số trường thông tin có thể "Ẩn hiện tùy biến" như thông tin nhà cung cấp, nguyên giá, email nhân viên

**Quy trình xử lý:**
1. Tìm kiếm và chọn yêu cầu cần hủy từ danh sách
2. Xem chi tiết thông tin yêu cầu và tài sản
3. Nhập lý do hủy (bắt buộc)
4. Hệ thống tự động thực hiện:
   - Unlock tài sản để cho phép tài sản có thể được sử dụng cho yêu cầu khác
   - Cập nhật trạng thái yêu cầu thành "Đã hủy"
   - Cập nhật tasklist cho các bên liên quan
   - Gửi thông báo email cho BU/user về việc hủy yêu cầu

**Tích hợp hệ thống:**
- Kết nối với OMS để lấy thông tin kho, địa chỉ kho và quản lý kho
- Liên quan đến RQ điều chuyển và RQ nhập kho
- Kết nối với Tasklist WM và Tasklist AMP/BU user cho việc cập nhật trạng thái xử lý

#### 4.2.6. Warehouse Exit Process

Quy trình xuất kho tài sản bao gồm việc phê duyệt yêu cầu cấp tài sản, tạo yêu cầu xuất kho và xác nhận xuất kho cho người nhận.

##### 4.2.6.1. Approve Asset Allocation Request

![Giao diện phê duyệt yêu cầu cấp tài sản](images/5_4_0a_A4_image8.png)

Asset Manager (AM) thực hiện việc phê duyệt hoặc từ chối các yêu cầu cấp tài sản từ người dùng thông qua quy trình 8 bước.

**Quy trình phê duyệt:**
1. Asset Manager tìm kiếm và xem danh sách các yêu cầu cần xử lý
2. Chọn yêu cầu cụ thể để xem xét chi tiết
3. Giao diện hiển thị đầy đủ thông tin về tài sản cần cấp, bao gồm thông tin kỹ thuật, người sử dụng, đơn vị nhận và các thông tin bảo hành
4. **Quyết định phê duyệt:**
   - **Nếu từ chối**: nhập lý do cụ thể (bắt buộc, tối đa 150 ký tự), hệ thống unlock tài sản
   - **Nếu phê duyệt**: hệ thống chuyển sang [tạo yêu cầu xuất kho](#421-create-warehouse-intake-request)
5. Hệ thống tự động cập nhật trạng thái yêu cầu, cập nhật tasklist cho các bên liên quan và gửi thông báo email cho AMP

**Đặc quyền AM:**
- Có thể thêm/xóa file đính kèm của người nhận nhưng không được xóa file của người khởi tạo
- Hiển thị 26 thuộc tính chi tiết của tài sản, với khả năng ẩn/hiện tùy biến cho một số trường
- Tích hợp với OMS làm nguồn dữ liệu cho thông tin người dùng và đơn vị

##### 4.2.6.2. Create Warehouse Exit Request

![Giao diện tạo yêu cầu xuất kho](images/5_4_1a__B5_image9.png)

Hệ thống tự động tạo yêu cầu xuất kho dựa trên thông tin từ phiếu cấp/thanh lý tài sản đã được phê duyệt.

**Tính năng tự động:**
- Khi có phiếu cấp hoặc thanh lý tài sản được phê duyệt, hệ thống sẽ tự động sinh ra yêu cầu xuất kho tương ứng
- Định dạng số yêu cầu: "XK.YY.xxxx" (YY=năm, xxxx=số chạy 1-9999 không tái sử dụng)
- Kế thừa tiêu đề và ghi chú từ RQ cấp/thanh lý, danh sách tài sản sync từ phiếu gốc

**Cấu trúc form yêu cầu xuất kho:**
- Thông tin chung (số yêu cầu, ngày tạo, tiêu đề)
- Danh sách tài sản xuất kho với 25+ thuộc tính chi tiết (từ thông tin cơ bản như mã, tên, mô tả đến thông tin bảo hành, vị trí đặt tài sản)
- Thông tin kho xuất, đầu mối nhận hàng và hồ sơ đính kèm

**Hành động sau khi tạo:**
- Cập nhật trạng thái RQ gốc và RQ xuất kho mới tạo
- Cập nhật tasklist cho các vai trò AM, WK, AMP
- Gửi thông báo email cho nhân viên kho để tiến hành [tiếp nhận yêu cầu xuất kho](#42631-receive-warehouse-exit-request)

##### 4.2.6.3. Process Warehouse Exit Request

###### 4.2.6.3.1. Receive Warehouse Exit Request

![Giao diện tiếp nhận yêu cầu xuất kho](images/5_4_2a__B5_image10.png)

Warehouse Keeper (WK) tiếp nhận và xử lý yêu cầu xuất kho thông qua quy trình 11 bước từ tìm kiếm đến ra quyết định.

**Quy trình tiếp nhận:**
1. WK tìm kiếm yêu cầu xuất kho theo các tiêu chí: mã yêu cầu, tiêu đề, người tạo, trạng thái, ngày tạo, nghiệp vụ kho và người xử lý
2. Hiển thị kết quả tìm kiếm dưới dạng danh sách yêu cầu
3. Chọn yêu cầu cụ thể để xem chi tiết
4. Hiển thị thông tin chi tiết bao gồm:
   - Thông tin chung (số yêu cầu format XK.YY.xxxx, ngày tạo, tiêu đề)
   - Danh sách tài sản xuất kho với đầy đủ thông tin về mã tài sản, tên, mô tả, trạng thái, phân nhóm, thông tin nhà cung cấp, giá trị, người sử dụng, đơn vị, địa chỉ đặt tài sản và thông tin bảo hành
5. **Quyết định xử lý:**
   - **Từ chối**: nhập lý do, cập nhật trạng thái từ chối, unlock tài sản, thông báo cho AMP
   - **Đồng ý**: cập nhật trạng thái "đã xác nhận" cho RQ cấp tài sản và "chờ xác nhận" cho RQ xuất kho, thông báo cho [Warehouse Manager để phê duyệt](#422-approve-warehouse-entry-request)

**Đặc biệt:** Ẩn nút "Từ chối" nếu yêu cầu xuất kho xuất phát từ yêu cầu thanh lý.

###### 4.2.6.3.2. Approve Warehouse Exit Request

![Giao diện phê duyệt yêu cầu xuất kho](images/5_4_3a__B5_image11.png)

Warehouse Manager phê duyệt hoặc từ chối các yêu cầu xuất kho tài sản thông qua quy trình 12 bước.

**Quy trình phê duyệt:**
1. Warehouse Manager tìm kiếm các yêu cầu xuất kho đang chờ phê duyệt
2. Sử dụng giao diện tìm kiếm với nhiều tiêu chí: mã yêu cầu, tiêu đề, người tạo, trạng thái, ngày tạo, loại cấp tài sản, người xử lý và ngày xác nhận
3. Chọn yêu cầu cụ thể để xem chi tiết đầy đủ
4. Hiển thị thông tin chi tiết bao gồm:
   - Thông tin chung, danh sách tài sản xuất kho với đầy đủ thông tin từ mã tài sản đến thông tin bảo hành
   - Thông tin kho xuất, thông tin đầu mối nhận hàng, ghi chú và hồ sơ đính kèm
5. **Quyết định phê duyệt:**
   - **Từ chối**: nhập lý do, cập nhật trạng thái, unlock tài sản, cập nhật tasklist và gửi thông báo cho AMP và WK
   - **Phê duyệt**: chuyển trạng thái yêu cầu cấp tài sản thành "Đã xác nhận", yêu cầu xuất kho thành "Chờ xác nhận" và chuyển quyền xử lý cho [BU user để nhận tài sản](#42633-asset-handover-confirmation)

**Đặc biệt:** Ẩn nút "Từ chối" đối với yêu cầu xuất kho xuất phát từ yêu cầu thanh lý.

###### 4.2.6.3.3. Asset Handover Confirmation

![Giao diện nhận tài sản từ kho](images/5_4_4a_B6_image12.png)

BU user thực hiện nhận tài sản từ kho sau khi yêu cầu xuất kho được phê duyệt thông qua quy trình 11 bước từ tìm kiếm yêu cầu đến cập nhật trạng thái cuối cùng.

**Quy trình nhận tài sản:**
1. Tìm kiếm yêu cầu xuất kho theo các tiêu chí: mã yêu cầu, tiêu đề, người tạo, trạng thái, ngày tạo, nghiệp vụ kho và người xử lý
2. Hiển thị danh sách yêu cầu và chọn yêu cầu cần xử lý
3. Xem thông tin chi tiết bao gồm:
   - Thông tin chung về yêu cầu (số yêu cầu "XK.YY.xxxx", ngày tạo MM.DD.YYYY)
   - Danh sách tài sản xuất kho với đầy đủ thông tin từ mã tài sản đến thông tin bảo hành
   - Thông tin kho xuất, thông tin đầu mối nhận hàng, và các tệp đính kèm
4. **Quyết định cuối cùng:**
   - **Từ chối**: cập nhật trạng thái "Từ chối", unlock tài sản, cập nhật tasklist và gửi thông báo
   - **Xác nhận**: cập nhật trạng thái "Đã xác nhận"/"Đã nhận tài sản", unlock tài sản, cập nhật đơn vị sử dụng

**Yêu cầu dữ liệu:**
- Danh sách tài sản xuất kho phải bằng với danh mục tài sản trong phiếu cấp/thanh lý
- Thông tin kho phải khớp với thông tin kho trên yêu cầu cấp tài sản
- Tích hợp với OMS để cung cấp thông tin địa chỉ kho và quản lý kho

##### 4.2.6.4. Cancel Warehouse Exit Request

![Giao diện hủy yêu cầu xuất kho](images/5_5_1a_B5_image13.png)

Chức năng cho phép hủy các yêu cầu xuất kho tài sản đã được tạo nhưng chưa được xác nhận với điều kiện trạng thái yêu cầu khác "Đã xác nhận".

**Điều kiện hủy:**
- Yêu cầu xuất kho đã được tạo thành công
- Trạng thái khác "Đã xác nhận"

**Quy trình hủy (8 bước):**
1. Tìm kiếm và chọn yêu cầu cần hủy
2. Hiển thị chi tiết yêu cầu bao gồm thông tin chung, danh sách tài sản xuất kho, thông tin kho xuất, đầu mối nhận hàng và hồ sơ đính kèm
3. Nhập lý do hủy (bắt buộc, tối đa 150 ký tự)
4. Hệ thống thực hiện:
   - Unlock tài sản để có thể sử dụng cho yêu cầu khác
   - Cập nhật trạng thái về "Đã hủy"
   - Cập nhật tasklist
   - Gửi thông báo email cho các bên liên quan

**Xử lý đặc biệt:** Đối với yêu cầu xuất kho liên kết với yêu cầu thanh lý, hệ thống sẽ ẩn nút "Từ chối" và cần xử lý đặc biệt để trả trạng thái tài sản về trạng thái trước khi thanh lý.

#### 4.2.7. Inter-Warehouse Transfer

Quy trình điều chuyển tài sản giữa các kho khác nhau trong hệ thống, bao gồm tạo yêu cầu và phê duyệt điều chuyển.

##### 4.2.7.1. Create Inter-Warehouse Transfer Request

![Giao diện tạo yêu cầu điều chuyển kho](images/5_6_1a_B6_image14.png)

Chức năng cho phép người dùng tạo yêu cầu điều chuyển tài sản từ kho này sang kho khác với giao diện phức tạp bao gồm nhiều phần thông tin.

**Cấu trúc giao diện:**
- Thông tin chung của yêu cầu (số yêu cầu tự động "CK.YY.xxxx", ngày tạo, tiêu đề)
- Công cụ tìm kiếm tài sản với nhiều tiêu chí lọc (mã, tên, phân loại, nhóm, PO number, trạng thái, nhà cung cấp, kho, vị trí)
- Hiển thị kết quả tìm kiếm với đầy đủ thông tin chi tiết về tài sản
- Thông tin về kho đi và kho nhập (tên kho, địa chỉ, thông tin quản lý kho từ OMS)
- Phần thông tin đầu mối giao hàng, ghi chú và tính năng đính kèm hồ sơ

**Quy trình tạo yêu cầu:**
1. Nhập thông tin chung và tiêu đề yêu cầu
2. Tìm kiếm và chọn tài sản cần điều chuyển với các bộ lọc đa dạng
3. Xác định kho đi và kho nhập với thông tin tự động từ OMS
4. Nhập thông tin đầu mối giao hàng và ghi chú
5. Đính kèm hồ sơ liên quan nếu cần
6. Gửi yêu cầu để chuyển sang [quy trình phê duyệt](#42722-approve-inter-warehouse-transfer-request)

**Tự động hóa sau khi gửi:**
- Khóa tài sản không thể dùng cho request khác cho đến khi hoàn thành
- Chuyển trạng thái sang "Chờ phê duyệt"
- Tự động tìm và gán người phê duyệt
- Cập nhật tasklist với trạng thái "Cần xử lý"
- Gửi email notification cho Asset Manager và Warehouse Manager

##### 4.2.7.2. Approve Inter-Warehouse Transfer Request

![Giao diện phê duyệt yêu cầu điều chuyển kho](images/5_6_2a_B5_image15.png)

Người phê duyệt (Approver) xử lý các yêu cầu điều chuyển tài sản giữa các kho trong hệ thống quản lý tài sản thông qua quy trình phê duyệt hoàn chỉnh gồm 14 bước.

**Quy trình phê duyệt chi tiết:**
1. Tìm kiếm yêu cầu điều chuyển theo số yêu cầu, ngày tạo, tiêu đề, người tạo, trạng thái, người xử lý, ngày xác nhận
2. Xem chi tiết thông tin tài sản cần chuyển, thông tin kho xuất và kho nhập, cùng các thông tin liên quan khác
3. Giao diện cung cấp đầy đủ thông tin tài sản bao gồm:
   - Thông tin cơ bản (mã, tên, trạng thái)
   - Thông tin người sử dụng hiện tại
   - Thông tin kho hiện tại và kho đích
   - Thông tin bảo hành và các tài liệu đính kèm
4. **Quyết định phê duyệt:**
   - **Từ chối**: bắt buộc nhập lý do (max 150 ký tự), hệ thống unlock tài sản, thông báo cho AMP
   - **Phê duyệt**: hệ thống tự động tạo biên bản điều chuyển, cập nhật thông tin tài sản và hỗ trợ quy trình bàn giao vật lý tài sản

**Hành động tự động sau phê duyệt:**
- Cập nhật trạng thái yêu cầu
- Gửi thông báo cho các bên liên quan (AMP, WK kho đi và kho đến)
- Tạo biên bản điều chuyển tài sản giữa các kho
- Cập nhật thông tin lưu trữ tài sản trong hệ thống
- Cập nhật tasklist cho các warehouse keeper của cả hai kho

**Tích hợp hệ thống:**
- OMS: Cung cấp thông tin kho và quản lý kho
- Biên bản điều chuyển: Template được tạo tự động sau khi phê duyệt
- Email notification system: Thông báo cho các bên liên quan

### 4.3. Asset Maintenance Module

Module sửa chữa tài sản tích hợp với hệ thống ITSM và cổng hỗ trợ chi nhánh, cho phép quản lý toàn bộ quy trình bảo trì và sửa chữa tài sản trong tổ chức.

#### Tích hợp ITSM:
Module được thiết kế để tích hợp chặt chẽ với hệ thống quản lý dịch vụ IT (ITSM) hiện có, cho phép tự động tạo ticket sửa chữa, theo dõi tiến độ và cập nhật trạng thái tài sản theo thời gian thực.

#### Cổng hỗ trợ chi nhánh:
Hệ thống cung cấp giao diện web cho các chi nhánh có thể truy cập qua intranet để tạo yêu cầu sửa chữa, theo dõi tiến độ và nhận thông báo về tình trạng tài sản của mình.

#### Quy trình sửa chữa:
- Tiếp nhận yêu cầu sửa chữa từ người dùng hoặc hệ thống tự động
- Phân loại và ưu tiên hóa theo mức độ nghiêm trọng
- Phân công kỹ thuật viên phù hợp
- Theo dõi tiến độ sửa chữa và cập nhật trạng thái
- Xác nhận hoàn thành và bàn giao tài sản

**Các bên liên quan:** Người dùng tài sản, Kỹ thuật viên, Quản lý bảo trì, ITSM, Cổng hỗ trợ chi nhánh

## 5. Assumptions & Constraints

### Giả định:
- Hệ thống OMS và EMS sẽ duy trì API ổn định cho việc tích hợp
- Người dùng có kiến thức cơ bản về quy trình quản lý tài sản
- Hạ tầng mạng đủ mạnh để hỗ trợ dashboard real-time
- Các chi nhánh có truy cập internet ổn định cho [module sửa chữa](#43-asset-maintenance-module)

### Ràng buộc:
- Phải tuân thủ chính sách bảo mật dữ liệu hiện tại
- Không được thay đổi cấu trúc database chính hiện có
- Thời gian phát triển giới hạn trong Q4 năm hiện tại
- Ngân sách giới hạn cho tích hợp với hệ thống bên ngoài
- [Dashboard module](#41-asset-dashboard-module) phải tương thích với các trình duyệt web chính

## 6. Dependencies

### Phụ thuộc hệ thống:
- **OMS (Organization Management System)**: Cung cấp dữ liệu tổ chức cho [dashboard](#41-asset-dashboard-module) và thông tin kho cho [module quản lý kho](#42-warehouse-management-module)
- **EMS**: Đồng bộ thông tin PO và thời gian bảo hành cho tất cả các module
- **ITSM**: Cần thiết cho hoạt động của [module sửa chữa](#43-asset-maintenance-module)

### Phụ thuộc quy trình:
- [Quy trình phê duyệt yêu cầu nhập kho](#422-approve-warehouse-entry-request) phụ thuộc vào [quy trình tạo yêu cầu](#421-create-warehouse-intake-request)
- [Xác nhận nhập kho](#423-warehouse-receipt-confirmation) chỉ có thể thực hiện sau khi được phê duyệt
- [Quy trình xuất kho](#426-warehouse-exit-process) phụ thuộc vào việc phê duyệt cấp tài sản trước đó
- [Điều chuyển giữa các kho](#427-inter-warehouse-transfer) yêu cầu xác nhận từ cả hai kho

### Phụ thuộc kỹ thuật:
- API endpoints ổn định từ các hệ thống tích hợp
- Database performance đủ mạnh cho real-time dashboard
- Email server hoạt động ổn định cho notification system

## 7. Acceptance Criteria

### Cho Asset Dashboard Module:
- Dashboard hiển thị đúng 100% dữ liệu tài sản trong vòng 5 giây
- Tất cả biểu đồ phải tương tác được và hiển thị tooltip chính xác
- Bộ lọc hoạt động đúng với kết quả real-time
- Xuất Excel thành công với đầy đủ dữ liệu đã lọc
- Tích hợp OMS cập nhật dữ liệu tự động mỗi 15 phút

### Cho Warehouse Management Module:
- [Tạo yêu cầu nhập kho](#421-create-warehouse-intake-request) tự động 100% thành công từ yêu cầu điều chuyển
- [Quy trình phê duyệt](#422-approve-warehouse-entry-request) gửi notification đúng thời điểm
- [Xác nhận nhập kho](#423-warehouse-receipt-confirmation) cập nhật trạng thái tài sản chính xác
- [Nhập kho thủ công](#424-manual-warehouse-entry) validation đầy đủ các trường bắt buộc
- [Hủy yêu cầu](#425-cancel-warehouse-entry-request) unlock tài sản và cập nhật trạng thái đúng
- [Quy trình xuất kho](#426-warehouse-exit-process) tích hợp hoàn hảo với quy trình cấp tài sản
- [Điều chuyển kho](#427-inter-warehouse-transfer) tạo biên bản tự động sau phê duyệt

### Cho Asset Maintenance Module:
- Tích hợp ITSM hoạt động 99.9% thời gian uptime
- Cổng hỗ trợ chi nhánh truy cập được từ tất cả location
- Notification system gửi thông báo trong vòng 2 phút
- Tracking tiến độ sửa chữa real-time

### Yêu cầu hiệu suất chung:
- Thời gian phản hồi trung bình < 3 giây
- System uptime ≥ 99.5%
- Concurrent users: hỗ trợ tối thiểu 500 users
- Data integrity: 100% consistency giữa các module

## 8. Glossary

### Thuật ngữ nghiệp vụ:
- **AMP (Asset Management Personnel)**: Nhân viên quản lý tài sản, chịu trách nhiệm xử lý các yêu cầu liên quan đến tài sản
- **AM (Asset Manager)**: Quản lý tài sản cấp cao, có thẩm quyền phê duyệt các yêu cầu quan trọng
- **WM (Warehouse Manager)**: Quản lý kho, phê duyệt các yêu cầu nhập/xuất kho
- **WK (Warehouse Keeper)**: Thủ kho, thực hiện các thao tác vật lý nhập/xuất kho
- **BU (Business Unit)**: Đơn vị kinh doanh, nơi sử dụng tài sản cuối cùng

### Thuật ngữ hệ thống:
- **OMS (Organization Management System)**: Hệ thống quản lý thông tin tổ chức và cấu trúc kho
- **EMS**: Hệ thống quản lý doanh nghiệp, cung cấp thông tin đơn đặt hàng (PO)
- **ITSM (IT Service Management)**: Hệ thống quản lý dịch vụ IT
- **Tasklist**: Danh sách công việc cần xử lý của từng vai trò
- **RQ**: Request - Yêu cầu trong hệ thống

### Mã định dạng:
- **NK.YY.xxxx**: Định dạng số yêu cầu nhập kho (NK + năm + số thứ tự)
- **XK.YY.xxxx**: Định dạng số yêu cầu xuất kho (XK + năm + số thứ tự)  
- **CK.YY.xxxx**: Định dạng số yêu cầu điều chuyển kho (CK + năm + số thứ tự)

### Trạng thái quy trình:
- **Chờ phê duyệt**: Yêu cầu đã được tạo và đang chờ người có thẩm quyền xem xét
- **Đã phê duyệt**: Yêu cầu đã được chấp thuận và chuyển sang bước tiếp theo
- **Từ chối**: Yêu cầu bị từ chối, tài sản được unlock để sử dụng cho yêu cầu khác
- **Đã nhập kho/Đã xuất kho**: Quá trình vật lý đã hoàn tất
- **Đã hủy**: Yêu cầu bị hủy bỏ trước khi hoàn thành

---

*Generated by Claude Sonnet 4.5 from 37 sheet summaries*
*Headings: 44 | Internal Links: 58*

*⚠️ Validation warnings - some links may need manual review*
