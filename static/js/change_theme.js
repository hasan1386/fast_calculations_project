function change_theme(tag) {
    if (tag.checked) {
        $("html").attr('data-bs-theme', 'light');
        $.get('/change-theme?theme=light');
    } else {
        $("html").attr('data-bs-theme', 'dark');
        $.get('/change-theme?theme=dark');
    }
}
