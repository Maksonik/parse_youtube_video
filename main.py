from pytube import YouTube

def parse_youtube_video(url):
    try:
        yt = YouTube(url)

        print("📺 Название:", yt.title)
        print("🧑 Автор:", yt.author)
        print("⏱️ Длительность (сек):", yt.length)
        print("📅 Дата публикации:", yt.publish_date)
        print("👀 Просмотры:", yt.views)
        print("📃 Описание:\n", yt.description[:300], "...")

        # Скачать видео (по желанию)
        # yt.streams.get_highest_resolution().download(output_path="downloads")

    except Exception as e:
        print("❌ Ошибка:", e)

# parse_youtube_video("https://www.youtube.com/video)
