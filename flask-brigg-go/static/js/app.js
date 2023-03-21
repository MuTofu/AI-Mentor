
    window.onload = function () {
        var select = document.getElementById('menu')
        var option = select.options[select.selectedIndex];




        select.onchange = function () {
            if (select.value == 'about') {
                location.href = 'about'
                console.log(option.value)
            } else if (select.value == 'home'){
                location.href = 'home'
            } else {
                location.href = 'faq'
            }
        }
    }


