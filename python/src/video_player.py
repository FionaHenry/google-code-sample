"""A video player class."""

from .video_library import VideoLibrary
import random


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.current_video = "none"
        self.video_paused = False

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        print("Here's a list of all available videos:")
        available_videos = self._video_library.get_all_videos()
        available_videos.sort(key=lambda video: video.title)
        for item in available_videos:
            print(f"  {item.title} ({item.video_id}) [{item.tags}]")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        

        if self.current_video == "none":
            if video_id == "funny_dogs_video_id":
                self.current_video = "Funny Dogs"
                print("Playing video: Funny Dogs")
            elif video_id == "amazing_cats_video_id":
                self.current_video = "Amazing Cats"
                print("Playing video: Amazing Cats")
            elif video_id == "another_cat_video_id":
                self.current_video = "Another Cat Video"
                print("Playing video: Another Cat Video")
            elif video_id == "life_at_google_video_id":
                self.current_video = "Life at Google"
                print("Playing video: Life at Google")
            elif video_id == "nothing_video_id":
                self.current_video = "Video about nothing"
                print("Playing video: Video about nothing")
            else:
                print("Cannot play video: Video does not exist")
        else:
            print(f"Stopping video: {self.current_video}")

            if video_id == "funny_dogs_video_id":
                self.current_video = "Funny Dogs"
                print("Playing video: Funny Dogs")
            elif video_id == "amazing_cats_video_id":
                self.current_video = "Amazing Cats"
                print("Playing video: Amazing Cats")
            elif video_id == "another_cat_video_id":
                self.current_video = "Another Cat Video"
                print("Playing video: Another Cat Video")
            elif video_id == "life_at_google_video_id":
                self.current_video = "Life at Google"
                print("Playing video: Life at Google")
            elif video_id == "nothing_video_id":
                self.current_video = "Video about nothing"
                print("Playing video: Video about nothing")
            else:
                print("Cannot play video: Video does not exist")

    def stop_video(self):
        """Stops the current video."""

        if self.current_video == "none":
            print("Cannot stop video: No video is currently playing")
        else:
            print(f"Stopping video: {self.current_video}")

    def play_random_video(self):
        """Plays a random video from the video library."""

        video = random.randint(1, 5)

        print(video)

        if video == 1:
            self.current_video = "Funny Dogs"
            self.play_video
        elif video == 2:
            self.current_video = "Amazing Cats"
            self.play_video
        elif video == 3:
            self.current_video = "Another Cat Video"
            self.play_video
        elif video == 4:
            self.current_video = "Life at Google"
            self.play_video
        elif video == 5:
            self.current_video = "Video about nothing"
            self.play_video

    def pause_video(self):
        """Pauses the current video."""

        if self.video_paused == False and self.current_video != "none":
            print(f"Pausing video: {self.current_video}")
        elif self.video_paused == True and self.current_video != "none":
            print(f"Video already paused: {self.current_video}")
        else:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""

        if self.video_paused == False and self.current_video != "none":
            print("Cannot continue video: Video is not paused")
        elif self.current_video == "none":
            print("Cannot continue video: No video is currently playing")
        else:
            print(f"Continuing video: {self.current_video}")

    def show_playing(self):
        """Displays video currently playing."""

        if self.current_video != "none":
            print(f"Currently playing: {self.current_video}")
        else:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
