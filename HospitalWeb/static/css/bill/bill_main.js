 $(document).on('change', '#rc', function (e) {
        var dc = $('#dc').val()
        var rc = $('#rc').val()
        var total = Number(dc) + Number(rc)
        console.log("total", total,dc,rc)
        $('#total').val(total)
        console.log("yes you are doing right ",  $('#total').val() )
        })