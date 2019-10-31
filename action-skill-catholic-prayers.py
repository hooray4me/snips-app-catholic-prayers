#!/usr/bin/env python3.7

from snipsTools import SnipsConfigParser
from hermes_python.hermes import Hermes
from hermes_python.ontology import *

CONFIG_INI = "config.ini"

MQTT_IP_ADDR: str = "localhost"
MQTT_PORT: int = 1883
MQTT_ADDR: str = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

class Prayers(object):

    def __init__(self):
        try:
            self.config = SnipsConfigParser.read_configuration_file(CONFIG_INI)
        except Exception:
            self.config = None

        self.start_blocking()

    def recitePrayer_callback(self, hermes, intent_message):

        prayer = intent_message.slots.prayer.first().value
        myaction = intent_message.slots.myaction.first().value
        print(prayer)
        print(my action)
        grace = 'Bless us, oh Lord, and these, thy gifts, which we are about to receive, From thy bounty, through Christ, our Lord. Amen. May the souls, of the faithly departed, through the mercy of God, rest in peace. AMEN.'
        lords_prayer = 'Our Father, who art in heaven, hallowed be thy name. Thy kingdom come, thy will be done, on earth, as it is in heaven. Give us this day, our daily bread, and forgive us our trespasses, as weforgive those who trespass against us. and lead us not into temptation, but deliver us from evil. Amen.'
        hail_mary = 'Hail Mary. Full of Grace, The Lord is with thee. Blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners now, and at the hour of our death. Amen.'
        glory_be = 'Glory be to the Father, and to the Son, and to the Holy Spirit. As it was in the beginning, is now, and ever shall be, world without end. Amen.'
        nicene_creed = 'I believe in one God, the Father, the Almighty, Maker of heaven and earth, of all things visible and invisible. I believe in one Lord Jesus Christ, the only-begotten Son of God, born of the Father before all ages, God from God, Light from Light, true God from true God, begotten, not made, consubstantial with the Father. Through him all things were made. For us and for our salvation he came down from heaven:by the power of the Holy Spirit was incarnate of the Virgin Mary, and became man. For our sake he was crucified under Pontius Pilate; he suffered death and was buried, and rose again on the third day in accordance with the Scriptures. He ascended into heaven and is seated at the right hand of the Father. He will come again in glory to judge the living and the dead, and his kingdom will have no end. I believe in the Holy Spirit, the Lord, the giver of life, who proceeds from the Father and the Son. With the Father and the Son he is adored and glorified. He has spoken through the Prophets. I believe in one, holy, catholic and apostolic Church. I confess one baptism for the forgiveness of sins, and I look forward to the resurrection of the dead, and the life of the world to come. Amen'
        prayer_to_saint_michael = 'Saint Michael, the Archangel, defend us in battle. Be our defense against the wickedness and snares of the Devil. May God rebuke him, we humbly pray, and do thou, O Prince of the heavenly hosts, by the power of God, thrust into hell Satan, and all the evil spirits, who prowl about the world, seeking the ruin of souls. Amen'
        act_of_contrition = 'My God, I am sorry for my sins with all my heart. In choosing to do wrong and failing to do good, I have sinned against you whom I should love above all things. I firmly intend, with your help, to do penance, to sin no more, and to avoid whatever leads me to sin. Our Savior Jesus Christ suffered and died for us. In His name. My God have mercy.'

        if myaction == "say" or action == "recite":
            if prayer == "grace":
                hermes.publish_end_session(intent_message.session_id, grace)
            elif prayer == "lords prayer":
                hermes.publish_end_session(intent_message.session_id, lords_prayer)
            elif prayer == "hail mary":
                hermes.publish_end_session(intent_message.session_id, hail_mary)
            elif prayer == "glory be":
                hermes.publish_end_session(intent_message.session_id, glory_be)
            elif prayer == "nicene creed":
                hermes.publish_end_session(intent_message.session_id, nicene_creed)
            elif prayer == "prayer to saint michael":
                hermes.publish_end_session(intent_message.session_id, prayer_to_saint_michael)
            elif prayer == "act of contrition":
                hermes.publish_end_session(intent_message.session_id, act_of_contrition) 


    def master_intent_callback(self,hermes, intent_message):
        coming_intent = intent_message.intent.intent_name
        if coming_intent == 'hooray4me:prayers':
            self.recitePrayer_callback(hermes, intent_message)


    # register callback function to its intent and start listen to MQTT bus
    def start_blocking(self):
        with Hermes(MQTT_ADDR) as h:
            h.subscribe_intents(self.master_intent_callback).start()

if __name__ == "__main__":
    Prayers()
