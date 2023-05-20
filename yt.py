from pytube import YouTube
print(r"""
            $$\                             
            $$ |                            
$$\   $$\ $$$$$$\        $$$$$$\  $$\   $$\ 
$$ |  $$ |\_$$  _|      $$  __$$\ $$ |  $$ |
$$ |  $$ |  $$ |        $$ /  $$ |$$ |  $$ |
$$ |  $$ |  $$ |$$\     $$ |  $$ |$$ |  $$ |
\$$$$$$$ |  \$$$$  |$$\ $$$$$$$  |\$$$$$$$ |
 \____$$ |   \____/ \__|$$  ____/  \____$$ |
$$\   $$ |              $$ |      $$\   $$ |
\$$$$$$  |              $$ |      \$$$$$$  |
 \______/               \__|       \______/ 
""")
print('------------ Created by SciMathist\n(yt.py webapp will be launced soon.)\n')

while True:
    # URL of the YouTube video you want to download
    video_url = input("Enter the YouTube video URL (or 'exit' to quit): ")

    if video_url.lower() == 'exit':
        print("Exiting...")
        break

    # Create a YouTube object
    youtube = YouTube(video_url)

    # Get available video streams
    streams = youtube.streams.filter(progressive=True).order_by('resolution')

    # Print available resolutions for the user to choose from
    print("Available Resolutions:")
    for i, stream in enumerate(streams):
        print(f"{i+1}. Resolution: {stream.resolution}, Format: {stream.mime_type}")

    # Get user input for resolution selection
    choice = int(input("Enter the number corresponding to the desired resolution: "))

    # Validate user input
    if choice < 1 or choice > len(streams):
        print("Invalid choice. Please select a valid resolution.")
        continue

    # Get the selected stream based on user choice
    selected_stream = streams[choice - 1]

    # Download the video
    selected_stream.download()

    print("Video downloaded successfully!")

