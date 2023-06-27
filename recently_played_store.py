from collections import defaultdict
class RecentlyPlayedStore:
    def __init__(self, capacity):
        self.capacity = capacity
        self.recently_played = defaultdict(list)
    def play_song(self, user, song):
        self.recently_played[user].append(song)
        if len(self.recently_played[user]) > self.capacity:
            self.recently_played[user] = self.recently_played[user][-self.capacity:]
    def get_recently_played(self, user):
        return self.recently_played[user]