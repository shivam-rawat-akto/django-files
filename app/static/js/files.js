$(document).ready(function () {
    // Get and set the csrf_token
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

    // Define Hook Modal and Delete handlers
    const deleteHookModal = new bootstrap.Modal('#delete-file-modal', {})
    let hookID
    $('.delete-file-btn').click(function () {
        hookID = $(this).data('hook-id')
        console.log(hookID)
        deleteHookModal.show()
    })

    // Handle delete click confirmations
    $('#confirm-delete-hook-btn').click(function () {
        if ($('#confirm-delete-hook-btn').hasClass('disabled')) {
            return
        }
        console.log(hookID)
        $.ajax({
            type: 'POST',
            url: `/ajax/delete/file/${hookID}/`,
            headers: { 'X-CSRFToken': csrftoken },
            beforeSend: function () {
                console.log('beforeSend')
                $('#confirm-delete-hook-btn').addClass('disabled')
            },
            success: function (response) {
                console.log('response: ' + response)
                deleteHookModal.hide()
                console.log('removing #file-' + hookID)
                let count = $('#files-table tr').length
                $('#file-' + hookID).remove()
                if (count <= 2) {
                    console.log('removing #files-table@ #files-table')
                    $('#files-table').remove()
                }
                let message = 'File ' + hookID + ' Successfully Removed.'
                show_toast(message, 'success')
            },
            error: function (xhr, status, error) {
                console.log('xhr status: ' + xhr.status)
                console.log('status: ' + status)
                console.log('error: ' + error)
                deleteHookModal.hide()
                let message = xhr.status + ': ' + error
                show_toast(message, 'danger', '15000')
            },
            complete: function () {
                console.log('complete')
                $('#confirm-delete-hook-btn').removeClass('disabled')
            },
        })
    })
})