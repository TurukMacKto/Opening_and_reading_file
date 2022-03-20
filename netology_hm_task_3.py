import os

try:
    os.mkdir('task_three')
except:
    pass
os.chdir('task_three')
with open('first_text.txt', 'w') as first_text:
    first_text.write("Начальник полиции\n\
лично позвонил в шестнадцатый участок. А спустя одну минуту тридцать секунд\n\
в дежурке и других комнатах нижнего этажа раздались звонки\n\
Когда Иенсен -- комиссар  шестнадцатого участка -- вышел из своего\n\
кабинета, звонки еще не смолкли. Иенсен был мужчина средних лет, обычного\n\
сложения, с лицом плоским и невыразительным. На последней ступеньке винтовой\n\
лестницы он задержался и обвел взглядом помещение дежурки. Затем поправил\n\
галстук и проследовал к машине.")
with open('second_text.txt', 'w') as second_text:
    second_text.write("Тревога началась в тринадцать часов ноль две минуты.")
with open('third_text.txt', 'w') as third_text:
    third_text.write("В  это время  дня  машины текли сплошным  блестящим  потоком,  а  среди\n\
потока, будто  колонны из бетона  и стекла, высились  здания. Здесь,  в мире\n\
резких граней,  люди  на тротуарах  выглядели  несчастными и  неприкаянными.\n\
Одеты они были хорошо, но как-то удивительно походили друг на друга и все до\n\
одного спешили. Они шли нестройными  вереницами, широко разливались, завидев\n\
красный  светофор или  металлический  блеск кафе-автоматов.  Они непрестанно\n\
озирались по сторонам и теребили портфели и сумочки.\n\
Полицейские  машины  с  включенными  сиренами  пробивались  сквозь  эту\n\
толчею.")


def sorting():
    sorted_list = {}
    dir_ = os.getcwd()
    for items in os.listdir(dir_):
        with open(items, 'r+') as fd:
            common_list = fd.read().splitlines()
            str_len = len(common_list)
            sorted_list.update({str_len: [fd.name, str_len, common_list]})
    return sorted(sorted_list.values(), key=lambda x: x[2], reverse=True)


def created(created_file):
    with open(created_file + '.txt', 'w+') as newfile:
        for file in sorting():
            newfile.write(f'{file[0]}\n')
            newfile.write(f'{file[1]}\n')
            for string in file[2]:
                newfile.write(string + '\n')
            newfile.write('-------------------\n')


created('new_text')
