**English** | [Tiếng Việt](https://github.com/xuankhanh/MediaDownloader/blob/main/README.vi.md)

# K-Media Downloader

**Save videos, music, pictures, albums, subtitles and thumbnails from YouTube, Facebook, TikTok, Douyin, Bilibili, Instagram and 1800+ other sites, in the quality and format you choose.**

Paste a link, press **Analyze** to see what it has (a video and its qualities, a playlist, or a post's pictures), and press **Add to queue**. K-Media Downloader does the
rest: it downloads in the background, several at a time, and tells you when each one is saved.

![The main window: a video read from its link, the download options, the queue with three finished downloads and its Downloads and Uploads tabs, and the menus for Popular videos, Upload videos and the Library. Video: Big Buck Bunny, (c) Blender Foundation, CC BY 3.0](images/main-window.png)

## What it does

1. **You paste a link.** A video, a whole playlist or channel, a picture, album or post, or several links at once.
2. **You choose what to get.** Video with sound, video only, or just the sound as MP3, M4A, FLAC and more, in the
   quality you want: each quality shows its size. Or a post's or album's pictures, all of them or only the latest.
3. **It downloads in the background.** Pause, resume or cancel any download, and add more while others run.
4. **It keeps itself working.** Sites change often: the download engine (yt-dlp) updates itself each time the app
   starts, and one click updates the other tools and K-Media Downloader itself, the window showing what is new in the new version. Settings can switch yt-dlp to its nightly builds, which get site fixes days sooner.

## Features

| | |
|---|---|
| **1800+ sites** | YouTube, Facebook, TikTok, Douyin, Bilibili, Instagram, X, Vimeo, SoundCloud, Bandcamp and many more. |
| **Any quality** | From 144p to 4K and 8K, 60 fps and HDR when the video has them, with the size of each. |
| **Pick exact streams** | **Choose streams...** lists every video and audio stream with its codec (H.264, VP9, AV1), HDR, audio language and size. Pick a dubbed language, or a codec your TV plays. |
| **Plays everywhere** | Choose **MP4 H.264** as the format and the video plays on any TV, phone, car or video editor: a video the site only has in VP9, AV1 or HEVC (often 1440p and 4K), or in HDR, is converted after downloading. |
| **Music and audio** | Save just the sound as MP3, M4A, AAC, Opus, FLAC or WAV, at the bitrate you choose, with the cover picture. |
| **Only the part you want** | Download from one time to another, or pick **Chapters**: some of them as one file, or each to its own file named after it. |
| **Playlists and channels** | See every video in the list and tick the ones you want. Open the same playlist or channel again later and the videos you already downloaded are greyed and unticked: only the new ones are added. |
| **Pictures and posts** | Photos and whole posts too, from 300+ sites (Instagram and X photos, Pinterest, Imgur, DeviantArt, Reddit galleries...): install **gallery-dl** from the Tools menu, and links yt-dlp can't read are read with it. Or choose **Pictures and posts** to get every file of a post or profile, or only its latest posts (the last 10, 50... or the last 7, 30 days). When a post has a video and pictures, both are offered. |
| **Sign in to sites** | For private, friends-only and members-only posts and videos, and YouTube's "confirm you're not a bot": Tools > **Sign in to sites** opens Facebook, YouTube, Instagram, X, TikTok and others in a separate browser window. Sign in there once, and downloads from that site use it. Your own browser isn't touched. |
| **Your file names** | Change a download's name before adding it, or a playlist's in its list (double-click or F2). The rest are named by Settings > **File name template**, which can also sort them into folders (by channel, by date...). **File date** dates each file when it was posted, or when it was downloaded. |
| **Drag and drop** | Drop a link from your browser, a link shortcut, or a text file of links on the window: it is read at once. Drop a video or sound file from your PC, and a menu opens it in the Tools that work on it: subtitles, hashtags and summary, pictures, voice, music and sound effects, or dubbing. |
| **Files on your PC too** | The Subtitle extractor, Hashtags, description and summary, Frame extractor, Separate voice, music and sound effects and Dub into another language take a video file on your PC as well as a link: **Choose a file...**, or drop it on their window. Nothing is downloaded. |
| **Faster downloads** | Each file is downloaded over many connections at once with **aria2**, which the app adds by itself: much faster on sites that slow down each connection (Facebook, Bilibili and others). If a site refuses it, that download is tried again without it. Turn it off in Settings > Network. |
| **Network settings** | A proxy, a speed limit per download, how many parts of a streamed video come at once, and a browser to look like (Chrome, Edge, Firefox, Safari) for sites that turn away downloaders: Settings > Network. |
| **Several downloads at once** | Choose how many run at the same time; the rest wait in the queue. Close the app whenever you like: the queue comes back next time, and unfinished downloads carry on where they stopped. |
| **Live streams** | Record a live stream from its beginning or from now, or wait for one that hasn't started. Press **Stop & save** to keep what's recorded so far. |
| **Subtitles and more inside the file** | Embed subtitles in your languages, the thumbnail as cover, the title and description, and chapter marks. |
| **Burned-in subtitles** | Or draw the subtitles on the picture (Settings > Subtitles in the video), so they show on any player or site. |
| **Skip the sponsors** | On YouTube, cut out the sponsor, intro and "subscribe" parts viewers have marked. |
| **Faster on your graphics card** | Converting to MP4 H.264, burning in subtitles and making re-up videos (picture-in-picture too) encode the whole video again: K-Media Downloader does it on your NVIDIA, AMD or Intel graphics card when that is faster than the processor, and on the processor otherwise. An NVIDIA card also decodes the video, which frees the processor (about 1.7 times as fast for 4K), and burns subtitles into WebM videos as AV1 (RTX 40 and newer; others make them VP9 on the processor). Files made on the card can be a little larger. Settings > **Encoding** shows what it found, and can turn it off. Downloading itself doesn't encode anything, so it doesn't need the card. The Frame extractor's one picture every few seconds is also taken on an NVIDIA card, about 3 times as fast for a 4K video. |
| **Thumbnails and subtitles on their own** | Tools > **Thumbnail saver** saves a video's cover picture, biggest first; **Subtitle extractor** saves its subtitles as SRT, VTT, ASS or LRC. From a video file on your PC, it saves the subtitles inside it (MKV, MP4) or beside it (SRT, WebVTT named after it), free even once the free days are over. |
| **Live chat archiver** | Tools > **Live chat archiver** saves a YouTube live stream's or premiere's chat replay: every message with its time, author, Super Chats and memberships. Filter it by words (or a regular expression), and save it as CSV for Excel or JSON. Double-click a message to watch that moment. |
| **Subtitles from speech** | Most TikTok, Douyin and Facebook videos have no subtitles: in the Subtitle extractor, **Make from speech** listens to what is said and offers a menu to extract the original subtitles, translate them with the local AI model into English, Vietnamese or another language and save a separate subtitle file, or translate and burn them directly into the video. Subtitles can stay at the bottom, cover existing bottom subtitles with a black band, or be placed at the top. From a link, or a video or sound file on your PC. It runs on your PC with whisper.cpp and Qwen3, nothing is sent anywhere, and several times faster on a graphics card of its own (NVIDIA, AMD or Intel Arc) when there is one; the first time it downloads the speech recognizer and a model (150 to 575 MB, by how accurate you choose), and the translator (about 5 GB). |
| **Hashtags, description and summary** | Tools > **Hashtags, description and summary** shows a video's hashtags, from its title, its description and the site's tags, ready to copy for your own post, and its description. **Summarize** writes what the video is about and its main points, in the language you choose (Vietnamese, English and more), from what is said in it: its own subtitles, or what the speech recognizer hears when it has none. It runs on your PC with Make from speech's translator (Qwen3 8B), nothing is sent anywhere; the first time it downloads it (about 5 GB). Save them all as a text file. A video file on your PC has its hashtags taken from its name and from the title and description inside it (K-Media Downloader puts them in the videos it downloads), and is summarized from the subtitles inside it or beside it, or what is said. |
| **Pictures from a video** | Tools > **Frame extractor** saves pictures from a video: one every few seconds, one at each change of scene, at the times you type, a number of them spread evenly, or every frame; of the whole video or only a part, which is all it downloads. As JPG, PNG or WebP, at the size you choose (1080p at first: 4K takes about twice as long), each named with its time in the video, and if you like a contact sheet with all of them in a grid. The pictures appear in the folder as they are made, and the ones made stay when you stop. Spread evenly reads the pictures straight from the video online, without downloading it, when they are 4 seconds apart or more; changes of scene are found in the site's smallest copy of the video when it has one (YouTube does), five times as quick for a 4K video. Every frame says first how much room the pictures take, and warns when the drive hasn't enough. Or choose a video file on your PC: the pictures are taken straight from it. Each video's pictures go in a folder named after it, unless you untick that. |
| **Voice, music and sound effects** | Tools > **Separate voice, music and sound effects** takes a video's sound apart into what is said, the background music (with its singing) and the sound effects, each to its own file (WAV, MP3, M4A or FLAC): a voice to dub over or subtitle, music without the talking, a video's sound without its music. From a link or a file on your PC. It runs on your PC with the BandIt v2 model, nothing is sent anywhere: on a graphics card of its own (NVIDIA, AMD or Intel) a minute of sound takes about a minute, on the processor several. The first time it downloads ONNX Runtime and the model (about 270 MB). |
| **Dub into another language** | Tools > **Dub into another language** makes a video speak another language. For example, a video where people speak Chinese comes back with a Vietnamese voice saying what they say. What is said is heard and translated (as Make from speech does), each line is read by a voice at its time, a little faster where the translation is longer, over the video's own music and sound effects with its voice taken out (or its sound turned down, if you untick that), and the picture is kept as it is. The original sound stays as a second audio track you can switch to. Into Vietnamese, English, Chinese, Indonesian, French, German, Spanish, Portuguese, Italian, Russian, Arabic or Turkish. From a link or a file on your PC. It all runs on your PC, with the Piper voices, nothing is sent anywhere. The voice is a synthetic one, not the speaker's. You can also burn the translation into the picture as subtitles (at the bottom, over a black box, or at the top), hide subtitles already burned into the video (blurred, covered with a black box or cut off, before the new ones are drawn: they are hidden, not taken out), and make a re-up video from it in the same pass. The first time it downloads Piper and the voice (about 85 MB), besides the speech recognizer, the translator and the separator when they aren't there yet. |
| **Re-up video** | Also make a version of each download ready to post again: tick the **Re-up video** box beside Add to queue, and set it in Settings > **Re-up**. There, **Frame** is 9:16 (Shorts, Reels, TikTok), 1:1, 4:5, 16:9 or **Same shape as the video** (the first, and the default: it keeps the video's own shape), **Video in the frame** is whole over a blurred copy of itself, filled in, or a picture-in-picture (smaller, with a white border, over a blurred copy: what the old **Make PiP video** box made), and your own logo goes in a corner. It is one video, saved next to the download as "Title_reup.mp4" ("Title.vi_reup.mp4" when its speech is translated into Vietnamese, with the language of the translation in its name). In that same video it can also have what is said translated (**Translate into**) and dubbed with a voice or burned in as subtitles, and it writes a title, description and hashtags to post with in a text file ("Title.post.txt", "Title.vi.post.txt" when translated). The **Re-up video** box is greyed out while these choices would make nothing (the video's own shape, whole, with no logo, no step and no old subtitles to hide): choose a frame, a logo, picture-in-picture or a step. What those need (the speech recognizer, the translator, the voice) is downloaded once from Tools > **Dub into another language**, which is also where the AI steps take their choices from (the music and original sound kept, where the subtitles go). The Dub window has its own **Also make a re-up video** box, and **Hide the video's old subtitles** (also in Settings > **Re-up**, the same choice; **Pick on a picture** shows a picture of the video, from a file on your PC or a link, and you drag a box over the subtitles instead of typing numbers; the box can be a part of the width, except when cutting off, which takes the whole width): it blurs, covers with a black box or cuts off the band where subtitles burned into the picture are, before the new ones are drawn. That hides them, it can't take them out. Robert can set all this for you: tell him the frame, the logo, the language and the steps you want. It all runs on your PC, nothing is sent anywhere. A video already on your PC is re-upped from Tools > **Re-up video...**, from the queue's right-click menu or from the Library. Only for videos you may post again: your own, or with the owner's permission. |
| **Popular videos** | The **Popular videos** menu lists what is popular on **YouTube** (the most popular chart of a country, by category), **Facebook** (the Watch page, or the Pages you add), **TikTok** (the Explore page, by category), **Douyin**, **Bilibili** (bilibili.com or bilibili.tv) and **Instagram** (Reels: the signed-in account's feed, a hashtag or an account), as a grid of covers. Choose the least views and the least likes, how many videos and the order (most viewed, newest, most liked, most a day...), press **Find**, tick the ones you want and add them to the queue. A card shows the video's likes beside its views when the site gives them (YouTube, Facebook Pages, TikTok, Bilibili and Instagram), and pointing at it shows its comments and shares too. For Facebook Pages, a drop-down list holds the Pages you add with **+** (take one out with **-**): **All Pages** reads three of them at random, side by side, and a Page chosen reads that one alone. Facebook, TikTok, Douyin, Bilibili and Instagram are read in a browser the app opens with no window; Instagram needs a sign-in, and a spare account is safer than your main one. |
| **Post videos** | The **Upload videos** menu posts a video to your **YouTube**, **Facebook** or **TikTok** account, from the queue, the Library or a file: choose the channel or Page, the title, the description and who can watch, and watch the progress on the **Uploads** tab. Post one video, a batch, or tick **Post when downloads finish**. Sign in to the site first (Tools > **Sign in to sites**): the post is made in a browser window of its own, as you would do it. |
| **Library** | The **Library** menu lists the videos you downloaded: search them, play them, find them in their folder, delete them, or post them. A video's re-up version is listed beside its original, with a filter to show only the re-up videos. |
| **An assistant to ask** | Help > **Ask Robert** (F1) opens a pane on the right of the window (F1 again closes it; left open, it opens again with the app) to chat with Robert, a robot cat who knows the app: ask how to do something, why a download failed (he reads its log), or tell him what to do, in Vietnamese or English: "download this video as MP3", "dub it into Vietnamese", "summarize this video". He fills in the main window or opens the right Tools window, and shows a card first: **Do it**, **Let me change it**, or **Cancel**. What needs a license still does. Press the microphone to ask by voice: he writes down what you said with the speech recognizer and reads his answer aloud with the dubbing's voice, in your language. He runs on your PC with the translator's language model (Qwen3 8B), nothing is sent anywhere; the first time he downloads it (about 5 GB), unless the translation or summaries did already. Free to use, also once the free days are over. |
| **Bilingual subtitles** | In the Subtitle extractor, tick two languages and **Bilingual**: one file shows each line in both, the language you choose on top, the other under it. For learning a language, or watching together. |
| **Browser extension** | In Chrome, Edge or Brave, one click on the extension's button sends the page you're on to the app, a video, pictures or a post (a blue arrow on the button shows when the page is a video), signed in as you are in the browser. Or right-click a link, a video or a picture and choose **Download with K-Media Downloader**. |
| **Copy a link, it's read** | Turn on Tools > **Watch the clipboard for links**: copy a video's or post's address in your browser and it's ready to download. |
| **Shut down when done** | Tick **Shut down the PC when done** under the queue: once the queue is empty, the PC turns off after a minute's countdown you can cancel. |
| **Posts and videos that need a sign-in** | Send them with the browser extension, which brings your sign-in along. Or use the cookies of the browser you're signed in with (Firefox), or a cookies file, for what only members or friends can see. |
| **Told when it's done** | A notification when a download ends while the window is in the background. |
| **Its own log** | Right-click a download and choose **Show log** to see exactly what happened, to fix a problem or ask for help. |
| **Light or dark, English or Vietnamese** | Follows your Windows theme. It opens in Vietnamese the first time; switch to English with the flags at the top right of the window (or in Settings > Language), and the app restarts in it. |
| **For scripts** | `MediaDownloader.exe <link>... [--dir <folder>] [--cookies <cookies.txt>]` opens the app with the links read, saving to that folder with those cookies for that run only. |

## Choosing the exact streams

For one video, the last entry of the Quality list, **Choose streams...**, opens every stream the site has:

![Choose streams: every video and audio stream with its resolution, frame rate, codec, HDR, type and size](images/stream-picker.png)

Pick a video stream and an audio stream, and press **Use these**. The pick shows in the Quality list and in the queue.

## Sending links from your browser

The extension for Chrome, Edge and Brave comes with the app. Add it once:

1. In K-Media Downloader, open **Tools > Browser extension...** and press **Open the folder**. Its path is copied too.
2. In the browser, open `chrome://extensions` (`edge://extensions` in Edge, `brave://extensions` in Brave) and turn
   on **Developer mode**.
3. Press **Load unpacked** and choose that folder (paste its path in the folder box).
4. Pin it: press the puzzle piece next to the address bar, then the pin next to K-Media Downloader.

Then, on a video's or post's page, click the K-Media Downloader button: the app opens (or comes to the front) with the
link read, ready to choose the quality and press **Add to queue**. A tick on the button says the link was sent.
Right-click a link, a video playing in the page or a picture for **Download with K-Media Downloader**.

Posts and videos you can only see signed in (members-only, private or age-restricted) work too: the extension sends your
browser's cookies for that site with the link, so the app is signed in as you are. When you add the extension, the
browser warns that it can "read and change all your data on all websites": that is what reading a site's cookies
needs. It sends nothing until you click, and then only the link and that one site's cookies, only to the app on your
PC. The app keeps them while it is open, uses them for that site only, and deletes them when you close it.

## Free trial

Try everything free for **30 days**, no key needed and nothing limited. The status bar shows how many days are left.
After that, K-Media Downloader still reads links, but downloading (videos, music, pictures, subtitles, thumbnails and chats) needs
a license key, and so do the Tools that work on a file on your PC (Make from speech, the summary, the Frame extractor,
Separate voice, music and sound effects, and Dub into another language). Saving the subtitles a file on your PC already has stays free.

## Buying a license

Open **Help > License...** (or click the license text at the right of the status bar), copy the machine code it
shows, and send it to us by email (the **Copy email** button helps). You get a license key back: paste it into the
same window and press **Register**.

Licenses are available for a period of time (for example monthly or yearly), for your PC.

## Requirements

- Windows 10 or Windows 11 (64-bit)
- An internet connection
- About 500 MB of free disk space, plus room for your downloads. The AI tools download what they need the first time
  you use one: up to about 600 MB for Make from speech, about 5 GB for translation, Summarize and the assistant, about
  200 MB for Separate voice, music and sound effects, about 85 MB for Dub into another language (about 7 GB for all of
  them)
- Optional: an NVIDIA, AMD or Intel graphics card with an up-to-date driver, for faster converting (see **Faster on
  your graphics card**)

## Installing

Run `MediaDownloader-<version>.exe` and follow the steps. No administrator rights are needed. Installing a new
version over the old one keeps your settings. Uninstalling deletes the sign-ins and cookies the app kept, the
download list and the record of what was downloaded, and leaves your settings, so a reinstall picks up where you left
off.

The first time it starts, K-Media Downloader downloads yt-dlp (about 24 MB), the engine that reads and downloads the
links, and ffmpeg (about 110 MB), which it needs to join HD video with its sound, convert audio and cut parts. The
status bar shows how far each got; it is ready to use when that is done. It then adds aria2 (about 5 MB), for faster
downloads, in the background. After that, it updates yt-dlp by itself when it starts and a new one is out.

For YouTube, the app offers to add Deno (about 45 MB) the first time you read a YouTube link: without it YouTube
gives fewer qualities, often not the best. You can also add it later from the Tools menu.

## Please note

Download only what you have the right to: your own videos, videos their owner lets you download, or what the law lets
you copy. Each site has its own terms. See the license agreement shown during setup.

K-Media Downloader uses yt-dlp, FFmpeg, Deno, gallery-dl, aria2, whisper.cpp, llama.cpp, ONNX Runtime, the BandIt v2 model and Piper, made by others and free to use under their own licenses: see
THIRD-PARTY-NOTICES.txt in the folder the app is installed in. FFmpeg is gyan.dev's build, the one ffmpeg.org links
to for Windows.

## Contact

- For support: **khanh1985@gmail.com**
- **Phone:** +84 985 884 764
- [Privacy policy](https://github.com/xuankhanh/MediaDownloader/blob/main/PRIVACY.md), including how to delete your data

© 2026 Truong Xuan Khanh. All rights reserved.
