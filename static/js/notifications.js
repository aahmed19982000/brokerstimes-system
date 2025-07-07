function markAsRead(id) {
    fetch(`/notifications/${id}/read/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({})
    })
    .then(res => res.json())
    .then(data => {
        if (data.success) {
            const element = document.getElementById(`note-${id}`);
            if (element) {
                element.classList.remove("unread");
                const readButton = element.querySelector('button[onclick^="markAsRead"]');
                if (readButton) {
                    readButton.remove();
                }
            }
        } else {
            console.error("فشل في تعليم الإشعار كمقروء:", data.error);
        }
    })
    .catch(err => console.error("خطأ:", err));
}

function deleteNotification(id) {
    fetch(`/notifications/${id}/delete/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({})
    })
    .then(res => res.json())
    .then(data => {
        if (data.success) {
            const element = document.getElementById(`note-${id}`);
            if (element) {
                element.remove();
            }
        } else {
            console.error("فشل في حذف الإشعار:", data.error);
        }
    })
    .catch(err => console.error("خطأ:", err));
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.slice(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
