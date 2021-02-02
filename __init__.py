from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
from mycroft.skills.context import adds_context, removes_context


class TeaSkill(MycroftSkill):
    @intent_handler(IntentBuilder("TeaIntent").require("bring").require("tea"))
    @adds_context("MilkContext")
    def handle_tea_intent(self, message):
        self.milk = False
        self.speak("Of course, would you like Milk with that?", expect_response=True)

    @intent_handler(
        IntentBuilder("NoMilkIntent").require("no").require("MilkContext").build()
    )
    @removes_context("MilkContext")
    @adds_context("HoneyContext")
    def handle_no_milk_intent(self, message):
        self.speak("all right, any Honey?", expect_response=True)

    @intent_handler(
        IntentBuilder("YesMilkIntent").require("yes").require("MilkContext").build()
    )
    @removes_context("MilkContext")
    @adds_context("HoneyContext")
    def handle_yes_milk_intent(self, message):
        self.milk = True
        self.speak("What about Honey?", expect_response=True)

    @intent_handler(
        IntentBuilder("NoHoneyIntent").require("no").require("HoneyContext").build()
    )
    @removes_context("HoneyContext")
    def handle_no_honey_intent(self, message):
        if self.milk:
            self.speak("Heres your Tea with a dash of Milk")
        else:
            self.speak("Heres your Tea, straight up")

    @intent_handler(
        IntentBuilder("YesHoneyIntent").require("yes").require("HoneyContext").build()
    )
    @removes_context("HoneyContext")
    def handle_yes_honey_intent(self, message):
        if self.milk:
            self.speak("Heres your Tea with Milk and Honey")
        else:
            self.speak("Heres your Tea with Honey")


def create_skill():
    return TeaSkill()
