from collections import defaultdict
from shared.eventInfrastructure.eventBus.EventBus import EventBus
from shared.eventInfrastructure.eventBus.EventListener import EventListener


# class EventBus:
#     def __init__(self):
#         self.subscribers:dict[str, list[EventListener]] = {}
#
#     def subscribe(self, eventType:str, subscriber:EventListener):
#         if eventType not in self.subscribers:
#             self.subscribers[eventType] = []
#         self.subscribers[eventType].append(subscriber)
#
#     def publish(self, event):
#         subscribers = self.subscribers.get(event.eventType, [])
#         for subscriber in subscribers:
#             command = event
#             subscriber.execute(command)

class EventBusImp(EventBus):
    def __init__(self):
        self.handlers = defaultdict(list)
    

    def subscribe(self, eventType, handler):
        self.handlers[eventType].append(handler)

    def publish(self, event):
        eventType = type(event).__name__
        if eventType in self.handlers:
            for handler in self.handlers[eventType]:
                handler(event)

