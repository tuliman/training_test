$(document).ready(function (){
    $('form').submit(function (event){
        var form_data = {
            userName: $('#userName').val(),
            userSurname:$('#userSurname').val(),
            gender:$('input[name=gender]:checked').val(),
            citizen:$('#citizen:checked').val(),
            dateBorn:$('#dateBorn').val(),
            education:$('select[name=education]').val(),
            comment:$('#comment').val()
        }

        console.log(form_data)
        $.ajax({
            type:'POST',
            url:'/add-form',
            data:JSON.stringify(form_data),
            dataType:'json',
            contentType: "application/json",
            encode:true,
        }).done(function (data){
            alert('sucess')
            console.log(data)
        })
        event.preventDefault()
    })
})
