# Privacy Policy

**Video Downloader** (the Windows app)

Last updated: October 26, 2026

Video Downloader is a Windows desktop app. It runs on your own PC. It has no account, we don't run a server that
receives your data, and it doesn't collect or send any usage or tracking information. We don't sell or share your data
with anyone.

## What the app connects to

- **The sites you download from.** When you analyze or download a link, the app (through yt-dlp) connects to that
  site, as your browser would, to read the video and download it. Each site has its own privacy policy.
- **SponsorBlock**, only when you tick **Cut sponsors** or make a PiP video of a YouTube video: the app sends the
  video's ID to `sponsor.ajay.app` to learn which parts viewers marked as sponsors. Nothing else is sent.
- **Its tools' download sites**, to download and update what it needs: GitHub (yt-dlp, and ffmpeg from gyan.dev's
  GitHub mirror), www.gyan.dev (ffmpeg, when GitHub can't be read) and dl.deno.land (Deno, for YouTube). They only
  learn that a copy is being downloaded, as for any download from your browser. Turn off update checks in Settings if
  you don't want the app to check for new versions when it starts.

If you set a proxy in Settings, these connections go through it.

## Cookies

Videos that need a sign-in can be downloaded with your cookies, only if you choose so in Settings:

- **From your browser:** the app (through yt-dlp) reads the cookies of the browser you pick, on your PC, each time it
  reads or downloads a link. They are sent only to the site you download from, as your browser would send them.
- **From a file, or pasted:** the same, from the cookies.txt file you choose; pasted cookies are kept in
  `%APPDATA%\VideoDownloader\cookies.txt`.

Cookies are never sent to us or anywhere else.

## Where it is stored

Everything stays on your PC:

- Your settings, in `%APPDATA%\VideoDownloader\settings.json`, and pasted cookies (above).
- ffmpeg and Deno, in `%LOCALAPPDATA%\VideoDownloader`.
- Your downloads, in the folder you choose.

A download's log stays in the app's memory and is gone when you close it, unless you save it yourself.

## Deleting your data

1. Uninstall Video Downloader in Windows (**Settings > Apps**).
2. Delete the folders `%APPDATA%\VideoDownloader` (settings and pasted cookies) and `%LOCALAPPDATA%\VideoDownloader`
   (ffmpeg and Deno). Uninstalling leaves them, so a reinstall keeps your settings.

Your downloads stay in their folder until you delete them.

If you wrote to us for support and want us to delete your emails, or you have any question about your data, write to
**khanh1985@gmail.com**. We delete them within 30 days and reply to confirm.

## Contact

- Email: **khanh1985@gmail.com**
- Phone: +84 985 884 764
