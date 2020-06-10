from mycroft import MycroftSkill, intent_file_handler


class LangHelper(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('helper.lang.intent')
    def handle_helper_lang(self, message):
        self.speak_dialog('helper.lang')


def create_skill():
    return LangHelper()

