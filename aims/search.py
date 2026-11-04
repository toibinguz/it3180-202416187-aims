def search_by_title(items, keyword):
    """Tìm kiếm đĩa theo từ khóa trong tiêu đề (không phân biệt hoa thường)."""
    return [dvd for dvd in items if keyword.lower() in dvd.title.lower()]