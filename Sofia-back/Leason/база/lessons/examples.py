def color(colorname):
    # функцияставит цвет блока
    return colorname

button_red.event('click', lambda: color('red'))
button_blue.event('click', lambda: color('blue'))
button_green.event('click', lambda: color('green'))

#  () => {}
# function () {}
#  setTimeout(function (){ console.log(123)}, 200)