# BÀI THẢO LUẬN LAB 03 – IT3180

## Câu 1 (Slide 43): Merge base là gì?
- **Định nghĩa:** `Merge base` (gốc hợp nhất) giữa hai nhánh/commit trong Git là **tổ tiên chung gần nhất** (best common ancestor) của chúng trên đồ thị có hướng không chu trình (DAG - Directed Acyclic Graph) của lịch sử commit.
- **Vai trò trong thuật toán 3-way merge (Hợp nhất 3 chiều):**
  + Khi thực hiện hợp nhất hai nhánh (ví dụ: gộp `feature` vào `master`), Git không chỉ so sánh trạng thái ngọn của hai nhánh (2-way diff) mà sử dụng thuật toán **3-way merge** dựa trên 3 điểm mốc:
    1. Trạng thái của nhánh hiện tại (`HEAD` / ours).
    2. Trạng thái của nhánh được gộp (`MERGE_HEAD` / theirs).
    3. Trạng thái của tổ tiên chung gần nhất (**Merge base** / base).
  + Git phân tích sự thay đổi `base -> ours` và `base -> theirs`. Nhờ có `merge base`, Git xác định chính xác dòng mã nào do bên nào chủ động sửa đổi so với gốc ban đầu, từ đó tự động tích hợp mã nguồn mà không sinh ra xung đột giả mạo nếu hai bên sửa ở các vị trí độc lập. Xung đột (`Merge conflict`) chỉ xảy ra khi cả hai bên cùng sửa đổi trên cùng một dòng hoặc khối mã so với `merge base`.
- **Lệnh kiểm tra:** `git merge-base <branch_A> <branch_B>`.

## Câu 2 (Slide 43): Vì sao master và release/* phải dùng revert thay vì reset?
- **Bản chất của `git reset` (Viết lại lịch sử):**
  + `git reset` hoạt động bằng cách dời con trỏ nhánh lùi về quá khứ và loại bỏ các commit sau đó ra khỏi lịch sử của nhánh.
  + Nếu thực hiện `reset` trên các nhánh công khai/dùng chung đã được chia sẻ lên remote như `master` hoặc `release/*`, để đồng bộ lên remote bắt buộc phải dùng lệnh nguy hiểm `git push --force`.
  + Hậu quả: Phá hủy tính toàn vẹn của lịch sử dự án, làm mất đồng bộ repository cục bộ của tất cả thành viên khác trong nhóm và gây xung đột nghiêm trọng khi họ kéo code về. Hơn nữa, tính năng **Branch protection** trên GitHub nghiêm cấm hoàn toàn hành vi `force push` lên nhánh `master` và `release/*`.
- **Bản chất của `git revert` (Tiến lên phía trước - Safe Undo):**
  + `git revert` không xóa bỏ hay di chuyển bất kỳ commit nào trong quá khứ. Thay vào đó, nó tạo ra một **commit mới** có nội dung đảo ngược (nghịch đảo) chính xác những thay đổi của commit/PR muốn hoàn tác.
  + Do commit cũ vẫn tồn tại trong lịch sử, chuỗi DAG luôn tiến lên phía trước một cách tuyến tính và an toàn.
  + Thao tác này an toàn 100% trong môi trường cộng tác nhóm, không gây xung đột lịch sử, không đòi hỏi `push --force`, tuân thủ hoàn hảo cơ chế bảo vệ nhánh và quy trình kiểm duyệt qua Pull Request của SCM.

## Bảng so sánh tổng kết: `git reset` vs `git revert`

| Tiêu chí | `git reset` | `git revert` |
| :--- | :--- | :--- |
| **Cơ chế** | Dời con trỏ nhánh lùi về commit cũ | Tạo một commit mới đảo ngược thay đổi |
| **Viết lại lịch sử** | Có (làm mất/ẩn commit sau đó) | Không (lịch sử luôn tiến về phía trước) |
| **Yêu cầu khi push** | Bắt buộc `git push --force` (nếu đã push) | Chỉ cần `git push` thông thường |
| **Phạm vi áp dụng** | Nhánh cá nhân, commit local chưa chia sẻ | Nhánh dùng chung (`master`, `release/*`), commit đã push |
| **Khả năng truy vết SCM** | Rất kém (xóa dấu vết thay đổi) | Tốt (lưu giữ đầy đủ lịch sử lỗi và bản sửa) |

