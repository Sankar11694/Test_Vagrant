import unittest
from recently_played_store import RecentlyPlayedStore
class TestRecentlyPlayedStore(unittest.TestCase):
    def setUp(self):
        self.store = RecentlyPlayedStore(3)
    def test_play_song(self):
        self.store.play_song("user1", "S1")
        self.assertEqual(self.store.get_recently_played("user1"), ["S1"])
        self.store.play_song("user1", "S2")
        self.assertEqual(self.store.get_recently_played("user1"), ["S1", "S2"])
        self.store.play_song("user1", "S3")
        self.assertEqual(self.store.get_recently_played("user1"), ["S1", "S2", "S3"])
        self.store.play_song("user1", "S4")
        self.assertEqual(self.store.get_recently_played("user1"), ["S2", "S3", "S4"])
        self.store.play_song("user1", "S2")
        self.assertEqual(self.store.get_recently_played("user1"), ["S3", "S4", "S2"])
        self.store.play_song("user1", "S1")
        self.assertEqual(self.store.get_recently_played("user1"), ["S4", "S2", "S1"])
    def test_multiple_users(self):
        self.store.play_song("user1", "S1")
        self.store.play_song("user2", "S2")
        self.store.play_song("user1", "S3")
        self.store.play_song("user2", "S4")
        self.assertEqual(self.store.get_recently_played("user1"), ["S1", "S3"])
        self.assertEqual(self.store.get_recently_played("user2"), ["S2", "S4"])
    def test_capacity_less_than_played_songs(self):
        self.store.play_song("user1", "S1")
        self.store.play_song("user1", "S2")
        self.store.play_song("user1", "S3")
        self.store.play_song("user1", "S4")
        self.store.play_song("user1", "S5")
        self.assertEqual(self.store.get_recently_played("user1"), ["S3", "S4", "S5"])
if __name__ == '__main__':
    unittest.main()