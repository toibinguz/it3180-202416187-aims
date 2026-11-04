# BÀI THẢO LUẬN LAB 05 – IT3180

## Câu 1 (Slide 64): Ưu, nhược điểm của Upstream First so với Release First?

### 1. Mô hình Upstream First (Sửa lỗi trên nhánh chính `master` trước, sau đó cherry-pick về `release/*`):
- **Cơ chế:** Khi phát hiện lỗi (kể cả lỗi được báo cáo từ môi trường sản xuất), lập trình viên sẽ phân tích, viết kiểm thử tái hiện và sửa lỗi trực tiếp trên nhánh `master` (thông qua luồng `bugfix/*` -> PR -> `master`). Sau khi bản sửa đã được tích hợp ổn định vào nhánh chính, commit sửa lỗi mới được cherry-pick ngược về các nhánh bảo trì `release/*`.
- **Ưu điểm:**
  + **Triệt tiêu nguy cơ quên lan truyền (No Forgotten Backports):** Lỗi được giải quyết dứt điểm tại nguồn gốc (`master`), đảm bảo mọi bản phát hành trong tương lai đều thừa hưởng bản sửa lỗi này và không bao giờ bị lỗi hồi quy (regression bug).
  + **Đúng chuẩn triết lý Trunk-based / Continuous Delivery:** Nhánh `master` luôn phản ánh trạng thái hoàn thiện và mới nhất của hệ thống.
  + **Trải nghiệm kiểm thử toàn diện:** Bản sửa lỗi được chạy qua toàn bộ hệ thống CI/CD và bộ test suite đầy đủ nhất của dự án trên nhánh `master`.
- **Nhược điểm:**
  + **Thời gian phản ứng chậm hơn trong tình huống khẩn cấp:** `master` thường chứa nhiều tính năng mới đang phát triển dở dang hoặc chờ duyệt PR phức tạp. Nếu việc sửa trên `master` gặp vướng mắc, bản vá cho người dùng ở production sẽ bị trì hoãn.
  + **Nguy cơ xung đột khi cherry-pick về bản cũ:** Do `master` đã đi xa so với baseline cũ, việc mang bản vá từ `master` ngược về `release/*` cũ có thể gặp xung đột mã nguồn lớn.

---

### 2. Mô hình Release First (Sửa trực tiếp trên nhánh `release/*` trước, sau đó cherry-pick về `master` - như thực hiện trong Lab 05):
- **Cơ chế:** Tạo nhánh `hotfix/*` trực tiếp từ mốc release bị lỗi (`release/lab04`), thực hiện sửa lỗi và phát hành bản vá khẩn cấp (PATCH `v1.0.1`) cho người dùng ngay lập tức. Sau đó, lập trình viên cherry-pick commit sửa lỗi đó lan truyền sang `master` và các nhánh release khác (`release/lab05`).
- **Ưu điểm:**
  + **Tốc độ phản ứng khẩn cấp cực nhanh (Rapid Time-to-Patch):** Bản vá được xây dựng và kiểm thử trên đúng môi trường baseline đang chạy thực tế của khách hàng, không bị phụ thuộc hay ảnh hưởng bởi các commit mới chưa ổn định trên `master`.
  + **Tách biệt rủi ro hoàn toàn:** Quá trình vá lỗi trên release cũ không làm gián đoạn tiến độ phát triển tính năng của các nhóm khác trên `master`.
- **Nhược điểm:**
  + **Rủi ro quên lan truyền rất cao (High Risk of Regression):** Nếu quy trình SCM không có kỷ luật kiểm toán chặt chẽ, lập trình viên rất dễ quên cherry-pick bản vá về `master` hoặc các nhánh release song song. Hậu quả là ở bản phát hành tiếp theo, lỗi cũ lại xuất hiện trở lại gây bức xúc cho người dùng.
  + **Đòi hỏi kỷ luật tách commit nghiêm ngặt:** Bắt buộc phải tách commit sửa lỗi thuần túy (để lan truyền) và commit bump version (chỉ dùng cục bộ cho nhánh release đó), nếu không sẽ gây xung đột phiên bản khi đưa về `master`.

---

## Câu 2 (Slide 64): Nếu quên lan truyền bản sửa sang `release/lab05`, lệnh nào ở Phần F sẽ phát hiện?

Trong quy trình Kiểm toán đa phiên bản (Multi-version Configuration Audit) ở Phần F, có **2 công cụ/lệnh độc lập** sẽ lập tức phát hiện nếu ta quên lan truyền bản sửa sang `release/lab05`:

### 1. Lệnh kiểm toán mã nguồn bằng `git cherry`:
```bash
git cherry -v origin/release/lab05 origin/release/lab04
```
- **Nguyên lý hoạt động:** `git cherry` so sánh các thay đổi (dựa trên patch-id) giữa hai nhánh:
  + Dấu `-`: Commit đã có bản tương đương trên nhánh đích.
  + Dấu `+`: Commit có trên nhánh nguồn nhưng **CHƯA CÓ** trên nhánh đích.
- **Dấu hiệu phát hiện:** Nếu quên lan truyền, commit `fix: make search_by_title case-insensitive` sẽ xuất hiện với **dấu `+`**, lập tức cảnh báo đội ngũ quản lý cấu hình rằng nhánh `release/lab05` đang bị thiếu bản vá này.

### 2. Vòng lặp kiểm tra hành vi tự động (Multi-version behavioral test loop):
```bash
for ref in v1.0.1 v1.1.0 master; do
  git switch --detach -q $ref; printf "%-8s " $ref
  python -c "from aims.dvd import DigitalVideoDisc as D; from aims.search import search_by_title; print(len(search_by_title([D('The Lion King')], 'lion')))"
done; git switch -q master
```
- **Nguyên lý hoạt động:** Chạy cùng một kịch bản kiểm thử tìm kiếm từ khóa viết thường `"lion"` xuyên suốt qua cả 3 mốc cấu hình đã gắn tag.
- **Dấu hiệu phát hiện:**
  + Kỳ vọng đạt chuẩn: Cả 3 dòng đều phải in ra `1` (tìm thấy 1 đĩa).
  + Nếu quên lan truyền sang `release/lab05`: Mốc `v1.1.0` sẽ in ra `0` (không tìm thấy), trong khi `v1.0.1` và `master` in ra `1`. Kết quả bất thường này ngay lập tức chỉ ra `release/lab05` chưa được tích hợp bản sửa lỗi.
