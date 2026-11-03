def search_by_title(items, keyword):
    """Tìm kiếm đĩa theo từ khóa trong tiêu đề."""
    return [dvd for dvd in items if keyword in dvd.title]