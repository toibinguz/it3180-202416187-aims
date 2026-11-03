# BÀI THẢO LUẬN LAB 02 – IT3180

## Câu 1 (Slide 35): Vì sao phải đồng bộ master trước khi gửi PR?
- **Phát hiện và giải quyết xung đột sớm (Conflict Prevention):** Nhánh master liên tục nhận các commit mới từ những thành viên khác. Việc kéo master về nhánh của mình giúp lập trình viên chủ động xử lý xung đột ngay dưới môi trường phát triển local, tránh để PR trên GitHub bị nghẽn do báo lỗi "This branch has conflicts".
- **Đảm bảo tính tương thích tích hợp (Integration Testing):** Đảm bảo tính năng mới được kiểm thử chạy tương thích hoàn toàn trên nền tảng mã nguồn mới nhất của hệ thống trước khi gửi yêu cầu đồng đội review.

## Câu 2 (Slide 35): Khi nào không được rebase?
- **Quy tắc vàng của Git:** Tuyệt đối không bao giờ được rebase trên các nhánh công khai/dùng chung đã được chia sẻ cho nhiều người (như `master`, `main`, `release/*`, `develop`).
- **Lý do:** Lệnh `rebase` viết lại lịch sử commit (tạo ra các commit hoàn toàn mới với mã băm SHA khác). Nếu rebase một nhánh dùng chung, lịch sử của các thành viên khác sẽ bị phân nhánh lệch lạc, gây hỗn loạn và xung đột nghiêm trọng khi họ kéo code về. Rebase chỉ được dùng cho nhánh cá nhân cục bộ (local branch) trước khi chia sẻ.

## Câu 3 (Slide 35): `feature/*` khác `topic/*` ra sao?
- **`feature/*`:** Dành cho các nhánh phát triển **tính năng nghiệp vụ/chức năng phần mềm mới** phục vụ trực tiếp yêu cầu người dùng cuối (ví dụ: `feature/cart-print`, `feature/search-by-title`).
- **`topic/*`:** Dành cho các nhánh phục vụ **công việc kỹ thuật, tài liệu, cấu hình, hạ tầng hoặc cải tiến nội bộ** của dự án (ví dụ: tạo mẫu `topic/pr-template`, cập nhật tài liệu `topic/use-case-diagram`, cấu hình CI `topic/ci-unit-tests`).