import os
from yt_dlp import YoutubeDL
from moviepy.editor import VideoFileClip
from moviepy.video.fx.all import resize, crop  # Correct import for functions

def download_video(url, output_dir="~/Downloads/vids_ig"):
	if not os.path.exists(output_dir):
		os.makedirs(output_dir)
		
	output_path = os.path.join(output_dir, 'minecraft_parkour_video.mp4')
	home_directory = os.path.expanduser("~")

	ydl_opts = {
		'outtmpl': output_path,
		'format': 'bestvideo+bestaudio/best',
		'merge_output_format': 'mp4',
		'noplaylist': True,  # Ensure only the single video is downloaded
	}

	try:
		with YoutubeDL(ydl_opts) as ydl:
			ydl.download([url])
		return output_path
	except Exception as e:
		print(f"An error occurred while downloading the video: {e}")
		return None

def split_video(input_path, segment_length=60, output_dir='~/Downloads/vids_ig/clips', output_path_template='segment_{:03d}.mp4'):
	video = VideoFileClip(input_path)
	duration = int(video.duration)
	segments = []

	tik_tok_width = 1080
	tik_tok_height = 1920

	for start in range(0, duration, segment_length):
		end = min(start + segment_length, duration)
		segment = video.subclip(start, end)

		# Use the resize function correctly
		if segment.size[0] / segment.size[1] < tik_tok_width / tik_tok_height:
			segment = resize(segment, height=tik_tok_height)
		else:
			segment = resize(segment, width=tik_tok_width)

		# Use the crop function correctly
		segment = crop(segment, width=tik_tok_width, height=tik_tok_height, x_center=segment.size[0] / 2, y_center=segment.size[1] / 2)
		segments.append(segment)

	save_segments(segments, output_dir, output_path_template)
	return segments

def save_segments(segments, output_dir='~/Downloads/vids_ig/clips', output_path_template='segment_{:03d}.mp4'):
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
	youtube_url = "https://www.youtube.com/watch?v=u7kdVe8q5zs"  # Replace VIDEO_ID with a valid video ID
	main(youtube_url)
