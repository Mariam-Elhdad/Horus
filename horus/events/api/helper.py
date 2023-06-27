from abc import ABC, abstractmethod

from django.contrib.auth.models import User
from rest_framework import status

from horus.events.models import Event, Going


class IAttendance(ABC):
    @abstractmethod
    def reset(self):
        """
        reset the attributes of the object
        """

    @abstractmethod
    def press(self):
        """
        perform going and its effect on the interesting state
        """


class MessageList:
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._messages = []

    def append(self, message, state):
        self._messages.append((message, state))

    def get_top(self):
        if self._messages:
            return self._messages[-1]
        return None


class GoingEvent(IAttendance):
    def __init__(self, user: User, event_id: int) -> None:
        self.reset()
        self.user = user
        self.event = self.get_event(event_id)

    def set_error(self, message: str, state: int) -> None:
        self.is_there_error = True
        self.message_list.append(message, state)

    def get_event(self, user_id: int):
        """
        get event or None
        if there is no event that append error massage
        """
        event = Event.objects.filter(id=user_id)
        if event.count() == 0:
            self.set_error("the event not found", status.HTTP_404_NOT_FOUND)
            return None
        return event.first()

    def get_going_or_none(self):
        going = Going.objects.filter(event=self.event, user=self.user)
        if going.count() == 0:
            return None
        return going.first()

    def reset(self):
        self.is_there_error = False
        self.message_list = MessageList()

    def press(self):
        if self.is_there_error:
            return False
        going = self.get_going_or_none()
        if going:
            going.delete()
            self.message_list.append("removed", status.HTTP_204_NO_CONTENT)
        else:
            Going.objects.create(user=self.user, event=self.event)
            self.message_list.append("created", status.HTTP_201_CREATED)
        return True
