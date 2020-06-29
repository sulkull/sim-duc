$(document).ready(function () {
        var csrfToken = $("input[name=csrfmiddlewaretoken]").val();

        $(".box").on('click','#btn_timkiem',function() {
            var serializedData = $(".box").serialize();
            $.ajax({
                url : '/tim-kiem/ajax/?mang=23',
                data : serializedData,
                type : 'get',
                success : function (data) {
                    $("#table-body").append(data.html)
                },
            })
        })

    })