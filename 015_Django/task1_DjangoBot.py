from third_app.models import *
import telebot
config = {
    'name': 'BanVital_bot',
    'token': '5787697902:AAHmBf2JqZGctl3zbwunMgfBQVvhxXEUfI8'
}
botler = telebot.TeleBot(config['token'])
@botler.message_handler(content_types=['text'])
def get_text(message):
    if message.text == "/Curators":
        academy = Curators.objects.all()
        curators=""
        for i in academy:
            curators=curators+f'Name: {i.name}, Surname: {i.surname}\n'
        botler.send_message(message.chat.id, curators)
    if message.text == "/Faculties":
        academy = Faculties.objects.all()
        curators = ""
        for i in academy:
            curators =curators + f'Name: {i.name}\n'
        botler.send_message(message.chat.id, curators)
    if message.text == "/Departments":
        academy = Departments.objects.all()
        curators = ""
        for i in academy:
            curators = curators + f'Name: {i.name}, Building: {i.building}, Financing: {i.financing}, FacultID: {i.facultyId}\n'
        botler.send_message(message.chat.id, curators)
    if message.text == "/Groups":
        academy = Groups.objects.all()
        curators = ""
        for i in academy:
            curators = curators + f'Name: {i.name}, Year: {i.year}, Departamentid: {i.departamentid}\n'
        botler.send_message(message.chat.id, curators)
    if message.text == "/GroupsCurators":
        academy = GroupsCurators.objects.all()
        curators = ""
        for i in academy:
            curators = curators + f'CuratorId: {i.curatorId}, GroupId: {i.groupId}\n'
        botler.send_message(message.chat.id, curators)
    if message.text == "/Students":
        academy = Students.objects.all()
        curators = ""
        for i in academy:
            curators = curators + f'Name: {i.name}, Surname: {i.surname}, Rating: {i.rating}\n'
        botler.send_message(message.chat.id, curators)
    if message.text == "/Subjects":
        academy = Subjects.objects.all()
        curators = ""
        for i in academy:
            botler.send_message(message.chat.id, f'Name: {i.name}\n')
    if message.text == "/Teachers":
        academy = Teachers.objects.all()
        curators = ""
        for i in academy:
            curators = curators + f'Name: {i.name}, Surname: {i.surname}, IsProfessor: {i.IsProfessor}, salary: {i.salary}\n'
        botler.send_message(message.chat.id, curators)
    if message.text == "/GroupsStudents":
        academy = GroupsStudents.objects.all()
        curators = ""
        for i in academy:
            curators = curators + f'GroupId: {i.groupId}, StudentId: {i.studentId}\n'
        botler.send_message(message.chat.id, curators)
    if message.text == "/Lectures":
        academy = Lectures.objects.all()
        curators = ""
        for i in academy:
            curators = curators + f'Date: {i.date}, SubjectId: {i.subjectId}, TeacherId: {i.teacherId}\n'
        botler.send_message(message.chat.id, curators)
    if message.text == "/GroupsLectures":
        academy = GroupsLectures.objects.all()
        curators = ""
        for i in academy:
            curators = curators + f'CuratorId: {i.curatorId}, GroupId:{i.groupId}\n'
        botler.send_message(message.chat.id, curators)

botler.polling(none_stop=True,interval=0)