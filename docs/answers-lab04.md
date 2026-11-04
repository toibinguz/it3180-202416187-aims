# BÀI THẢO LUẬN LAB 04 – IT3180

## Câu 1 (Slide 52): Vì sao `release/*` không bao giờ merge ngược vào `master`?
- **Bản chất của Release Flow (Trunk-based Development):** Trong mô hình Release Flow, nhánh `master` là thân cây phát triển chính, đóng vai trò là "Single Source of Truth" (Nguồn chân lý duy nhất) và luôn luôn tiến về phía trước. Nhánh `release/*` chỉ là nhánh rẽ (fork) được tạo ra tại các mốc phát hành (Sprint/Milestone) nhằm phục vụ mục đích đóng băng baseline và bảo trì sau triển khai.
- **Bảo vệ tính toàn vẹn của nhánh `master`:** Nếu thực hiện merge toàn bộ nhánh `release/*` ngược vào `master`, những cấu hình riêng biệt của môi trường sản xuất cũ (như mã phiên bản cố định, tệp cài đặt môi trường triển khai) hoặc các điều chỉnh mang tính tạm thời trên bản phát hành có thể vô tình đè lên, gây xung đột hoặc làm ô nhiễm các tính năng mới đang được tích cực phát triển trên `master`.
- **Nguyên tắc "Upstream First" và kỹ thuật Cherry-pick:** Thay vì merge cả một nhánh, Release Flow quy định: nếu phát hiện lỗi trên phiên bản phát hành cần khắc phục khẩn cấp (hotfix), ta thực hiện sửa lỗi có chọn lọc và lan truyền bản sửa sang các nhánh khác bằng lệnh `git cherry-pick -x`. Nhờ vậy, chỉ có các thay đổi mã nguồn sửa lỗi thuần túy được đưa vào `master` mà không kéo theo toàn bộ lịch sử phân nhánh của `release/*`, giữ cho đồ thị Git luôn sạch sẽ và các baseline hoàn toàn độc lập.

---

## Câu 2 (Slide 52): So sánh Release Flow với GitFlow

| Tiêu chí | GitFlow | Release Flow (Áp dụng trong học phần) |
| :--- | :--- | :--- |
| **Nhánh chính (Sống vĩnh viễn)** | Có 2 nhánh song song: `master`/`main` (chứa mã đã phát hành) và `develop` (chứa mã đang tích hợp). | Chỉ có duy nhất 1 nhánh `master` (mọi hoạt động đều tích hợp liên tục vào master). |
| **Nhánh tính năng (`feature/*`)** | Rẽ nhánh từ `develop` và hợp nhất trở lại vào `develop`. | Rẽ nhánh trực tiếp từ `master` và hợp nhất trực tiếp trở lại vào `master`. |
| **Quy trình đóng nhánh `release/*`** | Khi chốt phát hành, phải thực hiện **merge kép** vào cả 2 nhánh: vừa merge vào `master` vừa merge ngược lại `develop`. | Rẽ nhánh từ `master` để đóng băng baseline, hoàn toàn **không bao giờ merge ngược lại `master`**. |
| **Cơ chế xử lý Hotfix** | Rẽ nhánh từ `master`, sau khi vá xong bắt buộc phải **merge kép** vào cả `master` và `develop`. | Sửa lỗi có định hướng (upstream/release first) và lan truyền bản sửa độc lập thông qua `git cherry-pick -x`. |
| **Nguy cơ xung đột (Merge Conflict)** | Rất cao ("Merge Hell") do phải đồng bộ phức tạp giữa 2 nhánh sống dài hạn song song. | Thấp, nhánh ngắn ngày (short-lived), tránh được việc phân kỳ lịch sử quá xa so với nhánh chính. |
| **Mức độ tương thích với CI/CD** | Cồng kềnh, khó tự động hóa hoàn toàn, phù hợp hơn với chu kỳ phát hành dài ngày đóng gói theo quý. | Tối ưu tuyệt đối cho CI/CD hiện đại, chu kỳ phát hành ngắn (sprint 1-2 tuần), triển khai liên tục (Continuous Delivery). |

---

## Câu 3 (Slide 52): Vì sao nâng lên phiên bản `1.0.0` mà không phải `0.4.0`?
- **Theo quy ước Semantic Versioning (SemVer 2.0.0 - `MAJOR.MINOR.PATCH`):**
  - **Dải phiên bản `0.y.z` (Lab 01 – Lab 03):** Đại diện cho giai đoạn **phát triển ban đầu (Initial Development)**. Theo quy tắc số 4 của đặc tả SemVer, trong giai đoạn `0.x.x`, API phần mềm chưa ổn định, hệ thống đang định hình cấu trúc, có thể thay đổi liên tục bất cứ lúc nào mà không cần đảm bảo tính tương thích ngược.
  - **Phiên bản `1.0.0` (Lab 04):** Định danh bản phát hành ổn định chính thức đầu tiên (**First Stable Public Release**).
- **Lý do chuyển đổi tại cột mốc Lab 04:**
  1. **Hoàn thiện tính năng cốt lõi:** Sản phẩm AIMS-mini đã hội tụ đầy đủ các chức năng nghiệp vụ then chốt: quản trị giỏ hàng, hiển thị thông tin, tính toán đơn hàng có chiết khấu, tìm kiếm và sắp xếp DVD.
  2. **Chất lượng được bảo đảm bằng kiểm thử tự động:** Hệ thống đã thiết lập bộ hồi quy tự động hoàn chỉnh (`unittest`) với độ tin cậy cao trước khi chuyển giao.
  3. **Thiết lập quy trình chuẩn:** Đã có tài liệu đặc tả ca sử dụng (`docs/use-case.md`), tệp theo dõi thay đổi (`CHANGELOG.md` chuẩn Keep a Changelog) và cơ chế bảo vệ nhánh đóng băng baseline (`release/lab04`).
  4. **Cam kết về tính ổn định của API:** Bước lên `1.0.0` là một cam kết của đội ngũ phát triển rằng API công khai đã đi vào khuôn khổ, từ đó trở đi mọi thay đổi sẽ tuân thủ nghiêm ngặt quy tắc SemVer: tăng `PATCH` khi vá lỗi nhỏ không đổi API (ví dụ: `1.0.1` ở bài hotfix) và tăng `MINOR` khi thêm tính năng mới tương thích ngược (ví dụ: `1.1.0`).
