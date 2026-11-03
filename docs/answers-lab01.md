# BÀI THẢO LUẬN LAB 01 – IT3180

## Câu 1 (Slide 19): Cấu hình `--global` được lưu ở đâu? Khác gì so với `--local`?
- **Vị trí lưu:**
  + Cấu hình `--global` được lưu tại file `~/.gitconfig` trong thư mục gốc của người dùng (trên Windows là `C:\Users\<Tên_User>\.gitconfig`).
  + Cấu hình `--local` được lưu tại file `.git/config` bên trong chính repository đó.
- **Khác biệt:**
  + `--global` áp dụng cho tất cả các repository của user trên máy tính.
  + `--local` chỉ áp dụng riêng cho repository hiện tại và có độ ưu tiên cao hơn, ghi đè lên thiết lập `--global`.

## Câu 2 (Slide 26): Vì sao dùng `git mv`?
- `git mv <cũ> <mới>` tương đương chuỗi lệnh di chuyển file + `git rm` file cũ + `git add` file mới vào Staging area.
- Lệnh này giúp Git ghi nhận ngay hành động đổi tên/di chuyển (rename) với độ tin cậy 100%, bảo toàn trọn vẹn metadata và lịch sử commit của tệp. Lịch sử này có thể truy vết dễ dàng bằng `git log --follow`. Nếu di chuyển bằng chuột/hệ điều hành thông thường rồi mới `add .`, Git có nguy cơ hiểu lầm là xóa file cũ và tạo file mới tinh.

## Câu 3 (Slide 26): `release/lab01` có phải baseline không?
- **Có.** Theo lý thuyết SCM, Baseline là một trạng thái cấu hình phần mềm đã được kiểm tra, thống nhất và chính thức "đóng băng" tại một mốc thời gian, dùng làm điểm tựa cho các bước phát triển tiếp theo và chỉ thay đổi qua quy trình kiểm soát chính thức.
- Nhánh `release/lab01` đại diện cho sản phẩm hoàn chỉnh chốt mốc nộp bài của Lab 01, không nhận thêm commit phát triển mới, nên nó chính là một Baseline.

## Câu 4 (Slide 26): Vì sao không commit thẳng master dù làm một mình?
- **Kỷ luật quy trình:** Đảm bảo nhánh `master` luôn luôn ở trạng thái "sạch", chạy tốt và phản ánh đúng phiên bản ổn định nhất.
- **Tự rà soát (Self-review):** Quy trình tạo Pull Request buộc người làm phải xem lại toàn bộ khác biệt mã nguồn (tab *Files changed*), giúp phát hiện tệp rác, lỗi cú pháp hoặc sót code trước khi hợp nhất.
- **Chuẩn bị cho tự động hóa:** PR là chốt chặn để gắn các công cụ kiểm tra tự động (CI/CD, linter, unit test) trước khi mã vào nhánh chính.