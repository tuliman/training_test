function tryValid (obj){
    var bool = false
    if (obj.val().length === 0 ){

        obj.after('<span class="text-error"> Поле обязательно к заполнению </span>').focus()
        bool =true

    }
    else  if (obj.val()[0]===obj.val()[0].toLowerCase()){
        obj.after('<span class="text-error"> Введите  с большой буквы </span>')
        bool = true
    }
    return bool
}





$(document).ready(function (){


    $('.addUser').on('click',function (){
        var el = $('<div class="form_atrs"  >' +
            '<h4>Имя</h4>\n' +
            '    <input type="text" id="userName" class ="userName" name="userName" size="40">\n' +
            '    <h4>Фамилия</h4>\n' +
            '    <input type="text" id="userSurname" class ="userSurname" name="userSurname" size="40">\n' +
            '\n' +
            '    <h4>Отчество</h4>\n' +
            '    <input  type="text" class="patronomic" id="patronymic" name="patronymic" size="40">\n' +
            '\n' +
            '    <div><h4>Пол:</h4>\n' +
            '   <input type="radio" name="gender" value="Man">Мужчина\n' +
            '   <input type="radio" name="gender" value="Women">Женщина\n' +
            '    </div><br>\n' +
            '\n' +
            '    <div>\n' +
            '    <input type="checkbox" id="citizen" name="citizen">\n' +
            '    <label for="citizen">Гражданин РФ</label>\n' +
            '    </div> <br>\n' +
            '    <h4>Дата рождения:</h4>\n' +
            '    <input type="date" id="dateBorn" name="dateBorn"\n' +
            '       value="1990-01-01"\n' +
            '       min="1900-01-01" max="2021-12-31">\n' +
            '\n' +
            '    <h4>Образование</h4>\n' +
            '    <p><select name="education">\n' +
            '    <option>Выберите образование</option>\n' +
            '    <option value="1">Среднее</option>\n' +
            '    <option value="2">Высшее неоконченное</option>\n' +
            '    <option value="3">Высшее</option>\n' +
            '    </select></p>\n' +
            '    <h4>Phone</h4>\n' +
            '    <label for="phone"></label><input id="phone" name="phone" type="text">\n' +
            '\n' +
            '    <h4>О себе:</h4>\n' +
            '    <textarea name="comment" id="comment"></textarea>\n' +
            '</div>')

        $('.formForm').append(el)

        el.attr('id',$('.form_atrs').length)

    })

    $('.dellUser').on('click',function (){
        var id = ($('.form_atrs').last().attr('id'))
        console.log('#'+String(id))
        if (id !== '1'){
            $('#'+id).remove()
        }


    })

    $('.save').on('click',function(event){
        event.preventDefault()
        if (validateForm()){

            event.preventDefault()
            return false
        }
        else {
            var getOnDiv = $('.form_atrs').toArray().map(el => $(el).children())
            var res = []
            console.log(res)
            $.each(getOnDiv,function (key,data){
                var inp_chek = data.children().serializeArray()
                var text_chek = $(data).serializeArray()
                var all_data =  $.merge(inp_chek,text_chek)
                    res.push(all_data)
            })
            $.ajax({
                type:'POST',
                url:'/add-form',
                data:JSON.stringify(res),
                dataType:'json',
                contentType: "application/json",
                encode:true,
            }).done(function (data){
                alert('success')
                console.log(data)
            })
            }
        function validateForm(){
            var name = $('.userName')
            var surname = $('.userSurname')
            var patr = $('.patronymic')
            var v_name = false
            var s_name = false
            var patr_chek = false
            $.each(name,function (key,value){
                var vals = $(value)
                if(tryValid(vals)){
                    v_name = true

                }
                $.each(surname,function (key,value){
                    var data = $(value)
                    if(tryValid(data)){
                        s_name = true
                    }

                })
                $.each(patr,function (key,value){
                    var patr_data = $(value)
                    if (patr_data.val()>0){
                        if(patr_data.val()[0]===patr_data.val()[0].toLowerCase()){
                            patr_data.after('<span class="text-error"> Введите  с большой буквы </span>')
                            patr_chek = true

                        }
                    }

                })
            })
            return (v_name||s_name||patr_chek)
        }
    })
})

