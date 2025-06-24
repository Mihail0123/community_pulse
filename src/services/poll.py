from src.services.database import DatabaseService
from src.models.poll import Poll

class PollService:
    db_service = DatabaseService()

    def get_by_poll_id(self, poll_id):
        poll, exep = self.db_service.get_by_id(Poll, poll_id)
        if exep:
            return None, exep
        if not poll:
            return None, str(Poll.DoesNotExist)
        return poll.to_dict(), None
