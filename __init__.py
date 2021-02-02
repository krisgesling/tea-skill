from mycroft import MycroftSkill, intent_file_handler


class Tea(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('tea.intent')
    def handle_tea(self, message):
        self.speak_dialog('tea')


def create_skill():
    return Tea()

