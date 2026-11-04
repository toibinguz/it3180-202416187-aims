# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.0] - 2026-11-04

### Added
- `Cart.sort_by_title()`: Sắp xếp các DVD trong giỏ hàng theo thứ tự bảng chữ cái tiêu đề (A-Z).
- `Cart.sort_by_cost()`: Sắp xếp các DVD trong giỏ hàng theo giá tiền.
- `search_by_category()`: Tìm kiếm danh sách DVD theo thể loại trong module `aims.search`.

## [1.0.1] - 2026-11-04

### Fixed
- `search_by_title`: Tìm kiếm không phân biệt chữ hoa / chữ thường (Refs #20).

## [1.0.0] - 2026-11-04

### Added
- `Cart.print_cart()`: In toàn bộ danh sách đĩa DVD trong giỏ hàng kèm bảng tính chi tiết và tổng giá trị.
- `search_by_title()`: Hỗ trợ tìm kiếm danh sách đĩa DVD theo tiêu đề trong gói `aims.search`.
- `Cart.total_cost_with_discount()`: Tính tổng giá trị giỏ hàng sau khi áp dụng phần trăm giảm giá hợp lệ (0 - 100%).
- Thông báo tiếng Việt thân thiện khi thêm DVD vào giỏ hàng (`aims/cart.py`).
- Mẫu Pull Request (`.github/pull_request_template.md`) chuẩn hóa quy trình đề xuất thay đổi.
- Bộ tài liệu hệ thống và biểu đồ ca sử dụng (`docs/use-case.md`).
- Bộ kiểm thử tự động với thư viện chuẩn `unittest` (`tests/test_cart.py`).

### Fixed
- Sửa lỗi giới hạn giỏ hàng cho phép nhận đĩa thứ 21 (`Cart accepts the 21st DVD although the limit is 20`) - Fixes #6.
- Sửa công thức tính giảm giá và kiểm tra điều kiện phần trăm trong `total_cost_with_discount`.
