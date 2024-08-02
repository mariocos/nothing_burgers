import os
from pytube import YouTube
from moviepy.editor import VideoFileClip
from moviepy.video.fx import resize, crop

def download_video(url, output_dir="/home/mario/Downloads/vids_ig"):
	try:
		yt = YouTube(url)
		stream = yt.streams.get_highest_resolution()
		if not os.path.exists(output_dir):
			os.makedirs(output_dir)
		output_path = os.path.join(output_dir, 'minecraft_parkour_video.mp4')
		stream.download(output_path=output_path)
		return output_path
	except Exception as e:
		print(f"An error occurred while downloading the video: {e}")
		return None

def split_video(input_path, segment_length=60, output_dir='/home/mario/Downloads/vids_ig', output_path_template='segment_{:03d}.mp4'):
	try:
		video = VideoFileClip(input_path)
		duration = int(video.duration)
		segments = []

		tik_tok_width = 1080
		tik_tok_height = 1920

		for start in range(0, duration, segment_length):
			end = min(start + segment_length, duration)
			segment = video.subclip(start, end)

			if segment.size[0] / segment.size[1] < tik_tok_width / tik_tok_height:
				segment = resize(segment, height=tik_tok_height)
			else:
				segment = resize(segment, width=tik_tok_width)
			segment = crop(segment, width=tik_tok_width, height=tik_tok_height, x_center=segment.size[0] / 2, y_center=segment.size[1] / 2)
			segments.append(segment)
		save_segments(segments, output_dir, output_path_template)
		return segments
	except Exception as e:
		print(f"An error occurred while splitting the video: {e}")
		return []

def save_segments(segments, output_dir='/home/mario/Downloads/vids_ig/clips', output_path_template='segment_{}.mp4'):
	if not os.path.exists(output_dir):
		os.makedirs(output_dir)

	for i, segment in enumerate(segments):
		segment_path = os.path.join(output_dir, output_path_template.format(i))
		try:
			segment.write_videofile(segment_path, codec="libx264", fps=24)
		except Exception as e:
			print(f"An error occurred while saving the segment {i}: {e}")

def main(youtube_url):
	video_path = download_video(youtube_url)
	if video_path:
		segments = split_video(video_path)
		save_segments(segments)

# Example usage
if __name__ == "__main__":
	youtube_url = "https://www.youtube.com/watch?v=_-2ZUciZgls"  # Test with a simple, working URL
	main(youtube_url)
