# Video Downloader

**Save videos, music, subtitles and thumbnails from YouTube, Facebook, TikTok and 1800+ other sites, in the quality and format you choose.**

Paste a link, press **Analyze** to see the video and its qualities, and press **Add to queue**. Video Downloader does the
rest: it downloads in the background, several at a time, and tells you when each one is saved.

![The main window: a video read from its link, the download options, and the queue with three finished downloads. Video: Big Buck Bunny, (c) Blender Foundation, CC BY 3.0](images/main-window.png)

## What it does

1. **You paste a link.** A video, a whole playlist or channel, or several links at once.
2. **You choose what to get.** Video with sound, video only, or just the sound as MP3, M4A, FLAC and more, in the
   quality you want: each quality shows its size.
3. **It downloads in the background.** Pause, resume or cancel any download, and add more while others run.
4. **It keeps itself working.** Sites change often; one click updates the download engine (yt-dlp) and its tools.

## Features

| | |
|---|---|
| **1800+ sites** | YouTube, Facebook, TikTok, Instagram, X, Vimeo, SoundCloud, Bandcamp and many more. |
| **Any quality** | From 144p to 4K and 8K, 60 fps and HDR when the video has them, with the size of each. |
| **Pick exact streams** | **Choose streams...** lists every video and audio stream with its codec (H.264, VP9, AV1), HDR, audio language and size. Pick a dubbed language, or a codec your TV plays. |
| **Music and audio** | Save just the sound as MP3, M4A, AAC, Opus, FLAC or WAV, at the bitrate you choose, with the cover picture. |
| **Only the part you want** | Download from one time to another, or pick **Chapters**: some of them as one file, or each to its own file named after it. |
| **Playlists and channels** | See every video in the list and tick the ones you want. |
| **Several downloads at once** | Choose how many run at the same time; the rest wait in the queue. |
| **Subtitles and more inside the file** | Embed subtitles in your languages, the thumbnail as cover, the title and description, and chapter marks. |
| **Skip the sponsors** | On YouTube, cut out the sponsor, intro and "subscribe" parts viewers have marked. |
| **PiP video** | Also make a picture-in-picture version of a download, ready to post. |
| **Thumbnails and subtitles on their own** | Tools > **Thumbnail saver** saves a video's cover picture, biggest first; **Subtitle extractor** saves its subtitles as SRT, VTT, ASS or LRC. |
| **Live chat archiver** | Tools > **Live chat archiver** saves a YouTube live stream's or premiere's chat replay: every message with its time, author, Super Chats and memberships. Filter it by words (or a regular expression), and save it as CSV for Excel or JSON. Double-click a message to watch that moment. |
| **Bilingual subtitles** | In the Subtitle extractor, tick two languages and **Bilingual**: one file shows each line in both, the language you choose on top, the other under it. For learning a language, or watching together. |
| **Browser extension** | In Chrome, Edge or Brave, one click on the extension's button sends the video you're watching to the app, signed in as you are in the browser. Or right-click a link or a video and choose **Download with Video Downloader**. |
| **Copy a link, it's read** | Turn on Tools > **Watch the clipboard for links**: copy a video's address in your browser and it's ready to download. |
| **Videos that need a sign-in** | Send them with the browser extension, which brings your sign-in along. Or use the cookies of the browser you're signed in with (Firefox), or a cookies file, for videos only members or friends can see. |
| **Its own log** | Right-click a download and choose **Show log** to see exactly what happened, to fix a problem or ask for help. |
| **Light or dark** | Follows your Windows theme, or choose one in Settings. |

## Choosing the exact streams

For one video, the last entry of the Quality list, **Choose streams...**, opens every stream the site has:

![Choose streams: every video and audio stream with its resolution, frame rate, codec, HDR, type and size](images/stream-picker.png)

Pick a video stream and an audio stream, and press **Use these**. The pick shows in the Quality list and in the queue.

## Sending videos from your browser

The extension for Chrome, Edge and Brave comes with the app. Add it once:

1. In Video Downloader, open **Tools > Browser extension...** and press **Open the folder**. Its path is copied too.
2. In the browser, open `chrome://extensions` (`edge://extensions` in Edge, `brave://extensions` in Brave) and turn
   on **Developer mode**.
3. Press **Load unpacked** and choose that folder (paste its path in the folder box).
4. Pin it: press the puzzle piece next to the address bar, then the pin next to Video Downloader.

Then, on a video's page, click the Video Downloader button: the app opens (or comes to the front) with the video read,
ready to choose the quality and press **Add to queue**. A tick on the button says the video was sent. Right-click a
link, or a video playing in the page, for **Download with Video Downloader**.

Videos you can only see signed in (members-only, private or age-restricted) work too: the extension sends your
browser's cookies for that site with the link, so the app is signed in as you are. When you add the extension, the
browser warns that it can "read and change all your data on all websites": that is what reading a site's cookies
needs. It sends nothing until you click, and then only the link and that one site's cookies, only to the app on your
PC. The app keeps them while it is open, uses them for that site only, and deletes them when you close it.

## Free trial

Try everything free for **30 days**, no key needed and nothing limited. The status bar shows how many days are left.
After that, Video Downloader still reads links, but downloading (videos, music, subtitles, thumbnails and chats) needs
a license key.

## Buying a license

Open **Help > License...** (or click the license text at the right of the status bar), copy the machine code it
shows, and send it to us by email (the **Copy email** button helps). You get a license key back: paste it into the
same window and press **Register**.

Licenses are available for a period of time (for example monthly or yearly), for your PC.

## Requirements

- Windows 10 or Windows 11 (64-bit)
- An internet connection
- About 500 MB of free disk space, plus room for your downloads

## Installing

Run `VideoDownloader-<version>.exe` and follow the steps. No administrator rights are needed. Installing a new
version over the old one keeps your settings.

The first time it starts, Video Downloader downloads ffmpeg (about 110 MB), which it needs to join HD video with its
sound, convert audio and cut parts. The status bar shows how far it got; it is ready to use when that is done.

For YouTube, the app offers to add Deno (about 45 MB) the first time you read a YouTube link: without it YouTube
gives fewer qualities, often not the best. You can also add it later from the Tools menu.

## Please note

Download only what you have the right to: your own videos, videos their owner lets you download, or what the law lets
you copy. Each site has its own terms. See the license agreement shown during setup.

Video Downloader uses yt-dlp and FFmpeg, made by others and free to use under their own licenses: see
THIRD-PARTY-NOTICES.txt in the folder the app is installed in. FFmpeg is gyan.dev's build, the one ffmpeg.org links
to for Windows.

## Contact

- For support: **khanh1985@gmail.com**
- **Phone:** +84 985 884 764
- [Privacy policy](https://github.com/xuankhanh/VideoDownloader/blob/main/PRIVACY.md), including how to delete your data

© 2026 Truong Xuan Khanh. All rights reserved.
